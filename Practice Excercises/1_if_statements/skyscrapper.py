# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:59:10 2022

@author: vikas
"""

#!/usr/bin/env python
 
import os
from copy import deepcopy
 
# set path here
path_to_files = '.' 
 
class Puzzle(object):
 
    def __init__(self, size):
        self.size = size
        self.cells = [[set(range(size)) for _x in range(size)]
                      for _y in range(size)]
        self.clues = [None] * 4
 
    def is_full(self):
        for row in self.cells:
            for cell in row:
                if len(cell) != 1:
                    return False
        return True
 
    def is_solvable(self):
        for row in self.cells:
            for cell in row:
                if len(cell) == 0:
                    return False
        return True
 
    def is_solved(self):
        if not self.is_full():
            return False
 
        for index in range(self.size):
            column = [next(iter(self.cells[x][index]))
                      for x in range(self.size)]
            if not self.satisfies_clue(column, self.clues[0][index], self.clues[3][index]):
                return False
 
            row = [next(iter(self.cells[index][y])) for y in range(self.size)]
            if not self.satisfies_clue(row, self.clues[1][index], self.clues[2][index]):
                return False
 
        return True
 
    def satisfies_clue(self, values, clue_left, clue_right):
        current = - 1
        for height in values:
            if current < height:
                clue_left -= 1
                current = height
        if clue_left != 0:
            return False
        current = - 1
        for height in reversed(values):
            if current < height:
                clue_right -= 1
                current = height
        if clue_right != 0:
            return False
        return True
 
    def set_cell_to(self, x, y, value):
        value = set([value])
        for i in range(self.size):
            self.cells[i][x] -= value
            self.cells[y][i] -= value
        self.cells[y][x] = value
 
    def fix(self):
        for i in range(self.size):
            for j in range(self.size):
                if len(self.cells[i][j]) == 1:
                    self.set_cell_to(j, i, next(iter(self.cells[i][j])))
 
    def solve_basic_clues(self):
        # top clues
        for index, clue in enumerate(self.clues[0]):
            if clue == 1:
                self.set_cell_to(index, 0, self.size - 1)
            elif clue == self.size:
                for i in range(self.size):
                    self.set_cell_to(index, i, i)
 
        # bottom clues
        for index, clue in enumerate(self.clues[3]):
            if clue == 1:
                self.set_cell_to(index, self.size - 1, self.size - 1)
            elif clue == self.size:
                for i in range(self.size):
                    self.set_cell_to(index, i, self.size - (i + 1))
 
        # left clues
        for index, clue in enumerate(self.clues[1]):
            if clue == 1:
                self.set_cell_to(0, index, self.size - 1)
            elif clue == self.size:
                for i in range(self.size):
                    self.set_cell_to(i, index, i)
        # right clues
        for index, clue in enumerate(self.clues[2]):
            if clue == 1:
                self.set_cell_to(self.size - 1, index, self.size - 1)
            elif clue == self.size:
                for i in range(self.size):
                    self.set_cell_to(i, index, self.size - (i + 1))
 
    def __repr__(self):
        result = []
        if self.is_full():
            for row in self.cells:
                result.append(
                    ' '.join(str(next(iter(cell)) + 1) for cell in row))
        else:
            for row in self.cells:
                result.append(repr(row))
        return '\n'.join(result)
 
 
def main():
    input_file_name = os.path.join(path_to_files, 'skyscraper_puzzles_unsolved.txt')
    output_file_name = os.path.join(path_to_files, 'skyscraper_puzzles_solved.txt')
 
    lines = open(input_file_name)
    output_file = open(output_file_name,'w')
 
    npuzzles = int(next(lines))
    print >>output_file, npuzzles
 
    for i in range(npuzzles):
        size = int(next(lines))
        p = Puzzle(size)
        for i in range(4):
            p.clues[i] = [int(x) for x in next(lines).split()]
        p.solve_basic_clues()
        p.fix()
        solution = recursive_solve(p, 0)
 
        print >>output_file, p.size
        print >>output_file, solution or 'Invalid puzzle'
 
 
def recursive_solve(puzzle, index):
 
    x = index % puzzle.size
    y = index / puzzle.size
    for value in puzzle.cells[y][x]:
        tmp = deepcopy(puzzle)
        tmp.set_cell_to(x, y, value)
        tmp.fix()
        if not tmp.is_solvable():
            continue
        elif tmp.is_solved():
            return tmp
        elif not tmp.is_full():
            tmp2 = recursive_solve(tmp, index + 1)
            if tmp2 is None:
                continue
            elif tmp2.is_solved():
                return tmp2
    return None
 
if __name__ == '__main__':
    main()
    
    
    
'''
include "globals.mzn";

int: N = 4;
set of int: POS = 1..N;
set of int: SEEN = 1..N;
set of int: HEIGHT = 1..N;

array[POS] of SEEN: top = [2, 1, 2, 2];
array[POS] of SEEN: bottom = [2, 4, 3, 1];
array[POS] of SEEN: left = [2, 3, 1, 2];
array[POS] of SEEN: right = [2, 2, 3, 1];    

array[POS, POS] of var HEIGHT: height;

constraint forall(p in POS)
    (all_different(row(height, p)) /\
     all_different(col(height, p)));

predicate sum_seen(array[POS] of var HEIGHT: values, int: seen) = 
    (sum(i in 2..N)(values[i] > max([values[j] | j in 1..i-1])) = seen - 1);

constraint forall(p in POS)
    (sum_seen(row(height, p), left[p]) /\
     sum_seen(reverse(row(height, p)), right[p]) /\
     sum_seen(col(height, p), top[p]) /\
     sum_seen(reverse(col(height, p)), bottom[p]));

solve satisfy;

output ["height = "] ++ [show2d(height)];
'''