################################################
# Class: EECS 118                              #
# Term Project Part 2                          #
# Team Number: 6                               #
# Team Members:                                #
# Nathaniel Aponte, aponten@uci.edu, 41858361  #
# Guy Darel, gdarel@uci.edu, 86251615          #
################################################

import matplotlib.pyplot as plt
import networkx as nx
import csv
import sys


def order_path(original_path):#verifies that the given path exists and reorders it so that its terms flow through path
    #returns false if such a path doesnt exist
    old_path = original_path.copy()
    new_path = [old_path[0]]
    del old_path[0]
    while old_path:
        foo = True
        for num in range(len(old_path)):
            if new_path[-1][1] == old_path[num][0]:
                new_path.append(old_path[num])
                del old_path[num]
                foo = False
                break
            elif new_path[-1][1] == old_path[num][1]:
                temp = old_path[num][0]
                old_path[num][0] = old_path[num][1]
                old_path[num][1] = temp
                new_path.append(old_path[num])
                del old_path[num]
                foo = False
                break
        if foo:
            break
    if not foo:
        return new_path
    while old_path:
        foo = True
        for num in range(len(old_path)):
            if new_path[0][0] == old_path[num][1]:
                new_path.insert(0, old_path[num])
                del old_path[num]
                foo = False
                break
            elif new_path[0][0] == old_path[num][0]:
                temp = old_path[num][0]
                old_path[num][0] = old_path[num][1]
                old_path[num][1] = temp
                new_path.insert(0, old_path[num])
                del old_path[num]
                foo = False
                break
        if foo:
            return False
    return new_path


def is_path(orig_path, a, b):#check if the given path exists and if the given path goes from a to b
    path = order_path(orig_path)
    if path and (a == path[0][0] and b == path[-1][1]) or (
            b == path[0][0] and a == path[-1][1]):
        return True
    return False


def is_ordered_path(path):#checks that the path has no duplicates
    if not path:
        return False
    nodes = []
    for edge in path:
        if edge[0] in nodes:
            return False
        nodes.append(edge[0])
    if path[-1][1]==nodes[0]:
        return False
    return True


def path_gen(edge_list):#generates all possible paths with given set of edges and outputs them as a list
    final_path_list = []
    new_path_list = []
    for xedge in edge_list:
        for yedge in edge_list:
            if xedge == yedge: # if edge is the same edge skip
                continue
            possible_path = [xedge,yedge]
            valid_path = order_path(possible_path)
            if valid_path and valid_path not in new_path_list:
                new_path_list.append(valid_path)
    for master_edge in edge_list:
        final_path_list = final_path_list + new_path_list
        old_path_list = new_path_list.copy()
        new_path_list.clear()
        for path in old_path_list:
            temp_path_list = []
            for edge in edge_list:
                valid_path = path.copy()
                valid_path.append(edge)
                valid_path = order_path(valid_path)
                if is_ordered_path(valid_path):
                    temp_path_list.append(valid_path)
            for temp_path in temp_path_list:
                if temp_path not in new_path_list:
                    new_path_list.append(temp_path)
    return final_path_list


def total_weight(path_array, n):#checks if given path's weigths add up exactly to given num
    total = 0
    for x in range(len(path_array)):
        total = total + float(path_array[x][2])
    if total == n:
        return True
    return False


def color(path_array, k, n):#checks if given path has more than n edges of color k
    check_num = 0
    for x in range(len(path_array)):
        if path_array[x][3] == k:
            check_num += 1
    if check_num > n:
        return True
    return False


def main():
    # print(sys.argv[1])
    g = nx.Graph()
    edge_array = []
    # testing outside of command line
    with open('test.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            edge_array.append(row)
            g.add_edge(str(row[0]), str(row[1]), weight=float(row[2]), color=row[3])
    # Actual code for command line input
    # with open(sys.argv[1], mode='r') as csv_file:
    #    csv_reader = csv.reader(csv_file)
    #    for row in csv_reader:
    #        edge_array.append(row)
    #        g.add_edge(str(row[0]), str(row[1]), weight=float(row[2]), color=row[3])
    # input asking for values of A,B,C,D and Color
    print("Problem 45: find s where is_path(s,A,B) and total_weight(s,t)"
          "and color(s,Color,u) and t=C and u>D")
    # Predicate[0] = A Predicate[1] = B Predicate[2] = C Predicate[3] = D Predicate[4] = Color
    inital = input("Enter values for A, B, C, D, and a color:")
    predicate = inital.split(',')
    
    ####################
    ####################
    potential_paths = path_gen(edge_array)
    successful_paths = []
    for path in potential_paths:#loops through all possible paths
        if not path:
            continue
        new_path = order_path(path)
        weight = total_weight(new_path, float(predicate[2]))
        if not weight:
            continue
        check_color = color(new_path, predicate[4], int(predicate[3]))
        if not check_color:
            continue
        successful_paths.append(path)#any path that satisfies all conditions is added to sucessful_path list
    if not successful_paths:#if not paths were successful
        print("no valid paths")
    else:
        path_num = 0
        for path in successful_paths:
            path_num += 1
            print("path_", path_num)
            for edge in path:
                print(edge[0], ",", edge[1])
    ####################
    ####################
    green_edges = [(u, v) for (u, v, d) in g.edges(data=True) if d['color'] == 'green']
    blue_edges = [(u, v) for (u, v, d) in g.edges(data=True) if d['color'] == 'blue']
    red_edges = [(u, v) for (u, v, d) in g.edges(data=True) if d['color'] == 'red']
    pos = nx.spring_layout(g)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(g, pos, node_size=700)

    # edges
    if len(green_edges) > 0:
        nx.draw_networkx_edges(g, pos, edgelist=green_edges, edge_color='g',
                               width=6)
    if len(blue_edges) > 0:
        nx.draw_networkx_edges(g, pos, edgelist=blue_edges, edge_color='b',
                               width=6)
    if len(red_edges) > 0:
        nx.draw_networkx_edges(g, pos, edgelist=red_edges,
                               width=6, alpha=0.5, edge_color='r')

    # labels
    nx.draw_networkx_labels(g, pos, font_size=20, font_family='sans-serif')

    plt.axis('off')
    plt.show()


main()
