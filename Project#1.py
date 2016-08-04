"""
For your first project, you will write Python code that creates 
dictionaries corresponding to some simple examples of graphs. 
You will also implement two short functions that compute information 
about the distribution of the in-degrees for nodes in these graphs. 
You will then use these functions in the Application component of 
Module 1 where you will analyze the degree distribution of a citation
graph for a collection of physics papers. This final portion of module 
will be peer assessed.

"""

# define three constants

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}


EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}



def make_complete_graph(num_nodes):
    """
    function to make complete graph
    """
    graph = {}
    for node1 in range(num_nodes):
        graph[node1] = set([])
        for node2 in range(num_nodes):
            if node1 != node2:
                graph[node1].add(node2)
    return graph


def compute_in_degrees(digraph):
    """
    function to compute in-degree nodes
    """
    all_values = digraph.values()
    all_values_list = []
    for val in all_values:
        all_values_list += list(val)
    return {i:all_values_list.count(i) for i in set(digraph.keys())}

def in_degree_distribution(digraph):
    """
    function to compute in-degree distribution
    """
    occurrences = set(compute_in_degrees(digraph).values())
    output = {}
    for count in occurrences:
        output[count] = (compute_in_degrees(digraph).values()).count(count)
    return output


