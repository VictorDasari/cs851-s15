library(xlsx)
read.xlsx(file.choose(),1, header=T) -> random
plot(random[,2],random[,1],type="l",col="red",xlab="Rank",ylab="Frequency",main="Graph of unique terms after using boilerpipe")