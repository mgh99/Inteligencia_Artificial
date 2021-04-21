# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        # EXERCISE 1
        # Reflex agent

        range = []  # Distance to Manhattan
        listFood = currentGameState.getFood().asList() # List of food
        positionPacman = list(successorGameState.getPacmanPosition())  # Posicion de Pacman

        if action == 'Stop':
          return -float("inf")

        for ghostState in newGhostStates: # State of 2 ghosts
          if ghostState.getPosition() == tuple(positionPacman) and ghostState.scaredTimer is 0:
            return -float("inf")

        # Calculates the position on the x-axix and y-axis of the food
        for food in listFood:
          x = -1 * abs(food[0] - positionPacman[0])
          y = -1 * abs(food[1] - positionPacman[1])
          range.append(x + y)

        return max(range)
        #return successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2) 
    """
    #EXERCISE 2

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.
        Here are some method calls that might be useful when implementing minimax.
        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1
        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action
        gameState.getNumAgents():
        Returns the total number of agents in the game
        gameState.isWin():
        Returns whether or not the game state is a winning state
        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        #EXERCISE 2 
        #MINIMAX
        #DOESN'T WORK WHEN RUNNING THE autograder.py AND I DON'T KNOW WHY

        numberGhost = gameState.getNumAgents() - 1
        bestAction = Directions.STOP
        score = -(float("inf"))

        def maxAgent(gameState, depth, numberGhost):

            # If the game is over
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)

            # i = -INF in the max
            i = -(float("inf"))
            legalActions = gameState.getLegalActions(0) # Set to 0 because it indexes with pacman

            # For each action we try to obtain the maximum score for the minimum number of moves
            for action in legalActions: 
                i = max(i, minAgent(gameState.generateSuccessor(0, action), depth - 1, 1, numberGhost))
            return i #The recursion ends when => depth returns the best action

        def minAgent(gameState, depth, agentindex, numberGhost):

            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)

            # i = INF in min   
            i = float("inf")
            legalActions = gameState.getLegalActions(agentindex) # Actions allowed to index with the agent

            if agentindex == numberGhost:

                for action in legalActions:
                    # If it's a terminal
                    i = min(i, maxAgent(gameState.generateSuccessor(agentindex, action), depth - 1, numberGhost))
            else:# The last ghost

                for action in legalActions:
                    # If it isn't a terminal
                    i = min(i, minAgent(gameState.generateSuccessor(agentindex, action), depth, agentindex + 1, numberGhost)) #Se pone +1 para seleccionar el siguiente fantasma
            return i # Return score

        legalActions = gameState.getLegalActions()
        
        
        for action in legalActions:

            nextState = gameState.generateSuccessor(0, action) #depth = 0
            prevScore = score

            # The score is updated to the best of the maximum
            score = max(score, minAgent(nextState, self.depth, 1, numberGhost))

            if score > prevScore:
                bestAction = action

        return bestAction # Return the best action

        util.raiseNotDefined()

       # util.raiseNotDefined() 


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #EXERCISE 3 
        #ALPHA-BETA AGENT

        numberGhost = gameState.getNumAgents() - 1
        alpha = float("-inf")
        beta = float("inf")

        def maxAgent(gameState, depth, alpha, beta):

          # If the game is over
          if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

          # We start with the best action and the best score
          # i = -INF in the max
          bestAction = None
          bestScore = float("-inf")
          legalActions = gameState.getLegalActions(0) # is 0 because it's the way to index with pacman
          
          # For each action the maximum score can be obtained with the minimum number of moves
          for action in legalActions:
            successorGameState = gameState.generateSuccessor(0, action)
            i = minAgent(successorGameState, depth, 1, alpha, beta)

            # Updates to the best score
            if(i > bestScore):
              bestScore = i
              bestAction = action

            if(bestScore > beta):
              return bestScore
            alpha = max(alpha, bestScore)

          # Para que la llamada recursiva termine => depth = profundidad inicial, que devuelve la mejor accion
          if depth == 0:
            return bestAction
          else: # For the recursive call to terminate => depth = initial depth, which returns the best action
            return bestScore

        def minAgent(gameState, depth, ghost, alpha, beta):

          if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

          # We start the score
          # i = INF in the min
          bestScore = float("inf")
          legalActions = gameState.getLegalActions(ghost) # The actions allowed for the ghosts that exist at the moment
          
          for action in legalActions:
            successorGameState = gameState.generateSuccessor(ghost, action)

            if(ghost < numberGhost):
              # Ghosts still to move
              # If +1 is used it's to select the next ghost.
              i = minAgent(successorGameState, depth, ghost + 1, alpha, beta) # Returns the score
            else:

              # If it is the last ghost, the path to the pacman is returned.
              if(depth == self.depth - 1): # If it is a terminal
                i = self.evaluationFunction(successorGameState)
              else:
                # If it isn't a terminal
                i = maxAgent(successorGameState, depth + 1, alpha, beta) # Returns the score
            
            # Updates to best minimum score
            bestScore = min(i, bestScore)
            
            if(bestScore < alpha):
              return bestScore
            beta = min(beta, bestScore)

          return bestScore


        # HERE THE ACTION IS RETURNED
        return maxAgent(gameState, 0, alpha, beta) # depth = 0

        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    pacmanIndex = 0
    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        #EXERCISE 4
        #EXPECTIMAX

        depth = 0
        indexAgent = 0
        val = self.valor(gameState, indexAgent, depth)
        return val[0]

    def valor(self, gameState, indexAgent, depth):

        if indexAgent >= gameState.getNumAgents():
          indexAgent = 0
          depth = depth + 1

        # If depth is equal to own depth, gameState is returned
        if depth == self.depth:
          return self.evaluationFunction(gameState)

        if indexAgent == self.pacmanIndex:
          return self.maxAgent(gameState, indexAgent, depth) # The best max score is returned.
        else:
          return self.expValor(gameState, indexAgent, depth)

    def expValor(self, gameState, indexAgent, depth):

        i = ["unknown", 0]

        if not gameState.getLegalActions(indexAgent):
          return self.evaluationFunction(gameState)

        # The probability of finding the path is calculated
        probability = 1.0 / len(gameState.getLegalActions(indexAgent))

        for action in gameState.getLegalActions(indexAgent):
          if action == "Stop":
            continue

          retVal = self.valor(gameState.generateSuccessor(indexAgent, action), indexAgent + 1, depth)

          if type(retVal) is tuple:
            retVal = retVal[1]

          i[1] = i[1] + (retVal * probability)
          i[0] = action

        return tuple(i) # Returns a list of all values

    def maxAgent (self, gameState, indexAgent, depth):
        i = ("unknown", -1 * float("inf"))

        if not gameState.getLegalActions(indexAgent):
          return self.evaluationFunction(gameState)

        for action in gameState.getLegalActions(indexAgent):
          if action == "Stop":
            continue

          retVal = self.valor(gameState.generateSuccessor(indexAgent, action), indexAgent + 1, depth)
          if type(retVal) is tuple:
            retVal = retVal[1]

          iNew = max(i[1], retVal)

          if iNew is not i[1]:
            i = (action, iNew)
            
        return i
        #util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    #EXERCISE 5
    # Evaluation function

    distanceToFood = [] # Distance to Manhattan
    distanceToNearestGhost = [] # Distance to nearest ghost

    foodList = currentGameState.getFood().asList() 
    ghostStates = currentGameState.getGhostStates()
    capsuleList = currentGameState.getCapsules()
    numberOfScaredGhosts = 0

    pacmanPos = list(currentGameState.getPacmanPosition()) # Position of the agent (pacman)

    # For each position of the ghost
    for ghostState in ghostStates:

        # If the timer of the frightened ghosts is set to 0
        if ghostState.scaredTimer is 0: 
            numberOfScaredGhosts = numberOfScaredGhosts + 1 
            distanceToNearestGhost.append(0)
            continue

        ghostCoord = ghostState.getPosition()

        # Positions on the x- and y-axis of the ghosts
        x = abs(ghostCoord[0] - pacmanPos[0]) 
        y = abs(ghostCoord[1] - pacmanPos[1])

        if (x + y) == 0:
            distanceToNearestGhost.append(0)
        else:
            distanceToNearestGhost.append(-1.0 / (x + y))

    for food in foodList:
      x = abs(food[0] - pacmanPos[0])
      y = abs(food[1] - pacmanPos[1])
      distanceToFood.append(-1 * (x + y))

    # If there is no distance left to the food then it is added to the list in position 0.
    if not distanceToFood:
      distanceToFood.append(0)

    return max(distanceToFood) + min(distanceToNearestGhost) + currentGameState.getScore() - 80*len(capsuleList) - 30 *(len(ghostStates) - numberOfScaredGhosts)

    #util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
