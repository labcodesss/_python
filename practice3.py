text =input("enter text")


if("make a lot money" in text):
    spam = True
elif("now!!! "in text):
    spam =True
else:
    spam=False        
 

if(spam):
    print("Spam detected")
else:
    print("Not spam")
