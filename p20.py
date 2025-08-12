post=input("Enter the post:")
if("Harry"in post):
    print("Yes")
elif("Harry".lower() in post.lower()):
    print("Yes")
else:
    print("No")