from multiprocessing import Queue
from Queue import Queue
import time
import test
import sys
if sys.platform == "win32":
    import psutil
    print("psutil", psutil.Process().memory_info().rss)
# else:
    # Note: if you execute Python from cygwin,
    # the sys.platform is "cygwin"
    # the grading system's sys.platform is "linux2"
#     import resource
#     print("resource", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

# board_state = [1,2,5,3,4,0,6,7,8]


class CalcBoardSolution:
      
    use_search_algorithm_to = None
    tile_positions = None
    start_time = None
      
    def with_the_search_algorithm(self,algorithm_string):
        self.start_time = time.time()
        if (algorithm_string == "bfs"):
            self.use_search_algorithm_to = BFS()
        elif(algorithm_string == "dfs"):
            self.use_search_algorithm_to = DFS()
        return self
    
    def and_the_board(self,tile_positions):
        self.tile_positions = tile_positions
        eight_puzzle_result = self.use_search_algorithm_to.get_the_optimal_solution_with_board(self.tile_positions)
        eight_puzzle_result.running_time = time.time() - self.start_time
        eight_puzzle_result.print_result()
        return eight_puzzle_result
    
      
class EightPuzzleResult:
    path_to_solution = []
    cost_of_path = 0
    nodes_expanded = 0
    search_depth = 0
    max_search_depth = 0
    running_time = 0
    max_ram_usage = 0
    leaf_search_depth = 0
    
    def get_path_to_solution(self,board_state):
        if(board_state != None and board_state.parent_board != None):
            self.path_to_solution.insert(0,board_state.direction)
            self.cost_of_path += 1
            self.search_depth += 1
            self.get_path_to_solution(board_state.parent_board)
        else:
            return self.path_to_solution
        
    def calculate_search_depth_to_current_board_leaf(self,board_state):
        if(board_state != None and board_state.parent_board != None):
            self.leaf_search_depth += 1
            if(self.leaf_search_depth > self.max_search_depth):
                self.max_search_depth = self.leaf_search_depth
            self.calculate_search_depth_to_current_board_leaf(board_state.parent_board)
        else:
            return self.max_search_depth

    def print_result(self):
        print("path_to_goal:" + str(self.path_to_solution) )
        print("cost_of_path:" + str(self.cost_of_path) )
        print("nodes_expanded:" + str(self.nodes_expanded) )
        print("search_depth:" + str(self.search_depth) )
        print("max_search_depth:" + str(self.max_search_depth) )
        print("running_time:" + str(self.running_time))
        print("max_ram_usage:" + str(self.max_ram_usage))
    
     
class Frontier:
    """Simple example class"""
    
    board_state = None
    explored_set = None
    
    def copy_class(self,board_state_to_copy):
        self.board_state = BoardState()
        self.board_state.current_board = board_state_to_copy.current_board[:]
        self.board_state.direction = board_state_to_copy.direction
        self.board_state.position_of_zero = board_state_to_copy.position_of_zero

    def left(self, parent_board_state):
        self.copy_class(parent_board_state)
        tile_position_array = self.board_state.current_board
        self.swap_board_positions(tile_position_array, self.board_state.position_of_zero, self.board_state.position_of_zero - 1)
        self.board_state.position_of_zero = self.board_state.position_of_zero - 1
        return self.board_state
     
    def right(self, parent_board_state):
        self.copy_class(parent_board_state)
        tile_position_array = self.board_state.current_board
        self.swap_board_positions(tile_position_array, self.board_state.position_of_zero, self.board_state.position_of_zero + 1)
        self.board_state.position_of_zero = self.board_state.position_of_zero + 1
        return self.board_state
    
    def up(self, parent_board_state):
        self.copy_class(parent_board_state)
        tile_position_array = self.board_state.current_board
        self.swap_board_positions(tile_position_array, self.board_state.position_of_zero, self.board_state.position_of_zero - 3)
        self.board_state.position_of_zero = self.board_state.position_of_zero - 3
        return self.board_state
    
    def down(self, parent_board_state):
        self.copy_class(parent_board_state)
        tile_position_array = self.board_state.current_board
        self.swap_board_positions(tile_position_array, self.board_state.position_of_zero, self.board_state.position_of_zero + 3)
        self.board_state.position_of_zero += 3
        return self.board_state
     
    def swap_board_positions(self, tile_position_array, current_position_of_zero, future_position_of_zero):
        temp = tile_position_array[future_position_of_zero]
        tile_position_array[future_position_of_zero] = tile_position_array[current_position_of_zero]
        tile_position_array[current_position_of_zero] = temp
        self.board_state.current_board = tile_position_array
        
class BoardState:
    position_of_zero = 0
    direction = None
    current_board = None
    parent_board = None
    next_in_queue = None
                   
class SearchAlgorithm:
    
    solution_is_not_found = True
    optimal_solution = [0,1,2,3,4,5,6,7,8]
    def get_the_optimal_solution_with_board(self,tile_positions):
        return self
    
    def get_location_of_zero(self,tile_number_array):
        position_of_zero = 0;
        for tile_position in range(0,8):
            if(tile_number_array[tile_position] == 0):
                position_of_zero = tile_position
        return position_of_zero
    
    
class BFS(SearchAlgorithm):
    frontier_queue = None
    explored_set = None
    union_of_frontier_and_explored_nodes = None
    end_of_frontier_queue = None
    def the_union_of_the_frontier_and_explored_nodes(self):
        self.union_of_frontier_and_explored_nodes = list(set().union(set(self.frontier_queue.queue),self.explored_set))
        return self
    
    def does_not_contain(self,current_board):
        for existing_board in self.union_of_frontier_and_explored_nodes:
            if (current_board == existing_board.current_board):
                return False
        return True
    
    def expand_node(self, direction, eight_puzzle_result, bfs_queue, new_board_state, current_board_state):
        #if (self.solution_is_not_found): 
        new_board_state.direction = direction
        new_board_state.parent_board = current_board_state
        if(self.the_union_of_the_frontier_and_explored_nodes().does_not_contain(new_board_state.current_board)):
            self.end_of_frontier_queue.next_in_queue = new_board_state
            self.end_of_frontier_queue = new_board_state
            
#             self.frontier_queue.put_nowait(new_board_state)
            eight_puzzle_result.leaf_search_depth = 0
            eight_puzzle_result.calculate_search_depth_to_current_board_leaf(new_board_state)
        
        if (new_board_state.current_board == self.optimal_solution):
            self.solution_is_not_found = False
    
        return new_board_state

    def frontier_queue_is_not_empty(self):
        return not self.frontier_queue.empty()
    
    def get_the_optimal_solution_with_board(self,tile_number_array):
        eight_puzzle_result = EightPuzzleResult()
        frontier = Frontier()
        self.frontier_queue = Queue()
        self.explored_set = set()
        board_state = BoardState()
        board_state.current_board = tile_number_array;
        board_state.position_of_zero = self.get_location_of_zero(tile_number_array)
        self.explored_set.add(board_state)
        self.end_of_frontier_queue = board_state
        while(board_state.current_board != self.optimal_solution):
            if (-1 < board_state.position_of_zero < 9):
                if(5 < board_state.position_of_zero < 9):
                    self.expand_node("Up",eight_puzzle_result, self.frontier_queue, frontier.up(board_state), board_state)
                elif(2 < board_state.position_of_zero < 6):
                    self.expand_node("Up",eight_puzzle_result, self.frontier_queue, frontier.up(board_state), board_state)
                    self.expand_node("Down",eight_puzzle_result, self.frontier_queue, frontier.down(board_state), board_state)
                elif(-1 < board_state.position_of_zero < 3):
                    self.expand_node("Down",eight_puzzle_result, self.frontier_queue, frontier.down(board_state), board_state)
                    
                if((board_state.position_of_zero + 1) % 3 == 0):
                    self.expand_node("Left",eight_puzzle_result, self.frontier_queue, frontier.left(board_state), board_state)
                elif((board_state.position_of_zero + 2) % 3 == 0):
                    self.expand_node("Left",eight_puzzle_result, self.frontier_queue, frontier.left(board_state), board_state)
                    self.expand_node("Right",eight_puzzle_result, self.frontier_queue, frontier.right(board_state), board_state)
                elif((board_state.position_of_zero + 3) % 3 == 0):
                    self.expand_node("Right",eight_puzzle_result, self.frontier_queue, frontier.right(board_state), board_state)
            else:
                print "Error: Empty space out of the bounds of the board_state"
                return None

#             print self.frontier_queue.qsize()
#            print board_state.current_board

#             resource.test_getrusage()
#             mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            
            if(board_state.next_in_queue == None):
                return None
            
            board_state = board_state.next_in_queue
            
            eight_puzzle_result.nodes_expanded += 1
            if (eight_puzzle_result.nodes_expanded > 54000): 
                print eight_puzzle_result.nodes_expanded
            self.explored_set.add(board_state)
        
        eight_puzzle_result.get_path_to_solution(board_state)
        return eight_puzzle_result

class DFS(SearchAlgorithm):
    def get_the_optimal_solution_with_board(self,tile_positions):
        return self
    def using(self):
        return self
    