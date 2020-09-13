#Day9
#Assignment1

%%writefile testPrime.py
import unittest
import primecheck

class testPrime(unittest.TestCase):
    def testnumprime(self):
        x=13
        result=primecheck.primeornot(x)
        self.assertEquals(result,"It is a prime number")
if __name__=="__main__":
    unittest.main()

#output    
'''Overwriting testPrime.py'''

!python testprime.py
#output
#It is a prime number



#Assignment2

print("Enter 'x' for exit.");
print("Enter the interval (starting and ending number): ");
start = input();
if start == 'x':
    exit();
else:
    end = input();
    lower = int(start);
    upper = int(end);
    for num in range(lower, upper+1):
        tot = 0;
        temp = num;
        while temp != 0:
            dig = temp % 10;
            tot += dig ** 3;
            temp //= 10;
        if num == tot:
            print(num);
            
'''
output:            
Enter 'x' for exit.
Enter the interval (starting and ending number): 
1
1000
1
153
370
371
407
'''