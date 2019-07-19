import networkx as nx
import matplotlib.pyplot as plt
import copy
from time import clock

#t0 = clock()
F = nx.read_gml("netscience.gml")  #graph object made from gml file
G = max(nx.connected_component_subgraphs(F), key=len) #giant component
#G = nx.barabasi_albert_graph(500,5)


def flippedMeasures(G): #modifies list containing number of flips from each node
    index = 0
    ties = 0.5
    for Gnode in G.nodes():  #iterate through each node in graph
        H = G.copy()
        H.remove_node(Gnode)  #remove selected node from copied graph
        
        Hdegrees = nx.degree_centrality(H).values() #removed node measures
        Hbtwn = nx.betweenness_centrality(H).values()
        Hclose = nx.closeness_centrality(H).values()
        Heigen = nx.eigenvector_centrality_numpy(H).values()
        
        MGdegrees = copy.deepcopy(Gdegrees) #copy original network degree list
        MGbtwn = copy.deepcopy(Gbtwn)
        MGclose = copy.deepcopy(Gclose)
        MGeigen = copy.deepcopy(Geigen)
        
        del MGdegrees[index] #remove that specific value in original list
        del MGbtwn[index]
        del MGclose[index]
        del MGeigen[index]
        
        Dresult = 0 #value that eventually becomes number of flips for a given
        Bresult = 0 #node
        Cresult = 0
        Eresult = 0
        
        for j in range (H.number_of_nodes()): #compare possible pairs
            for k in range (j+1, H.number_of_nodes()):
                
                if Hdegrees[k] < Hdegrees[j]: #check order is reversed
                    if MGdegrees[k] > MGdegrees[j]:
                        Dresult += 1
                    elif MGdegrees[k] == MGdegrees[j]:
                        Dresult += ties
                elif Hdegrees[k] > Hdegrees[j]:
                    if MGdegrees[k] < MGdegrees[j]:
                        Dresult += 1
                    elif MGdegrees[k] == MGdegrees[j]:
                        Dresult += ties
                elif Hdegrees[k] == Hdegrees[j]: #check if node is ordered to tied
                    if MGdegrees[k] > MGdegrees[j]: #or vice versa
                        Dresult += ties
                    elif MGdegrees[k] < MGdegrees[j]:
                        Dresult += ties
                        
                        
                if Hbtwn[k] < Hbtwn[j]:
                    if MGbtwn[k] > MGbtwn[j]:
                        Bresult += 1
                    elif MGbtwn[k] == MGbtwn[j]:
                        Bresult += ties
                elif Hbtwn[k] > Hbtwn[j]:
                    if MGbtwn[k] < MGbtwn[j]:
                        Bresult += 1
                    elif MGbtwn[k] == MGbtwn[j]:
                        Bresult += ties
                elif Hbtwn[k] == Hbtwn[j]:
                    if MGbtwn[k] > MGbtwn[j]:
                        Bresult += ties
                    elif MGbtwn[k] < MGbtwn[j]:
                        Bresult += ties
                        
                        
                if Hclose[k] < Hclose[j]:
                    if MGclose[k] > MGclose[j]:
                        Cresult += 1
                    elif MGclose[k] == MGclose[j]:
                        Cresult += ties
                elif Hclose[k] > Hclose[j]:
                    if MGclose[k] < MGclose[j]:
                        Cresult += 1
                    elif MGclose[k] == MGclose[j]:
                        Cresult += ties
                elif Hclose[k] == Hclose[j]:
                    if MGclose[k] > MGclose[j]:
                        Cresult += ties
                    elif MGclose[k] < MGclose[j]:
                        Cresult += ties
                        
                
                if Heigen[k] < Heigen[j]:
                    if MGeigen[k] > MGeigen[j]:
                        Eresult += 1
                    elif MGeigen[k] == MGeigen[j]:
                        Eresult += ties
                elif Heigen[k] > Heigen[j]:
                    if MGeigen[k] < MGeigen[j]:
                        Eresult += 1
                    elif MGeigen[k] == MGeigen[j]:
                        Eresult += ties
                elif Heigen[k] == Heigen[j]:
                    if MGeigen[k] > MGeigen[j]:
                        Eresult += ties
                    elif MGeigen[k] < MGeigen[j]:
                        Eresult += ties         
                                
        
        #if Dresult >= 0 and Dresult <= 547:
        degrees.append(Dresult)
        #if Bresult >= 0 and Bresult <= 297:
        btwn.append(Bresult)
        #if Cresult >= 0 and Cresult <= 2920:
        close.append(Cresult)
        #if Eresult >= 112 and Eresult <= 2825:
        eigen.append(Eresult)
        
        index += 1
        #t1 = clock()
        #if (t1 - t0 >= 42000):
        #    break
    return 
    
degrees = []
btwn = []
close = []
eigen = []


#for i in range(20):
    #G = nx.watts_strogatz_graph(500,10,0.05)
    #G = nx.barabasi_albert_graph(500,4)
Gdegrees = nx.degree_centrality(G).values()
Gbtwn = nx.betweenness_centrality(G).values()
Gclose = nx.closeness_centrality(G).values()
Geigen = nx.eigenvector_centrality_numpy(G).values()
flippedMeasures(G)

plt.hist(degrees, histtype='step', lw=2,label='Degree')
plt.hist(btwn, histtype='step', lw=2,label='Btwn')
plt.hist(close, histtype='step', lw=2,label='Close')
plt.hist(eigen, histtype='step', lw=2,label='Eigen')
plt.title('Barabasi-Albert Reordered Pairs Distribution, k=2')
plt.xlabel('Number of pairs reordered')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.show()

#print bins, counts

print degrees
print btwn
print close
print eigen

#COLOR CODE

#for i in range (len(degrees)):
#    G.add_node(degrees[i], colorD = "red")
   
#for i in range (len(btwn)):    
#    G.add_node(btwn[i], colorB = "red")
    
#for i in range (len(close)):
#    G.add_node(close[i], colorC = "red")
    
#for i in range (len(eigen)):
#    G.add_node(eigen[i], colorE = "red")

#nx.write_gml(G,"NetscienceFull_color.gml")