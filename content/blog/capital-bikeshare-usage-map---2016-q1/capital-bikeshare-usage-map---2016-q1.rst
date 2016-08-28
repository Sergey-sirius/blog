Capital Bikeshare Usage Map - 2016 Q1
#####################################

:date: 2016-6-15 11:21
:tags: map, data, opendata, analysis, DC
:category: general
:slug: capital-bikeshare-usage-map---2016-q1
:summary: This map shows the relative number of trips between pairs of stations for Capital Bikeshare, the Washington, DC bikeshare program.
:status: published
:authors: Keith Kelly

This map shows the relative number of trips between pairs of stations for Capital Bikeshare, the Washington, DC bikeshare program.
The data was obtained from the `Capital Bikeshare Trip History <https://s3.amazonaws.com/capitalbikeshare-data/index.html>`_ and was processed using `python <https://www.python.org/>`_, `pandas <http://pandas.pydata.org/>`_, and finally plotted using `bokeh <http://bokeh.pydata.org/en/latest/>`_.
The width of the line that connects two stations is proportional to the number of trips that went between those stations.
The stations themselves are labeled on the map with dots.
Unfortunately, `hover tooltips are not currently implemented for MultiLine objects <http://bokeh.pydata.org/en/latest/docs/reference/models/tools.html#bokeh.models.tools.HoverTool>`_, so I can't display the number of trips between stations.

The code used to generate the map can be found as either a `script <https://github.com/kwkelly/notebooks/blob/master/capitalbikeshare/map.py>`_ or a `jupyter notebook <https://github.com/kwkelly/notebooks/blob/master/capitalbikeshare/bikeshare_map2016q1.ipynb>`_, both on github.
Keep in mind you can't use either without the data!
The map by itself (not embedded in this page) may be viewed `here <../../../../../embed_html/gmap_plot.html>`_.

.. raw:: html
  :file: ./gmap_plot.html
