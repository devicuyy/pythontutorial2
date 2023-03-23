
import math 

# 1. input 
while True:
     x1 = input("Enter X1: ")
     x2 = input ("Enter X2: ")
     x3 = input ("Enter X3: ")
     op = input("Enter operator: ")

# 2. Process 
     if op == "+":
          sum= int(x1) + int (x2)
     elif op == "-":
          sum= int(x1) - int (x2)
     elif op == "*":
          sum= int(x1) * int (x2)
     elif op == "/":
          sum= int(x1) / int (x2)
     elif op == "avg":
          sum= int(x1) + int (x2)/2
     elif op == "SD":
          mean = (int (x1) + int (x2) + int (x3))/3 
          tmp1 = int (x1) - mean 
          tmp2 = int (x2) - mean 
          tmp3 = int (x3) - mean 
          tmp4 = (int (tmp1)**2)+ (int (tmp2)**2) + (int (tmp3)**2)
          tmp5 = int (tmp4)/3
          sum = math.sqrt(tmp5)


# 3. Output
 
          print (f"Sum:{sum}") 
          res = input ("Continue? (Y/N)")
          if res == "N":
               break;