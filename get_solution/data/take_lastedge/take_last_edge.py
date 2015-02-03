import cPickle as pk
# go from 5816 (ending point of car-8) to 10872, then take the last edge: (10872,2962)

# just do another Dijkstra from 5816...
#~ start = 5816
#~ N = 11348
#~ 
#~ class Vertex:
    #~ def __init__(self, Id, x, y):
        #~ self.Id = Id;
        #~ self.adj_list = {} 
        #~ self.coord = (x,y)
#~ G = pk.load( open('Graph.dat','r') ) 
#~ def get_tl(u,v): return G[u].adj_list[v] # helpher function for getting time and length, returns tuple (t,l)
#~ 
#~ dist = {} # dist[v] = shortest distance(in time) from `dep` to `v`
#~ prev = {} # prev[v] =  previous node of `v`
#~ unvisited = set() # visited vertices
#~ INF = 99999999
#~ for i in xrange(N):
    #~ dist[i] = 0 if i==start else INF
    #~ unvisited.add(i)
#~ dist[start] = 0
#~ prev[start] = -1 # -1 means undefined
#~ 
#~ while len(unvisited)>0:
    #~ print '\r%.3f%%' % (100*(1.0-len(unvisited)*1.0/N)),
    #~ u = min(unvisited.intersection( dist.keys() ), key=lambda x: dist[x]) # find the node with least dist
    #~ unvisited.remove(u)
    #~ for v in G[u].adj_list.keys(): # v is neighbour of u
        #~ dist_v = dist.get(v, INF) # if v not in dist, get INF
        #~ t, l =get_tl(u,v)
        #~ if dist[u] + t < dist_v: # if we can make dist[v] shorter
            #~ dist[v] = dist[u] + t
            #~ prev[v] = u
    #~ #end while 1
#~ pk.dump( (dist,prev), open('Dijkstra_from5816.dat','w') ) 

(dist,prev) = pk.load(open('Dijkstra_from5816.dat','r'))
print dist[10872] #1642 -- so no pb for car-8 to get there!

def get_shortest_path(dst):
    'returns the shortest path from start to `dst`'
    shortes_path = [dst]
    while prev[dst] != -1:
        shortes_path.insert(0, prev[dst])
        dst = prev[dst]
    return shortes_path

path = get_shortest_path(10872)
path.append(2962)

pk.dump(path, open('path_to_lastedge.dat','w'))
print 'over'
