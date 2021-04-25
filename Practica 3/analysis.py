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

# EJERCICIO 2
def question2():
    answerDiscount = 0.9
    answerNoise = 0.01 # He cambiado el valor de 0.2 por 0.01
    # Tengo que mirar de donde sale el 0.01 pq no tengo ni idea
    return answerDiscount, answerNoise

# EJERCICIO 3 parte 1/5
# NOTA: no sé el por qué de esos valores, tengo que INVESTIGAR para todos los 3

def question3a():
    answerDiscount = 0.3  # He cambiado el valor de None por 0.3
    answerNoise = float(0)  # He cambiado el valor de None por float(0)
    answerLivingReward = float(0)  # He cambiado el valor de None por float(0)

    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 3 parte 2/5
def question3b():
    answerDiscount = 0.1 # He cambiado None por 0.1
    answerNoise = 0.1  # He cambiado None por 0.1
    answerLivingReward = 0.7 # He cambiado None por 0.7
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 3 parte 3/5
def question3c():
    answerDiscount = 0.9  # He cambiado None por 0.9
    answerNoise = float(0)  # He cambiado None por float(0)
    answerLivingReward = float(0)  # He cambiado None por float(0)
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 3 parte 4/5
def question3d():
    answerDiscount = 0.9  # He cambiado None por 0.9
    answerNoise = 0.5  # He cambiado None por 0.5
    answerLivingReward = 1.0  # He cambiado None por 1.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 3 parte 5/5
def question3e():
    answerDiscount = 0.01  # He cambiado None por 0.01
    answerNoise = float(0)  # He cambiado None por float(0)
    answerLivingReward = 100  # He cambiado None por 100
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 8
# CRUCE DE PUENTES REVISITADO
def question8():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
