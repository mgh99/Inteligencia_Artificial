# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

# EXERCISE 2
# BRIDGE CROSSING ANALYSIS
"""
    For the agent to survive, the noise must be eliminated but not completely.
"""
def question2():
    answerDiscount = 0.9
    answerNoise = 0.01 
    return answerDiscount, answerNoise

# EXERCISE 3 part 1/5
# POLICIES
"""
    Just change the live reward to one that forces the agent to finish quickly.
    I admit this one I found by just pure luck, but it works!
"""
def question3a():
    answerDiscount = 0.3  
    answerNoise = float(0)  
    answerLivingReward = float(0)  
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EXERCISE 3 part 2/5
# POLICES
"""
        First we have to change the live reward where the agent wants to finish quickly. 
        But without dropping it, so we have to change the noise to tell him that it isn't a good 
    idea to go to the bridge a good idea to go to the bridge and in doing that we have to 
    change the discount rate.
"""
def question3b():
    answerDiscount = 0.1 
    answerNoise = 0.1  
    answerLivingReward = 0.7 
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EXERCISE 3 part 3/5
# POLICES
"""
    We need a reward that isn't too big to be positive.
"""
def question3c():
    answerDiscount = 0.9  
    answerNoise = float(0)  
    answerLivingReward = float(0)  
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EXERCISE 3 part 4/5
# POLICES
"""
    I have set a negative reward response to make it the longest path there is.
"""
def question3d():
    answerDiscount = 0.9  
    answerNoise = 0.5  
    answerLivingReward = -0.1  
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EXERCISE 3 part 5/5
# POLICES
"""
    We put a big reward, so that you know which one is better without finishing the game.
"""
def question3e():
    answerDiscount = 0.01  
    answerNoise = float(0)  
    answerLivingReward = 100  
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EXERCISE 8
# BRIDGE CROSSING REVISITED
"""
        If we decrease epsilon, the agent will go to the best places, but won´t
    explore the new ones  but that is a fail, because it will not find the terminal state within many interactions.
        And by increasing epsilon, the agent will discover new places, but it will be 
    random and the policy won't be optimal after many iterations. 
        It might find the good path, but we won't have a guaranteed success.
"""
def question8():
    answerEpsilon = 0.3
    answerLearningRate = 0.5
    #return answerEpsilon, answerLearningRate
    #if not possible, 
    return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))

