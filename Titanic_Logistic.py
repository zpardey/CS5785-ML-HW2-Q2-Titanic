import csv
import numpy
from matplotlib import pyplot


# First create a reference name for the data file.
Titanic_training_data = "Titanic_training_data.csv"

# Next create an object to represent the opened CSV file.
titanic_training_csvObject = open(Titanic_training_data, "r")

# Finally, create a reader object comprised of a number of rows, where each row is a list of strings.
reader = csv.reader(titanic_training_csvObject)

# Transform the reader object into a Python list data type.
readerList = list(reader)
print(readerList)


# Make readerList into a numPy matrix.
readerMatrix = numpy.matrix(readerList)
print("Reader matrix:", readerMatrix)

# Use the colon in the first position to select every row, and use 4 to select the 5th column of data, the labels
# Use 4 because the matrix is zero-indexed.
labelsVector = readerMatrix[:,4]
print("Labels vector: ", labelsVector)
# Select the first four columns of the matrix by using 0:4 in the columns place. 0:4 bc final entry is non-inclusive.
attributesMatrix = readerMatrix[:,0:4]
#print(attributesMatrix)

ggggg

test test