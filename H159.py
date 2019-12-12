#!/usr/local/bin/python3
import math
from copy import deepcopy
from pprint import pprint
import numpy as np
from collections import Counter

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
    triangles_val = {'ar1': INIT,
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

    ar1 = {'l': 'sb1',
           'r': 'sa1',
           'b': 'sc1',
           'al': 'a1',
           'ar': 'b1',
           'au': 'c1'}
    ar2 = {'l': 'sc2',
           'r': 'sb2',
           'b': 'sa2',
           'al': 'b2',
           'ar': 'c2',
           'au': 'a2'}
    ar3 = {'l': 'sa3',
           'r': 'sc3',
           'b': 'sb3',
           'al': 'c3',
           'ar': 'a3',
           'au': 'b3'}
    ar4 = {'l': 'sc4',
           'r': 'sb4',
           'b': 'sa4',
           'al': 'b4',
           'ar': 'c4',
           'au': 'a4'}
    ar5 = {'l': 'sb5',
           'r': 'sc5',
           'b': 'sa5',
           'al': 'a1',
           'ar': 'a3',
           'au': 'a2'}
    ar6 = {'l': 'sa6',
           'r': 'sc6',
           'b': 'sa2',
           'al': 'c6',
           'ar': 'a6',
           'au': 'a4'}

    triangles = {'ar1': ar1,
                 'ar2': ar2,
                 'ar3': ar3,
                 'ar4': ar4,
                 'ar5': ar5,
                 'ar6': ar6}

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

    def intelli_update(self, index: str, lst: list):
        lst2 = lst.copy()
        lst2[0], lst2[1] = lst2[1], lst2[0]
        if lst in self.predicates[index] or lst2 in self.predicates[index] or lst[0] == lst[1]:
            return
        self.predicates[index].append(lst)

    def seq(self, l1, l2) -> list:
        return [[i, j] for i in l1 for j in l2]

    def parallel(self, s1, s2) -> bool:
        return [s1, s2] in self.predicates['parallel'] or [s2, s1] in self.predicates['parallel']

    def batch_parallel(self, l1) -> bool:
        rlt = np.array([self.parallel(i[0], i[1]) for i in l1])
        return True if np.sum(rlt) > 0 else False

    def perpendicular(self, s1, s2) -> bool:
        return [s1, s2] in self.predicates['perpendicular'] or [s2, s1] in self.predicates['perpendicular']

    def batch_perpendicular(self, l1) -> bool:
        rlt = np.array([self.perpendicular(i[0], i[1]) for i in l1])
        return True if np.sum(rlt) > 0 else False

    def equal(self, s1, s2) -> bool:
        return [s1, s2] in self.predicates['equal'] or [s2, s1] in self.predicates['equal']

    def congruent(self, s1, s2) -> bool:
        return [s1, s2] in self.predicates['congruent'] or [s2, s1] in self.predicates['congruent']

    def similar(self, s1, s2) -> bool:
        return [s1, s2] in self.predicates['similar'] or [s2, s1] in self.predicates['similar']

    def batch_equal(self, l1) -> bool:
        rlt = np.array([self.equal(i[0], i[1]) for i in l1])
        return True if np.sum(rlt) > 0 else False

    def dichotomy_shuffler(self, flatten) -> list:
        # awesome idea!
        result = [[flatten[i], flatten[j]] for i in range(len(flatten))
                  for j in range(len(flatten)) if i > j]
        return result

    def fraction(self, s1, s2) -> float:
        reconst = [[i[0], i[1]] for i in self.predicates['fraction']]
        if [s1, s2] in reconst or [s2, s1] in reconst:
            for i in self.predicates['fraction']:
                if (s1, s2) == (i[0], i[1]) or (s2, s1) == (i[0], i[1]):
                    return i[2]
        return - 1

    def update_similar(self, ar1: str, ar2: str):
        for k in ('l', 'r', 'b'):
            self.intelli_update(
                'parallel', [self.triangles[ar1][k], self.triangles[ar2][k]])
        for k in ('al', 'ar', 'au'):
            self.intelli_update(
                'equal', [self.triangles[ar1][k], self.triangles[ar2][k]])
    
    def update_congruent(self, ar1: str, ar2: str):
        for k in ('l', 'r', 'b'):
            self.intelli_update(
                'equal', [self.triangles[ar1][k], self.triangles[ar2][k]])
        for k in ('al', 'ar', 'au'):
            self.intelli_update(
                'equal', [self.triangles[ar1][k], self.triangles[ar2][k]])

    def cont_inferer(self, list2d):
        result = {}
        f_result = []

        def recursive_search(lists, target, depth, max_depth=6) -> list:
            depth = depth + 1
            result = []
            if depth >= max_depth:
                return result
            for l in lists:
                if l[0] == target:
                    result.append(l[1])
                    result = result + recursive_search(lists, l[1], depth)
            return result

        for i in list2d:
            i.sort()

        for i in list2d:
            result[i[0]] = recursive_search(list2d, i[0], 0)
        for k, v in result.items():
            f_result.append([k] + list(v))
        return f_result

    # Handlers and rules
    def parallel_handler(self):
        if self.batch_parallel(self.seq(['sa2'], ['sc1', 'sa4', 'sb3', 'sa5'])):
            self.intelli_update('equal', ['a6', 'b1'])
            self.intelli_update('equal', ['c6', 'c3'])

        if self.batch_parallel(self.seq(['sa1', 'sb4', 'sc6'], ['sb2', 'sc3', 'sc5'])):
            self.intelli_update('equal', ['a6', 'c2'])

        if self.parallel('sb1', 'sa3') or self.parallel('sb1', 'sc4') or self.parallel('sc2', 'sa3') or self.parallel('sc2', 'sc4'):
            self.intelli_update('equal', ['b2', 'c6'])

    def perpendicular_handler(self):
        if self.batch_perpendicular(self.seq(['sa1', 'sb4', 'sc6'], ['sc1', 'sa4', 'sb3', 'sa5'])):
            self.intelli_update('sum', ['a1', 'c1', 90])
            self.intelli_update('sum', ['a4', 'b4', 90])
        if self.batch_perpendicular(self.seq(['sa3', 'sc4', 'sa6'], ['sc1', 'sa4', 'sb3', 'sa5'])):
            self.intelli_update('sum', ['b3', 'a3', 90])
            self.intelli_update('sum', ['a4', 'c4', 90])
        if self.batch_perpendicular(self.seq(['sa2'], ['sa1', 'sb4', 'sc6'])):
            self.intelli_update('sum', ['a4', 'c6', 90])
        if self.batch_perpendicular(self.seq(['sa2'], ['sa3', 'sc4', 'sa6'])):
            self.intelli_update('sum', ['a4', 'a6', 90])
        if self.batch_perpendicular(self.seq(['sb1', 'sc2', 'sb5'], ['sb2', 'sc3', 'sc5'])):
            self.intelli_update('sum', ['a1', 'a3', 90])
        if self.batch_perpendicular(self.seq(['sc1', 'sb3', 'sa4', 'sa5'], ['sb2', 'sc3', 'sc5'])):
            self.intelli_update('sum', ['a1', 'a2', 90])
        if self.batch_perpendicular(self.seq(['sc1', 'sb3', 'sa4', 'sa5'], ['sb1', 'sc2', 'sb5'])):
            self.intelli_update('sum', ['a2', 'a3', 90])

    def equal_handler(self):
        for i in self.predicates['equal']:
            self.intelli_update('fraction', [i[0], i[1], 1])

        # isosceles triangle
        for i in range(1, 5):
            if self.equal('sb{}'.format(i), 'sc{}'.format(i)):
                self.intelli_update(
                    'equal', ['c{}'.format(i), 'b{}'.format(i)])
            if self.equal('sb{}'.format(i), 'sa{}'.format(i)):
                self.intelli_update(
                    'equal', ['a{}'.format(i), 'b{}'.format(i)])
            if self.equal('sa{}'.format(i), 'sc{}'.format(i)):
                self.intelli_update(
                    'equal', ['a{}'.format(i), 'c{}'.format(i)])

        # Inspected by rt
        if self.batch_equal(self.seq(['a6'], ['b1', 'c4'])):
            self.intelli_update('parallel', ['sa2', 'sc1'])
        if self.batch_equal(self.seq(['c6'], ['c3', 'b4'])):
            self.intelli_update('parallel', ['sa2', 'sc1'])

        if self.batch_equal(self.seq(['c2'], ['a6'])) or self.batch_equal(self.seq(['a6'], ['c2'])):
            self.intelli_update('parallel', ['sb2', 'sa1'])
        if self.batch_equal(self.seq(['a4'], ['c1'])):
            self.intelli_update('parallel', ['sc4', 'sc2'])
        if self.batch_equal(self.seq(['a4'], ['b3'])):
            self.intelli_update('parallel', ['sb2', 'sb4'])

    def fraction_handler(self):
        for i in self.predicates['fraction']:
            if i[2] == 1:
                self.intelli_update('equal', [i[0], i[1]])

    def sum_handler(self):
        def helper(a: str, b: str, value=90):
            return [a, b, value] in s or [b, a, value] in s

        s = self.predicates['sum']
        if helper('a1', 'c1'):
            self.intelli_update('perpendicular', ['sa1', 'sc1'])
        if helper('b1', 'c1'):
            self.intelli_update('perpendicular', ['sb1', 'sc1'])
        if helper('b1', 'a1'):
            self.intelli_update('perpendicular', ['sb1', 'sa1'])

    def similar_handler(self):
        flattens = self.cont_inferer(self.predicates['similar'])
        for item in flattens:
            for inner_item in self.dichotomy_shuffler(item):
                self.update_similar(item[0], item[1])

    def congruent_handler(self):
        for i in self.predicates['congruent']:
            self.intelli_update('similar', i)

        flattens = self.cont_inferer(self.predicates['congruent'])
        for item in flattens:
            for inner_item in self.dichotomy_shuffler(item):
                self.update_congruent(item[0], item[1])

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
            self.congruent_handler()
            diffkeys = [
                k for k in self.prev_predicates if self.prev_predicates[k] != self.predicates[k]]
            if not len(diffkeys):
                for i in self.predicates['congruent']:
                    self.predicates['similar'].remove(i)
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
    inputs = inputs + \
        'set_fraction({},{},{})\n'.format(name1, name2, str(frac))


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
