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
    #Búsqueda en profundidad (DFS): algoritmo de búsqueda no informada, para recorrer todos los nodos de
    #manera ordenada pero no uniforme.
    
    temp = problem.getStartState()
    past = []
    fringe = util.Stack() #STACK -> lista
    fringe.push((temp, []))

    #Aqui empiezo a comentar lo que hace, lo anterior no se para que sirve
    while not fringe.isEmpty(): # As long as the lifo list is empty
        
        temp, path = fringe.pop() # The temp and path variables are placed at the beginning of the list
        past.append(temp) #

        if problem.isGoalState(temp): # Si no lo sé 
            return path 

        for child in problem.getSuccessors(temp): # For each child and their successors 
            if child[0] not in past: # Si 
                fringe.push((child[0], path + [child[1]]))

    #NO ENTIENDO NADA PERO ES LA SOLUCIÓN CORRECTA PQ ES LA PRACTICA DE INTERNET Y LA HE ENCONTRADO

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Búsqueda primero en amplitud (BFS): procesa todos los nodos por encima de la solución más superficial. Explorando
    #los nodos vecinos en profundidad antes de pasar a los nodos del siguiente nivel de profundidad.

    fringe = util.Queue # es una cola -- finge = franja
    fringe.push( (problem.getStartState(), []) )
    expanded = []
    #Aqui empiezo a comentar lo que hace, lo anterior no se para que sirve

    while not fringe.isEmpty(): #Mientras no esté vacía la lista
        node = fringe.pop() #el nodo, los pasos a seguir y el costo entre los nodos se pone al principio de la lista
        coordinate = nextNode [0]
        newPass = nextNode [1]

        if problem.isGoalState(coordinate):
            return newPass
        
        if coordinate not in done:
            done.add(coordinate)

            for i in problem.getSuccessors(coordinate):

                if i[0] not in done:
                    fringe.push((i[0], newPass[i[1]]))


    return [] #no se si hace falta o no

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    #BUSQUEDA POR COSTE UNIFORME
    fringe = util.PriorityQueue
    fringe.push((problem.getStartState(), [], 0))
    exploredState = []

    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if problem.isGoalState(state):
            return actions

        if state not in exploredState:
            sucessors = problem.getSucessors(state)

            for succ in sucessors:
                coordinates = succ[0]

                if coordinates not in exploredState:
                    directions = succ[0]
                    newCost = actions + [directions]
                    fringe.push((coordinates, actions + [directions]), problem.getCostOfActions(newCost))
        
        exploredState.append(state)
    return actions


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
    #A*
    fringe = util.PriorityQueue
    start_node = problem.getStartState()
    start_heuristic = heuristic(start_node, problem)
    visited_nodes = []
    fringe.push((start_node, [], 0), start_heuristic)
    directions = []

    while not fringe.isEmpty():
        get_xy, directions, get_cost = fringe.pop()

        if problem.isGoalState(get_xy):
            return directions

        if not get_xy in visited_nodes:
            visited_nodes.append(get_xy)

            for coordinates, direction, sucessor_cost in problem.getSuccessors(get_xy):

                if not coordinates in visited_nodes:
                    actions_list = list(directions)
                    actions_list = actions_list + [direction]

                    cost_actions = problem.getCostOfActions(actions_list)
                    get_heuristic = heuristic(coordinates, problem)
                    fringe.push((coordinates, actions_list, 1), cost_actions + get_heuristic)
    
    return[]
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
