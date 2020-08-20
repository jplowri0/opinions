import csv


inputFile = 'test.csv'
outputFile = 'test1.csv'

infile = inputFile #This is the input file.

#def cleanedText(text):
#    text = re.sub('@[A-Za-z0-9]+', '', text) #Removes recommendations
#    text = re.sub('RT[\s]+', '', text) #Removes RT
#    text = re.sub('https?:\/\/\S+', '', text)
#    return text

#Need to Clean the CSV
#Remove Blank lines
with open(inputFile) as in_file:
    with open(outputFile, 'w') as out_file:
        writer=csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(row):
                writer.writerow(row)
