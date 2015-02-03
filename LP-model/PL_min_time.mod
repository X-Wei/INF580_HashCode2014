option gurobi_options 'mipgap 1e-10';
param T,  >= 0, <= 432000;

param N, integer, >=0;

set V:=0..N-1;
param start in V;

set E within (V cross V);

param t{(u,v) in E}, > 0;
param l{(u,v) in E}, > 0;

var f{ v in V},  >= 0, <=1;
#var x{(u,v) in E},binary;
var y{(u,v) in E}, integer, >=0;

minimize Temps: sum{ (u,v) in E } y[u,v]*t[u,v];

#s.t. C1{ (u,v) in E }: x[u,v] <= y[u,v];

s.t. C1bis{ (u,v) in E }: y[u,v] + y[v,u] >= 1;

s.t. C2: sum{ (u,v) in E } y[u,v]*t[u,v] <= T;

s.t. C3{vertex in V: vertex!=start}: sum{ (u,v) in E : v==vertex }y[u,v] = sum{ (u,v) in E : u==vertex }y[u,v] + f[vertex];

s.t. C4: f[start] + sum{ (u,v) in E : u==start } y[u,v] - sum{ (u,v) in E : v==start } y[u,v] = 1;

s.t. C5: sum{ v in V }f[v] = 1;
