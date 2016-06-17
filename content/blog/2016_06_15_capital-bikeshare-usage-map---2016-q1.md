Title: Capital Bikeshare Usage Map - 2016 Q1
Date: 2016-6-15 0:31
Tags:
Category:
Slug: capital-bikeshare-usage-map---2016-q1
Summary:
Status: draft
Authors: Keith Kelly

This map shows the relative number of trips between pairs of stations for Capital Bikeshare, the Washington, DC bikeshare program.
The data was obtained from the [Capital Bikeshare Trip History](https://s3.amazonaws.com/capitalbikeshare-data/index.html) and was processed using [python](https://www.python.org/), [pandas](http://pandas.pydata.org/), and finally plotted using [bokeh](http://bokeh.pydata.org/en/latest/).
The width of the line that connects two stations is proportional to the number of trips that went between those stations.
The stations themselves are labeled on the map with dots.
Unfortunately, it does not seem that bokeh allows me to add hover tooltips to the lines to display the actual number of trips.

The code used to generate the map can be found as either a [script](https://github.com/kwkelly/notebooks/blob/master/capitalbikeshare/map.py) or a [jupyter notebook](https://github.com/kwkelly/notebooks/blob/master/capitalbikeshare/bikeshare_map2016q1.ipynb), both on github.
Keep in mind you can't use either without the data!
The map by itself (not embedded in this page) may be viewed [here](../../../../../embed_html/gmap_plot.html).

<script language="JavaScript">
<!--
function autoResize(id){
var newheight;
var newwidth;

if(document.getElementById){
	newheight = document.getElementById(id).contentWindow.document .body.scrollHeight;
	newwidth = document.getElementById(id).contentWindow.document .body.scrollWidth;
}

document.getElementById(id).height = (newheight) + "px";
document.getElementById(id).width = (newwidth) + "px";
}
//-->
</script>
<iframe id="iframe1" frameborder="0" width=100% height=100% src="../../../../../embed_html/gmap_plot.html" onload="autoResize('iframe1');"></iframe>
