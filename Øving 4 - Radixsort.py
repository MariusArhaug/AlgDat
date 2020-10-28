def char_to_int(char):
    return ord(char) - 97

def int_to_char(int):
    return chr(int+97)

def flexradix(A, d):
    k = len(A)

    exp = 1
    while d/exp > 0:
        counting_sort(A,k,exp)
        exp *= 10
    

def counting_sort(A, k, exp):
    C = [0 for i in range(k)]
    B = [0] * len(A)
    for j in range(0,len(A)):
        C[ int((A[j]/exp)%10) ] += 1

    for i in range(1,k):
        C[i] = C[i] + C[i-1]

    for j in range(len(A)-1,-1,-1):
        B[C[ int((A[j]/exp)%10)] -1] = A[j]
        C[ int((A[j]/exp)%10)] -= 1

    for i in range(len(A)):
        A[i] = B[i] 

tests = (
    (([], 1), []),
    (([1], 1), [1]),
    (([1, 2], 1), [1, 2]))


"""tests = (
    (([], 1), []),
    ((["a"], 1), ["a"]),
    ((["a", "b"], 1), ["a", "b"]),
    ((["b", "a"], 1), ["a", "b"]),
    ((["ba", "ab"], 2), ["ab", "ba"]),
    ((["b", "ab"], 2), ["ab", "b"]),
    ((["ab", "a"], 2), ["a", "ab"]),
    ((["abc", "b"], 3), ["abc", "b"]),
    ((["abc", "b"], 4), ["abc", "b"]),
    ((["abc", "b", "bbbb"], 4), ["abc", "b", "bbbb"]),
    ((["abcd", "abcd", "bbbb"], 4), ["abcd", "abcd", "bbbb"]),
    ((["a", "b", "c", "babcbababa"], 10), ["a", "b", "babcbababa", "c"]),
    ((["a", "b", "c", "babcbababa"], 10), ["a", "b", "babcbababa", "c"]),
)"""

for test, solution in tests:
    student_answer = flexradix(test[0], test[1])
    if student_answer != solution:
        print(
            "Feilet for testen {:}, resulterte i listen ".format(test)
            + "{:} i stedet for {:}.".format(student_answer, solution)
        )