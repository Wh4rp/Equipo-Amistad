library(tidyverse)
library(dplyr)
library(ggplot2)
library(readr)

#Importing datasets
arab <- read_delim("Desktop/answers111/answer_question_arab.csv", 
                   delim = ";", escape_double = FALSE, trim_ws = TRUE)
ceban <- read_delim("Desktop/answers111/answer_question_ceb.csv", 
                   delim = ";", escape_double = FALSE, trim_ws = TRUE)

chin <- read_delim("Desktop/answers111/answer_question_chin.csv", 
                                   delim = ";", escape_double = FALSE, trim_ws = TRUE)

dutch <- read_delim("Desktop/answers111/answer_question_dutch.csv", 
                                   delim = ";", escape_double = FALSE, trim_ws = TRUE)


eng<- read_delim("Desktop/answers111/answer_question_eng.csv", 
                                   delim = ";", escape_double = FALSE, trim_ws = TRUE)

fren<- read_delim("Desktop/answers111/answer_question_fr.csv", 
                                   delim = ";", escape_double = FALSE, trim_ws = TRUE)


germ<- read_delim("Desktop/answers111/answer_question_ger.csv", 
                                   delim = ";", escape_double = FALSE, trim_ws = TRUE)


ita <- read_delim("Desktop/answers111/answer_question_ita.csv", 
                                   delim = ";", escape_double = FALSE, trim_ws = TRUE)


japo <- read_delim("Desktop/answers111/answer_question_japo.csv", 
                                   delim = ";", escape_double = FALSE, trim_ws = TRUE)

kore <- read_delim("Desktop/answers111/answer_question_kor.csv", 
                   delim = ";", escape_double = FALSE, trim_ws = TRUE)

russi <- read_delim("Desktop/answers111/answer_question_rus.csv", 
                   delim = ";", escape_double = FALSE, trim_ws = TRUE)

spa <- read_delim("Desktop/answers111/answer_question_spa.csv", 
                   delim = ";", escape_double = FALSE, trim_ws = TRUE)


swah <- read_delim("Desktop/answers111/answer_question_swah.csv", 
                   delim = ";", escape_double = FALSE, trim_ws = TRUE)

swe <- read_delim("Desktop/answers111/answer_question_swe.csv", 
                   delim = ";", escape_double = FALSE, trim_ws = TRUE)

#creando entradas de frequencia: idioma/affirmation/negation/noncommittal
#probablemente hay una manera mas rapida de hacerlo, yo estaba apurado

arab$classification<-as.factor(arab$classification)

arab$language<-as.factor(arab$language)

table(arab$language, arab$classification)


ceban$classification<-as.factor(ceban$classification)

ceban$language<-as.factor(ceban$language)

table(ceban$language, ceban$classification)


chin$classification<-as.factor(chin$classification)

chin$language<-as.factor(chin$language)

table(chin$language, chin$classification)

dutch$classification<-as.factor(dutch$classification)

dutch$language<-as.factor(dutch$language)

table(dutch$language, dutch$classification)

eng$classification<-as.factor(eng$classification)

eng$language<-as.factor(eng$language)

table(eng$language, eng$classification)

fren$classification<-as.factor(fren$classification)

fren$language<-as.factor(fren$language)

table(fren$language, fren$classification)

germ$classification<-as.factor(germ$classification)

germ$language<-as.factor(germ$language)

table(germ$language, germ$classification)

ita$classification<-as.factor(ita$classification)

ita$language<-as.factor(ita$language)

table(ita$language, ita$classification)

japo$classification<-as.factor(japo$classification)

japo$language<-as.factor(japo$language)

table(japo$language, japo$classification)

kore$classification<-as.factor(kore$classification)

kore$language<-as.factor(kore$language)

table(kore$language, kore$classification)

russi$classification<-as.factor(russi$classification)

russi$language<-as.factor(russi$language)

table(russi$language, russi$classification)

spa$classification<-as.factor(spa$classification)

spa$language<-as.factor(spa$language)

table(spa$language, spa$classification)

swah$classification<-as.factor(swah$classification)

swah$language<-as.factor(swah$language)

table(swah$language, swah$classification)

swe$classification<-as.factor(swe$classification)

swe$language<-as.factor(swe$language)

table(swe$language, swe$classification)

#analizando totalidad de lenguas (no honest primer)

resumlinga <- read_csv("Desktop/aaaaaa - Sheet1.csv") #base con nombres breves

#negaciones
resumlinga<-resumlinga[order(resumlinga$negation),] #ordenar de forma ascendente
resumlinga$language <- factor(resumlinga$language, levels = resumlinga$language)#este es necesario para evitar el orden alfabetico en el ploteo
ggplot(data = resumlinga, aes(x = language, y = negation)) + geom_bar(stat = "identity") + theme_minimal()

#afirmaciones
resumlinga<-resumlinga[order(resumlinga$affirmation),] #ordenar de forma ascendente
resumlinga$language <- factor(resumlinga$language, levels = resumlinga$language)#este es necesario para evitar el orden alfabetico en el ploteo
ggplot(data = resumlinga, aes(x = language, y = affirmation)) + geom_bar(stat = "identity") + theme_minimal()

#noncommittal
resumlinga<-resumlinga[order(resumlinga$noncommittal),] #ordenar de forma ascendente
resumlinga$language <- factor(resumlinga$language, levels = resumlinga$language)#este es necesario para evitar el orden alfabetico en el ploteo
ggplot(data = resumlinga, aes(x = language, y = noncommittal)) + geom_bar(stat = "identity") + theme_minimal()


#stacked boxplot (mejorar la parte estetica)

useful <- read_csv("Downloads/usefuldata.csv")

useful$class<-factor(useful$class, levels = c("negation", "affirmation", "noncommittal"))
ggplot(data = useful, aes(x = language, y = freq, fill = class))+geom_bar(stat = "identity") + theme_minimal()


