import random

uppercase=["A","B","C","D"]
lowecase=["a","b","c""d"]
numbre=[1,2,3,4]
special=["#","*","^","%"]
password=random.choice(lowecase) + random.choice(uppercase) +str(random.choice(numbre)) +str(random.choice(special))
print(password)