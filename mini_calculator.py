# mini calculator

first = input("first number: ")
second = input("second number: ")
operation = input("enter operation(1-addition,2-subtraction,3-multiplication,4-division,5-remainder): ")
first = int(first)
second = int(second)
operation = int(operation)
if operation == 1 :
    print(first + second)
elif operation == 2 :
    print(first - second)
elif operation == 3 :
    print(first * second) 
elif operation == 4 :
    print(first / second)        
elif operation == 5 :
    print(first % second)  
else:
    print("choose valid operation")                             
