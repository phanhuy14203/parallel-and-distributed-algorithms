#21520935 - Phan Quoc Huy
#21520780 - Nguyen Thanh Duy

import numpy as np
import multiprocessing 
import time
def flatten(matran):
    return [phantu for hang in matran for phantu in hang]
def chia_ma_tran(matran, n):
    so_hang = len(matran)
    kich_thuoc_moi = so_hang // n
    mang_chia = []
    for i in range(0, so_hang, kich_thuoc_moi):
        mang_chia.append(matran[i:i + kich_thuoc_moi])
    return mang_chia 
def Flatten_X(a):
    procs = multiprocessing.cpu_count()
    pool = multiprocessing.Pool()
    mang_ma_tran_con = chia_ma_tran(a, procs)
    results = pool.map(flatten, mang_ma_tran_con)
    ma_tran_1d = [phantu for sublist in results for phantu in sublist]
    return ma_tran_1d
if __name__ == '__main__':
  A = np.random.randint(0, 100, size=(1000, 1000))
  s = time.time_ns()
  B = Flatten_X(A)
  e = time.time_ns()
  print(B)
  print("flatten in:", (e-s)/10**9)