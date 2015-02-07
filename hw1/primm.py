"""Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the
straightforward O(mn) time implementation of Prim's algorithm should
work fine. OPTIONAL: For those of you seeking an additional challenge,
try implementing a heap-based version. The simpler approach, which
should already give you a healthy speed-up, is to maintain relevant
edges in a heap (with keys = edge costs). The superior approach stores
the unprocessed vertices in the heap, as described in lecture. Note
this requires a heap that supports deletions, and you'll probably need
to maintain some kind of mapping between vertices and their positions
in the heap."""

import os
import heapq

class Edge:
    def __init__(self,n0,n1,w):
        self.n0 = n0
        self.n1 = n1
        self.w = w

    def __repr__(self):
        return "%i-%i:%i" % (self.n0, self.n1, self.w)

    def __lt__(self, other):
        return self.w < other.w

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = []

    def __repr__(self):
        es = ''
        for e in self.edges:
            if e.n0 == self.id:
                n = e.n1
            else:
                n = e.n0
            es = es + '%i:%i,' % (n,e.w)
        return "%i, %i edges: %s" % (self.id, len(self.edges), es)

    def addEdge(self, edge):
        self.edges.append(edge)

def parse_graph(fn="edges.txt"):
    f = open(fn,'r')
    num_nodes, num_edges = [int(x) for x in f.readline().split()]
    edges = []
    for line in f.readlines():
        n0,n1,w = [int(x) for x in line.split()]
        edges.append(Edge(n0,n1,w))
    if len(edges) != num_edges:
        raise Exception('len(edges) != num_edges')

    nodes = {}
    for e in edges:
        if e.n0 not in nodes:
            nodes[e.n0] = Node(e.n0)
        if e.n1 not in nodes:
            nodes[e.n1] = Node(e.n1)
        nodes[e.n0].addEdge(e)
        nodes[e.n1].addEdge(e)

    if len(nodes.keys()) != num_nodes:
        raise Exception('len(nodes) %i != num_nodes %i' % (len(nodes), num_nodes))

    return nodes

def primms_pick_edge(graph, nodes, edges, heap):
    while len(heap) > 0:
        e = heapq.heappop(heap)
        n0in = e.n0 in graph
        n1in = e.n1 in graph
        # if both in or out, exclude
        if not n0in ^ n1in: 
            continue
        # new external edge found
        # add it to the graph

        # get the node not in the graph
        if n0in:
            n1id = e.n1
        else:
            n1id = e.n0

        edges.append(e)
        n_new = nodes[n1id]
        graph[n1id] = n_new
        for e in n_new.edges:
            heapq.heappush(heap, e)
        return n_new

def primms():
    """Primm's algo works as follows: 
    - pick a node
    - grab the shortest edge from the node to a node not already in the set
    """
    nodes = parse_graph('edges.txt')
    n = nodes[nodes.keys()[0]]
    graph = {}
    graph[n.id] = n
    edges = []

    # build a list of all edges in the non internal nodes of the graph
    heap = n.edges[:]
    heapq.heapify(heap)

    while n != None:
        n = primms_pick_edge(graph,nodes,edges, heap)

    costs = [ e.w for e in edges ]
    return (sum(costs), edges)

# -2233719

