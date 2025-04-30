String_v1 = "I am exploring NLP"
#To extract particular character or range of characters from string
ec_roc_f_str = "===Extract Character (or) Range of Characters From String==="
print(ec_roc_f_str)
print(String_v1[0])

#To extract exploring
ex_word = "===Extract Word From String==="
print(ex_word)
print(String_v1[5:14])

#replace exploring with learning
repl_words = "===Replace Words==="
String_v2 = String_v1.replace("exploring", "learning")
print(repl_words)
print(String_v2)

#concatenate two strings
concat_strings = "===Concatenate 2 Strings==="
s1 = "nlp"
s2 = "machine learning"
s3 = s1+s2
print(concat_strings)
print(s3)

#Searching for a substring in a string
srch_substring_in_str = "===Search For Substring in a String==="
var="I am learning NLP"
f= "learn"
print(srch_substring_in_str)
print(var.find(f))

#keep window open & closes only if user press enter button
input("\nPress Enter to exit...")