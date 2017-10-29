from collections import deque
import time
from _heapq import heappush, heappop, heapify

class EightPuzzleResult:
    path_to_solution = []
    cost_of_path = 0
    nodes_expanded = 0
    search_depth = 0
    max_search_depth = 0
    running_time = 0
    max_ram_usage = 0
    def __init__(self):
        self.path_to_solution = []
        self.cost_of_path = 0
        self.nodes_expanded = 0
        self.search_depth = 0
        self.max_search_depth = 0
        self.running_time = 0
        self.max_ram_usage = 0
    
    def get_path_to_solution(self,frontier_dict,board_state):
        self.search_depth = self.cost_of_path = frontier_dict[board_state]['search_depth']
        while(board_state != None and frontier_dict[board_state]["parent"] != None):
            self.path_to_solution.insert(0,frontier_dict[board_state]['direction'])
            board_state = frontier_dict[board_state]["parent"]

            #self.get_path_to_solution(frontier_dict,frontier_dict[board_state]["parent"])
        
        return self.path_to_solution

    def calculate_max_search_depth(self,frontier_dict,board_state):
        while(board_state != None and frontier_dict[board_state]["parent"] != None):
            self.max_search_depth += 1
            board_state = frontier_dict[board_state]["parent"]
        return self.max_search_depth
        
#     def calculate_search_depth(self,frontier_dict):
#         parent_and_direction_dict in frontier_dict:
#             if(frontier_dict != None and frontier_dict[board_state]['parent'] != None):
#                 self.leaf_search_depth += 1
#                 if(self.leaf_search_depth > self.max_search_depth):
#                 self.max_search_depth = self.leaf_search_depth
#             self.calculate_search_depth_to_current_board_leaf(board_state.parent_board)
#         else:
#             return self.max_search_depth
    
    def print_result(self):
        print("path_to_goal:" + str(self.path_to_solution) )
        print("cost_of_path:" + str(self.cost_of_path) )
        print("nodes_expanded:" + str(self.nodes_expanded) )
        print("search_depth:" + str(self.search_depth) )
        print("max_search_depth:" + str(self.max_search_depth) )
        print("running_time:" + str(self.running_time))
        print("max_ram_usage:" + str(self.max_ram_usage))


class CalcBoardSolution:
    
    use_search_algorithm_to = None
    start_time = None
    def with_the_search_algorithm(self,search_algorithm):
        self.start_time = time.time()
        if (search_algorithm == "bfs"):
            self.use_search_algorithm_to = BFS()
        elif(search_algorithm == "dfs"):
            self.use_search_algorithm_to = DFS()
        elif(search_algorithm == "ast"):
            self.use_search_algorithm_to = AST()
        return self

    def and_the_board(self,tile_positions):
        eight_puzzle_result = EightPuzzleResult()
        if(self.use_search_algorithm_to != None and tile_positions != None):
            eight_puzzle_result = self.use_search_algorithm_to.get_the_optimal_solution_with_board(tile_positions)
        if (eight_puzzle_result == None):
            print "No result was found"
            return None
        eight_puzzle_result.running_time = time.time() - self.start_time
        eight_puzzle_result.print_result()
        return eight_puzzle_result
          
def get_location_of_zero_for(board_state):
    board_state_tuple = (str(board_state))
    for index in range(1,10):
        if (int(board_state_tuple[index]) == 0):
            return index
        
class TreeOperations:
    def get_all_neighbors_for(self,board_state):
        location_of_zero = get_location_of_zero_for(board_state)
        neighbors = None
        if(0 < location_of_zero < 10):
            if(location_of_zero == 1):
                neighbors = {"Down": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 3),
                             "Right": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 1)}
            elif(location_of_zero == 2):
                neighbors = {"Down": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 3),
                             "Left": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 1),
                             "Right": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 1)}
            elif(location_of_zero == 3):
                neighbors = {"Down": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 3),
                             "Left": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 1)}
            elif(location_of_zero == 4):
                neighbors = {"Up": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 3),
                             "Down": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 3),
                             "Right": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 1)}
            elif(location_of_zero == 5):
                neighbors = {"Up": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 3),
                             "Down": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 3),
                             "Left": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 1),
                             "Right": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 1)}
            elif(location_of_zero == 6):
                neighbors = {"Up": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 3),
                             "Down": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 3),
                             "Left": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 1)}
            elif(location_of_zero == 7):
                neighbors = {"Up": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 3),
                             "Right": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 1)}
            elif(location_of_zero == 8):
                neighbors = {"Up": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 3),
                             "Left": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 1),
                             "Right": self.swap_board_positions(board_state,location_of_zero,location_of_zero + 1)}
            elif(location_of_zero == 9):
                neighbors = {"Up": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 3),
                             "Left": self.swap_board_positions(board_state,location_of_zero,location_of_zero - 1)}
        else:
            print "The location of the empty tile is:", location_of_zero, "outside of accepted positions on the board."
            return None
        
        return neighbors
    
    def swap_board_positions(self,board_state, location_of_zero, new_location_of_zero):
        board_state_tuple = (str(board_state))
        number_to_swap_zero_with = int(board_state_tuple[new_location_of_zero])
        return board_state - number_to_swap_zero_with*pow(10,9-new_location_of_zero) + number_to_swap_zero_with*pow(10,9-location_of_zero) 
            

class SearchAlgorithm:
    goal_state = 1012345678
    frontier = None
    frontier_dict = None
    max_search_depth = None
    
    def __init__(self):
        self.frontier = deque()

    def goal_test(self,board_state):
        if board_state == self.goal_state:
            return True
    
    def get_the_next_board_state_from_the_frontier(self):
        return None

    def put_neighbor_into_frontier(self, neighbor):
        return self.frontier.append(neighbor)


    def determine_if_to_insert_neighbor_into_frontier(self, explored_set, board_state, direction, neighbor):
        if neighbor not in self.frontier_dict and neighbor not in explored_set:
            self.frontier_dict[neighbor] = {'parent':board_state, 'direction':direction, 'search_depth':self.frontier_dict[board_state]['search_depth'] + 1}
            self.put_neighbor_into_frontier(neighbor)
            if (self.frontier_dict[neighbor]['search_depth'] > self.max_search_depth):
                self.max_search_depth = self.frontier_dict[neighbor]['search_depth']

    def get_the_optimal_solution_with_board(self,initial_board_configuration):
            
        def convert_initial_board_configuration_to_a_unique_number():    
            result = pow(10,9)
            for index in range(9):
                result += pow(10,8-index)*initial_board_configuration[index]
            return result
            
        def frontier_queue_is_not_empty():
            return self.frontier

        order_of_search=self.get_order_of_search()
        board_configuration_number = convert_initial_board_configuration_to_a_unique_number()
        self.frontier_dict = {board_configuration_number:{'parent':None,'direction':None,'search_depth':0}}
        self.put_neighbor_into_frontier(board_configuration_number)
        explored_set = set()
        eight_puzzle_result = EightPuzzleResult()
        tree_operations = TreeOperations() 
        self.max_search_depth = 0
        while(frontier_queue_is_not_empty()):
            board_state = self.get_the_next_board_state_from_the_frontier()
            explored_set.add(board_state)
#             print board_state
            if(self.goal_test(board_state)):
                eight_puzzle_result.get_path_to_solution(self.frontier_dict,board_state)   
                eight_puzzle_result.max_search_depth = self.max_search_depth             
                return eight_puzzle_result
            eight_puzzle_result.nodes_expanded += 1
            neighbors = tree_operations.get_all_neighbors_for(board_state)
            for direction in order_of_search:
                if direction in neighbors:
                    neighbor = neighbors[direction]
                    self.determine_if_to_insert_neighbor_into_frontier(explored_set, board_state, direction, neighbor)
        return None

class BFS(SearchAlgorithm):    

    def get_the_next_board_state_from_the_frontier(self):
        return self.frontier.popleft()

    def get_order_of_search(self):
        return "Up", "Down", "Left","Right"


class DFS(SearchAlgorithm):    

    def get_the_next_board_state_from_the_frontier(self):
        return self.frontier.pop()

    def get_order_of_search(self):
        return "Right","Left","Down","Up"


class AST(SearchAlgorithm):
    
    cost_from_here_to_goal_var = 0
    priority_and_board_state_dict = {}
    
    def __init__(self):
        self.frontier = []
        self.priority_and_board_state_dict = {}
        self.cost_from_here_to_goal_var = 0

    def get_order_of_search(self):
        return "Up", "Down", "Left","Right"
 
    def get_the_next_board_state_from_the_frontier(self):
        while self.frontier:
            board_state = heappop(self.frontier)[1]
            if board_state is not 'removed':
                del self.priority_and_board_state_dict[board_state]
                return board_state
        raise KeyError('The heap is empty')

    def cost_from_here_to_goal(self,board_state):
        tuple_of_board_state = (str(board_state))
        cost_to_goal = 0
        for board_position, board_tile_value in enumerate(tuple_of_board_state[1:10]):
            goal_row = int(board_tile_value)/3
            curr_row = board_position/3
            cost_to_goal += abs((int(board_tile_value) - goal_row*3) - (board_position - curr_row*3)) + abs(goal_row - curr_row)
        return cost_to_goal
            
    def remove_priority_and_board_state_tuple_from_heap(self, neighbor):
        priority_and_board_state_tuple = self.priority_and_board_state_dict[neighbor] 
        self.frontier.remove(priority_and_board_state_tuple)
        self.priority_and_board_state_dict[neighbor] = (priority_and_board_state_tuple[0],"removed")
        heapify(self.frontier)
        
    def put_neighbor_into_frontier(self, neighbor):
        if neighbor in self.priority_and_board_state_dict:
            self.remove_priority_and_board_state_tuple_from_heap(neighbor)
        cost_to_this_point = self.frontier_dict[neighbor]['search_depth']
        cost = cost_to_this_point + self.cost_from_here_to_goal_var
        priority_and_board_state_tuple = (cost,neighbor)
        self.priority_and_board_state_dict[neighbor] = priority_and_board_state_tuple
        heappush(self.frontier,priority_and_board_state_tuple)
            
    def determine_if_to_insert_neighbor_into_frontier(self, explored_set, board_state, direction, neighbor):
        self.cost_from_here_to_goal_var = self.cost_from_here_to_goal(neighbor)
        if neighbor not in self.frontier_dict and neighbor not in explored_set:
            self.frontier_dict[neighbor] = {'parent':board_state, 'direction':direction, 'search_depth':self.frontier_dict[board_state]['search_depth'] + 1}
            self.put_neighbor_into_frontier(neighbor)
            if (self.frontier_dict[neighbor]['search_depth'] > self.max_search_depth):
                self.max_search_depth = self.frontier_dict[neighbor]['search_depth']
        elif neighbor in zip(*self.frontier)[1]:
            cost_to_this_point = self.frontier_dict[neighbor]['search_depth']
            cost = cost_to_this_point + self.cost_from_here_to_goal_var
            cost_of_board_state_in_frontier = self.priority_and_board_state_dict[neighbor][0]
            if cost < cost_of_board_state_in_frontier:
                self.frontier_dict[neighbor] = {'parent':board_state, 'direction':direction, 'search_depth':self.frontier_dict[board_state]['search_depth'] + 1}
                self.put_neighbor_into_frontier(neighbor)