#!/usr/bin/python3
# coding=utf-8


def sheet_cutting(w, h, p, subsolutions = {}):
    if w == 1 and h == 1:
        return p[(1,1)]
    if (w,h) in subsolutions:
        return subsolutions[(w,h)]

    reduce_width = 0 
    reduce_height = 0
    if 1 < w:
        reduce_width = sheet_cutting(w-1,h,p, subsolutions) + sheet_cutting(1,h,p, subsolutions)
    if 1 < h:
        reduce_height = sheet_cutting(w,h-1,p, subsolutions) + sheet_cutting(w,1,p, subsolutions)
    
    subsolutions[(w,h)] = max(reduce_height, reduce_width, p[(w,h)])
    return subsolutions[(w,h)]
    

# Tester på formatet (p, w, h, solution)
tests = [
    ({(1, 1): 1}, 1, 1, 1),
    ({(1, 1): 1, (2, 1): 3, (1, 2): 3, (2, 2): 3}, 2, 2, 6),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 5}, 2, 2, 5),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (2, 1): 0, (1, 2): 0, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (1, 2): 1}, 1, 2, 2),
    ({(1, 1): 1, (2, 1): 3}, 2, 1, 3),
    (
        {(1, 1): 1, (2, 1): 2, (1, 2): 2, (3, 1): 4, (2, 2): 3, (3, 2): 7},
        3, 2, 8,
    ),
    (
        {(1, 1): 1, (2, 1): 2, (1, 2): 2, (1, 3): 4, (2, 2): 3, (2, 3): 7},
        2, 3, 8,
    ),
    (
        {(1, 1): 1, (2, 1): 3, (3, 1): 3, (4, 1): 7, (5, 1): 3, (6, 1): 8},
        6, 1, 10,
    ),
    (
        {(1, 1): 1, (1, 2): 2, (2, 1): 2, (1, 3): 1, (3, 1): 1, (1, 4): 2,
         (4, 1): 2, (1, 5): 2, (5, 1): 2, (1, 6): 5, (6, 1): 5, (1, 7): 10,
         (7, 1): 10, (1, 8): 10, (8, 1): 10, (2, 2): 5, (2, 3): 5,
         (3, 2): 5, (2, 4): 2, (4, 2): 2, (2, 5): 10, (5, 2): 10,
         (2, 6): 7, (6, 2): 7, (2, 7): 11, (7, 2): 11, (2, 8): 16,
         (8, 2): 16, (3, 3): 1, (3, 4): 1, (4, 3): 1, (3, 5): 1, (5, 3): 1,
         (3, 6): 11, (6, 3): 11, (3, 7): 11, (7, 3): 11, (3, 8): 24,
         (8, 3): 24, (4, 4): 12, (4, 5): 25, (5, 4): 25, (4, 6): 29,
         (6, 4): 29, (4, 7): 25, (7, 4): 25, (4, 8): 9, (8, 4): 9,
         (5, 5): 12, (5, 6): 10, (6, 5): 10, (5, 7): 26, (7, 5): 26,
         (5, 8): 45, (8, 5): 45, (6, 6): 35, (6, 7): 44, (7, 6): 44,
         (6, 8): 50, (8, 6): 50, (7, 7): 1, (7, 8): 41, (8, 7): 41, (8, 8): 5},
        8, 8, 91,
    )
]

failed = False

for prices, width, height, solution in tests:
    student_answer = sheet_cutting(width, height, prices)
    if student_answer != solution:
        failed = True
        print(
            "Feilet for testen w={:} h={:} ".format(width, height)
            + "p={:}, resulterte i ".format(prices)
            + "svaret {:} i stedet for {:}.".format(student_answer, solution)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")