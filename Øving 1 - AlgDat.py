
def insertion_sort(A):
    for i in range(1, len(A)): #start from index 1 and the length of the list A
      currentKey = A[i]                #first key 

      while (A[i-1] > currentKey and i > 0):   #if the previous key is bigger than curretnKey and i > 0, swap places. 
          A[i], A[i-1] = A[i-1], A[i]
          i -= 1
    return A


def take_pieces(n_pieces):
    if (n_pieces % 8 > 7):
        return range(1,8)
    else:
    	return n_pieces % 7


if __name__ == "__main__":

    tests = [
        (1, None),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 4),
        (6, 5),
        (7, 6),
        (8, 7),
    ]

    for (test, correct_answer) in tests:
        answer = take_pieces(test)

        if answer not in (1, 2, 3, 4, 5, 6, 7):
            print("Funksjonen returnerte en ugyldig verdi: {:}".format(answer))

        if answer != correct_answer and correct_answer is not None:
            print(
                "Koden feilet for følgende antall fyrstikker: {:}".format(test)
            )