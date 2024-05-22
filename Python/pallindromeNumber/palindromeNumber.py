import math
def palindrome(number):
    if ( number == 0):
        return(True)
    elif (number < 0):
        return(False)
    else:
        numDigits = int(math.log10(number)) + 1        
        MSD = 10**(numDigits-1)
        for _ in range(0,numDigits//2):

            if( number%10 != number//MSD):
                return(False)

            number %= MSD
            number //= 10
            MSD //= 100

        return(True)


number = int(input("Enter the number: "))
print("The numnber is", "a palindrome" if palindrome(number) else "not a palindrome")