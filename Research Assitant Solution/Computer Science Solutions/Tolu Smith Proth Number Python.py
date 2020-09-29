#QUESTION
# Write a function that takes in a Proth Number and uses
# Proth's theorem to determine if said number is prime?

#ANSWER
# Given a positive integer n, check if it is a Proth number. 
# If the given number is a Proth number then print ‘Yes!’ else print ‘No!’.
# Proth Number, In mathematics,is a positive integer of the form  n = k * 2n + 1
# where k is an odd positive integer and n is a positive integer such that 2n > k .

#SOLUTION

def isPowerOfTwo(n): #Check The Power Of Two
		
	return (n and (not(n & (n - 1)))) 

def isProthNumber( n):  # Check If The Given Number Is Proth Number Or Not

	k = 1
	
	while(k < (n//k)): # check if k divides n or not 
		
		if(n % k == 0): # Check if n / k is power of 2 or not 
			
			if(isPowerOfTwo(n//k)): 
					return True
		
		# update k to next odd number 
		k = k + 2	
	
	
	return False

# Get The Value For n
while True:
    print("Press 0 to end Program");
    n = int(input("Input a number to check for Proth's Validity: "));
    if(n == int("0")):
        print("Program Closed")
        break;
    if(isProthNumber(n-1)):
        print("Yes!, {} is a Proth Number".format(n));
    else: print("No!,{} is not a Proth Number".format(n)); 


