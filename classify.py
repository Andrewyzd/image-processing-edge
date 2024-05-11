import cv2 as cv
import numpy as np
import math

class PerformanceMetrics():
    """
    Attributes
    ----------
    cornerPointsA: list
        The list of corner points from image A
    cornerPointsB: list
        The list of corner points from image B
    cornerPointsC: list
        The list of corner points from image C
    cornerPointsD: list
        The list of corner points from image D
    cornerPointsE: list
        The list of corner points from image E
    img_A_B_euclideanDistance: list
        The list to store the Euclidean distance computed from image A and B
    img_A_C_euclideanDistance: list
        The list to store the Euclidean distance computed from image A and C
    img_A_D_euclideanDistance: list
        The list to store the Euclidean distance computed from image A and D
    img_A_E_euclideanDistance: list
        The list to store the Euclidean distance computed from image A and E

    Methods
    -------
    computeDistance():
        Access the corner points
    euclideanDistance(xA, yA, xI, yI, index):
        Compute the Euclidean distance
    sortDistances(euclideanDistancePoints):
        Sort the Euclidean distances
    medianDistance(allEuclideanDistancePoints):
        Calculate the median distances
    adaptiveThresholding(all_D):
        Calculate the adaptive threshold and check for the existing of the object of image A in image B, C, D, and E
    """
    def __init__(self, cornerPointsA, cornerPointsB, cornerPointsC, cornerPointsD, cornerPointsE):
        """
        Parameters
        ----------
        cornerPointsA: list
            The list of corner points from image A
        cornerPointsB: list
            The list of corner points from image B
        cornerPointsC: list
            The list of corner points from image C
        cornerPointsD: list
            The list of corner points from image D
        cornerPointsE: list
            The list of corner points from image E
        """
        self.cornerPointsA = cornerPointsA
        self.cornerPointsB = cornerPointsB
        self.cornerPointsC = cornerPointsC
        self.cornerPointsD = cornerPointsD
        self.cornerPointsE = cornerPointsE
        #Initialize the list for storing the Euclidean distance
        self.img_A_B_euclideanDistance = []
        self.img_A_C_euclideanDistance = []
        self.img_A_D_euclideanDistance = []
        self.img_A_E_euclideanDistance = []

    def computeDistance(self):
        """
        Access the corner points
        
        Returns
        -------
        img_A_B_euclideanDistance: list
            The list to store the Euclidean distance computed from image A and B
        img_A_C_euclideanDistance: list
            The list to store the Euclidean distance computed from image A and C
        img_A_D_euclideanDistance: list
            The list to store the Euclidean distance computed from image A and D
        img_A_E_euclideanDistance: list
            The list to store the Euclidean distance computed from image A and E
        """
        #Iterate through the detected corner in image A, B, C ,D and E
        for i in range(0, 4):
            for j in range(0, len(self.cornerPointsA)):
                xI = 0
                yI = 0
                #Access the corner in image A
                xA, yA = self.cornerPointsA[j].ravel()
                #Access the corner in image B, C, D, and E based on index
                if i == 0:
                    xI, yI = self.cornerPointsB[j].ravel()
                if i == 1:
                    xI, yI = self.cornerPointsC[j].ravel()
                if i == 2:
                    xI, yI = self.cornerPointsD[j].ravel()
                if i == 4:
                    xI, yI = self.cornerPointsE[j].ravel()
                #Pass the corners point of image A and image B or C or D or E to calculate the Euclidean distance
                self.euclideanDistance(xA, yA, xI, yI, i)

        #Return the Euclidean distance
        return self.img_A_B_euclideanDistance, self.img_A_C_euclideanDistance, self.img_A_D_euclideanDistance, self.img_A_E_euclideanDistance 

    def euclideanDistance(self, xA, yA, xI, yI, index):
        """
        Compute the Euclidean distance
        
        xA: float
            The x coordinate of corner point from image A 
        yA: float
            The y coordinate of corner point from image A 
        xI: float
            The x coordinate of corner point from image B, C, D, or E
        yI: float
            The y coordinate of corner point from image B, C, D, or E
        index: int
            The index to represent the current image pair
        """
        #Calculate Euclidean distance
        d = math.sqrt((xA - xI)**2 + (yA - yI)**2)
        #Save the distance according to the index
        if index == 0:
            self.img_A_B_euclideanDistance.append(d)
        if index == 1:
            self.img_A_C_euclideanDistance.append(d)
        if index == 2:
            self.img_A_D_euclideanDistance.append(d)
        if index == 3:
            self.img_A_E_euclideanDistance.append(d)

    def sortDistances(self, euclideanDistancePoints):
        """
        Sort the Euclidean distances
        
        Parameter
        ---------
        euclideanDistancePoints: list
            The list of unsorted Euclidean distance

        Return
        ------
        euclideanDistancePoints: list
            The list of sorted Euclidean distance
        """
        # Traverse through 1 to len(arr)
        for i in range(1, len(euclideanDistancePoints)):
     
            key = euclideanDistancePoints[i]
     
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and key < euclideanDistancePoints[j] :
                    euclideanDistancePoints[j + 1] = euclideanDistancePoints[j]
                    j -= 1
            euclideanDistancePoints[j + 1] = key

        #Return the sorted Euclidean distance
        return euclideanDistancePoints

    def medianDistance(self, allEuclideanDistancePoints):
        """
        Calculate the median distances
        
        Parameters
        ----------
        allEuclideanDistancePoints: list
            The list of all Euclidean distances

        Return
        ------
        median_distances: list
            The list of median distances
        """
        #Access the length of a list
        length = len(allEuclideanDistancePoints)
        #Initialize D to zero
        D = 0
        #Initialize the list
        median_distances = []
        #Iterate through the list
        for i in range(0, length):
            #Access the list in a list
            n = len(allEuclideanDistancePoints[i])
            #accessed the index based on odd and even number of the length of the list
            if (n % 2) == 0:
                D = 0.5*(allEuclideanDistancePoints[i][int(n/2)] + allEuclideanDistancePoints[i][int((n+1)/2)])
            else:
                D = allEuclideanDistancePoints[i][int((n+1)/2)]
            #Save the D to list
            median_distances.append(D)

        #return median distances
        return median_distances

    def adaptiveThresholding(self, median_distances):
        """
        Calculate the adaptive threshold and check for the existing of the object of image A in image B, C, D, and E
        
        Parameter
        ---------
        median_distances: list
            The list of median distances

        Return
        ------
        e: list
            The list of showing the 1 and 0 to indicate the existing of the object in image A in image B, C, D, and E 
        """
        #Initialize the e list
        e = []
        #Calculate the threshold value
        threshold = (((median_distances[1] + median_distances[0])/2) + ((median_distances[2] + median_distances[3])/2))/2
        print('Threshold value: ', threshold)
        #Iterate through the median distances
        for i in range(0, len(median_distances)):
            #Save 1 to list e if the median distance smaller than threshold, otherwise save 0
            if median_distances[i] < threshold:
                e.append(1)
            else:
                e.append(0)
        #return the list of e, showing 1 and 0
        return e
