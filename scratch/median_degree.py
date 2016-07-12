"""This is the challenge code that will do the following tasks:
	1. Use Venmo payments that stream in to build a graph of users and their relationship with one another.

	2. Calculate the median degree of a vertex in a graph and update this each time a new Venmo payment appears. 
	   I will be calculating the median degree across a 60-second sliding window.

The vertices on the graph represent Venmo users and whenever one user pays another user, an edge is formed between the two users."""

from sys import *
from os.path import exists
import json



#script,Out_file,In_file=argv # Name the input and Output file

""" 1. Upload the input text file in the List
	2. Extract created_time, actor, target values
	3. Calculate the median degree
	4. Make the graph based on median degree"""

# 1. Upload the input text file in the list
f = open("../venmo_input/venmo-trans.txt")
venmoList =[]
venmoData_ordered={}
for line in f:
   venmoData = {}
   newStr = line.strip('\n')
   venmoData.update(json.loads(newStr))# Dictionary where each item is a line of text file
   print venmoData # printing all user entries
   venmoList.append(venmoData) # complete list of 1792 values gets into a list

# 2. Presentation in List-Extract created_time, actor, target

for data in venmoList:
    print "actor: " + data['actor'] + " target: " + data['target'] + " created_time: " + data['created_time']

# 3. Calculating median Degree
reorganizedList={}
degree_node_a=0
degree_node_t=0

for data in venmoList:
    if reorganizedList.has_key(data['actor']):
        if (reorganizedList[data['actor']].has_key(data['target'])):
            reorganizedList[data['actor']][data['target']] += 1
            degree_node_a=reorganizedList[data['actor']] 
            degree_node_t=reorganizedList[data['target']]  
             
        else:
            reorganizedList[data['actor']][data['target']] = 1
            #degree_node_a=reorganizedList[data['actor']] 
            #degree_node_t=reorganizedList[data['target']]  
          
    else:
        reorganizedList[data['actor']] = {}
        reorganizedList[data['actor']][data['target']] = 1
        #degree_node_a=reorganizedList[data['actor']] 
        #degree_node_t=reorganizedList[data['target']]  
	  	
    list=[]
    list=[reorganizedList[data['actor']][data['target']]]
    list.append(reorganizedList[data['actor']][data['target']])
    print list
    for i in range(len(list)):
    	sum_degree_node=sum(list)
    	if (len(list)%2==0):
    		median=sum_degree_node/2
    print"degree_node of",data['actor'],"=",degree_node_a
    print"degree_node of",data['target'],"=",degree_node_t
    #print"median=%r" %(median)
        	
    print"No. of relations for",data['actor'],"=",reorganizedList[data['actor']][data['target']]
        
print reorganizedList




