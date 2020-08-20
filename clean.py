import csv
import pandas as pd

inputFile = "timSmithToClean.csv"

df = pd.read_csv(inputFile,engine='python')

#Deletes all columns other than the tweet column. As its the 10th Column. REF https://www.geeksforgeeks.org/how-to-drop-one-or-multiple-columns-in-pandas-dataframe/
df.drop(df.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]], axis = 1, inplace = True)

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

#Export cleaned dataframe to CSV. 
df.to_csv('timSmithCleaned.csv')
