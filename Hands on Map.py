number1=[1,2,3]
number2=[4,5,6]
result=map(lambda x,y:x+y,number1,number2)
result=list(result)
print(result)

numbers=[1,2,3,4,5,6,7]
def sq(n):
    return n*n
square=list (map(sq,numbers))
print(square)