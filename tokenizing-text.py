text=['This is introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity', 'There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage','I like this book','I want more books like this']
#convert list to dataframe
import pandas as pd
#using textblob
from textblob import TextBlob
#using nltk
import nltk
df = pd.DataFrame({'tweet':text})
h1 = "===Given Data==="
h2 = "===Tokenize Using TextBlob==="
h3 = "===Tokenize Using NLTK==="
h4 = "===Tokenize Using Split==="
print(h1)
print(df)
df2 = TextBlob(df['tweet'][3]).words
print(h2)
print(df2)
#create data
mystring = "My favorite animal is cat"
df3 = nltk.word_tokenize(mystring)
print(h3)
print(df3)
#using split
df4 = mystring.split()
print(h4)
print(df4)

