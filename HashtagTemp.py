import csv
import re
import random
#Filtert die Hashtags aus der CSV und fügt sie in eine eigene Spalte innerhalb der CSV Datei und gibt ihnen die passenden Indizes zum gleichen Tweet

inpute = open("C:/Users/topsen/Desktop/american-election.csv","r")
output = open("C:/Users/topsen/Desktop/new-american-election.csv","wb")

reader = csv.reader(inpute,delimiter=";")
writer = csv.writer(output,delimiter=";")
count = 0#Zähler für die Indexspalte der Tweets

index = ["index"]#Initiieriung der Liste für die Indizes
test = []#Initiieriung der Liste für die Hashtags
for row in reader: 
	row[1] = re.sub(r'[^\x00-\x7f]',r'',row[1])#Regulärer Ausdruck zum rausfiltern der Hashtags
	pat = re.compile(r"#(\w+)")

	hashtag = pat.findall(row[1])
	if not not hashtag:#für jeden Sortierten Hashtag einfügung in Test
		for i in range(len(hashtag)):
			hashtag[i] = ''.join(('#',hashtag[i]))
		global test
		test += hashtag
	if row[10] != "True":
		writer.writerow([index[len(index)-1],hashtag])#Einschreiben der Hashtags in die richtigen Spalten in der Temporären CSV Datei
	index.append(count)
	count += 1
def quicksort(test):# Quicksort Algorithmus zur Sortierung der Hashtags in der richtigen Reihenfolge
	if len(test)<2:
		return test
	else:
		x=random.randint(0,len(test)-1)
		pivo=test[x]
		ls=list(filter(lambda x:x<pivo,test))
		rs=list(filter(lambda x:x>pivo,test))
		y=quicksort(ls)+[pivo]+quicksort(rs)
		return test

inpute.close()
output.close()


