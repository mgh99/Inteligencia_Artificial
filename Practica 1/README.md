# PRACTICE 1

## Exercise 1
Finding a fixed food point by the first depth search
To run it:
``` 
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```

## Exercise 2: First breadth-first search
It implements the search algorithm (BFS) in the breadthFirstSearch function in search.py. Once again, write a graph search algorithm that avoids
Again, write a graph search algorithm that avoids expanding already visited states.
To run it: 
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

## Exercise 3: Variation of cost function
While BFS will find some of the most important solutions on the way to the goal, we may wish to find paths that are "better" in other ways.
we may wish to find paths that are "better" in other ways. Consider mediumDottedMaze
and mediumScaryMaze.
To run it:
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

## Exercise 4: A* Search
Implements the graph search A* in the empty function aStarSearch in search.py. A* takes a
heuristic function as an argument. The heuristic takes two arguments: a state in the search problem (the main argument) and the
search problem (the main argument) and the problem itself (for reference information).
To run it: 
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

## Exercise 5: Find all corners
In corner mazes, there are four points, one at each corner. Our new search problem is to find the
Our new search problem is to find the shortest path through the maze that touches all four corners (whether the maze actually has food there or not).
maze actually has food there or not). Note that for some mazes such as
tinyCorners, the shortest path does not always go to the nearest food first! Hint: the shortest path through tinyCorners
through tinyCorners takes 28 steps.
To run it:
``` 
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

## Exercise 6:  Corner problems: Heuristics
Implementing a non-trivial and consistent heuristic for the CornersProblem in cornersHeuristic
To run it:
``` 
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
``` 

## Exercise 7: Eating all the points
Now we will solve a difficult search problem: eat all the pacman food in as few steps as possible.
number of steps possible. To do this, we will need a new definition of the search problem that
formalizes the food search problem: FoodSearchProblem in searchAgents.py (already
implemented). A solution is defined as a path that collects all of the food in the world.
pacman. For the present project, the solutions do not take into account any ghosts or large points; the solutions only depend on the
large points; the solutions only rely on the placement of walls, normal food, and Pacman. (Of course, ghosts can ruin the
of course, ghosts can ruin the execution of a solution!
To run it:
``` 
python pacman.py -l testSearch -p AStarFoodSearchAgent
``` 

## Exercise 8: Suboptimal search
Sometimes, even with A* and a good heuristic, finding the optimal path through all the points is difficult.
difficult. In these cases, we would still like to find a reasonably good path, quickly.
In this section, you will write an agent that always eats the closest point. ClosestDotSearchAgent
is automatically implemented in searchAgents.py, but it's missing a key function that finds
a path to the nearest point.
To run it:
``` 
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
``` 



