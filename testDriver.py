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

    def test_CalcBoardSolution_for_BFS_case_1(self):
        tile_positions = [1,2,5,3,4,0,6,7,8]
        calc_board_solution = CalcBoardSolution()
        eight_puzzle_result = calc_board_solution.with_the_search_algorithm("bfs").and_the_board(tile_positions)
        print "\n"
        self.assertTrue(eight_puzzle_result.path_to_solution == ['Up','Left','Left'], "Error: " + str(eight_puzzle_result.path_to_solution))
        self.assertTrue(eight_puzzle_result.cost_of_path == 3, "Error: " + str(eight_puzzle_result.cost_of_path))
        self.assertTrue(eight_puzzle_result.nodes_expanded == 10, "Error: " + str(eight_puzzle_result.nodes_expanded))
        self.assertTrue(eight_puzzle_result.max_search_depth == 4, "Error: " + str(eight_puzzle_result.max_search_depth))
        self.assertTrue(eight_puzzle_result.search_depth == 3, "Error: " + str(eight_puzzle_result.search_depth))
      
    def test_CalcBoardSolution_for_BFS_case_2(self):
        tile_positions = [8,6,4,2,1,3,5,7,0]
        calc_board_solution = CalcBoardSolution()
        eight_puzzle_result = calc_board_solution.with_the_search_algorithm("bfs").and_the_board(tile_positions)
        print "\n"
        self.assertTrue(eight_puzzle_result.path_to_solution == ['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left'], "Error: " + str(eight_puzzle_result.path_to_solution))
        self.assertTrue(eight_puzzle_result.cost_of_path == 26, "Error: " + str(eight_puzzle_result.cost_of_path))
        self.assertTrue(eight_puzzle_result.nodes_expanded == 166786, "Error: " + str(eight_puzzle_result.nodes_expanded))
        self.assertTrue(eight_puzzle_result.max_search_depth == 27, "Error: " + str(eight_puzzle_result.max_search_depth))
        self.assertTrue(eight_puzzle_result.search_depth == 26, "Error: " + str(eight_puzzle_result.search_depth))
    
#          
#     def test_CalcBoardSolution_for_BFS_case_3(self):
#         tile_positions = [6,1,8,4,0,2,7,3,5]
#         calc_board_solution = CalcBoardSolution()
#         eight_puzzle_result = calc_board_solution.with_the_search_algorithm("bfs").and_the_board(tile_positions)
#         self.assertTrue(eight_puzzle_result.path_to_solution == ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], "Error: " + str(eight_puzzle_result.path_to_solution))
#         self.assertTrue(eight_puzzle_result.cost_of_path == 20, "Error: " + str(eight_puzzle_result.cost_of_path))
#         self.assertTrue(eight_puzzle_result.nodes_expanded == 54094, "Error: " + str(eight_puzzle_result.nodes_expanded))
#         self.assertTrue(eight_puzzle_result.search_depth == 20, "Error: " + str(eight_puzzle_result.search_depth))
#         self.assertTrue(eight_puzzle_result.max_search_depth == 21, "Error: " + str(eight_puzzle_result.max_search_depth))
#         print "\n"
        
    def test_CalcBoardSolution_for_DFS_case_1(self):
        tile_positions = [1,4,2,3,0,5,6,7,8]
        calc_board_solution = CalcBoardSolution()
        eight_puzzle_result = calc_board_solution.with_the_search_algorithm("dfs").and_the_board(tile_positions)
        print "\n"
        self.assertTrue(eight_puzzle_result.path_to_solution == ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], "Error: " + str(eight_puzzle_result.path_to_solution))
        self.assertTrue(eight_puzzle_result.cost_of_path == 46142, "Error: " + str(eight_puzzle_result.cost_of_path))
        self.assertTrue(eight_puzzle_result.nodes_expanded == 51015, "Error: " + str(eight_puzzle_result.nodes_expanded))
        self.assertTrue(eight_puzzle_result.search_depth == 46142, "Error: " + str(eight_puzzle_result.search_depth))
        self.assertTrue(eight_puzzle_result.max_search_depth == 46142, "Error: " + str(eight_puzzle_result.max_search_depth))
        

#     def test_CalcBoardSolution_for_DFS_case_1(self):
#         tile_positions = [6,1,8,4,0,2,7,3,5]
#         calc_board_solution = CalcBoardSolution()
#         eight_puzzle_result = calc_board_solution.with_the_search_algorithm("dfs").and_the_board(tile_positions)
#         self.assertTrue(eight_puzzle_result.path_to_solution == ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], "Error: " + str(eight_puzzle_result.path_to_solution))
#         self.assertTrue(eight_puzzle_result.cost_of_path == 46142, "Error: " + str(eight_puzzle_result.cost_of_path))
#         self.assertTrue(eight_puzzle_result.nodes_expanded == 51015, "Error: " + str(eight_puzzle_result.nodes_expanded))
#         self.assertTrue(eight_puzzle_result.search_depth == 46142, "Error: " + str(eight_puzzle_result.search_depth))
#         self.assertTrue(eight_puzzle_result.max_search_depth == 46142, "Error: " + str(eight_puzzle_result.max_search_depth))
#         print "\n"
#     
#     def test_CalcBoardSolution_for_DFS_case_2(self):
#         tile_positions = [8,6,4,2,1,3,5,7,0]
#         calc_board_solution = CalcBoardSolution()
#         eight_puzzle_result = calc_board_solution.with_the_search_algorithm("dfs").and_the_board(tile_positions)
#         self.assertTrue(eight_puzzle_result.path_to_solution == ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up'], "Error: " + str(eight_puzzle_result.path_to_solution))
#         self.assertTrue(eight_puzzle_result.cost_of_path == 9612, "Error: " + str(eight_puzzle_result.cost_of_path))
#         self.assertTrue(eight_puzzle_result.nodes_expanded == 9869, "Error: " + str(eight_puzzle_result.nodes_expanded))
#         self.assertTrue(eight_puzzle_result.search_depth == 9612, "Error: " + str(eight_puzzle_result.search_depth))
#         self.assertTrue(eight_puzzle_result.max_search_depth == 9612, "Error: " + str(eight_puzzle_result.max_search_depth))
#         print "\n"
