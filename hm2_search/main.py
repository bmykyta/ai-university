from modules.search import *
from modules.utils import *


def best_first_graph_search_for_vis(problem, f):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""

    # we use these two variables at the time of visualisations
    iterations = 0
    all_node_colors = []
    node_colors = {k: 'white' for k in problem.graph.nodes()}

    f = memoize(f, 'f')
    node = Node(problem.initial)

    node_colors[node.state] = "red"
    iterations += 1
    all_node_colors.append(dict(node_colors))

    if problem.goal_test(node.state):
        node_colors[node.state] = "green"
        iterations += 1
        all_node_colors.append(dict(node_colors))
        return iterations, all_node_colors, node

    frontier = PriorityQueue('min', f)
    frontier.append(node)

    node_colors[node.state] = "orange"
    iterations += 1
    all_node_colors.append(dict(node_colors))

    explored = set()
    while frontier:
        node = frontier.pop()

        node_colors[node.state] = "red"
        iterations += 1
        all_node_colors.append(dict(node_colors))

        if problem.goal_test(node.state):
            node_colors[node.state] = "green"
            iterations += 1
            all_node_colors.append(dict(node_colors))
            return iterations, all_node_colors, node

        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                node_colors[child.state] = "orange"
                iterations += 1
                all_node_colors.append(dict(node_colors))
            elif child in frontier:
                incumbent = frontier[child]
                # incumbent = frontier.get_item(child) # if utils modified
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
                    node_colors[child.state] = "orange"
                    iterations += 1
                    all_node_colors.append(dict(node_colors))

        node_colors[node.state] = "gray"
        iterations += 1
        all_node_colors.append(dict(node_colors))
    return None


def astar_search_graph(problem, h=None):
    h = memoize(problem.h, 'h')
    """ n.path_cost + h(n) in lambda not working! n.path_cost INT?! """
    return best_first_graph_search_for_vis(problem, lambda n: n)


ukraine_map = UndirectedGraph(dict(
    Kyiv=dict(Chernihiv=142, Poltava=344, Cherkasy=192, Vinnytsia=269, Zhytomyr=140),
    Chernihiv=dict(Sumy=307, Poltava=406),
    Poltava=dict(Sumy=174, Dnipro=160, Kropyvnytskyi=249, Cherkasy=243),
    Kharkiv=dict(Sumy=179, Luhansk=338, Donetsk=314, Poltava=143),
    Donetsk=dict(Luhansk=165, Zaporizhzhia=229),
    Dnipro=dict(Kharkiv=217, Donetsk=262, Kropyvnytskyi=246),
    Zaporizhzhia=dict(Kherson=99, Dnipro=85),
    Kherson=dict(Dnipro=98, Mykolaiv=71),
    Simferopol=dict(Sevastopol=73, Kherson=264),
    Mykolaiv=dict(Kropyvnytskyi=181, Dnipro=323),
    Odesa=dict(Vinnytsia=430, Mykolaiv=132),
    Vinnytsia=dict(Zhytomyr=128, Cherkasy=335, Khmelnytskyi=122),
    Kropyvnytskyi=dict(Cherkasy=129),
    Khmelnytskyi=dict(Rivne=194, Zhytomyr=183, Chernivtsi=188),
    Rivne=dict(Lutsk=73, Ternopil=159, Lviv=212, Zhytomyr=189),
    Lviv=dict(Lutsk=151, Ivano_Frankivsk=132, Uzhhorod=268),
    Ivano_Frankivsk=dict(Uzhhorod=270, Ternopil=130, Chernivtsi=135),
    Ternopil=dict(Lviv=134, Khmelnytskyi=111, Chernivtsi=172)))

ukraine_map.locations = dict(
    Kyiv=(100, 510), Chernihiv=(110, 634), Poltava=(480, 400),
    Cherkasy=(220, 300), Vinnytsia=(-10, 210), Zhytomyr=(-49, 480),
    Sumy=(480, 595), Kharkiv=(685, 440), Luhansk=(900, 180),
    Donetsk=(760, 130), Zaporizhzhia=(480, 80), Kherson=(330, -150),
    Mykolaiv=(220, -120), Odesa=(80, -170), Dnipro=(470, 170),
    Kropyvnytskyi=(230, 170), Khmelnytskyi=(-190, 250), Ternopil=(-310, 300),
    Rivne=(-320, 520), Chernivtsi=(-440, 85), Ivano_Frankivsk=(-495, 200),
    Uzhhorod=(-800, 135), Lutsk=(-450, 550), Lviv=(-640, 340),
    Simferopol=(400, -300), Sevastopol=(260, -320))

ukraine_locations = ukraine_map.locations

node_colors = {node: 'white' for node in ukraine_map.locations.keys()}
node_positions = ukraine_map.locations
node_label_pos = {k: [v[0], v[1] - 10] for k, v in ukraine_map.locations.items()}
edge_weights = {(k, k2): v2 for k, v in ukraine_map.graph_dict.items() for k2, v2 in v.items()}

ukraine_graph_data = {'graph_dict': ukraine_map.graph_dict,
                      'node_colors': node_colors,
                      'node_positions': node_positions,
                      'node_label_positions': node_label_pos,
                      'edge_weights': edge_weights
                      }

# show_map(ukraine_graph_data)

all_node_colors = []
ukraine_problem = GraphProblem('Kharkiv', 'Simferopol', ukraine_map)
# display_visual(ukraine_graph_data, user_input=False,
#                algorithm=astar_search_graph,
#                problem=ukraine_problem)
astar_search(ukraine_problem).solution()
