import random
import multiprocessing

def generate_random_array(length):
    array = []
    for _ in range(length):
        array.append(random.randint(1, 1000))  # Thay đổi phạm vi [1, 100] nếu cần
    # for i in range(length):
    #     array.append(i+1)
    return array

def split_array(array, num_subarrays):
    subarray_size = len(array) // num_subarrays
    subarrays = [array[i:i+subarray_size] for i in range(0, len(array), subarray_size)]
    return subarrays

def calculate_prefix_sum(array):
    prefix_sum = [0] * len(array)
    prefix_sum[0] = array[0]

    for i in range(1, len(array)):
        prefix_sum[i] = prefix_sum[i-1] + array[i]

    return prefix_sum

def merge_arrays(subarrays):
    merged_array = []
    for subarray in subarrays:
        merged_array.extend(subarray)
    return merged_array

def parallel_prefix_sum(array):
    subarrays = split_array(array,4)
    pool = multiprocessing.Pool()
    results = pool.map(calculate_prefix_sum, subarrays)
    for i in range(1, len(results)):
        results[i] = [results[i-1][-1] + results[i][j] for j in range(len(results[i]))]
    result = merge_arrays(results)
    return result

import time

if __name__ == '__main__':
    array = generate_random_array(10000000)
    s = time.time_ns()
    array = parallel_prefix_sum(array)
    e = time.time_ns()
    print("exe time: ", (e-s)/10**9)