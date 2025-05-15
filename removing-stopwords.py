import pandas as pd
import nltk
nltk.download('stopwords') #Download 'stopwords' library from NLTK package
from nltk.corpus import stopwords #import stopwords from NLTK package
text = ['Is Tranquility Meaning Given In Psalm 131 Now?','In the gentle moments of Matthew 19:13-14', 'we witness a profound teaching', 'Children in their innocence were brought to Jesus', 'and despite the disciples initial resistance' , 'Jesus welcomed them declaring', 'the kingdom of heaven belongs to such as these','This statement unveils a deep truth','the kingdom is not about adult-like ambition or', 'success but about embracing the pure qualities', 'of a child—chief among them trust.']
df = pd.DataFrame({'Tranquil Testament -> Daily Bible Study':text})
blanks1 = "=============Basic Data=============="
print(blanks1)
print(df)
blanks2 = "===================After Removing Stopwords=============="
#remove stop words
stop = stopwords.words('english')
df['Tranquil Testament -> Daily Bible Study'] = df['Tranquil Testament -> Daily Bible Study'].apply(lambda x: "".join(x for x in x.split() if x not in stop))
print(blanks2)
print(df['Tranquil Testament -> Daily Bible Study'])
#this code will keep window open
input("\nPress Enter to exit...")