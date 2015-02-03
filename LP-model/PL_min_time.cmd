solve;

#display x;
#display f;

display Temps;

printf "y[u,v]=\n";
for {(u,v) in E}{
    if y[u,v]!=0 then printf "%d %d %d\n", u, v, y[u,v];
}

printf "\nf[v]=\n";
for {v in V}{
    if f[v]!=0 then printf "%d %d \n",  v, f[v];
}

