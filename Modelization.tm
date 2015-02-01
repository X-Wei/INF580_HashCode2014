<TeXmacs|1.0.7.18>

<style|generic>

<\body>
  <doc-data|<doc-title|Modelization of Google <em|HashCode2014> by Linear
  Programming>|<doc-author|<author-data|<author-name|EO&XW>|<\author-affiliation>
    2015-01-22
  </author-affiliation>>>>

  <subsection|Problem fomulation>

  <\itemize>
    <item>Graph: <math|G<around*|(|V,E|)>\<nocomma\>,<around*|\||E|\|>=M\<nocomma\>,<around*|\||V|\|>=N>,
    in the statement, <math|E> is considered as not oriented, here we
    re-define <math|E<rsub|>> as the <em|oriented> edges
    (<math|<around*|\||E<around*|\|||\<nobracket\>>=2M|\<nobracket\>>>\|),
    for one-way roads, we just set the corresponding time to
    <math|\<infty\>>;

    <item><math|\<forall\>e<rsub|>=<around*|(|u,v|)>\<in\>E
    \<nocomma\>\<nocomma\>>, <math|\<exists\>
    t<rsub|e\<nocomma\>>\<nocomma\>,l<rsub|e>\<geqslant\>0>: time and length
    of each road, (<math|t<rsub|e>= \<infty\>> if this road is one-way);\ 

    <item><math|T>: time limit for each car;

    <item><math|v<rsub|start>: >Vertex that a car starts.
  </itemize>

  <math|\<Longrightarrow\>>Define the LP variables:\ 

  <\itemize>
    <item><math|\<forall\> v<rsub|>\<in\> V>, define
    <math|f<rsub|v>\<in\><around*|[|0,1|]>\<nocomma\>>, indicating if
    <math|v> is the last vertex that the car stops;

    <item><math|\<forall\> e<rsub|>\<in\>E>, define
    <math|x<rsub|e>\<in\><around*|[|0,1|]>>, indicating if this road is
    taken;

    <item><math|\<forall\> e\<in\> E<rsub|ori>>, define
    <math|y<rsub|e>\<in\>\<bbb-N\>>, indicating the number of times of
    passing this (oriented) edge.
  </itemize>

  <math|\<Longrightarrow\>><strong|So the LP problem for one car can be
  formulated as:>

  <\equation*>
    <below|Maximize|<stack|<tformat|<table|<row|<cell|x<rsub|e>\<in\><around*|[|0,1|]>>>|<row|<cell|y<rsub|e>\<in\>\<bbb-N\>>>|<row|<cell|f<rsub|v>\<in\><around*|{|0,1|}>>>>>>>\<nospace\>
    <below|<big|sum>|e\<in\>E>x<rsub|e>l<rsub|e> , <space|1em>s.t.
    <around*|{|<tabular|<tformat|<table|<row|\<forall\>e=<around*|(|u,v|)>\<in\>E,<space|1em>
    x<rsub|e>\<leqslant\>y<rsub|e><rsub|><htab|5mm>>|<row|<cell|>>|<row|<cell|\<forall\>e=<around*|(|u,v|)>\<in\>E\<nocomma\>\<nocomma\>\<nocomma\>,<space|1em>x<rsub|<around*|(|u,v|)>>+x<rsub|<around*|(|v,u|)>>\<leqslant\>1>>|<row|<cell|>>|<row|<cell|<below|<big|sum>|e\<in\>E<rsub|>>y<rsub|e>t<rsub|e>
    \<leqslant\>T>>|<row|<cell|>>|<row|<cell|\<forall\>
    v<rsub|i>\<in\>V\<nocomma\>,v<rsub|i>\<neq\>v<rsub|start>\<nocomma\>\<nocomma\>,<space|1em><below|<big|sum>|<stack|<tformat|<table|<row|<cell|e\<in\>E<rsub|>,>>|<row|<cell|e=<around*|(|u,v<rsub|i>|)>>>>>>>y<rsub|e>
    = <below|<big|sum>|<stack|<tformat|<table|<row|<cell|e<rprime|'>\<in\>E<rsub|>,>>|<row|<cell|e<rprime|'>=<around*|(|v<rsub|i>,u|)>>>>>>>y<rsub|e<rprime|'>>
    +f<rsub|v<rsub|i>>>>|<row|<cell|>>|<row|<cell|f<rsub|v<rsub|start>>+<below|<big|sum>|<stack|<tformat|<table|<row|<cell|e\<in\>E<rsub|>,>>|<row|<cell|e=<around*|(|v<rsub|start>,v<rsub|>|)>>>>>>>y<rsub|e>-<below|<big|sum>|<stack|<tformat|<table|<row|<cell|e<rprime|'>\<in\>E<rsub|>,>>|<row|<cell|e<rprime|'>=<around*|(|v,v<rsub|start><rsub|>|)>>>>>>>y<rsub|e<rprime|'>>
    = \<space\>1>>|<row|<cell|>>|<row|<cell|<below|<big|sum>|v\<in\>V>f<rsub|v>=1>>>>>
    |\<nobracket\>>
  </equation*>

  \;

  \;

  \ 
</body>

<\initial>
  <\collection>
    <associate|font|sys-chinese>
    <associate|language|chinese>
    <associate|page-type|letter>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|auto-1|<tuple|1|1>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|toc>
      <with|par-left|<quote|1.5fn>|Problem fomulation
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1>>
    </associate>
  </collection>
</auxiliary>