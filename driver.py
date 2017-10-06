from multiprocessing import Queue
from Queue import Queue


board_state = [1,2,5,3,4,0,6,7,8]
parent = board_state


class CalcBoardSolution:
      
    use_search_algorithm_to = None
    tile_positions = None
      
    def with_the_search_algorithm(self,algorithm_string):
        if (algorithm_string == "bfs"):
            self.use_search_algorithm_to = BFS()
        elif(algorithm_string == "dfs"):
            self.use_search_algorithm_to = DFS()
        return self
    def and_the_board(self,tile_positions):
        self.tile_positions = tile_positions
        eight_puzzle_result = self.use_search_algorithm_to.get_the_optimal_solution_with_board(self.tile_positions)
        return eight_puzzle_result
    
      
class EightPuzzleResult:
    path_to_goal = []
    cost_of_path = 0
    nodes_expanded = 0
    search_depth = 0
    max_search_depth = 0
    running_time = 0
    max_ram_usage = 0
     
class Frontier:
    """Simple example class"""
    
    board_state = None
    explored_set = None
    
    def left(self, parent_board_state):
        self.board_state = parent_board_state.copy_class()
        tile_position_array = self.board_state.current_board
        self.direction = "left"
        self.swap_board_positions(tile_position_array, self.board_state.position_of_zero, self.board_state.position_of_zero - 1)
        self.board_state.position_of_zero = self.board_state.position_of_zero - 1
        return self.board_state
     
    def right(self, parent_board_state):
        self.board_state = parent_board_state.copy_class()
        tile_position_array = self.board_state.current_board
        self.direction = "right"
        self.swap_board_positions(tile_position_array, self.board_state.position_of_zero, self.board_state.position_of_zero + 1)
        self.board_state.position_of_zero = self.board_state.position_of_zero + 1
        return self.board_state
    
    def up(self, parent_board_state):
        self.board_state = parent_board_state.copy_class()
        tile_position_array = self.board_state.current_board
        self.direction = "up"
        self.swap_board_positions(tile_position_array, self.board_state.position_of_zero, self.board_state.position_of_zero - 3)
        self.board_state.position_of_zero = self.board_state.position_of_zero - 3
        return self.board_state
    
    def down(self, parent_board_state):
        self.board_state = parent_board_state.copy_class()
        tile_position_array = self.board_state.current_board
        self.direction = "down"
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
    
    def copy_class(self):
        board_state = BoardState()
        board_state.current_board = self.current_board[:]
        board_state.direction = self.direction
        board_state.position_of_zero = self.position_of_zero
        return board_state
                
class SearchAlgorithm:
    
    solution_is_not_found = True
    optimal_solution = [0,1,2,3,4,5,6,7,8]
    def get_the_optimal_solution_with_board(self,tile_positions):
        return self
    
    def get_location_of_zero(self,tile_number_array):
        position_of_zero = 0;
        for tile_position in range(0,9):
            if(tile_number_array[tile_position] == 0):
                position_of_zero = tile_position
        return position_of_zero
    
class BFS(SearchAlgorithm):
    frontier_queue = None
    explored_set = None
    union_of_frontier_and_explored_nodes = None
    def the_union_of_the_frontier_and_explored_nodes(self):
        self.union_of_frontier_and_explored_nodes = list(set().union(set(self.frontier_queue.queue),self.explored_set))
        return self
    
    def does_not_contain(self,current_board):
        for existing_board in self.union_of_frontier_and_explored_nodes:
            if (current_board == existing_board.current_board):
                return False
        return True
    
    def expand_node(self, direction, eight_puzzle_result, bfs_queue, new_board_state, current_board_state):
        if (self.solution_is_not_found): 
            new_board_state.direction = direction
            if(self.the_union_of_the_frontier_and_explored_nodes().does_not_contain(new_board_state.current_board)):
                self.frontier_queue.put_nowait(new_board_state)
            eight_puzzle_result.nodes_expanded += 1
            if (new_board_state.current_board == self.optimal_solution):
                self.solution_is_not_found = False
    
        return current_board_state

    def get_the_optimal_solution_with_board(self,tile_number_array):
        eight_puzzle_result = EightPuzzleResult
#         eight_puzzle_result.path_to_goal = ['Up','Left','Left']
#         eight_puzzle_result.cost_of_path = 3
#         eight_puzzle_result.nodes_expanded = 10
#         eight_puzzle_result.search_depth = 3
#         eight_puzzle_result.max_search_depth = 4
        frontier = Frontier()
        self.frontier_queue = Queue()
        self.explored_set = set()
        board_state = BoardState()
        board_state.current_board = tile_number_array;
        board_state.position_of_zero = self.get_location_of_zero(tile_number_array)
        self.frontier_queue.put_nowait(board_state)
        self.explored_set.add(board_state)
        while(self.solution_is_not_found):
            if (0 < board_state.position_of_zero < 9):
                eight_puzzle_result.cost_of_path += 1
                eight_puzzle_result.search_depth += 1
                if(5 < board_state.position_of_zero < 9):
                    self.expand_node("up",eight_puzzle_result, self.frontier_queue, frontier.up(board_state), board_state)
                elif(2 < board_state.position_of_zero < 6):
                    self.expand_node("up",eight_puzzle_result, self.frontier_queue, frontier.up(board_state), board_state)
                    self.expand_node("down",eight_puzzle_result, self.frontier_queue, frontier.down(board_state), board_state)
                elif(-1 < board_state.position_of_zero < 3):
                    self.expand_node("down",eight_puzzle_result, self.frontier_queue, frontier.down(board_state), board_state)
                                    
                if((board_state.position_of_zero + 1) % 3 == 0):
                    self.expand_node("left",eight_puzzle_result, self.frontier_queue, frontier.left(board_state), board_state)
                elif((board_state.position_of_zero + 2) % 3 == 0):
                    self.expand_node("left",eight_puzzle_result, self.frontier_queue, frontier.left(board_state), board_state)
                    self.expand_node("right",eight_puzzle_result, self.frontier_queue, frontier.right(board_state), board_state)
                elif((board_state.position_of_zero + 3) % 3 == 0):
                    self.expand_node("right",eight_puzzle_result, self.frontier_queue, frontier.right(board_state), board_state)
            else:
                print "Error: Empty space out of the bounds of the board_state"
                return None
            print self.frontier_queue.qsize()
            print board_state.current_board
            board_state = self.frontier_queue.get_nowait()
            self.explored_set.add(board_state)
            eight_puzzle_result.path_to_goal.append(board_state.direction)
        return eight_puzzle_result

class DFS(SearchAlgorithm):
    def get_the_optimal_solution_with_board(self,tile_positions):
        return self
    def using(self):
        return self
    