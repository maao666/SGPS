#!/usr/local/bin/python3
import math
from copy import deepcopy
from pprint import pprint

global inputs
inputs = ''

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

    def __init__(self, name: str):
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


class Corner:
    name = ''
    angle = 0

    def __init__(self, name: str):
        self.name = name


class Triangle:
    p1, p2, p3 = None, None, None
    s1, s2, s3 = None, None, None
    name = ''

    def __init__(self, name: str):
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
            s = (self.s1.get_length() + self.s2.get_length() +
                 self.s3.get_length()) / 2
            return math.sqrt(s*(s - self.s1.get_length())*(s - self.s2.get_length())*(s - self.s3.get_length()))
        return 0

    def get_segments(self):
        return self.s1, self.s2, self.s3

    def get_points(self):
        return self.p1, self.p2, self.p3

    def __str__(self):
        return self.name


class Solver:
    INIT = (0, 0)
    areas = {'ar1': INIT,
             'ar2': INIT,
             'ar3': INIT,
             'ar4': INIT,
             'ar5': INIT,
             'ar6': INIT}

    segments = {'sa1': INIT, 'sb1': INIT, 'sc1': INIT,
                'sa2': INIT, 'sb2': INIT, 'sc2': INIT,
                'sa3': INIT, 'sb3': INIT, 'sc3': INIT,
                'sa4': INIT, 'sb4': INIT, 'sc4': INIT,
                'sa5': INIT, 'sb5': INIT, 'sc5': INIT,
                'sa6': INIT, 'sc6': INIT}

    angles = {'a1': INIT, 'b1': INIT, 'c1': INIT,
              'a2': INIT, 'b2': INIT, 'c2': INIT,
              'a3': INIT, 'b3': INIT, 'c3': INIT,
              'a4': INIT, 'b4': INIT, 'c4': INIT,
              'a6': INIT, 'c6': INIT}

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
            params = [i.strip()
                      for i in line[line.index('(')+1:line.index(')')].split(',')]
            if len(params) == 3:
                params[-1] = int(params[-1])
            self.predicates.get(index, []).append(params)

        return self

    def add_p(self, index: str, lst: list):
        lst2 = lst.copy()
        lst2[0], lst2[1] = lst2[1], lst2[0]
        if lst in self.predicates[index] or lst2 in self.predicates[index]:
            return
        self.predicates[index].append(lst)

    def generate_seq(self, l1, l2) -> list:
        return [[i, j] for i in l1 for j in l2]

    def parallel(self, s1, s2) -> bool:
        return [s1, s2] in self.predicates['parallel'] or [s2, s1] in self.predicates['parallel']

    def batch_parallel(self, l1) -> bool:
        for i in l1:
            if self.parallel(i[0], i[1]):
                return True
        return False

    def perpendicular(self, s1, s2) -> bool:
        return [s1, s2] in self.predicates['perpendicular'] or [s2, s1] in self.predicates['perpendicular']

    def batch_perpendicular(self, l1) -> bool:
        for i in l1:
            if self.perpendicular(i[0], i[1]):
                return True
        return False

    def equal(self, s1, s2) -> bool:
        return [s1, s2] in self.predicates['equal'] or [s2, s1] in self.predicates['equal']

    def batch_equal(self, l1) -> bool:
        for i in l1:
            if self.equal(i[0], i[1]):
                return True
        return False

    def fraction(self, a, b) -> float:
        pass

    # Handlers and rules
    def parallel_handler(self):
        if self.batch_parallel(self.generate_seq(['sa2'], ['sc1', 'sa4', 'sb3', 'sa5'])):
            self.add_p('equal', ['a6', 'b1'])
            self.add_p('equal', ['c6', 'c3'])

        if self.batch_parallel(self.generate_seq(['sa1', 'sb4', 'sc6'], ['sb2', 'sc3', 'sc5'])):
            self.add_p('equal', ['a6', 'c2'])

        if self.parallel('sb1', 'sa3') or self.parallel('sb1', 'sc4') or self.parallel('sc2', 'sa3') or self.parallel('sc2', 'sc4'):
            self.add_p('equal', ['b2', 'c6'])

    def perpendicular_handler(self):
        if self.batch_perpendicular(self.generate_seq(['sa1', 'sb4', 'sc6'], ['sc1', 'sa4', 'sb3', 'sa5'])):
            self.add_p('sum', ['a1', 'c1', 90])
            self.add_p('sum', ['a4', 'b4', 90])
        if self.batch_perpendicular(self.generate_seq(['sa3', 'sc4', 'sa6'], ['sc1', 'sa4', 'sb3', 'sa5'])):
            self.add_p('sum', ['b3', 'a3', 90])
            self.add_p('sum', ['a4', 'c4', 90])
        if self.batch_perpendicular(self.generate_seq(['sa2'], ['sa1', 'sb4', 'sc6'])):
            self.add_p('sum', ['a4', 'c6', 90])
        if self.batch_perpendicular(self.generate_seq(['sa2'], ['sa3', 'sc4', 'sa6'])):
            self.add_p('sum', ['a4', 'a6', 90])
        if self.batch_perpendicular(self.generate_seq(['sb1', 'sc2', 'sb5'], ['sb2', 'sc3', 'sc5'])):
            self.add_p('sum', ['a1', 'a3', 90])
        if self.batch_perpendicular(self.generate_seq(['sc1', 'sb3', 'sa4', 'sa5'], ['sb2', 'sc3', 'sc5'])):
            self.add_p('sum', ['a1', 'a2', 90])
        if self.batch_perpendicular(self.generate_seq(['sc1', 'sb3', 'sa4', 'sa5'], ['sb1', 'sc2', 'sb5'])):
            self.add_p('sum', ['a2', 'a3', 90])

    def equal_handler(self):
        for i in self.predicates['equal']:
            self.add_p('fraction', [i[0], i[1], 1])

        # isosceles triangle
        for i in range(1, 5):
            if self.equal('sb{}'.format(i), 'sc{}'.format(i)):
                self.add_p('equal', ['c{}'.format(i), 'b{}'.format(i)])
            if self.equal('sb{}'.format(i), 'sa{}'.format(i)):
                self.add_p('equal', ['a{}'.format(i), 'b{}'.format(i)])
            if self.equal('sa{}'.format(i), 'sc{}'.format(i)):
                self.add_p('equal', ['a{}'.format(i), 'c{}'.format(i)])

    def fraction_handler(self):
        for i in self.predicates['fraction']:
            if i[2] == 1:
                self.add_p('equal', [i[0], i[1]])

    def sum_handler(self):
        def helper(a: str, b: str, value=90):
            return [a, b, value] in s or [b, a, value] in s

        s = self.predicates['sum']
        if helper('a1', 'c1'):
            self.add_p('perpendicular', ['sa1', 'sc1'])
        if helper('b1', 'c1'):
            self.add_p('perpendicular', ['sb1', 'sc1'])
        if helper('b1', 'a1'):
            self.add_p('perpendicular', ['sb1', 'sa1'])

    def similar_handler(self):
        pass

    def congruent_handler(self):
        pass

    def solve(self):
        i = 0
        while True:
            i = i+1
            #print('iter', i)
            self.prev_predicates = deepcopy(self.predicates)
            self.parallel_handler()
            self.perpendicular_handler()
            self.equal_handler()
            self.fraction_handler()
            self.sum_handler()
            self.similar_handler()
            diffkeys = [
                k for k in self.prev_predicates if self.prev_predicates[k] != self.predicates[k]]
            if not len(diffkeys):
                break


def set_parallel(name1, name2):
    global inputs
    inputs = inputs + 'set_parallel({},{})\n'.format(name1, name2)


def set_perpendicular(name1, name2):
    global inputs
    inputs = inputs + 'set_perpendicular({},{})\n'.format(name1, name2)


def set_equal(name1, name2):
    global inputs
    inputs = inputs + 'set_equal({},{})\n'.format(name1, name2)


def set_fraction(name1, name2, frac):
    global inputs
    inputs = inputs + 'set_fraction({},{},{})\n'.format(name1, name2, str(frac))


def set_sum_value(name1, name2, sum_val):
    global inputs
    inputs = inputs + \
        'set_sum_value({},{},{})\n'.format(name1, name2, str(sum_val))


def set_similar(name1, name2):
    global inputs
    inputs = inputs + 'set_similar({},{})\n'.format(name1, name2)

def set_congruent(name1, name2):
    global inputs
    inputs = inputs + 'set_congruent({},{})\n'.format(name1, name2)


def set_tan(name1, name2):
    global inputs
    inputs = inputs + 'set_tan({},{})\n'.format(name1, name2)

def get_all():
    global inputs
    solver = Solver().parse_input(inputs)
    solver.solve()
    return solver.predicates


if __name__ == '__main__':
    with open('predicates.txt', mode='r') as f:
        solver = Solver().parse_input(f.read())
        print('Initial:')
        pprint(solver.predicates)
        solver.solve()
        print('\nResult:')
        pprint(solver.predicates)