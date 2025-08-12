comment=input("enter the comments:")
msg1="Make a lot of money"
msg2="buy now"
msg3="subscribe this"
msg4="click this"
if(msg1 in comment or msg2 in comment or msg3 in comment or msg4 in comment):
    print("Spam")
else:
    print("You are safe")