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
        #EJERCICIO 1
        #AGENTE REFLEJO

        distancia = []  # Distancia de Manhattan
        listaComida = currentGameState.getFood().asList() # Lista de comida
        posicaoPacman = list(successorGameState.getPacmanPosition())  # Posicion de Pacman

        if action == 'Stop':
          return -float("inf")

        for ghostState in newGhostStates: # Estado dos Fantasmas
          if ghostState.getPosition() == tuple(posicaoPacman) and ghostState.scaredTimer is 0:
            return -float("inf")

        for comida in listaComida:
          x = -1 * abs(comida[0] - posicaoPacman[0])
          y = -1 * abs(comida[1] - posicaoPacman[1])
          distancia.append(x + y)

        return max(distancia)
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
    #PREGUNTA 2

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
        #EJERCICIO 2 
        #MINIMAX: tiene que trabajar para cualquier numero de fantasmas, con varias capas minimas
        #NO FUNCIONA AL PASAR EL AUTOGRADER

        numberGhost = gameState.getNumAgents() - 1
        bestAction = Directions.STOP
        score = -(float("inf"))

        def maxAgent(gameState, depth, numberGhost):

            #Si el juego se ha terminado
            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)

            # i = -INF en el maximo
            i = -(float("inf"))
            #Se pone a 0 porque es el nexo con el pacman
            legalActions = gameState.getLegalActions(0)

            #Para cada accion se intenta obtener la maxima puntuacion para el minimo de movimientos
            for action in legalActions: 
                i = max(i, minAgent(gameState.generateSuccessor(0, action), depth - 1, 1, numberGhost))
            return i #La recursividad termina cuando =>depth devuelve la mejor accion

        def minAgent(gameState, depth, agentindex, numberGhost):

            if gameState.isWin() or gameState.isLose() or depth == 0:
                return self.evaluationFunction(gameState)

            # i = INF en el minimo   
            i = float("inf")
            legalActions = gameState.getLegalActions(agentindex) #Acciones perimitidas para seleccionar un nexo con el agente

            if agentindex == numberGhost:

                for action in legalActions:
                    #Si se trata de un terminal
                    i = min(i, maxAgent(gameState.generateSuccessor(agentindex, action), depth - 1, numberGhost))
            else:# El ultimo fantasma

                for action in legalActions:
                    #Si no se trata de un terminal
                    i = min(i, minAgent(gameState.generateSuccessor(agentindex, action), depth, agentindex + 1, numberGhost)) #Se pone +1 para seleccionar el siguiente fantasma
            return i #devuleve la puntuación

        legalActions = gameState.getLegalActions()
        
        
        for action in legalActions:

            nextState = gameState.generateSuccessor(0, action) #La profundidad es 0
            prevScore = score
            #Se actualiza la puntuación a la mejor del maximo
            score = max(score, minAgent(nextState, self.depth, 1, numberGhost))

            if score > prevScore:
                bestAction = action

        return bestAction # Devuelve la mejor puntuación

        util.raiseNotDefined()

       # util.raiseNotDefined() , no se si puedeo quitarlo


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #EJERCICIO 3 
        #PODA ALFA-BETA si que funciona

        numberGhost = gameState.getNumAgents() - 1
        alpha = float("-inf")
        beta = float("inf")

        def maxAgent(gameState, depth, alpha, beta):

          #Si el juego se ha terminado
          if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

          # Inicializamos la mejor accion y la mejor puntuacion
          # i = -INF en el maximo
          bestAction = None
          bestScore = float("-inf")
          legalActions = gameState.getLegalActions(0) # es 0 pq es la forma de indexarse con el pacman
          
          #Para cada accion se pude obtener la maxima puntuacion con el minimo de movimientos
          for action in legalActions:
            successorGameState = gameState.generateSuccessor(0, action)
            i = minAgent(successorGameState, depth, 1, alpha, beta)

            # Se actualiza a la mejor maxima puntuacion
            if(i > bestScore):
              bestScore = i
              bestAction = action

            if(bestScore > beta):
              return bestScore
            alpha = max(alpha, bestScore)

          # Para que la llamada recursiva termine => depth = profundidad inicial, que devuelve la mejor accion
          if depth == 0:
            return bestAction
          else: # Si se trata de diferentes profundidades se necesita devolver la puntuación
            return bestScore

        def minAgent(gameState, depth, ghost, alpha, beta):

          if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

          # Inicializamos la puntuacion
          # i = INF en el minimo
          bestScore = float("inf")
          legalActions = gameState.getLegalActions(ghost) # Las acciones perimitidas para los fantasma que existan en ese momento
          
          for action in legalActions:
            successorGameState = gameState.generateSuccessor(ghost, action)

            if(ghost < numberGhost):
              # Quedan fantasmas por moverse
              # Si se usa +1 es para seleccionar el siguiente fantasma
              i = minAgent(successorGameState, depth, ghost + 1, alpha, beta) # devuelve la puntuación
            else:

              # Si se trata del ultimo fantasma se devuleve el camino hasta el pacman
              if(depth == self.depth - 1): # Si estamos en un estado terminal
                i = self.evaluationFunction(successorGameState)
              else:
                # Si no es un estado terminal
                i = maxAgent(successorGameState, depth + 1, alpha, beta) # Y devuleve la puntuacion
            
            # Se actualiza a la mejor puntuacion minima
            bestScore = min(i, bestScore)
            
            if(bestScore < alpha):
              return bestScore
            beta = min(beta, bestScore)

          return bestScore


        # AQUI SE DEVUELVE LA ACCION
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
        #EJERCICIO 4
        #EXPECTIMAX

        depth = 0
        indexAgent = 0
        val = self.valor(gameState, indexAgent, depth)
        return val[0]

    def valor(self, gameState, indexAgent, depth):

        if indexAgent >= gameState.getNumAgents():
          indexAgent = 0
          depth = depth + 1

        #Si la profundidad es igual a la propia se devuelve gameState
        if depth == self.depth:
          return self.evaluationFunction(gameState)

        if indexAgent == self.pacmanIndex:
          return self.maxAgent(gameState, indexAgent, depth) # Se devuelve la mejor maxima puntuacion
        else:
          return self.expValor(gameState, indexAgent, depth)

    def expValor(self, gameState, indexAgent, depth):

        i = ["unknown", 0]

        if not gameState.getLegalActions(indexAgent):
          return self.evaluationFunction(gameState)

        probability = 1.0 / len(gameState.getLegalActions(indexAgent))

        for action in gameState.getLegalActions(indexAgent):
          if action == "Stop":
            continue

          retVal = self.valor(gameState.generateSuccessor(indexAgent, action), indexAgent + 1, depth)

          if type(retVal) is tuple:
            retVal = retVal[1]

          i[1] = i[1] + (retVal * probability)
          i[0] = action

        return tuple(i)

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

    distanceToFood = [] # Distancia de Manhattan
    distanceToNearestGhost = [] #Distancia al fantasma mas cercano

    foodList = currentGameState.getFood().asList() 
    ghostStates = currentGameState.getGhostStates()
    capsuleList = currentGameState.getCapsules()
    numberOfScaredGhosts = 0

    pacmanPos = list(currentGameState.getPacmanPosition()) #Posicion del pacman

    # Para cada posicion del fantasma
    for ghostState in ghostStates:

        #Si el temporizador de los fantasmas asustados esta en 0
        if ghostState.scaredTimer is 0: 
            numberOfScaredGhosts = numberOfScaredGhosts + 1 
            distanceToNearestGhost.append(0)
            continue

        ghostCoord = ghostState.getPosition()
        #Posiciones en el eje x e y de los fantasmas
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

    #Si no queda distancia hasta la comida entonces se añade a la lista en la posicion 0
    if not distanceToFood:
      distanceToFood.append(0)

    return max(distanceToFood) + min(distanceToNearestGhost) + currentGameState.getScore() - 80*len(capsuleList) - 30 *(len(ghostStates) - numberOfScaredGhosts)

    #util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
