#my solution for leetcode.com/problems/palindrome-number/

def isPalindrome(x):
    if x < 0:
        return False
    elif x < 10:
        return True
    elif x%10==0:
        return False
    else:
        x_length = 0
        x_copy = x
        while x_copy > 0:
            x_length+=1
            x_copy = x_copy//10
        x_copy = x 
        for j in range(x_length//2):
            if x//(10**(x_length-1-j)) != x_copy%10:
                print("x//(10**("+str(x_length)+"-1-"+str(j)+" = "+str(x//(10**(x_length-1-j))))
                print("j = " + str(j) + "x_copy = " + str(x_copy) + " x = "+ str(x))
                return False
            x_copy = x_copy//10
            x = x%(10**(x_length-1-j))
        return True



x = int(input())
print(isPalindrome(x))


