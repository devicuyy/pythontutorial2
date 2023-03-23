# 1. input 
sum=0
while True:
     x1 = input("Enter X1: ")
     x2 = input("Enter X2: ")
     op = input("Enter operator: ")
     if op == "+":
          sum= int(x1) + int (x2)
     elif op == "-":
          sum= int(x1) - int (x2)
     print(f"Sum: {sum}")
     res=input("Continue? (Y/N)")
     if res =="N":
          break;
