#Removing Punctuation In Existing Text
import re #importing regular expression package
import pandas as pd
import string
text = ['Is Tranquility Meaning Given In Psalm 131 Now?','In the gentle moments of Matthew 19:13-14', 'we witness a profound teaching', 'Children in their innocence were brought to Jesus', 'and despite the disciples initial resistance' , 'Jesus welcomed them declaring', 'the kingdom of heaven belongs to such as these','This statement unveils a deep truth','the kingdom is not about adult-like ambition or', 'success but about embracing the pure qualities', 'of a child—chief among them trust.']
df = pd.DataFrame({'Tranquil Testament -> Daily Bible Study':text})
blanks1 = "==============Basic Data============================="
print(blanks1)
print(df)
blanks2 = "==============Remove Punctuations Using RegEX Function========================"
print(blanks2)
s = "Is Tranquility Meaning Given In Psalm 131 Now?, In the gentle moments of Matthew 19:13-14"
#s = text
s1 = re.sub(r'[^\w\s]','',s)
print(s1)
blanks3 = "==================Remove Punctuations Using Replace Function====================="
r = "'Children in their innocence were brought to Jesus', 'and despite the disciples initial resistance'"
for c in string.punctuation:
    r = r.replace(c,"")
print(blanks3)
print(r)
#this code will keep window open
input("\nPress Enter to exit...")