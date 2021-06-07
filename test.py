import random
lower_case=['a',"b","c","d","e"]
upper_case=["A","B","C","D","E"]
special_char=["!","@","%","^","*"]
numbres=["1","2","3","4","5"]

password=random.choice(lower_case)+random.choice(upper_case)+random.choice(special_char)+random.choice(numbres)
password+=password+password

print(password)