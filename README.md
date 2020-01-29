# Python Pathfinders

## Done

Currently, there are 5 path-finding algorithms in this script :

* A star
* Dijkstra
* Depth-First Search
* Breadth-First Search
* Spanning Tree Walk

## To Do

In the future, I would like to implement a bunch of pathfinding algorithms that could be interesting for future projects :

* Iterative Deeping A* (IDA*)
* Bi-directional A*
* Best-First

I could also create a Cell class that has the costs (f, h, g) attributes instead of using heavy dictionnaries that results in heavy sorting. ( hard to read ) 

Also, creating a "diagonal" mode could be interesting in terms of optimal search, since a real robot will not just move only up, down, left and right. 

## Setup

To setup the project on your local machine:

1. Click on `Fork`.
2. Go to your fork and `clone` the project to your local machine.
3. `git clone https://github.com/master-coro/artin-pathfinding.git`

## Run

To run the project:
1. Cd into the root of the project `cd path/artin-pathfinding`
2. Run the main script with necessary args : `python src/PathFinder.py`

## Contribute

To contribute to the project:

1. Choose any open issue from [here](https://github.com/master-coro/artin-pathfinding/issues). 
2. Comment on the issue: `Can I work on this?` and get assigned.
3. Make changes to your fork and send a PR.

To create a PR:

Follow the given link to make a successful and valid PR: https://help.github.com/articles/creating-a-pull-request/

To send a PR, follow these rules carefully,**otherwise your PR will be closed**:

1. Make PR title in this format: `Fixes #IssueNo : Name of Issue`

For any doubts related to the issues, i.e., to understand the issue better etc, comment down your queries on the respective 
