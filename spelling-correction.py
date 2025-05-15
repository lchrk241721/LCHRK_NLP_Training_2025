text=['Introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity', 'R is good langauage','I like this book','I want more books like this']
# convert list to dataframe
import pandas as pd
from textblob import TextBlob
from autocorrect import Speller

df = pd.DataFrame({'LCHRK_NLP_TUTORIAL': text})
df2 = df['LCHRK_NLP_TUTORIAL'].apply(lambda x: str(TextBlob(x).correct()))
spell = Speller(lang="en")
#heading 1
rwdt = "====Given Original Data===="
#heading 2
scd = "=====Spelling Correction(manual method)===="
#heading 3
acsp = "=====Spelling Correction(automatic method)===="
print(rwdt)
# Print Only Raw Data
print(df)
print(scd)
# Print Spelling Corrected Data
print(df2)
print(acsp)
# print spelling corrected data with autocorrection
print(spell("I'm not slepy, I'm just tyred."))

