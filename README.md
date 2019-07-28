# Searching Algorithms
The searching algorithms are referenced by CMPT 317 assignment. Author is Professor Michael Horsch

## The Type of Searching Algorithms
* Uninformed Searching Algorithm
	* DepthFirstSearch(s)
	* BreadthFirstSearch(s)  
	* DepthLimitedSearch(s, dlimit)  
	* IDS(s)
* Informed Searching Algorithm
	* UCSSearch(s)  
	* BestFirstSearch(s)
	* AStarSearch(s)

## Instruction For Test
* The codes requires Python 3. X.
* Download all the Python code
* Run at the UNIX prompt:
	* UNIX$ python3 runCD.py
	* usage: python runCD examplefile solver timelimit 					     [depthlimit]
	* solver can be: 'DFS' 'BFS' 'DLS' 'IDS' 'GBFS' 'UCS' 'AStar'
	* if solver is 'DLS' you must provide an additional depthlimit argument
	* timelimit in seconds
* e. g.
	UNIX$ python3 runCD.py simple_examples.txt IDS 1
	<output>
