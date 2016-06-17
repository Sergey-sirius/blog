Title: The most important stations for Capital Bikeshare
Date: 2016-6-15 16:18
Tags: math, data, analysis, DC, pagerank, eig
Category:
Slug: the-most-important-stations-for-capital-bikeshare
Summary:
Status: published
Authors: Keith Kelly


In my previous two blog posts I've explored some of the data provided by DC's Capital Bikeshare.
I've looked at usage trends broken down by group and time and visualized the most traversed routes using Google Maps and Bokeh.
Looking back at the map post, it's pretty clear that the Bikeshare dock pair with the most usage is Lincoln Memorial and Jefferson Dr & 14th St SW.
They look like they link very heavily to each other, with only tenuous links to other locations.
On the other hand, Columbus Circle / Union Station has several heavily trafficked station pair routes emanating from it.
Certainly these locations seem very important to Capital Bikeshare, but does that mean they are the most important?
This depends, of course, upon exactly what is meant by "most important."

# Networks
Look again at that map from the previous post.

<div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-4 thumb">
<a href="../../../../../images/networks/whole_map.png" ><img class="img-responsive center-block" src="../../../../../images/networks/whole_mapt.png"></img></a>
</div>
<div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-4 thumb">
<a href="../../../../../images/networks/zoom.png" ><img class="img-responsive center-block" src="../../../../../images/networks/zoomt.png"></img></a>
</div>

This sort of structure is known as a *[graph](https://en.wikipedia.org/wiki/Graph_%28discrete_mathematics%29)*
The stations are nodes (or vertices) and the links between them are edges.
Graphs are very common in mathematics and computer science; they are used to represent [social networks](https://en.wikipedia.org/wiki/Social_network), [Markov chains](https://en.wikipedia.org/wiki/Markov_chain), [links on the internet](https://en.wikipedia.org/wiki/Webgraph), [map routes](https://en.wikipedia.org/wiki/Shortest_path_problem), and more.
The graphs that I've used to display relative bikeshare station pair utilization are called *weighted undirected* graphs.
Undirected implies that the graph does not distinguish between trip directions, so that trips from, for example, New Hampshire Ave & T St NW to Massachusettes Ave & Dupont Cir NW and the reverse trip are the same.
Weighted means that there is a number, called (unsurprisingly) a weight, associated to each edge whose meaning depends on context.
In our case edge weights indicate the number of trips from one station to another; on a map the weights could be distances between vertices.
In a social network the edges may be *un*weighted with with each edge weight set to 1, indicating that two people are connected.
In a Markov chain the edge weights represent transition probabilities.
The actual data provided by Capital Bikeshare does yield a *directed* graph, i.e. one where the direction matters, but I did not have a convenient way of displaying that data on top of a map.

In this blog post I am going to attempt to determine the nodes (stations) of the graph that are most important, or most central, to Capital Bikeshare.

## Example
Here is an example of a simple graph which represents a two state Markov chain that I took from wikipedia:

<a href="../../../../../images/networks/markov.png" ><img class="img-responsive center-block" src="../../../../../images/networks/markovt.png"></img></a>

There are two nodes and four edges.
The direction of the edge is given as an arrow and the weight of that edge is given by the number next to it.
We can also represent this graph by a matrix.
<style type="text/css">
.MathJax_Display {
text-align: center!important;
}
</style>
<div class="img-responsive center-block">
$$G=\begin{bmatrix}
0.3 & 0.4\\
0.7 & 0.6
\end{bmatrix}$$
</div>

The first row gives the probabilities of transitioning from node A to another node -- in this case either itself or node E, respctively.
The second row gives those probabilities for node E, again in the same order.
This is actually a very special type of matrix called a [right stochastic matrix](https://en.wikipedia.org/wiki/Stochastic_matrix) with some neat properties.

NB: This is not necessarily the most common matrix representation for the graph.
I chose to represent the incoming edges for a node along each row and the outgoing down each column.
Representing it the opposite way is also perfectly valid and perhaps more common, but the only difference is that the matrix is transposed.
I chose this representation because I prefer to multiply using column vectors, which will come up some time later.

# Centrality
In graph theory, a question that comes up somewhat regularly is "what is the most important node in my graph?"
Measures of graph *[centrality](https://en.wikipedia.org/wiki/Centrality)* provide an answer to this question, but the answer is not necessarily unique. On this issue of nonuniqueness, wikipedia says:

>The word "importance" has a wide number of meanings, leading to many different definitions of centrality. Two categorization schemes have been proposed. "Importance" can be conceived in relation to a type of flow or transfer across the network. This allows centralities to be classified by the type of flow they consider important. "Importance" can alternately be conceived as involvement in the cohesiveness of the network. This allows centralities to be classified based on how they measure cohesiveness. Both of these approaches divide centralities in distinct categories. A further conclusion is that a centrality which is appropriate for one category will often "get it wrong" when applied to a different category.

So centrality can give us a way of determining which nodes in a graph are most important, but there are many different ways of ranking centrality!
So which one should we use?
Let's explore different measures of centrality applied to the graph given by Capital Bikeshare usage to see if we can figure it out.

## Degree centrality
Degree centrality is perhaps the simplest method of determining the importance of a vertex.
For a directed graph like the one we have, we can compute both [indegree and outdegree](https://en.wikipedia.org/wiki/Directed_graph#Indegree_and_outdegree) centrality.
In our simple example above, the out degree is given by the column sums and the in degree is given by the row sums.
Using this knowledge, or by inspecting the picture, we can see that node A has the largest in degree, with a value of 1.3.
However, each node has out degree 1! This is one of those special properties of the stochastic matrix.


In the bikeshare example we can do the same thing.
We take our graph and turn it into a matrix with starting locations (nodes) running down the columns and ending stations running across the rows.

```
End station number    31000  31001  31002  31003  31004  31005  31006  31007  ...
Start station number
31000                    21      1      6      5      1     25      1      2
31001                     4     28      1      1     14     19     46      3
31002                     3      1     41     33      5     29     38      3
31003                     4      0     20     55      5     63     50      5
31004                     1     17     37     16     14    321     46     15
.
.
.
```

Our data here is in a [pandas](http://pandas.pydata.org/) dataframe so computing the maximum in and out degree is easy.

```python
max_out = grouped.sum(axis=0).argmax()
max_in  = grouped.sum(axis=1).argmax()
```

Computing this we learn that Columbus Circle / Union Station has both the maximum in degree and out degree at 13120 and 13879.
This means that in the first quarter of 2016 over 26000 bikes went through that station. Incredible!
The corresponding degrees for the Lincoln Memorial station are 9419 and 9388.
So even though we see that incredibly strong link coming from the Lincoln Memorial it's not the most important station, at least by this metric.
This should make some sense since there are several relatively large links surrounding Columbus Circle / Union Station, but only one large one coming from the Lincoln Memorial.

Let's look at another way of measuring centrality.

## Eigenvector centrality
Eigenvector centrality uses the principal eigenvector of the graph to assign a measure of centrality.
"It assigns relative scores to all nodes in the network based on the concept that connections to high-scoring nodes contribute more to the score of the node in question than equal connections to low-scoring nodes."
Note how this is different from degree centrality.
It doesn't only matter that a given node has many connections, but also if what it is connected to has many connections.
This should be better because a node that has very strong connections to one other node, but then both are barely connected to any others should not be central.

Let's do an example.

First, let's compute the eignvalue centrality for our network.
Exactly how this is done isn't important for this example and we'll get to the details later.
Our computation indicates that the central vertex is the Jefferson Dr & 14th St SW.
This is different from what degree centrality yields, but this seems like a reasonable choice since it is clearly strongly connected.

Now let's mess with the data a little bit to show why eigenvector centrality differs from degree centrality in another way.
We are going to take or data from before, but replace G(31000,31001) with 100,000.

```
End station number    31000  31001  31002  31003  31004  31005  31006  31007  ...
Start station number
31000                    21 100000      6      5      1     25      1      2
31001                     4     28      1      1     14     19     46      3
31002                     3      1     41     33      5     29     38      3
31003                     4      0     20     55      5     63     50      5
31004                     1     17     37     16     14    321     46     15
.
.
.
```
Previously, Eads St & 15th St S had an in degree of 299, and now it has 100,298 and while 18th & Eads St had an out degree 330 and now has an out degree of 100,329.
This is a huge change and of course now these two rank highest in degree centrality (we saw before that the maxima were only around 13,000).
However, the eigenvalue centrality still indicates that Jefferson Dr & 14th St SW is the most central node.
The eigenvalue centrality is unaffected by strongly connected nodes that are weakly connected to the rest of the graph.

### What is an eigenvector anyway? And how do we compute it?

A casual reader may skip this section if he or she is uninterested in the mathemetics.

Given a square matrix (or linear operator) $G$, a vector $v\ne0$ is an eigenvector of $G$ if and only if there exists a $\lambda$ such that $Gv = \lambda v$.
Notice that if $v$ is an eigenvector, then so too is any scalar multiple $av$, so we can assume for the rest of this discussion that our eigenvectors are scaled so that $\sum_{i=1}^n v_i = 1$, without loss of generality.
So why is the principal eigenvector of a graph a good measure of the centrality?

Consider the following example:
<div class="col-xs-12 thumb">
<a href="../../../../../images/networks/graph_start.png" ><img class="img-responsive center-block" src="../../../../../images/networks/graph_startt.png"></img></a>
</div>
<div class="col-xs-12 thumb">
$$G=\begin{bmatrix}
1 & 3 & 5\\
4 & 2 & 1\\
4 & 1 & 0
\end{bmatrix}$$
</div>

We have a weighted digraph (directed graph) with some self loops.
We are going to do a random walk on this graph, starting with each node being equiprobable.
So at each node we assign a probability of $1/3$.

<div class="col-xs-12 thumb">
<a href="../../../../../images/networks/graph_1.png" ><img class="img-responsive center-block" src="../../../../../images/networks/graph_1t.png"></img></a>
</div>

Now, we move from node to node, multiplying the probability at each node by the wight to an adjacent node.
Consider only the edges going into node A for a moment.
A to A gives us $1/3 \times 1 = 1/3$.
B to A gives us $1/3 \times 3 = 1$ and C to A gives us $1/3 \times 5 = 5/3$.
Do that with the other two nodes.
A to B gives us $1/3 \times 4 = 4/3$, B to B $1/3 \times 2 = 2/3$, C to B $1/3 \times 1 = 1/3$
And finally for C we get A to C gives us $1/3 \times 4 = 4/3$, B to C $1/3 \times 1 = 1/3$, C to C $1/3 \times 0 = 0$

Sum the values going into each node and we get A=$9/3$, B=$7/3$, C=$5/3$
Normalize (i.e. ensure everything still sums to 1) and we get A=$9/21$, B=$7/21$, C=$5/21$.

<div class="col-xs-12 thumb">
<a href="../../../../../images/networks/graph_2.png" ><img class="img-responsive center-block" src="../../../../../images/networks/graph_2t.png"></img></a>
</div>

We can iterate this process until the probabilities associated to each node cease to move appreciably.

<div class="col-xs-12 thumb">
<a href="../../../../../images/networks/graph_3.png" ><img class="img-responsive center-block" src="../../../../../images/networks/graph_3t.png"></img></a>
</div>

Putting the probabilities through the network again, really doesn't change it.

The process we just went through to find this [fixed point](https://en.wikipedia.org/wiki/Fixed_point_%28mathematics%29) is essentially [power iteration](https://en.wikipedia.org/wiki/Power_iteration) (though we used a different normalization).
This [pdf](http://math.arizona.edu/~ura-reports/074/Schaeffer.Amanda/Final.pdf) does a good job showing the connetion between power iteration and a fixed point method.

Running those probabilities through the network was exactly multiplication of the probability vector by the link matrix.
Repeating that process gets us the power method.

Here's a short example in python
```python
import numpy as np

# initialize the data
G = np.matrix('1 3 5; 4 2 1; 4 1 0')
v = np.array([1,1,1])/3
v.shape = (3,1)
print("G: {}".format(G))
print("v: {}".format(v))
# loop through multiplying each time
for i in range(10):
    v = (G*v)/sum(G*v)
		    print("v: {}".format(v))
```

```
G: [[1 3 5]
[4 2 1]
[4 1 0]]
v: [[ 0.33333333]
[ 0.33333333]
[ 0.33333333]]
v: [[ 0.42857143]
[ 0.33333333]
[ 0.23809524]]
v: [[ 0.35947712]
[ 0.35947712]
[ 0.28104575]]
v: [[ 0.40166205]
[ 0.34441367]
[ 0.25392428]]
v: [[ 0.37536845]
[ 0.35383827]
[ 0.27079328]]
v: [[ 0.39163744]
[ 0.34800827]
[ 0.26035428]]
v: [[ 0.38152852]
[ 0.35163086]
[ 0.26684062]]
v: [[ 0.38779355]
[ 0.34938576]
[ 0.26282069]]
v: [[ 0.38390453]
[ 0.35077941]
[ 0.26531606]]
v: [[ 0.38631623]
[ 0.34991516]
[ 0.26376861]]
v: [[ 0.38481974]
[ 0.35045144]
[ 0.26472883]]
```

### Back to why
As per the example, we see that the principal eigenvector indicates where random walks end up in the graph.
This means that the natural flow of information through the network ends up in a proportion according to the values in the principal eigenvector.
Since the first value in the principal eigenvector in our example above was the largest, it is the most central node in our graph, according to eigenvector centrality.
It should make sense then why we use the principal eigenvector for measuring which nodes in a graph are important.

## PageRank
PageRank is the famed algorithm by Larry Page and Sergey Brin that Google's search engine was originally based on.
This algorithm ranks web pages, represented as a graph of hyperlinks, by means of graph centrality.
There's a good, gentle introduction to PageRank [here](https://jeremykun.com/2011/06/12/googles-pagerank-introduction/), a good article on it from the AMS [here](http://www.ams.org/samplings/feature-column/fcarc-pagerank), and a good blog post with some mathematical rigor practical considerations [here](http://blog.kleinproject.org/?p=280).


PageRank is very similar to eigenvalue centrality, with a few key adjustemnts made.
There's some more math incoming, but only a little linear algebra is needed to understand it.
If you wish to skip it, just know that PageRank adjusts the matrix so that a most central node always exists and is always unqiue.

### Mathematical diversion
First we take $G$ and ensure that it is column stochastic by normalizing each column by the sum of its entries.
Specifically, let $B$ be a matrix, the same size as $G$ whose entries are all $1/n$, where $n$ is the size of $G$.
Note that $B$ is both column and row stochastic.
Define $p \in [0,1]$ as the probability of randomly jumping from one node to another.
Finally we can define the PageRank matrix
$$C = pB + (1-p)G.$$
Finally, we just compute the principal eigenvector of this new matrix, just like we did before.

That's it. Pretty simple, huh?
```python
def page_rank(A, p=0.15, num=1):
    """Compute the page rank of a given graph A and return the num largest values"""
    m,n = A.shape
    assert(m == n)
    A = A/A.sum(axis=0)[None, :] # normalize columns
    B = np.full((m, n), 1/m, dtype=A.dtype)
    C = p*B + (1-p)*A
    w, v = eigs(C, k=1, which='LM')
    return v
```

This matrix is still column stochastic since it is a convex combination of two column stochastic matrices.
For $p>0$ the graph $C$ is strongly connected (and is in fact a [complete digraph](https://en.wikipedia.org/wiki/Complete_graph)) and the matrix is actually a positive matrix in the sense that each entry is positive.
Positiivity is important because it ensures that the matrix satisifies the hypotheses of the [Perron-Frobenius theorem](https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem), which guarantees that the matrix C has a *unique* principal eigenvector with all positive components.
It also ensures that the algorithm to compute the eigenvector will converge.
The stochasticity property ensures that the principal eigenvalue is 1.

All of these changes seem reasonable and all of these properties are nice, but what's the point?
It seemed like eigenvector centrality was doing just fine, right?

### Back on track
On the issue of graph completeness and what could happen if this property is not satisfied, Sergey and Brin in their [original PageRank paper (pdf)](http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf) offer:
>Consider two web pages that point to each other but to no other page.
>And suppose there is some web page which points to one of them.
>Then, during iteration, this loop will accumulate rank but never distribute any rank (since there are no outedges).
>The loop forms a sort of trap which we call a rank sink.

So if the graph is not complete, the flow of information through the graph can get trapped and give some misleading answers.

So when we run PageRank, we find that the most important node is Columbus Circle / Union Station.
This seems reasonable given its high degree of incoming nodes (it is the most node with highest in degree and out degree), but is it necesarily the correct answer?
Surely if Google uses this algorithm it must be the best, right?
It does work incredibly well for link networks, but does that make it the correct choice for other types of networks?
PageRank emphasizes incoming links more than outgoing while in a bikeshare network it would seem that both of these should be important.

Caution: What we did here was not strictly PageRank since PageRank uses *un*weighted graphs to begin with. 
[Another paper from a few years later (pdf)](http://digital.library.unt.edu/ark:/67531/metadc30962/m2/1/high_res_d/Mihalcea-2004-TextRank-Bringing_Order_into_Texts.pdf) creates a new algorithm called TextRank which uses weighted graphs, but is exactly the same thing.
In writing this post I created that algorithm by accident.

### HITS

HITS is an algorithm that predates PageRank and is pretty similar to eigenvalue centrality as well.
Instead of just looking at the graph we've been using which is directed, HITS turns it into an undirected graph emphasizing incoming or outgoing edges, alternately.

To do this (more linear algebra) HITS computes the left and right singular vectors of the graph, as opposed to the eigenvectors.
It does not include the normalization and irreducibility adjustments that PageRank has, but a matrix always has a singular value decomposition though uniqueness is not guaranteed unless all the singular values are distinct.
I'm curious what similar adjustments could do for HITS, but that will have to be left for a different time.
Because we get two vectors (the left and right singular vectors) from the HITS algorithm, we get two different answers for centrality.

The left singular vectors are called the "hubs" of the graph and the right singular vectors are the "authorities."
The hubs are nodes in the graph that link to a lot of other nodes; they are important outlinking nodes.
The authorities are the opposite, many other nodes point to them, referring to them as one might expect many people to refer to an authority.
The algorithm for this is also pretty simple:
```python
def hits(A):
    m, n = A.shape
    Hu = np.dot(A.T, A)
    Au = np.dot(A, A.T)
    w, authorities = eigs(Au, k=1, which='LM')
    w, hubs = eigs(Hu, k=1, which='LM')
    return authorities, hubs
```

You'll notice (perhaps you already knew) that the singular vectors that I referred to are exactly the eigenvectors of the matrices
$A^TA$ and $AA^T$.

This algorithm gives that the authority is Jefferson Dr & 14th St SW and that the hub is Lincoln Memorial.
This shouldn't be too surprising since there are very strong links to this nodes from each other

## Summary

Here is a table that shows the top 6 most important Capital Bikshare docks for each of the centrality measures considered here.

<table class="tg table table-bordered table-striped table-condensed table-hover table-responsive">
<tr>
<th style="border-right: 1px solid #000; border-bottom: 1px solid #000"></th>
<th style="border-bottom: 1px solid #000">Algorithms</th>
<th style="border-bottom: 1px solid #000"><br></th>
<th style="border-bottom: 1px solid #000"></th>
<th style="border-bottom: 1px solid #000"></th>
<th style="border-bottom: 1px solid #000"></th>
<th style="border-bottom: 1px solid #000"></th>
</tr>
<tr>
<td style="border-right: 1px solid #000; border-bottom: 1px solid #000"><b>Ranks</b> </td>
<td style="border-bottom: 1px solid #000">In Degree Centrality</td>
<td style="border-bottom: 1px solid #000">Out Degree Centrality</td>
<td style="border-bottom: 1px solid #000">Eigenvector Centrality</td>
<td style="border-bottom: 1px solid #000">PageRank</td>
<td style="border-bottom: 1px solid #000">HITS Hubs</td>
<td style="border-bottom: 1px solid #000">HITS Authorities</td>
</tr>
<tr>
<td style="border-right: 1px solid #000">1</td>
<td>Columbus Circle / Union Station</td>
<td>Columbus Circle / Union Station</td>
<td>Jefferson Dr &amp; 14th St SW</td>
<td>Columbus Circle / Union Station</td>
<td>Lincoln Memorial</td>
<td>Jefferson Dr &amp; 14th St SW</td>
</tr>
<tr>
<td style="border-right: 1px solid #000">2</td>
<td>Massachusetts Ave &amp; Dupont Circle NW</td>
<td>Massachusetts Ave &amp; Dupont Circle NW</td>
<td>Lincoln Memorial</td>
<td>Lincoln Memorial</td>
<td>Jefferson Dr &amp; 14th St SW</td>
<td>Lincoln Memorial</td>
</tr>
<tr>
<td style="border-right: 1px solid #000">3</td>
<td>Lincoln Memorial</td>
<td>Lincoln Memorial</td>
<td>Columbus Circle / Union Station</td>
<td>Massachusetts Ave &amp; Dupont Circle NW</td>
<td>Columbus Circle / Union Station</td>
<td>Massachusetts Ave &amp; Dupont Circle NW</td>
</tr>
<tr>
<td style="border-right: 1px solid #000">4</td>
<td>Jefferson Dr &amp; 14th St SW</td>
<td>Jefferson Dr &amp; 14th St SW</td>
<td>Massachusetts Ave &amp; Dupont Circle NW</td>
<td>Jefferson Dr &amp; 14th St SW</td>
<td>Massachusetts Ave &amp; Dupont Circle NW</td>
<td>Columbus Circle / Union Station</td>
</tr>
<tr>
<td style="border-right: 1px solid #000">5</td>
<td>15th &amp; P St NW</td>
<td>Thomas Circle</td>
<td>15th &amp; P St NW</td>
<td>15th &amp; P St NW</td>
<td>15th &amp; P St NW</td>
<td>15th &amp; P St NW</td>
</tr>
<tr>
<td style="border-right: 1px solid #000">6</td>
<td>14th &amp; V St NW</td>
<td>15th &amp; P St NW</td>
<td>Jefferson Memorial</td>
<td>Jefferson Memorial</td>
<td>New Hampshire Ave &amp; T St NW</td>
<td>14th &amp; V St NW</td>
</tr>
</table>

Looking at this we can see that for the graph considered here, the various different measures do not produce super different results.
Regardless of the centrality measure that we used, the top several most important nodes in the graph appear over and over again.
I don't mean to imply that it doesn't matter which one you use, just that for some graphs it may not matter too much.
The Wikipedia page on [graph centrality](https://en.wikipedia.org/wiki/Centrality) has the following figure showing how the most central nodes can be very different depending on the measure chosen for a particular example graph.


<div class="col-xs-12 thumb">
<figure>
<a href="https://upload.wikimedia.org/wikipedia/commons/1/11/6_centrality_measures.png" ><img class="img-responsive center-block" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/6_centrality_measures.png/400px-6_centrality_measures.png"></img></a>
<figcaption>
Examples of A) Betweenness centrality, B) Closeness centrality, C) Eigenvector centrality, D) Degree centrality, E) Harmonic centrality and F) Katz centrality of the same graph.
</figcaption>
</figure>
</div>

Clearly these are all different, so which is the best method for ranking nodes in a bikeshare network?
I really don't know. 
If anyone does, you can find my email on my [About]({filename}../pages/about.md) or message me on [twitter](https://twitter.com/KeithKelly).
The code I used to comptute all the ranks can be found on my [github](https://github.com/kwkelly/notebooks/blob/master/capitalbikeshare/centrality.py).
