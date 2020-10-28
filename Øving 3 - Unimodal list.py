import random
import sys

random.seed(123)

def find_maximum(list):
    if len(list) == 1:
        return list[0]   
    return findMax(list, 0, len(list)-1)


def findMax(list, start, stop):
    median = (start+stop)//2

    if stop - start < 2:
        return max(list[start], list[stop]) 

    #if start is ascending then descending then we know that median is max value
    if list[start-1] < list[start] > list[start+1]: 
            return list[start]

    #if start is ascending
    if list[start-1] < list[start] < list[start+1]:
        #then if median is ascending we know where to divide next, the interval from [median, stop]
        if list[median] < list[median+1] and list[start] < list[median]:
            return findMax(list, median, stop)

        #if not, then we divide from [start, median]
        return findMax(list, start, median)

    
    elif list[median] < list[start] or list[median] < list[median+1]:
       return findMax(list, median, stop)
    
    return findMax(list, start, median)


# Noen håndskrevne tester
tests = [
    ([1], 1),
    ([1, 3], 3),
    ([3, 1], 3),
    ([1, 2, 1], 2),
    ([1, 0, 2], 2),
    ([2, 0, 1], 2),
    ([0, 2, 1], 2),
    ([0, 1, 2], 2),
    ([2, 1, 0], 2),
    ([2, 3, 1, 0], 3),
    ([2, 3, 4, 1], 4),
    ([2, 1, 3, 4], 4),
    ([4, 2, 1, 3], 4),
]


def generate_random_test_case(length, max_value):
    test = random.sample(range(max_value), k=length)
    m = max(test)
    test.remove(m)
    t = random.randint(0, len(test))
    test = sorted(test[:t]) + [m] + sorted(test[t:], reverse=True)
    t = random.randint(0, len(test))
    test = test[t:] + test[:t]
    return (test, m)


def test_student_maximum(test_case, answer):
    student = find_maximum(test_case)
    if student != answer:
        if len(test_case) < 20:
            response = (
                "'Find maximum' feilet for følgende input: "
                + "(x={:}). Din output: {:}. ".format(test_case, student)
                + "Riktig output: {:}".format(answer)
            )
        else:
            response = (
                "Find maximum' feilet på input som er "
                + "for langt til å vises her"
            )
        print(response)
        sys.exit()


# Testing student maximum on custom made tests
for test_case, answer in tests:
    test_student_maximum(test_case, answer)

# Testing student maximum on random test cases
for i in range(40):
    test_case, answer = generate_random_test_case(random.randint(1, 10), 20)
    test_student_maximum(test_case, answer)