def appearance(intervals: dict):

    def add_marker_and_sort(lst: list):
        '''function to add marker (1 for entry, -1 for leave) to list element inplace, then sort'''
        lst[0::2] = [(elem, 1) for elem in lst[0::2]]
        lst[1::2] = [(elem, -1) for elem in lst[1::2]]
        lst.sort(key=lambda x: x[0])

    def process_times(lst: list, full: int = 1):
        '''function to return intervals with right overlapping'''
        cur = 0
        res_lst = []

        for time, status in lst:
            if cur + status == full and cur == full - 1: # start
                res_lst.append((time, 1))
            if cur + status == full - 1 and cur == full: # stop
                res_lst.append((time, -1))
            cur += status

        return res_lst

    
    res_lst = []
    for _, val in intervals.items():
        add_marker_and_sort(val) # add markers to starts and stops, then sorting
        val = process_times(val) # getting rid of overlapping presence
        res_lst += val # concatenating lists into big one

    res_lst.sort(key=lambda x: x[0]) # sorting the big one

    # now getting intervals with all 3 present (lesson, tutor, pupil)
    res_lst = process_times(res_lst, 3) 
    # sum over differences in time
    res = sum([t * (-s) for t, s in res_lst])

    return res#, appearence_times, res_lst



    




tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [
                 1594702789, 1594704500, 
                 1594702807, 1594704542, 
                 1594704512, 1594704513, 
                 1594704564, 1594705150, 
                 1594704581, 1594704582, 
                 1594704734, 1594705009, 
                 1594705095, 1594705096, 
                 1594705106, 1594706480, 
                 1594705158, 1594705773, 
                 1594705849, 1594706480, 
                 1594706500, 1594706875, 
                 1594706502, 1594706503, 
                 1594706524, 1594706524, 
                 1594706579, 1594706641
                ],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


# res = appearance(tests[1]['data'])

# print('res: ', res)
# print('appearence_times: ', *appearence_times)
# print('res_lst: ', *res_lst)


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
