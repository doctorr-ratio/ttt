import string

print("Task #1")

# Simple pythonic-way solution, but works t~O(N)
def task_simple(array: string):
    return array.find('0')

# Hand-written binary search, works t~O(logN)
def task_fast(array: string):
    '''Let's realize binary search'''
    length = len(array)
    mid = length // 2
    left = 0
    right = length - 1

    # Under assumption that array with no 0 shoud return -1
    if length == 0 or array[-1] == '1': # not in, beacuse it's O(N)
        return -1
    elif array[0] == '0':
        return 0

    # Binary search for first zero
    while array[mid] != '0' and array[mid - 1] != '1':
        if array[mid] == '1':
            mid = (mid + right) / 2
            left = mid
        else:
            mid = (mid + left) / 2
            right = mid - 1

    return mid - 1

# Let's make some tests

tests = [
    {"data": "", "answer": -1},
    {"data": "0", "answer": 0},
    {"data": "00000", "answer": 0},
    {"data": "1", "answer": -1},
    {"data": "11111", "answer": -1},
    {"data": "1111110000000000000", "answer": 6}
]

if __name__ == '__main__':
    print("Tests for simple solution:")
    for i, test in enumerate(tests):
       test_answer = task_simple(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i} for simple solution, got {test_answer}, expected {test["answer"]}'


    print("Tests for simple solution:")
    for i, test in enumerate(tests):
       test_answer = task_fast(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i} for fast solution, got {test_answer}, expected {test["answer"]}'
