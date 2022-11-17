'''calculator prgm'''
def add(x,y):
    '''function to add 2 numbers'''
    if x+y is not None:
        return x+y
    return "wrong input"

x=int(input("Enter the value of x : "))
y=int(input("Enter the value of y : "))
print(add(x,y))
