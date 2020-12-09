data <- read.csv("../twitter_bidirected_degdist.txt", header=F)
colnames(data) <- c("degree", "count")
png("../twitter_bidirected_degdist.png")
plot(log(data$count), log(data$degree), type="p")
dev.off()

