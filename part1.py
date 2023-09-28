# Time Complexity: O(n)
# 
# Basic Algorithm:
#   traversing to all inputs
#       Check if input divisiable for 3 and 5
#       Check if input divisiable for 3
#       Check if input divisiable for 5
#       Check if input divisiable neither
#
#


class Fizz:
    def fizzBuzz(self,n:int):
        arr=[]
        for i in range(1,n+1):              
            if i%3==0 and i%5==0:       
                arr.append("FizzBuzz")
            elif i%3==0:                
                arr.append("Fizz")
            elif i%5==0:                
                arr.append("Buzz")
            else:                       
                arr.append(str(i))
        return arr

#creating an object of the above class so as to execute the function
f=Fizz()
#Function calls for sample
print(f.fizzBuzz(3))                            #test 1
print(f.fizzBuzz(5))                            #test 2
print(f.fizzBuzz(15))                           #test 3
