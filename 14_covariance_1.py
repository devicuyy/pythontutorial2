#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    cov = 0 
    print(f'Input X : {input_x},', f'Input Y: {input_y}')

    N = len(input_y)

    Mean_X = statistics.mean(input_x)
    Mean_Y = statistics.mean(input_y)
    print(f'Mean X : {Mean_X},' f'Mean Y : {Mean_Y}')

    for r in range (len(input_x)): 
        cov += (input_x[r]-Mean_X) * (input_y[r]-Mean_Y)
    COVxy = cov/N 
    return COVxy 

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'Answer: {answer}')
