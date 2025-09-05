player1=input("Enter your choice:")#String choices
dict1={"s":1,"w":-1,"g":0}#Converting the string to its corresponding  integer values
p1=dict1[player1]
player2=input("Enter your choice:")#String choices
p2=dict1[player2]#Converting the string into its corresponding integer values
dict2={1:"Snake",-1:"Water",0:"Gun"}#Converting the integer choices into its corresponding string values
print(f"Player1 chose {dict2[p1]} and Player2 chose {dict2[p2]}")
if(p1==1 and p2==-1):
    print("Player 1 wins!!")
elif(p1==-1 and p2==0):
    print("Player 1 wins!!")
elif(p1==0 and p2==1):
    print("Player 1 wins!!")
elif(p1==-1 and p2==1):
    print("Player 2 wins!!")
elif(p1==0 and p2==-1):
    print("Player 2 wins!!")
elif(p1==1 and p2==-0):
    print("Player 2 wins!!")
elif(p1==p2):
    print("It's a draw!!!")
else:
    print("Invalid choice")