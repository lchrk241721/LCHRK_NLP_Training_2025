import re

#run the split query
output = re.split('\s+','I like this book.')
splitq = "===split query==="
print(splitq)
print(output)

#extract email address
doc = "For more details, please email us at: info@tranquiltestament.com"
extractemail = "===extract email==="
print(extractemail)
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
for address in addresses:
    print(address)

#replace email id
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'tranquiltestament@gmail.com', doc)
replace_email = "===replace email==="
print(replace_email)
print(new_email_address)


