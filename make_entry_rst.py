import sys
from datetime import datetime

# copied from http://nafiulis.me/making-a-static-blog-with-pelican.html

TEMPLATE = """
{title}
{hashes}

:date: {year}-{month}-{day} {hour}:{minute:02d}
:tags:
:category:
:slug: {slug}
:summary:
:status: draft
:authors: Keith Kelly


"""


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/blog/{}.rst".format(slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print("No title given")
