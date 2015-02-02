# finding out the left edge(s)

f = open('paris_54000.txt','r')
N, M, T, N_car, start = map(int, f.readline().split() )
for i in range(N):
    f.readline()
E={} # E in the form: E[(u,v)] = (t,l)
for i in range(M):
    u,v,d,t,l = map(int, f.readline().split() )
    E[(u,v)] = (t,l)
    if d==2:
        E[(v,u)] = (t,l)
print len(E)

#now that we get all edges, then we look at the solution file
f = open('path_8T_time-reg2.txt', 'r')
path = []
f.readline()
f.readline()
while 1:
    line = f.readline()
    if line=='': break
    path.append(int(line))

for i in range(len(path)-1):
    u,v = path[i], path[i+1]
    E.pop( (u,v), None )
    E.pop( (v,u), None )

print len(E)
print E
## the last edge left is: {(10872, 2962): (1, 7)}
