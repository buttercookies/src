import json

import statistics

from datetime import datetime
from dateutil import parser
from src.Graph import Graph
from src.Node import Node

__author__ = 'lawrenberg'


def main():
    '''
    1. We first read in the file.  The challenge said that each new line is a single Venmo payment written in JSON format
    so we import
    '''
    f = open("venmo_input/venmo-trans_short.txt")
    graph= Graph()

    # this holds a list of median degrees
    rollingMedianDegree = []
    storeFile =[]
    for line in f:
        newStr = line.strip('\n')
        storeFile.append(newStr)

    for line in storeFile:
        #find the current max time of the graph
        max = findMaxTime(graph)

        newStr = line.strip('\n')
        data = json.loads(newStr)
        if add_to_graph(data['created_time'], max):
            node = Node(data['actor'])
            neighbor = Node(data['target'])
            graph.add_node(node)
            graph.add_node(neighbor)
            graph.add_edge(node, neighbor)
            key = data['actor'] + "->" + data['target']
            metadata = data['created_time']
            graph_node = graph.get_node(node.id)
            graph_node.add_metadata(key, metadata)
        else:
            continue
        #get new max
        max = findMaxTime(graph)
        # set the weight in this case it is the number of neighbors the node has
        setWeight(graph)

        #find expired edges
        expiredNode = findExpiredNode(graph, 60, max)

        #remove those relationships
        for actor, target in expiredNode.items():
            graph.get_node(actor).remove_metadata(actor + "->" + target)
            graph.remove_edge(actor, target)

        #find the median degree
        degree = getMedianDegree(graph)

        #add to rolling median degree records.  this is what will be saved in the output.
        rollingMedianDegree.append(degree)
        

    
    print(graph)
    print(rollingMedianDegree)

def findExpiredNode(graph, timeThreshold, maxTime):
    eject = {}

    max_time_datetime_format = parser.parse(maxTime)
    for ndx, node in graph.get_vertices().items():
        metadata = node.get_metadata()
        for idx, meta in metadata.items():
            date = parser.parse(meta)

            if (max_time_datetime_format - date).seconds > timeThreshold:
                eject[node.id] = idx

    return eject

def findMaxTime(graph):
    maxTime = ""
    nodeRelation = {}
    for ndx, node in graph.get_vertices().items():
        metadata = node.get_metadata()
        for idx, meta in metadata.items():
            if maxTime == "":
                maxTime = meta
                continue
            if parser.parse(maxTime) < parser.parse(meta):
                maxTime = meta

    return maxTime

def setWeight(graph):
    for ndx, node in graph.get_vertices().items():
        count = node.neighbor_count()
        node.set_weight(count)

def getMedianDegree(graph):
    weights = []

    for ndx, node in graph.get_vertices().items():
        weights.append(node.get_weight())

    medianDegree = statistics.median(weights)

    return medianDegree

def add_to_graph(timestamp, maxTime, threshold = 60):

    if maxTime == "" or maxTime is None:
        return True

    timestamp_converted = parser.parse(timestamp)
    maxTime_converted = parser.parse(maxTime)

    return not (maxTime_converted - timestamp_converted).total_seconds() > threshold


main()