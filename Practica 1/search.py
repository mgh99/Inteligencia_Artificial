# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #EJERCICIO 1

    #Búsqueda en profundidad (DFS): algoritmo de búsqueda no informada, para recorrer todos los nodos de
    #manera ordenada pero no uniforme. 

    """
    EXERCISE 1

    Deep Search (DFS): uninformed search algorithm, 
    to search through all nodes in an ordered but non-uniform manner. 

    If my list isn't empty, I delete the path and the temp. Then it's added temp to the list.
    If I have found the goal I get back the path traveled.
    For each child that has a successor and if the child isn't in the list add it.

    ------------------------------------------------------------------------------------
    To test this part here are the commands available for it:
        python pacman.py -l tinyMaze -p SearchAgent (500)
        python pacman.py -l mediumMaze -p SearchAgent (380)
        python pacman.py -l bigMaze -z .5 -p SearchAgent (380)
    -------------------------------------------------------------------------------------

    """

    #************************************************************************************************
    temp = problem.getStartState()
    past = []
    fringe = util.Stack() 
    fringe.push((temp, []))

    while not fringe.isEmpty(): 

        temp, path = fringe.pop() 
        past.append(temp) 

        #Si se ha llegado a la meta devuelve el camino
        if problem.isGoalState(temp): 
            return path 

        #Si los hijos tienen sucesores y no están añadidos a la lista se añaden
        for child in problem.getSuccessors(temp): 
            if child[0] not in past: 
                fringe.push((child[0], path + [child[1]]))

    #************************************************************************************************

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    """
    EXERCISE 2

    Breadth first search (BFS): processes all nodes above the next highest shallowest solution.
    Exploring neighbouring nodes in depth before moving on to nodes at the next depth level. 

        As long as the empty fringe isn't available, the directions and get_state_xy are removed from the queue.
        If the goal has been located at the selected coordinates, the path is returned. 
    But for each: address, cost and successor, where if the state hasn't been visited, 
    the successor is visited and added to the queue and the: successor, address and address position 
    are added to the fringe.

    ------------------------------------------------------------------------------------
    To test this part here are the commands available for it:
        python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs        # 442 -> score
        python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5     # 300 -> score

        python eightpuzzle.py
    -------------------------------------------------------------------------------------

    """

    #****************************************************************************************************
    fringe = util.Queue()
    directions = []
    visited_states = []

    fringe.push((problem.getStartState(), []) )
    visited_states.append(problem.getStartState())

    while not fringe.isEmpty():
        
        get_state_xy, directions = fringe.pop()

        if problem.isGoalState(get_state_xy):
            return directions

        else:

            #For successor, direction and cost, if they have successors with coordinates, the following are tracked
            #the visited states
            for successor, direction, cost in problem.getSuccessors(get_state_xy):

                # Track visited states
                if not successor in visited_states:
                    visited_states.append(successor)
                    fringe.push((successor, directions + [direction]))
                
    return []
    #*************************************************************************************************

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    """
    EXERCISE 3

    Uniform Cost Search (UCS): algoritmo de búsqueda no informada  para recorrer el camino de costo
    mínimo entre un nodo raíz y un nodo destino. La búsqueda comienza por el nodo raíz y 
    continúa visitando el siguiente nodo que tiene menor costo total desde la raíz.

        As long as the fringe isn't empty: the fringe of the next state is removed from the queue with priority.
        If the path is found, it's returned and the successor gets the next state.
       For each successor, it is assigned a position in the queue and a check is made to verify that this state
    hasn't been visited before, and if it hasn't, it's added and the states are also updated.
        Finally, as long as the final state is different from the initial state, it tracks the state, 
    adds it to the queue with priority and the actions are added to a reserved list.

    ------------------------------------------------------------------------------------
    To test this part here are the commands available for it:
        python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs           # 442 -> score
        python pacman.py -l mediumDottedMaze -p StayEastSearchAgent       # 646 -> score
        python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
    -------------------------------------------------------------------------------------

    """

    #*********************************************************************************
    priority_queue = util.PriorityQueue()
    trace = {}
    seen = []

    start_state = problem.getStartState()
    prev_cost = 0
    trace[start_state] = [None, None, prev_cost]

    priority_queue.update(start_state, 0)
    seen.append(start_state)

    while not priority_queue.isEmpty():
        
        curr_state = priority_queue.pop()

        if problem.isGoalState(curr_state):
            break

        successors = problem.getSuccessors(curr_state)
        
        for successor in successors:

            next_state = successor[0]
            next_action = successor[1]
            next_cost = successor[2]

            # avoid traveling back to previous states
            if next_state not in seen:
                prev_cost = trace[curr_state][2]
                seen.append(next_state)
                priority_queue.update(next_state, next_cost + prev_cost)
                
            # update and allow tracing to the best state
            if next_state in trace:
                if trace[next_state][2] > next_cost + prev_cost:
                    trace[next_state][2] = next_cost + prev_cost
                    trace[next_state][1] = next_action
                    trace[next_state][0] = curr_state
            else:
                trace[next_state] = [curr_state, next_action, next_cost + prev_cost]

    # back track
    actions = []
    backtrack_state = curr_state # the goal state

    while backtrack_state != start_state:
        prev_state, action, _ = trace[backtrack_state] 
        actions.append(action)
        backtrack_state = prev_state

    actions = list(reversed(actions))
    return actions
    #**********************************************************************************

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    
    """
    EXERCISE 4

    A* (astar): represents the heuristic value of the node to be evaluated from the current node, n,
    to the end, and the actual cost of the path to reach that node, n, from the initial node.

        As long as the fringe is not empty: if the goal is found with the selected coordinates, 
    the path travelled is returned.  
        If the nodes have not been visited, they are added to the queue with the selected priority.
        If the coordinates haven't passed through the visited nodes, first the list of actions 
    is passed by reference with the addresses added to it. And secondly, the coordinates, 
    the address stored in the queue, the position where it's to be stored, the cost of the actions 
    required for the path and the heuristic are added to the queue.

    ------------------------------------------------------------------------------------
    To test this part here are the commands available for it:
        python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
    -------------------------------------------------------------------------------------

    """

    #**********************************************************************************
    fringe = util.PriorityQueue()
    start_node = problem.getStartState()
    start_heuristic = heuristic(start_node, problem)
    visited_nodes = []
    fringe.push( (start_node, [], 0), start_heuristic)
    directions = []

    while not fringe.isEmpty():
        get_xy, directions, get_cost = fringe.pop()

        if problem.isGoalState(get_xy):
            return directions
        
        if not get_xy in visited_nodes:
            # Track visited_nodes
            visited_nodes.append(get_xy)
            
            for coordinates, direction, successor_cost in problem.getSuccessors(get_xy):
                if not coordinates in visited_nodes:
                    # Pass by reference
                    actions_list = list(directions)
                    actions_list += [direction]
                    # Get cost so far
                    cost_actions = problem.getCostOfActions(actions_list)
                    get_heuristic = heuristic(coordinates, problem)
                    fringe.push( (coordinates, actions_list, 1), cost_actions + get_heuristic)
    return []
    #*************************************************************************************

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


