import ast

input_filename = 'data/y_min_time.txt'
output_filename = 'bigpath_min_time.txt'

E={} # oriented edges, with count: (u,v) --> k
somme = 0
with open(input_filename,'r') as f:
    for line in f:
        u,v,k = map(int, line.split() )
        if k>0:
            somme+=k
            E[(u,v)]=k
# now E is the graph described by `y`


start = 4516 # starting point
f = 5 # finishing point
visited = set()


def find_path(E,start):
    print 'finding path...',
    v = start
    path = [v]
    while len(E)>0:
        nextv=None
        for key in E.keys():#find next vertex to go 
            if key[0]==v: 
                nextv = key[1] # next vertex to go 
                E[key] -= 1 # "delete" one edge
                if E[key]==0: del E[key]
                break
        if nextv == None: # if we can not move any more,: return this path...
            return path # return a path: normaly should be a cycle
        path.append(nextv)
        visited.add(nextv)
        v = nextv
    return path


path  = [] 
path1 = []
path2 = []

while True:
    sub_path = find_path(E,start)
    path = path1 + sub_path +path2
    if len(E)==0: # if we've gone through all edges --> finish
        break
    else:
        start = None
        for key in E.keys(): #finding a new vertex to start
            if key[0] in path:
                start = key[0]
                break
        if start == None:
            print 'Error! Not only one connected components!'
            break
        print '\r re-starting at vertex', start, '...',
        idx = path.index(start)
        path1 = path[:idx]
        path2 = path[idx+1:]

print '\nThe solution contains %d vertices, and the path found contains %d vertices.'% ( somme+1, len(path) )

with open(output_filename, 'w') as f:
    f.write('1\n%d\n'%len(path))
    for v in path:
        f.write(str(v)+'\n')



    
