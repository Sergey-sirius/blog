Adding galleries to pelican and bootstrap
#########################################

:date: 2016-5-23 23:13
:tags: pelican, photos, meta
:category:
:slug: adding-galleries-to-pelican-and-bootstrap
:summary: I had a few problems getting the photos plugin to play nice with pelican and with my pelican-bootstrap3 theme. This post explains what I went through to get everything working properly.
:status: published
:authors: Keith Kelly
:gallery: {photo}woke

Let's start with a bit of background on what powers this blog.
We are using `pelican <http://blog.getpelican.com/>`_, a static site generator written in python, to produce the pages.
The site uses the ``pelican-bootstrap3`` theme provided by `pelicanthemes <http://www.pelicanthemes.com/>`_.
The HTML is served by ``nginx`` from a linode ubuntu server.

Now onto the issue at hand.

I had a bit of trouble getting the pelican `photo plugin <https://github.com/getpelican/pelican-plugins/tree/master/photos>`_ working on this site so I thought I'd take a few minutes to document it in case I or anyone else runs into similar issues in the future.
The first thing to do is to indicate to pelican that you are using the plugin via the ``PLUGINS`` variable, indicate the photos base directory and, and specify the maximum sizes of the photos. Here's an excerpt from my ``pelicanconf.py``::

    PLUGIN_PATHS = ['../pelican-plugins/']
    PLUGINS = ['photos']
     
    PHOTO_LIBRARY = "~/Pictures"
    PHOTO_GALLERY = (4096, 4096, 100)
    PHOTO_ARTICLE = (768, 768, 80)
    PHOTO_THUMB = (512, 512, 60)

The next step is adding the relevant jinja2/html/python code to the ``article.html`` template.
The pelican photo plugin github page gives this example code::

    {% if article.photo_gallery %}
    <div class="gallery">
        {% for name, photo, thumb, exif, caption in article.photo_gallery %}
        <a href="{{ SITEURL }}/{{ photo }}" title="{{ name }}" exif="{{ exif }}" caption="{{ caption }}"><img src="{{ SITEURL }}/{{ thumb }}"></a>
        {% endfor %}
    </div>
    {% endif %}

but I was unable to get that to work. 
Python gave an error that I was trying to unpack too many items from a list or tuple.
I ended up changing the third line to read::

    {% for name, photo, thumb, exif, caption in article.photo_gallery[0][1] %}

which seemed to work.

Thirdly, I needed to add some styling to the generated html.
Since this blog is using `bootstrap <http://getbootstrap.com/>`_ to make it not hopelessly hideous, I placed a ``div`` around the ``img`` tag, added ``class="img-responsive"`` to the image tag, and specified the `grid layout options for bootstrap <http://getbootstrap.com/css/#grid-options>`_.::

      {% if article.photo_gallery %}
      <div class="gallery">
        {% for name, photo, thumb, exif, caption in article.photo_gallery[0][1] %}
        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-4 thumb">
          <a href="{{ SITEURL }}/{{ photo }}" title="{{ name }}" exif="{{ exif }}" caption="{{ caption }}"><img class="img-responsive" src="{{ SITEURL }}/{{ thumb }}"></a>
        </div>
        {% endfor %}
      </div>
      {% endif %}

However, I still needed to add some vertical spacing between the images and ensure that the ``#content`` ``div`` grew to accomodate the photos.
Failing to specify ``overflow: auto;`` for the container resulted in it being covered by other elements for narrow window sizes.
To this end, I added::

  #content {
    overflow: auto;
    height: auto;
  }

  .thumb {
    margin-bottom: 30px;
  }

to the ``style.css`` file in the ``pelican-bootstrap3`` directory.

Finally, I wanted a lightbox.
The pelican photos documentation again very helpfully provides some code to achieve this and explains what to do with it.
I just had to change a few lines to get it working with my theme. 
Instead of linking to an external jQuery, I just sourced the local one necessary for my theme to work.
I changed ``<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>`` to ``<script src="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/js/jquery.min.js"></script>``.
One more problem, however. The guide I was following said to put the ``magnific-popup.{js,css}`` files in the base of the theme directory, but the theme that I'm using checks for them in the ``css`` and ``js`` directories within a ``static``. It will not work if you symlink the files instead of copying them.
I ended up with the following code.::

    {% if (article and article.photo_gallery) or (articles_page and articles_page.object_list[0].photo_gallery) %}
       <link rel="stylesheet" href="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/magnific-popup.css">
    {% endif %}

and::

    {% if (article and article.photo_gallery) or (articles_page and articles_page.object_list[0].photo_gallery) %}
        <script src="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/js/jquery.min.js"></script>

        <!-- Magnific Popup core JS file -->
        <script src="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/js/magnific-popup.js"></script>
        <script>
        $('.gallery').magnificPopup({
            delegate: 'a',
            type: 'image',
            gallery: {
                enabled: true,
                navigateByImgClick: true,
                preload: [1,2]
            },
            image: {
                titleSrc: function(item) {
                    if (item.el.attr('caption') && item.el.attr('exif')) {
                        return (item.el.attr('caption').replace(/\\n/g, '<br />') +
                            '<small>' + item.el.attr('title') + ' - ' + item.el.attr('exif') + '</small>');
                    }
                return item.el.attr('title') + '<small>' + item.el.attr('exif') + '</small>';
            } }
        });
        </script>
    {% endif %}

This all still needs more work.
I'd like to be able to adjust the number of pictures in a row based on the width of thumbnail that is generated.
I'd also like to be able to place content above and below the gallery.
Right now, placing content above and below would require adding each picture individually, though this is not yet implemented.`

Now, just to show that it works, here's an example.
I took the gallery from an `imgur link <http://imgur.com/gallery/9sEzy>`_.

