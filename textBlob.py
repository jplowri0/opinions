import csv
from textblob import TextBlob
import pandas as pd

inputFile = 'timSmithTweetsA.csv'
outputFile = 'timSmithTweetsA1.csv'

infile = inputFile #This is the input file.

#def cleanedText(text):
#    text = re.sub('@[A-Za-z0-9]+', '', text) #Removes recommendations
#    text = re.sub('RT[\s]+', '', text) #Removes RT
#    text = re.sub('https?:\/\/\S+', '', text)
#    return text

#Need to Clean the CSV
#Remove Blank lines # REF https://stackoverflow.com/questions/4521426/delete-blank-rows-from-csv
#with open(inputFile) as in_file:
#    with open(outputFile1, 'w') as out_file:
####            writer.writerow(row)


#Remove special character
#Remove Numbers
#Remove Begginning with RT
#Remove emoji


with open(inputFile, 'r') as csvfile: #opening the input file.
    rows = csv.reader(csvfile)
    f = open(outputFile, "w") #opening the output file. REF https://stackoverflow.com/questions/25115140/python-only-last-line-is-saved-to-file. Important to open this outside of the loop.
    for row in rows:
        sentence = row[0]
        blob = TextBlob(sentence)
        sentimentrow = blob.sentiment.polarity #Sentiment Polarity Analysis
        subjectivityrow = blob.sentiment.subjectivity #Subjectivity Polarity Analysis
        f.write(sentence + "," + str(sentimentrow) + "," + str(subjectivityrow) + "\n") #REF https://stackoverflow.com/questions/25115140/python-only-last-line-is-saved-to-file
    f.close() #REF https://stackoverflow.com/questions/25115140/python-only-last-line-is-saved-to-file. Important to close this outside of the loop.


#Now to add a header to the CSV REF https://stackoverflow.com/questions/28162358/append-a-header-for-csv-file
with open(outputFile,newline='') as header:
    r = csv.reader(header)
    data = [line for line in r]
with open(outputFile,'w',newline='') as header:
    w = csv.writer(header)
    w.writerow(['Sentence','Polarity','Subjectivity'])
    w.writerows(data)

#Below we are stats from the CSV` REF https://stackoverflow.com/questions/50165953/python-dataframes-describing-a-single-column
df = pd.read_csv(outputFile,engine='python') #Converting a csv to a panda dataframe. Need to use engine=python as per https://www.shanelynn.ie/pandas-csv-error-error-tokenizing-data-c-error-eof-inside-string-starting-at-line/
describePolarity = df['Polarity'].describe() #Computing the common statistics of the Polarity column in the dataframe/
print(describePolarity)
print(df)
