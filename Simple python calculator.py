#Def 
def Add(x , y ):
  return x + y 

def Minus(x , y):
  return x - y

def Div(x , y):
  return x / y 

def Multiply(x , y):
  return x * y 

#Inputs 
x = int(input('Give number one '))

op = input('Give an operation ')

y = int(input('Give number two '))


#Answer
answer = Add(x , y )

answer2 = Minus(x , y)

answer3 = Div(x , y)

answer4 = Multiply(x , y)

#If statements and print 
if op == '+':
  print(x , '+' , y , '=' , answer)

elif op == '-':
  print( x , '-' , y , '=' , answer2)

elif op == '/':
    print(x , '/' , y , '=' , answer3)

elif op == 'x':
  print(x , 'x' , y , '=' , answer4)

else:
  print('nothing')
    
