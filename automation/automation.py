import re



with open("assets/potential-contacts.txt","r")as file:
    data=file.read()
    print(data)

def phone_num(data):
    pattern_num=r"[0-9-+x.()]{7,}"
    phone_nums=[]

    nums=re.findall(pattern_num,data)
    for num in nums:
        num=num.replace(".","").replace("(","").replace(")","")
        if len(num)==10:
            num=num[:3]+"-"+num[3:6]+"-"+num[6:]
        phone_nums.append(num)
    phone_nums=list(set(phone_nums)) # remove duplicat
    phone_nums.sort() #ascend
    return phone_nums

# https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/   for email regex pattern 
def email(data):
    pattern_email=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails=re.findall(pattern_email,data)
    emails=list(set(emails)) # remove duplicat
    emails.sort() #ascend
    return emails

with open("assets/phone_numbers.txt","w") as file:
    string2=""
    for item in phone_num(data):
        string2+=item+"\n"
    file.write(string2)

with open("assets/emails.txt","w") as file:
    string1=""
    for item in email(data):
        string1+=item+"\n"
    file.write(string1)

if __name__=="__main__":
  x=phone_num(data)
  print(x)
  y=email(data)
  print(y)

