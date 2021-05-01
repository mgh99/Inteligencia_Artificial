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
# ANÁLISIS DE CRUCE DE PUENTES
"""
    Para que el agente sobreviva, hay que eliminar el ruido pero no por completo
"""
def question2():
    answerDiscount = 0.9
    answerNoise = 0.01 # He cambiado el valor de 0.2 por 0.01
    # Tengo que mirar de donde sale el 0.01 pq no tengo ni idea
    return answerDiscount, answerNoise

# EJERCICIO 3 parte 1/5
# POLÍTICAS
"""
    Sólo hay que cambiar la recompensa viva por una que oblige al agente a terminar rápido.
    Lo admito esta la he encontrado de pura suerte, pero funciona
"""
def question3a():
    answerDiscount = 0.3  
    answerNoise = float(0)  
    answerLivingReward = float(0)  
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 3 parte 2/5
# POLÍTICAS
"""
    En primer lugar, tenemos que cambiar la recompensa viva en la que el agente quiera terminar
    rápido. 
    Pero sin que se caiga, así que tenemos que cambiar el ruido para decirle que no es
    una buena idea ir al puente y al hacer eso, tenemos que cambiar la tasa de descuento.
"""
def question3b():
    answerDiscount = 0.1 
    answerNoise = 0.1  
    answerLivingReward = 0.7 
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 3 parte 3/5
# POLÍTICAS
"""
    Necesitamos una recompensa no demasiado grande para que vaya en + 1
"""
def question3c():
    answerDiscount = 0.9  
    answerNoise = float(0)  
    answerLivingReward = float(0)  
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 3 parte 4/5
# POLÍTICAS
"""
    Se pone una respuesta de recompensa negativa para que haga el camino más largo que exista
"""
def question3d():
    answerDiscount = 0.9  
    answerNoise = 0.5  
    answerLivingReward = -0.1  
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 3 parte 5/5
# POLÍTICAS
"""
    Así que ponemos una gran recompensa, para que se sepa cuál es mejor sin terminar el juego
"""
def question3e():
    answerDiscount = 0.01  
    answerNoise = float(0)  
    answerLivingReward = 100  
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

# EJERCICIO 8
# CRUCE DE PUENTES REVISITADO
"""
        Si disminuimos epsilon, el agente irá a los mejores lugares, pero no explorará los nuevos
    pero eso es un fallo, porque no encontrará el estado terminal dentro de 50 interacciones.
        Y al aumentar epsilon, el agente descubrirá nuevos lugares, pero será aleatorio y la 
    política no será óptima después de 50 iteraciones. 
        Puede que encuentre el camino bueno, pero no tendremos un éxito asegurado
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
