import datetime
import os
import json

from pylatex import Document, Command, FlushRight, NewPage, Center, HugeText, Package
from pylatex.utils import NoEscape


class Doc(Document):
    def __init__(self):
        super().__init__(documentclass='book',
            document_options=['12pt', 'a4paper', 'twoside'],
            indent=True,
            geometry_options=['margin=1in'],
        )
        self.preamble.append(Command('title', 'Blogs of Paul Graham'))
        self.preamble.append(Command('author', 'scrapy by gk'))
        self.preamble.append(Command('date', NoEscape(r'\today')))
        self.append(NoEscape(r'\maketitle'))
        self.append(NoEscape(r'\tableofcontents'))

    def add_article(self, title, url, data, escape=False):
        self.append(NoEscape(r'\chapter{'))
        self.append(title)
        self.append(NoEscape(r'}'))

        with self.create(FlushRight()):
            self.append(url)
        if escape:
            self.append(data)
        else:
            self.append(NoEscape(data))
        self.append(NewPage())


with open('./urls.jl') as f:
    j = json.load(f)
order = j['article_urls']

articles = []
with open('./items.jl') as f:
    while True:
        l = f.readline()
        if not l:
            break
        j = json.loads(l)
        articles.append({
            'num': order.index(j['url'][0]),
            'name': j['name'][0],
            'url': j['url'][0],
            'content': j['content'][0]
        })

articles.sort(key=lambda x: x['num'])

doc = Doc()
for a in articles:
    c = a['content']
    c = c.replace(r'&', r'\&')
    c = c.replace(r'%', r'\%')
    c = c.replace(r'$', r'\$')
    c = c.replace(r'{', r'\{')
    c = c.replace(r'}', r'\}')
    c = c.replace(r'#', r'\#')
    c = c.replace(r'≈', r'\approx')
    doc.add_article(a['name'], a['url'], c)
doc.generate_pdf('book', clean_tex=False)

# ['http://paulgraham.com/ineq.html',
#  'http://paulgraham.com/startupideas.html',
#  'http://paulgraham.com/hw.html',
#  'http://paulgraham.com/rootsoflisp.html',
#  'https://sep.yimg.com/ty/cdn/paulgraham/acl1.txt?t=1570864329&',
#  'https://sep.yimg.com/ty/cdn/paulgraham/acl2.txt?t=1570864329&']
