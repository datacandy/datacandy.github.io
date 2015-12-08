#read the data into R-Studio
uncleanData <- read.csv('/Users/BH/datacandy.github.io/warwick/R/data2.csv', header=T, sep=',')

#Define a function to remove all the characters, including the commas
cleanFunction <- function(argument){
  as.numeric( gsub('[^a-zA-Z0-9.]', '', argument))
}

# the "sapply" command traverses over a set of 
# data like a list or vector, and calling the specified function (cleanFunction) for each item. 
uncleanData[] <- sapply(uncleanData, cleanFunction)

#Displays sample in the console
str(uncleanData)

#Shows the whole thing cleaned up
uncleanData