# Referenced by CMPT 317 assignments
# CMPT 317.201809: A Python implementation of node queues for informed search.
# Assumes a problem class with the methods:
#   is_goal(problem_state): returns True if the state is the goal state
#   actions(problem_state): returns a list of all valid actions in state
#                           (the actions are only passed to result())
#   result(state, action): returns a new state that is the result of doing action in state.
#
# Search methods are based on TreeSearch (no repeated state checking):
# 1. UCSSearch(s)
# 2. BestFirstSearch(s)
# 3. AStarSearch(s)
# These methods return a SearchResult object, containing information about the search.
# See the definition in UninformedFrontier.
#
# Usage:
#   import InformedSearch as Search
#   pi = <create a problem instance>
#   searcher = Search.Search(pi, <timelimit>)
#   s = <create an initial state for the problem>
#   result = searcher.AStarSearch(s)
#            # or any of the methods above
#   print(str(result))
#   # or public access to any of the data stored in the result.

import InformedFrontier as Frontiers
import Uninformed_Search as BlindSearch

class InformedSearch(BlindSearch.Search):
    """A class to contain informed search algorithms."""

    def __init__(self, problem, timelimit=10):
        """The Search object needs to be given:
            the search Problem,
            a queue for Node(s) to explore
            possibly a depth limit to terminate search
        """
        BlindSearch.Search.__init__(self, problem, timelimit=timelimit)


    def BestFirstSearch(self, initialState):
        # configure search
        self._frontier = Frontiers.FrontierGBFS()
        # run search
        return self._tree_search(initialState)

    def UCSSearch(self, initialState):
        # configure search
        self._frontier = Frontiers.FrontierUCS()
        # run search
        return self._tree_search(initialState)

    def AStarSearch(self, initialState):
        # configure search
        self._frontier = Frontiers.FrontierAStar()
        # run search
        return self._tree_search(initialState)
