#convert list to data frame
import pandas as pd
# read/create text data
text=['This is introduction to LCHRK_NLP_TRAINING_2025','It is likely to be useful,to people ','Machine learning is the new electrcity','There would be less hype around AI and more action going forward','python is the best tool!','R is good langauage','I like this book','I want more books like this']
df = pd.DataFrame({'tweet':text})
r_c_t_data = "=== Read/Create Text Data ==="
print(r_c_t_data)
print(df)

# execute lower() function on the text data
df['tweet'] = df['tweet'].apply(lambda x: " ".join(x.lower() 
for x in x.split()))
df['tweet']
ex_l_func_t_data = "=== Execute Lower Function On The Text Data ==="
print(ex_l_func_t_data)
print(df)
#this code will keep window open
input("\nPress Enter to exit...")
