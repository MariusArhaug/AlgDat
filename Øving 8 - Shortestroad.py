#!/usr/bin/python3
# coding=utf-8


def shortest_road(build_map, start, end):
    road = []
    road.append(start)
    for i in range(len(build_map)):
        for j in range(len(build_map[i])):
            if build_map[i][j] == True and (i,j) not in road:
                road.append((i,j))

    if road[len(road)-1] == end:
        
    return None
    
    
import collections
 
"""def shortest_road(build_map, start, end):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for northSouth, eastWest in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= northSouth < len(build_map) and 0 <= eastWest < len(build_map[0]) and build_map[northSouth][eastWest] != False and (northSouth, eastWest) not in seen:
                queue.append(path + [(northSouth, eastWest)])
                seen.add((northSouth, eastWest))    """

# Disjoint-set forest
class Set:
    def __init__(self):
        self.__p = self
        self.rank = 0

    @property
    def p(self):
        if self.__p != self:
            self.__p = self.__p.p
        return self.__p

    @p.setter
    def p(self, value):
        self.__p = value.p


def union(x, y):
    x = x.p
    y = y.p
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        y.rank += x.rank == y.rank


# fmt: off
tests = [
    (([[True, True]], (0, 1), (0, 0)), 2),
    (([[True, False, True]], (0, 0), (0, 2)), None),
    (([[True, True, True]], (0, 0), (0, 2)), 3),
    (([[True, True, False]], (0, 1), (0, 0)), 2),
    (([[True], [True]], (1, 0), (0, 0)), 2),
    (([[True, False], [True, True]], (0, 0), (1, 1)), 3),
    (([[False, True], [True, True]], (0, 1), (1, 0)), 3),
    (([[True, True], [True, True]], (1, 1), (0, 0)), 3),
    (([[False, False, True], [True, False, True]], (1, 2), (0, 2)), 2),
    (([[False, False], [True, True], [False, False]], (1, 1), (1, 0)), 2),
    (([[True, False], [True, False]], (0, 0), (1, 0)), 2),
    (([[True, False], [False, False], [True, True]], (0, 0), (2, 1)), None),
    (([[False, False, True], [False, False, True], [True, False, True]], (0, 2), (2, 2)), 3),
    (([[False, False], [True, True], [False, False]], (1, 1), (1, 0)), 2),
    (([[True, True, True], [False, False, False]], (0, 2), (0, 1)), 2),
    (([[True, False, True], [True, False, False]], (0, 2), (1, 0)), None),
    (([[True, True], [False, False], [False, True]], (0, 0), (0, 1)), 2),
    (([[False, True, False], [False, True, False]], (1, 1), (0, 1)), 2),
]
# fmt: on

for test_case, answer in tests:
    build_map, start, end = test_case
    student_map = [i[:] for i in build_map]
    student = shortest_road(student_map, start, end)
    response = None
    if answer is None and student is not None:
        response = (
            "Du returnerte en liste med posisjoner når riktig svar var None."
        )
    elif student is None and answer is not None:
        response = "Du returnerte None, selv om det finnes en løsning."
    elif student is not None and answer < len(student):
        response = "Det finnes en liste med færre koordinater som fortsatt danner en gyldig vei."
    elif student is not None:
        for pos in student:
            if not (
                0 <= pos[0] < len(build_map)
                and 0 <= pos[1] < len(build_map[0])
            ):
                response = "Du prøver å bygge utenfor kartet."
                break
            if not build_map[pos[0]][pos[1]]:
                response = (
                    "Du prøver å bygge en plass der det ikke er mulig å bygge."
                )
                break
        else:
            disjoint_set = {pos: Set() for pos in student}
            for pos in student:
                for i, j in [
                    (pos[0] + 1, pos[1]),
                    (pos[0] - 1, pos[1]),
                    (pos[0], pos[1] + 1),
                    (pos[0], pos[1] - 1),
                ]:
                    if (i, j) in disjoint_set and disjoint_set[
                        (i, j)
                    ].p != disjoint_set[pos].p:
                        union(disjoint_set[pos], disjoint_set[(i, j)])
            if start not in disjoint_set:
                response = "Du har ikke med startlandsbyen i listen."
            if end not in disjoint_set:
                response = "Du har ikke med sluttlandsbyen i listen."
            if disjoint_set[start].p != disjoint_set[end].p:
                response = "Listen din gir ikke en sammenhengende vei."
    if response is not None:
        response += " Input: (build_map={:}, start={:}, ".format(
            build_map, start
        )
        response += "end={:}). Ditt svar: {:}".format(end, student)
        print(response)
        break