import random as r
#Function to provide random number with similar probability as two dice
def randdicenum():
	a=r.randint(1,6)
	b=r.randint(1,6)
	num=a+b
	return num
	
#Possibilities of dice numbers: 
#2/12:1/36
#3/11:2/36
#4/10:3/36
#5/9: 4/36
#6/8: 5/36
#7:   6/36
def prob(x):
	if (x==2 or x==12):
		return 1/36
	elif (x==3 or x==11):
		return 2/36
	elif (x==4 or x==10):
		return 3/36
	elif (x==5 or x==9):
		return 4/36
	elif (x==6 or x==8):
		return 5/36
	elif (x==7):
		return 6/36

csum=0
psum=0
for i in range(1, 4):
	#Computer set here
	startnum=randdicenum()
	rsum=startnum
	pr=prob(startnum)
	startnumposs=pr
  #Changing these numbers modifies computer performance.
  while (startnumposs<=0.5 or rsum<50):
		num=randdicenum()
		rsum=	rsum+num
		if num==startnum:
			rsum=0
			break
		startnumposs=startnumposs+pr
	print("This round:", rsum)
	csum=csum+rsum
	print("Computer total:", csum)

	#Player set here	
	startnum=randdicenum()
	rsum=startnum
	print("Your starting number is:", startnum)
	while(1):
		num=randdicenum()
		print("You have rolled", num)
		rsum=	rsum+num
		if num==startnum:
			rsum=0
			break
		print("Your total so far is", rsum)
		stop=input("Do you want to stop? y/n\n")
		if (stop=='y'):
			break
	print("This round:", rsum)
	psum=psum+rsum
	print("Player total:", psum)
	print()

#Finishing the round
print("Player has", psum, "points, and computer has", csum, "points.")
if (psum>csum):
	print("Player Wins!")
elif(psum==csum):
	print("It's a Draw.")
else:
	print("Computer Wins!")

