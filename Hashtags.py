import csv

in_file = open("C:/Users/topsen/Desktop/new-american-election.csv","r")
out_file = open("C:/Users/topsen/Desktop/hashtags.csv","wb")

reader = csv.reader(in_file,delimiter=";")
writer = csv.writer(out_file,delimiter=";")

for row in reader:#Bereinigt die Hashtag und entfernt leere Einträge
    if row[1]!= "[]":
        row[1] = row[1].replace("[","")
        row[1] = row[1].replace("]","")
        writer.writerow(row)

in_file.close()
out_file.close()
