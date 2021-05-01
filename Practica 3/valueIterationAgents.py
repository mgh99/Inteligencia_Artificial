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
        
        # For the selected range of iterations the following happens
        for i in range(0,self.iterations):
            temporal = util.Counter() # The counter

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
        # EXERCISE 1 part 1/2
        # VALUE ITERATION

        # It's checked if it's the final state
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
        # EXERCISE 1 part 2/2
        # VALUE ITERATION

        # We check that the game isn't over
        if self.mdp.isTerminal(state):
            return None

        maxSum = float ("-inf") 
        endAction = None 

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

        # EXERCISE 4
        # ASYNCHRONOUS VALUE ITERATION

        # For the range of interactions required.
        for i in range(self.iterations):

            index = i %  len(self.mdp.getStates()) # The modulus of the Markov decision process is calculated.
            state = self.mdp.getStates()[index] 
            top = self.computeActionFromValues(state)

            if not top: # If not at the top the value of q is 0.
                qval = 0
            else: # If not, it's added.
                qval = self.computeQValueFromValues(state, top)

            self.values[state] = qval


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
        # EXERCISE 5
        # PRIORITISED SCANNING VALUE ITERATION

        pq = util.PriorityQueue()
        predecessors = {}

        # We calculate the predecessors in each state.
        for state in self.mdp.getStates():
          if not self.mdp.isTerminal(state):
            for action in self.mdp.getPossibleActions(state):
              for nextState, prob in self.mdp.getTransitionStatesAndProbs(state, action):

                if nextState in predecessors:
                  predecessors[nextState].add(state)
                else:
                  predecessors[nextState] = {state}

        # We obtain the difference of each state and it's maximum value.
        for state in self.mdp.getStates():
          if not self.mdp.isTerminal(state):
            values = []

            for action in self.mdp.getPossibleActions(state):
              q_value = self.computeQValueFromValues(state, action)
              values.append(q_value)

            diff = abs(max(values) - self.values[state])
            # We add to the queue with priority to the smallest value (min-heap).
            pq.update(state, -diff)

        # Iterating on the predecessors and exploring the states with the most diff.
        for i in range(self.iterations):
          if pq.isEmpty():
            break

          temp_state = pq.pop()
          if not self.mdp.isTerminal(temp_state):
            values = []

            for action in self.mdp.getPossibleActions(temp_state):
              q_value = self.computeQValueFromValues(temp_state, action)
              values.append(q_value)
            self.values[temp_state] = max(values)

          for p in predecessors[temp_state]:
            if not self.mdp.isTerminal(p):
              values = []

              for action in self.mdp.getPossibleActions(p):
                q_value = self.computeQValueFromValues(p, action)
                values.append(q_value)
              diff = abs(max(values) - self.values[p])

              # We add to the queue with priority if the difference is greater than the tolerated noise.
              if diff > self.theta:
                pq.update(p, -diff)

