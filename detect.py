from classify import PerformanceMetrics
import cv2 as cv
import numpy as np

class Resolution():
    """
    A class for resizing the image

    Method
    ------
    resizeImage(image, image_file_name)
        Resize the image to a smaller resolution
    """
    def resizeImage(self, image, image_file_name):
        """
        Resize the image to a smaller resolution

        Parameters
        ----------
        image: str
            The file name of the image
        image_file_name: str
            The file name of the resized image
        """
        #Read the image
        image = cv.imread(image)
        scale_percent_small = 15 #define 50% scale percent of original size
        original_width = image.shape[1]#extract width of the original image
        original_height = image.shape[0]#extract height of the original image

        #Scale the image to small dimension 
        small_image_width = int(original_width * scale_percent_small / 100)#scale image horizontally
        small_image_height = int(original_height * scale_percent_small / 100)#scale image vertically
        small_dimension = (small_image_width, small_image_height)#set new dimension of size

        #resize the image
        resized_image = cv.resize(image, small_dimension, interpolation = cv.INTER_AREA)#resize the image to small dimension

        #Write the image
        cv.imwrite(image_file_name, resized_image)

class CornerDetection():
    """
    A class for detecting the object in the image

    Attributes
    ----------
    image_file: str
        The file name of the image
    image: numpy array
        The array to store the pixel values of an colour image
    greyimage: numpy array
        The array to store the pixel values of an greyscale image
    corners: list
        The list to store the detected corner values

    Methods
    --------
    readImage()
        Read the image
    convertToGray()
        Covert the image to greyscale mode
    cornerDetection()
        Detect the corner in an image
    labelCorner()
        Label the detected corner on the image
    showImage()
        Display the image with the detected corner
    allCornerPoints()
        Return all the detected corners
    """
    def __init__(self, image):
        """
        Parameters
        ----------
        image: str
            The image file name
        """
        self.image_file = image
        self.image = image
        self.greyimage = image
        self.corners = []

    def readImage(self):
        """
        Read the image

        Return
        ------
        image: numpy array
            The array to store the pixels of the image
        """
        #Read the image
        self.image = cv.imread(self.image)
        #Return the pixels image
        return self.image

    def convertToGray(self):
        """
        Covert the image to greyscale mode
        """
        #Convert the colour image to greyscale image
        self.greyimage = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        #Convert the datatype of pixels of greyscale image to float32 
        self.greyimage = np.float32(self.greyimage)

    def cornerDetection(self):
        """
        Detect the corner in an image
        """
        #Tract the corners on the greyscale image
        self.corners = cv.goodFeaturesToTrack(self.greyimage, 28, 0.2, 5)
        self.corners = np.int0(self.corners)# int32 or int64

    def labelCorner(self):
        """
        Label the detected corner on the image
        """
        #Iterate through the detected corners
        for corner in self.corners:
            x, y = corner.ravel()
            #Draw the corner in a circle using the detected corner
            cv.circle(self.image, (x,y), 4, 255, -1)

    def showImage(self):
        """
        Display the image with the detected corner
        """
        #Shows the image
        cv.imshow(self.image_file, self.image)
        #Write the image
        cv.imwrite('Corner detected '+self.image_file, self.image)

    def allCornerPoints(self):
        """
        Return all the detected corners
        """
        #Return the list of the detected corners
        return self.corners

if __name__ == '__main__':
    #Initialize the Resolution class
    resize = Resolution()
    #Resize and write the image
    resize.resizeImage('Image 1.jpg', 'Image A.jpg')
    resize.resizeImage('Image 2.jpg', 'Image B.jpg')
    resize.resizeImage('Image 3.jpg', 'Image C.jpg')
    resize.resizeImage('Image 4.jpg', 'Image D.jpg')
    resize.resizeImage('Image 5.jpg', 'Image E.jpg')
    #Detect the corner in image A
    corner_detection_imgA = CornerDetection('Image A.jpg')
    corner_detection_imgA.readImage()#Read the image
    corner_detection_imgA.convertToGray()#Convert to grey
    corner_detection_imgA.cornerDetection()#Detect the corner
    corner_detection_imgA.labelCorner()#Label the corner
    corner_detection_imgA.showImage()#Show the image
    cornerPointsA = corner_detection_imgA.allCornerPoints()#Access the corners
    #Detect the corner in image B
    corner_detection_imgB = CornerDetection('Image B.jpg')
    corner_detection_imgB.readImage()#Read the image
    corner_detection_imgB.convertToGray()#Convert to grey
    corner_detection_imgB.cornerDetection()#Detect the corner
    corner_detection_imgB.labelCorner()#Label the corner
    corner_detection_imgB.showImage()#Show the image
    cornerPointsB = corner_detection_imgB.allCornerPoints()#Access the corners
    #Detect the corner in image C
    corner_detection_imgC = CornerDetection('Image C.jpg')
    corner_detection_imgC.readImage()#Read the image
    corner_detection_imgC.convertToGray()#Convert to grey
    corner_detection_imgC.cornerDetection()#Detect the corner
    corner_detection_imgC.labelCorner()#Label the corner
    corner_detection_imgC.showImage()#Show the image
    cornerPointsC = corner_detection_imgC.allCornerPoints()#Access the corners
    #Detect the corner in image D
    corner_detection_imgD = CornerDetection('Image D.jpg')
    corner_detection_imgD.readImage()#Read the image
    corner_detection_imgD.convertToGray()#Convert to grey
    corner_detection_imgD.cornerDetection()#Detect the corner
    corner_detection_imgD.labelCorner()#Label the corner
    corner_detection_imgD.showImage()#Show the image
    cornerPointsD = corner_detection_imgD.allCornerPoints()#Access the corners
    #Detect the corner in image E
    corner_detection_imgE = CornerDetection('Image E.jpg')
    corner_detection_imgE.readImage()#Read the image
    corner_detection_imgE.convertToGray()#Convert to grey
    corner_detection_imgE.cornerDetection()#Detect the corner
    corner_detection_imgE.labelCorner()#Label the corner
    corner_detection_imgE.showImage()#Show the image
    cornerPointsE = corner_detection_imgE.allCornerPoints()#Access the corners
    #Define the performance metrics class
    performanceMetrics = PerformanceMetrics(cornerPointsA, cornerPointsB, cornerPointsC, cornerPointsD, cornerPointsE)
    #Calculate the Euclidean distance
    img_A_B_ED, img_A_C_ED, img_A_D_ED, img_A_E_ED = performanceMetrics.computeDistance()
    #Sort the distance respectively    
    img_A_B_ED = performanceMetrics.sortDistances(img_A_B_ED)
    img_A_C_ED = performanceMetrics.sortDistances(img_A_C_ED)
    img_A_D_ED = performanceMetrics.sortDistances(img_A_D_ED)
    img_A_E_ED = performanceMetrics.sortDistances(img_A_E_ED)
    #Save all the Euclidean distance in a list
    all_ED = []
    all_ED.append(img_A_B_ED)
    all_ED.append(img_A_C_ED)
    all_ED.append(img_A_D_ED)
    all_ED.append(img_A_E_ED)
    #Perform median distances
    median_distances = performanceMetrics.medianDistance(all_ED)
    #Print the distances, D with the paired images accordingly
    print('Median distance for Euclidean distance of image A and B: ', median_distances[0])
    print('Median distance for Euclidean distance of image A and C: ', median_distances[1])
    print('Median distance for Euclidean distance of image A and D: ', median_distances[2])
    print('Median distance for Euclidean distance of image A and E: ', median_distances[3])
    #Sort the distances, D
    median_distances = performanceMetrics.sortDistances(median_distances)
    print('Sorted median distance, D = ', median_distances)
    #Applied the adaptive thresholding
    e = performanceMetrics.adaptiveThresholding(median_distances)
    print('1 indicate object in image A appear in image B or C or D or E, otherwise 0')
    print('e = ', e)
    #Close all the windows when the key is pressed 
    cv.waitKey(0)
    cv.destroyAllWindows()
