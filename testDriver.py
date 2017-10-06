'''
Created on Sep 27, 2017

@author: walker
'''
import unittest

from driver import CalcBoardSolution
from driver import EightPuzzleResult

class TestDriver(unittest.TestCase):
    '''
    classdocs
    '''

    def test_CalcBoardSolution_forBFS_case_1(self):
        tile_positions = [1,2,5,3,4,0,6,7,8]
        calc_board_solution = CalcBoardSolution()
        eight_puzzle_result = EightPuzzleResult()
        eight_puzzle_result = calc_board_solution.with_the_search_algorithm("bfs").and_the_board(tile_positions)
        self.assertTrue(eight_puzzle_result.path_to_goal == ['Up','Left','Left'], "Error: " + str(eight_puzzle_result.path_to_goal))
        self.assertTrue(eight_puzzle_result.cost_of_path == 3, "Error: " + str(eight_puzzle_result.cost_of_path))
        self.assertTrue(eight_puzzle_result.nodes_expanded == 10, "Error: " + str(eight_puzzle_result.nodes_expanded))
        self.assertTrue(eight_puzzle_result.search_depth == 3, "Error: " + str(eight_puzzle_result.search_depth))
        self.assertTrue(eight_puzzle_result.max_search_depth == 4, "Error: " + str(eight_puzzle_result.max_search_depth))