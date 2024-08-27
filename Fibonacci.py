import multiprocessing
import time
import numpy as np

def MatMul(matA, matB):
    matC = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                matC[i][j] += matA[i][k]*matB[k][j]
    return matC

def fibo(n):
    a = [[1,1],[1,0]]
    matrix = [[1,1],[1,0]]
    for i in range(n-1):
        a = MatMul(a, matrix)

    return a

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        n -= 1
        pool = multiprocessing.Pool()
        fib1 = pool.apply_async(fibo, args = (n//2, ))
        fib2 = pool.apply_async(fibo, args = (n - n//2, ))
        result = MatMul(fib1.get(), fib2.get())
        return result[0][0]
         

if __name__ == "__main__":
    n = 20000
    start = time.time()
    fibo = fibonacci(n)
    end = time.time()
    print("So fino thu ", n)
    exetime = end - start
    print("exetime: ","{:.5f}".format(exetime))
