install.packages("psych")
install.packages("tidyverse")
install.packages("hrbrthemes")
install.packages("ggplot2")
install.packages("plotrix")

library(tidyverse)
library(hrbrthemes)

#Histograma delincuencia por edad
data <-DatosDelincuencia
p <-data %>%
  filter( Edad<50 ) %>%
  ggplot( aes(x=Edad)) +
  geom_histogram( binwidth=1, fill="#69b3a2", color="#e9ecef", alpha=0.9) +
  ggtitle("Delincuencia por Edad") +
  theme_ipsum() +
  theme(plot.title = element_text(size=15))
p

#Delincuencia por género
library(ggplot2)
library(plotrix)
count<-table(DatosDelincuencia$Sexo)
label<-paste(round((count*100)/14408,2),"%",sep="")
par(mfrow=c(1,2))
pie(count,main="Delincuencia por Género")
pie(count,labels=label,main="Delincuencia por Género")

#Boxplot edad por departamento
DatosDelincuencia%>% 
  ggplot(aes(x=Edad, y= Departamento))+
  geom_boxplot()+ggtitle("Edad por Departamento")+
  labs(x="Edadl",y="Departamento")+
  theme_minimal()
theme(axis.text.x = element_text(size=8))

#Arma empleada por género
DatosDelincuencia %>% 
  ggplot(aes(x=Sexo, colour = `Arma empleada`))+
  geom_density()