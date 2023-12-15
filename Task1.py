
#Basic operators in python
#arithmatic operators
a = 20
b = 4

c = (a + b)              #addition
print(c)

c = (a - b)               #subtraction
print(c)

c = (a * b)               #multiplication
print(c)

c = (a / b)                #division
print(c)

c = (a % b)                #modulus
print(c)

c = (a ** b)               #exponent
print(c)

c = (a // b)               #floor division
print(c)

#Relational operators

print(a < b)              #lees than

print(a > b)               #greater than

print(a <= b)               #less than equal to

print(a >= b)                #greater than equal to

print(a == b)                #equal to

print(a != b)               #not equal to

#logical operators
print(a > b and a < b)           #and
    #true       #false
print(a > b or a < b)             #or
      #true     #false
print(not a == b)               #not (works with boolean value)
           #false

#Bitwise operator
x = 7
y = 9
print(x & y)            #bitwise and
print(x | y)            #bitwise or
print(x ^ y)            #bitwise XOR
print(~ x)             #bittwise not (convert decimal into binary inverts all bits and convrt binary back to decimal)
print(~ y)             #(works with int value )
print(x << 1)         #left shift one time
print(y >> 1)         #right shift one time

#Assignment operator
a = 50
print(a)
a += 10
print(a)
a -= 10
print(a)
a /= 10
print(a)
a %= 10
print(a)
a //= 10
print(a)
a **= 10
b = 30
print(a)
b &= 10
print(b)
b |= 10
print(b)
b ^= 10
print(b)

#Identity operator
a = 10
b = 10
print (a is b)
print(a is not b)
a = 5
b = 9
print(a is b)
print(a is not b)

#membership operator
name = "My name is mamoona"
print("name" in name)
        #true
print("name" not in name) #false
print("Hoor" not in name)   #true
print("Hoor" in name)  #false

#Ternary operator
marks = 50
print("You are pass." if marks > 30 else "You are fail.")


#any and all operator in python
L1 = [0, 1, 0, 1, 0, 0]
L2 = [1, 1, 1, 1, 1, 1]
print(any(L1))
print(any(L2))

print(all(L1))
print(all(L2))

#inplace operators
a = 10
a += 10
print(a)
a -= 10
print(a)
a *= 10
print(a)
a /= 2
print(a)
a %= 5
print(a)

a = [2,3,4]
a += [5,6,7]
print(a)
#standard operators
x = 10
x = x + 5
print(x)

x = [1,2,3]
x = x + [4,5,6]
print(x)

#operator functions in python
import operator
#arithmatic
a = operator.add(5,10)
print(a)
a = operator.sub(5,10)
print(a)
a = operator.mul(5,10)
print(a) 
a = operator.truediv(5,10) 
print(a)
a = operator.floordiv(5,10)
print(a)
a = operator.mod(5,10)
print(a) 
a = operator.pow(5,10) 
print(a)
#relational
print(operator.eq(5,10))
print(operator.ne(5,10))
print(operator.lt(5,10))
print(operator.le(5,10))
print(operator.gt(5,10))
print(operator.ge(5,10))
#logical
print(operator.and_(0,1))
print(operator.or_(0,1))
print(operator.not_(0))

#inplace operator set 1

a =  operator.iadd(9,10)
print(a)
a =  operator.isub(9,10)
print(a)
a =  operator.imul(9,10)
print(a)
a =  operator.imod(9,10)
print(a)
a =  operator.itruediv(9,10)
print(a)
a =  operator.iconcat('Mamoona',' Shamraiz')
print(a)
#Logic gates in python
#AND
def AND(false, true):
  return false and true
print(AND(False, False)) 
print(AND(False, True))   
print(AND(True, False))   
print(AND(True, True))  
#OR
def OR(true, false):
  return true or false
print(OR(False, False)) 
print(OR(False, True))   
print(OR(True, False))   
print(OR(True, True))
#NOT
def NOT(true):
  return not true
print(NOT(True))   
print(NOT(False)) 
#XOR
def XOR(true, false):
    return (true or false) and not (true and false)
print(XOR(False, False))  
print(XOR(False, True)) 
print(XOR(True, False))
print(XOR(True, True))

#a += b is not always a = a + b
#immutable
a = 5
b = 3
a += b  # This is equivalent to a = a + b
print(a)
a = a + b
print(a) 

#mutable
a = [1, 2, 3]
a += [4, 5] # Modifies existing list
print(a)

b = [1, 2, 3]
b = b + [4, 5] # Creates new list
print(b) 

#Difference between == and is operator in Python
a = 10
b = 10
print(a == b)
print( a is b)








