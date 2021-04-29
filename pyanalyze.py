


#Elvis Nunez
#Python Programming
#Analyze data and produce the right approach to your hypothesis


#WARNING: pip install textblob vadersentiment, run this command in the files directory thought cmd
#put the txt files in the same directory 
#importing the vader sentiment library 

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analizando_sentimientos = SentimentIntensityAnalyzer()

contador = 0
correctas = 0

#opening the txt file 
with open("positive.txt","r") as que:


	#loop for spliting the sentences 
    for lineas_entre_espacio in que.read().split('\n'):
        texto = analizando_sentimientos.polarity_scores(lineas_entre_espacio)

        if not texto['neg'] > 0.1:
            if texto['pos']-texto['neg'] > 0:
                correctas += 1
            contador +=1



contador_negativo = 0
correctas_negativas = 0

with open("negative.txt","r") as que:
    for lineas_entre_espacio in que.read().split('\n'):
        texto = analizando_sentimientos.polarity_scores(lineas_entre_espacio)

        if not texto['pos'] > 0.1:
            if texto['pos']-texto['neg'] <= 0:
                correctas_negativas += 1
            contador_negativo +=1



s= format(correctas_negativas/contador_negativo*100.0,'.2f')
s_correct=format(correctas/contador*100.0,'.2f')


#formating the print statement
print("Negative accuracy of the data analysis={} % {},  sentences were negative".format(s, contador_negativo))
print("Positive accuracy of the data analysis ={} %  {},  sentences were positive".format(s_correct, contador))
