f = open('paris_54000.txt','r')
N, M, T, N_car, start = map(int, f.readline().split() )
for i in range(N):
    f.readline()

#** each edge(u,v) is described by a tuple: (u,v,t,l) **#
E = set() # set of all edges
INF = 100*T

for i in range(M):
    u,v,d,t,l = map(int, f.readline().split() )
    E.add( (u,v,t,l) ) #add edge (u,v)
    t_inv = t if d==2 else INF
    E.add( (v,u,t_inv,l) )
    
with open('out.txt', 'w') as output:
    output.write('param : E : t l:= \n')
    for (u,v,t,l) in E:
        output.write( ' '.join(map(str,[u,v,t,l])) + '\n' )

print 'over!'
