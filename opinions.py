import csv
import pandas as pd
from textblob import TextBlob

inputFile = "timSmithToClean.csv"
Stage1File = "timSmithCleaned.csv"
Stage2File = "timSmithSentimentApplied.csv"

df = pd.read_csv(inputFile,engine='python')

#Deletes all columns other than the tweet column. As its the 10th Column. REF https://www.geeksforgeeks.org/how-to-drop-one-or-multiple-columns-in-pandas-dataframe/
df.drop(df.columns[[0, 1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]], axis = 1, inplace = True)

#changes all text to lower case. REF https://medium.com/@koshut.takatsuji/twitter-sentiment-analysis-with-full-code-and-explanation-naive-bayes-a380b38f036b
df['tweet'] = df['tweet'].apply(lambda x: x.lower())

#Removing special chars from the dataframe REF https://stackoverflow.com/questions/51778480/remove-certain-string-from-entire-column-in-pandas-dataframe
df['tweet'] = df['tweet'].str.replace('@', '')
df['tweet'] = df['tweet'].str.replace('.', '')
df['tweet'] = df['tweet'].str.replace(',', '')
df['tweet'] = df['tweet'].str.replace('#', '')
df['tweet'] = df['tweet'].str.replace('&', '')
df['tweet'] = df['tweet'].str.replace('!', '')
df['tweet'] = df['tweet'].str.replace('%', '')
df['tweet'] = df['tweet'].str.replace('(', '')
df['tweet'] = df['tweet'].str.replace(')', '')

#Removing line breaks. REF https://stackoverflow.com/questions/44227748/removing-newlines-from-messy-strings-in-pandas-dataframe-cells
df = df.replace('\n','', regex=True)

DFList = []
for group in df.groupby(df.index.date):
    DFList.append(group[1])


#Export cleaned dataframe to CSV.
df.to_csv(Stage1File)


with open(Stage1File, 'r') as csvfile: #opening the input file.
    rows = csv.reader(csvfile)
    f = open(Stage2File, "w") #opening the output file. REF https://stackoverflow.com/questions/25115140/python-only-last-line-is-saved-to-file. Important to open this outside of the loop.
    for row in rows:
        sentence = row[2] #This picks the column.
        blob = TextBlob(sentence)
        sentimentrow = blob.sentiment.polarity #Sentiment Polarity Analysis
        subjectivityrow = blob.sentiment.subjectivity #Subjectivity Polarity Analysis
        f.write(sentence + "," + str(sentimentrow) + "," + str(subjectivityrow) + "\n") #REF https://stackoverflow.com/questions/25115140/python-only-last-line-is-saved-to-file
    f.close() #REF https://stackoverflow.com/questions/25115140/python-only-last-line-is-saved-to-file. Important to close this outside of the loop.


#Now to add a header to the CSV REF https://stackoverflow.com/questions/28162358/append-a-header-for-csv-file
with open(Stage2File,newline='') as header:
    r = csv.reader(header)
    data = [line for line in r]
with open(Stage2File,'w',newline='') as header:
    w = csv.writer(header)
    w.writerow(['Sentence','Polarity','Subjectivity'])
    w.writerows(data)

#Below we are stats from the CSV` REF https://stackoverflow.com/questions/50165953/python-dataframes-describing-a-single-column
df3 = pd.read_csv(Stage2File,engine='python') #Converting a csv to a panda dataframe. Need to use engine=python as per https://www.shanelynn.ie/pandas-csv-error-error-tokenizing-data-c-error-eof-inside-string-starting-at-line/
describePolarity = df3['Polarity'].describe() #Computing the common statistics of the Polarity column in the dataframe/
print(describePolarity)
print(df3)
