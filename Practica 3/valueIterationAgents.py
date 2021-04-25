# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        #esto es nuevo pero en la practica no pone nada de añadirlo
        # Si lo quito deja de funcionar así que lo voy a dejar de momento como provisional
        
        # Para el rango de iteraciones seleccionadas pasa lo siguiente
        for i in range(0,self.iterations):
            temporal = util.Counter() # El contador

            for s in self.mdp.getStates():

                if self.mdp.isTerminal(s):
                    temporal[s] = 0
                else:
                    maxVal = float("-inf")

                    for action in self.mdp.getPossibleActions(s):
                        total = 0

                        for nextState, prob in self.mdp.getTransitionStatesAndProbs (s, action):

                            vals = self.values[nextState]
                            total = total + (prob * (self.mdp.getReward(s,action,nextState) + (self.discount*vals)))

                        maxVal = max(total, maxVal)
                        temporal[s] = maxVal
                        print("temporal[state]: ",  temporal[s])

            self.values = temporal
            print("self.values", self.values)
            


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 1
        # ITERACION DE VALOR

        # Se comprueba si es el estado final
        endStates = self.mdp.getTransitionStatesAndProbs(state, action)
        Qvalue = 0

        for nextState, probs in endStates:
            Qvalue = Qvalue + (probs * (self.mdp.getReward(state,action,nextState) + (self.discount*self.values[nextState])))
        return Qvalue

        #util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # EJERCICIO 1
        # ITERACION DE VALOR

        # Se comprueba que el juego no haya terminado
        if self.mdp.isTerminal(state):
            return None

        maxSum = float ("-inf") # = val
        endAction = None # = policy

        for i in self.mdp.getPossibleActions(state):

            temporal = self.computeQValueFromValues(state, i)
            
            if temporal >= maxSum:
                maxSum = temporal
                endAction = i
        return endAction

        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        #esto es como la parte de arriba
        # se supone que no hay que hacer nada según el enunciado de la practica
        # si lo quito funciona igual
        # para que sirve? Si solo dejo esta parte no unciona
        # de momento lo dejo pero creo que lo puedo quitar

        """
        vals = util.Counter()
        states = self.mdp.getStates()

        for i in range(self.iterations):
            currentState = states[i % len(states)]
            vals = self.values.copy()
            possibleVals = []

            if self.mdp.isTerminal(currentState):
                self.values[currentState] = 0
            elif not self.mdp.isTerminal(currentState):
                for action in self.mdp.getPossibleActions(currentState):
                    tempValue = 0
                    
                    for t in self.mdp.getTransitionStatesAndProbs(currentState, action):
                        tempValue += t[1]*(self.mdp.getReward(currentState, action, t[0]) + self.discount * vals[t[0]])
                    possibleVals.append(tempValue)
                self.values[currentState] = max(possibleVals)
        """


class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
