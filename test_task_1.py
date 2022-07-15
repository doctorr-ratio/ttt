import string

print("Task #1")

# Simple pythonic-way solution, but works t~O(N)
def task_simple(array: string):
    return array.find('0')

# Hand-written binary search, works t~O(logN)
def task_fast(array: string):
    '''Let's realize binary search'''
    length = len(array)
    left = 0
    right = length
    mid = (right + left) // 2

    # Under assumption that array with no 0 shoud return -1
    if length == 0 or array[-1] == '1': # not in, beacuse it's O(N)
        return -1
    elif array[0] == '0':
        return 0

    # Binary search for first zero
    while not (array[mid] == '0' and array[mid - 1] == '1'):
        mid = (right + left) // 2
        if array[mid] == '1':
            left = mid + 1
        else:
            right = mid - 1

    return mid

# Let's make some tests

tests = [
    {"data": "", "answer": -1},
    {"data": "0", "answer": 0},
    {"data": "00000", "answer": 0},
    {"data": "1", "answer": -1},
    {"data": "11111", "answer": -1},
    {"data": "10000", "answer": 1},
    {"data": "1110", "answer": 3},
    {"data": "1111110000000000000", "answer": 6}
]

if __name__ == '__main__':
    print("Tests for simple solution:")
    for i, test in enumerate(tests):
       test_answer = task_simple(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i} for simple solution, got {test_answer}, expected {test["answer"]}'
    print('DONE!')

    print("Tests for fast solution:")
    for i, test in enumerate(tests):
       test_answer = task_fast(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i} for fast solution, got {test_answer}, expected {test["answer"]}'
    print('DONE!')