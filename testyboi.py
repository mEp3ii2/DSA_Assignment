import sys
from LinkedList import *
import numpy as np
import StackAndQ as sq
import inSort
from Graphy import *

def findShortestPath(graph, source, destination):
    # Create a queue to perform BFS
    queue = sq.DSAQueue()

    # Create an array to store the visited vertices and their predecessors
    visited = np.zeros(graph.vertCount, dtype=bool)
    predecessors = np.empty(graph.vertCount, dtype=object)
    predecessors[:] = None

    # Enqueue the source vertex and mark it as visited
    source_index = graph.getVertexIndex(source)
    queue.enqueue(source_index)
    visited[source_index] = True

    # Perform BFS until the queue is empty or the destination is found
    while not queue.isEmpty():
        current_vertex = queue.dequeue()

        if graph.getVertexLabel(current_vertex) == destination:
            # Destination found, reconstruct the path from destination to source
            path = reconstructPath(graph, predecessors, source_index, current_vertex)
            return path

        # Get the adjacent vertices of the current vertex
        adjacent_vertices = graph.getAdjacent(graph.getVertexByCount(current_vertex))

        for vertex in adjacent_vertices:
            vertex_index = graph.getVertexIndex(vertex)
            if not visited[vertex_index]:
                # Enqueue the unvisited vertex and mark it as visited
                queue.enqueue(vertex_index)
                visited[vertex_index] = True
                predecessors[vertex_index] = current_vertex

    # No path found
    return None

def reconstructPath(graph, predecessors, source_index, destination_index):
    # Reconstruct the path from destination to source using the predecessors array
    current_vertex = destination_index
    path = DSALinkedList()

    while current_vertex is not None:
        vertex_label = graph.getVertexByCount(current_vertex)
        path.insertFirst(vertex_label)
        current_vertex = predecessors[current_vertex]

    return path