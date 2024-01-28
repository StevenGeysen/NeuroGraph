#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""     NeuroGraph: Graph class -- Version 1.1
Last edit:  2024/01/28
Author:     Geysen, Steven (SG)
Notes:      - Graph class to build NeuroGraph. Based on article of Bernd Klein.
            - Release notes:
                * Initial commit
To do:      - Information in nodes
            - Filters
            - Plotting
Comments:   
Sources:    https://python-course.eu/applications-python/graphs-python.php
"""



#%% ~~ Imports and directories ~~ %%#


from pathlib import Path


# Directories
SPINE = Path.cwd()



#%% ~~ Graph class ~~ %%#
#########################


class Graph(object):
    """Graph class."""

    def __init__(self, graph_dict=None):
        """
        Initialise a graph object.
        
        If no dictionary or None is given, an empty dictionary will be used.
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """Return a list of all the edges of a vertice."""
        return self._graph_dict[vertice]
        
    def all_vertices(self):
        """Return the vertices of a graph as a set."""
        return set(self._graph_dict.keys())

    def all_edges(self):
        """Return the edges of a graph."""
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """Add vertex to graph.
        
        If the vertex "vertex" is not in self._graph_dict, a key "vertex" with
        an empty list as a value is added to the dictionary. Otherwise nothing
        has to be done.
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        Add edge to graph.
        
        Assumes that edge is of type set, tuple or list; between two vertices
        can be multiple edges!
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add(y)
            else:
                self._graph_dict[x] = [y]

    def pathway(self):
        """
        Return information of pahtway.
        
        Information of neurological pathway used to filter on different
        neurotransmitters and hormones.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return self._graph_dict

    def __generate_edges(self):
        """
        Generate the edges of the graph "graph".
        
        Edges are represented as sets with one (a loop back to the vertex) or
        two vertices.
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """Allows to iterate over the vertices."""
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res



# ------------------------------------------------------------------------- End
