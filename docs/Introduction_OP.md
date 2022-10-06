## Identity the problem you wish to solve 
* Linear Optimization
	* Objective and constraints are linear expressions in the variables 
*  Constraint optimization 
	* Identify feasible solutions out of a very large set of candidates
	* CP is based on feasibility (finding a feasible solution) rather than optimization (finding an optimal soluion )
* Mixed-integer optimization
	* Some or all of the variables are required to be integers 
	* For example, the assignment problem, in which of a group of workers needs to be assigned to a set of tasks
	* For each worker and task, you define a variable whose value is 1 if the given worker is assigned to the given task and 0 otherwise. 
	* In this case,  the variables can only take on the values of 0 or 1.
* Bin packing
	* Packing a set of objects of different sizes into containers with different capacities.
	* Goal: Pack as many  of the objects as possible, subject to the capacities of the containers.
	* A special case is the knapsack problem, in which there is just one container.
* Network flows
	* Problems can be represented by a directed graph consiting of nodes and directed arcs between them.
* Assignment 
	* Assign a group of agents (workers or machines) to a set of tasks, where there is a fixed cost for assigning each agent to a specific task. 
	* Find the assignment with the least total cost.
	* Assignment problems are actually a special case of network flow problems.
* Scheduling 
	* Assign resources to perform a set of tasks at specific times.
	* An important example: job shop problem, multiple jobs are processed on several machines. Each job consists of a sequence of tasks, which must be performed in a given order and each task must be processed on a specific machine.
	* The problem is to assign a schedule so that all jobs are completed in as short an interval of time as possible.

* Routing 
	* Finding the optimal routes for a fleet of vehicles to traverse a network 
	* Defined by a directed graph.




## Routing Problem 
Input: 
* Given a set of locations 


Find an optimal routes for one/multiple vehicles.
There is one vehicle -> Traveling Salesperson Problem.

Optimal route: least total distance. 

Optimal solution is to assign just one vehicle/person to visist all locations, and find the shortest route for that vehicle. 

A better way to define optimal routes is to minimize the length of the longest  single route among all vehicles. 

Vehicle Routing Problem:
* Generalize the Travelling Sales Problem by adding some constraints on the vehicles.
	* **Capacity constraints**: the vehicles need to pick up items at each location  they visit, but have a maximum carrying capacity.
	* **Time windows**: each location must be visited within a specific time window.


