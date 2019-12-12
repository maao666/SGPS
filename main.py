#!/usr/local/bin/python3
import math
import scipy


class Point:
    x, y = 0, 0

    def set_xy(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)


class Segment:
    p1, p2 = None, None
    name = ''

    def __init__(self, name):
        self.name = name

    def get_length(self) -> float:
        if isinstance(self.p1, Point):
            return math.sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)
        return 0

    def set_points(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        return self

    def __str__(self):
        return self.name


class Triangle:
    p1, p2, p3 = None, None, None
    s1, s2, s3 = None, None, None
    name = ''

    def __init__(self, name):
        self.name = name

    def set_points(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.s1 = Segment('default').set_points(p1, p2)
        self.s2 = Segment('default').set_points(p2, p3)
        self.s3 = Segment('default').set_points(p1, p3)
        return self

    def get_area(self) -> float:
        if isinstance(self.p1, Point):
            s = (self.s1.get_length() + self.s2.get_length() + self.s3.get_length()) / 2
            return math.sqrt(s*(s - self.s1.get_length())*(s - self.s2.get_length())*(s - self.s3.get_length()))
        return 0

    def get_segments(self):
        return self.s1, self.s2, self.s3

    def get_points(self):
        return self.p1, self.p2, self.p3

    def __str__(self):
        return self.name


class Solver:
    predicates = {'parallel': [],
                  'perpendicular': [],
                  'equal': [],
                  'fraction': [],
                  'sum': [],
                  'similar': [],
                  'congruent': [],
                  'tan': []}

    def parse_input(self, raw_predicates: str):
        raw_predicates = raw_predicates.replace('sum_value', 'sum')
        for line in raw_predicates.splitlines():
            index = str(line[line.index('set_')+4:line.index('(')].strip())
            params = [i.strip() for i in line[line.index('(')+1:line.index(')')].split(',')]
            if len(params) == 3:
                params[-1] = int(params[-1])
            self.predicates.get(index,[]).append(params)

        return self


if __name__ == '__main__':
    with open('shit.txt', mode='r') as f:
        solver = Solver().parse_input(f.read())
        print(solver.predicates)
