Title: Analyzing Capital Bikeshare Data with Python and Pandas
Date: 2016-6-13 1:32
Tags: data, analysis, DC, statistics
Category:
Slug: analyzing-capital-bikeshare-data-with-python-and-pandas
Summary: I stumbled across Jake VanderPlas's blog post Analyzing Pronto CycleShare Data with Python and Pandas and thought it could be interesting to do something similar for the data from Washington DC's Capital Bikeshare.
Status: draft
Authors: Keith Kelly

This post looks terrible on mobile, please view on a larger screen.
You can view this notebook on [github](https://github.com/kwkelly/notebooks/blob/master/capitalbikeshare/capital_bikeshare.ipynb) but the plots don't work.
For the best viewing experience, you can view the notebook as its own page [here](../../../../../embed_html/capital_bikeshare.html)

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

<iframe id="iframe1" frameborder="0" width=100% height=100% src="../../../../../embed_html/capital_bikeshare.html" onload="setTimeout(autoResize('iframe1'),0);"></iframe>


This page may load slowly. The notebook is embeded in an iframe because I could not get the liquid tags notebook plugin to work properly.
It clobbered my blog css and didn't work with plotly.
