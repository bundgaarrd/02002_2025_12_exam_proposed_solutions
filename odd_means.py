# Opgave 5 (Odd Means)
import numpy as np

def odd_means(M):
    oddMeans = []
    j = M.shape[1] # No. of columns
    for i in range(1, j+1):
        if (i % 2 != 0): # If columun number j is odd do
            oddMeans.append(np.mean(M[:, i-1])) # append to list
    return np.array(oddMeans) # convert list to numpy array