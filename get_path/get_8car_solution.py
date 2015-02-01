import cPickle as pk

solution_filename = 'path_8T_time-reg2.txt'
sub_filename = 'sub_8T_time-reg2.txt'

fi = open('solution/paris_54000.txt','r')
N, M, T, N_car, start = map(int, fi.readline().split() ) # N= nb vertices, M = nb streets

def readtab(fi, ty): return tuple(map(ty, fi.readline().split()))

class Vertex:
    def __init__(self, Id, x, y):
        self.Id = Id;
        self.adj_list = {} 
        self.coord = (x,y)

G = {} 
''' * `G` is a hashMap: Id --> Vertex obj 
    * `adj_list` of each vertex is a hashmap in the form of: { v1:(t1,l1), v2:(t2,l2), ...}
    
    ex. getting time and length for edge [u,v] is just:
            t, l = G[u].adj_list[v]
'''
def get_tl(u,v): return G[u].adj_list[v] # helpher function for getting time and length, returns tuple (t,l)

######################################################################## 
print '1. reading data into graph `G`...',
for i in xrange(N):
    x,y = readtab(fi, float)
    G[i] = Vertex(i, x, y)
for i in xrange(M):
    u,v,d,t,l = readtab(fi, int)
    G[u].adj_list[v] = (t,l)
    if d==2: G[v].adj_list[u] = (t,l)

pk.dump( G, open('Graph.dat','w') ) 


#~ G = pk.load( open('Graph.dat','w') ) 
print 'done!'


######################################################################## 
print '2. doing a Dijkstra for graph (source = start)...'
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
#~ # now that we have the informations stored in `dist` and `prev`
#~ pk.dump( (dist,prev), open('Dijkstra.dat','w') ) 

(dist,prev) = pk.load(open('Dijkstra.dat','r'))
print 'done!'


def get_shortest_path(dst):
    'returns the shortest path from start to `dst`'
    shortes_path = [dst]
    while prev[dst] != -1:
        shortes_path.insert(0, prev[dst])
        dst = prev[dst]
    return shortes_path
    


######################################################################### 
print '3. reading the solution with 1 car and 8T...'
fi = open(solution_filename, 'r')
fi.readline() # 1
fi.readline() # 30917
fi.readline() # 4516

def append_path(t_left, partial_path):
    '''
    given the time left `t_left` and the partial path, add path until time up by reading from the `fi` (i.e. following the solution by NEOS)
    returns the next vertex to go (for next car) and the time left
    '''
    current = partial_path[-1] if len(partial_path)>0 else start
    while 1:
        line = fi.readline()
        if line=='':#meaning that we are at the end of file
            return -1, t_left
        nxt = int(line)
        t, l = get_tl(current, nxt)
        if t_left < t: # if cannot go to nxt --> return 
            #~ print 'time left =%d' % t_left
            return nxt, t_left
            #~ return current, t_left 
        partial_path.append(nxt)
        t_left -= t
        current = nxt



all_paths = [] # contain 8 lists, each indicating a path for each car
start_i = start # starting point for car i
for i in range(N_car):
    print 'car %d...' % (i+1)
    path = []
    t = T
    # 1. go from google to dep_i
    path = get_shortest_path(start_i)
    if start_i != start: 
        path.append(next_i)#remember: the edge (current,nxt) is not yet done in last call for `append_path` !!!
    t -= dist[start_i] # don't forget dist[v] is the shortest(time) to get from google to v ! 
    print 'time left for doing the solution is: %d, ' % t, 
    # 2. take the path provided by "sub_8T.txt"
    next_i, t = append_path(t, path) # `next_i` is the next vertex that the next car should visit
    start_i = path[-1] # next car will start by the end of  last path
    print 'next departure is: %d' % start_i
    all_paths.append(path)    
    print 'Done! Time left is %d'%t


######################################################################## 
print '4. outputting to submission file...',
with open(sub_filename, 'w') as fo:
    fo.write('%d\n' % N_car)
    for i in range(N_car):
        path = all_paths[i]
        fo.write('%d\n' % len(path))
        for v in path:
            fo.write(str(v)+'\n')
print 'done!!!!!'
