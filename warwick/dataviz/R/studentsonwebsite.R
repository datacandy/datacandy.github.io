#red the data in
data <- read.csv("https://raw.githubusercontent.com/kevinrobinson/mobile-learning-experience/master/edx-dataset/minutes_per_day.csv", header=T,
                 colClasses=c("integer",
                              "Date",
                              "integer"))

#Get a statistical summary of the data
summary(data)

#Load in a library called dplyr
library(dplyr)
avgdata <- data %>%
  group_by(date) %>%
  summarise(avg_minutes = mean(minutes_on_site))
# dplyr helps to calcualte the average time spend on the website each day

#Load in a library called ggplot2
library(ggplot2)
outputviz <- qplot(data=avgdata, x=date, y=avg_minutes) +
  geom_line() +
  geom_point()
# Create a graph of average minutes on the website over the time preiod

install.packages("plotly")
Sys.setenv("plotly_username"="benbenben")
Sys.setenv("plotly_api_key"="future1000")
library(plotly)
ggplotly(outputviz)