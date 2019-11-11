import datetime
import os

from pylatex import Document, Section, Subsection,\
    Command, FlushRight, NewPage, Center, HugeText, NewLine
from pylatex.utils import italic, NoEscape
import pylatex.config as cf
import lorem

l = '''
Minim amet sed exercitation. Labore lorem lorem ea amet officia lorem. Anim quis sint ut, nulla quis proident eiusmod anim. Dolor est sit reprehenderit. Lorem minim amet irure, cillum quis voluptate labore magna culpa esse aute. Ullamco aliquip reprehenderit lorem irure occaecat. Duis magna velit nulla reprehenderit elit occaecat, eu dolor veniam dolore.

Qui minim duis consectetur elit. Consectetur amet veniam nisi sit culpa sunt amet, magna sed tempor nisi sed pariatur in labore. Magna consectetur voluptate sit. Ad excepteur ad elit non ullamco, qui in est deserunt consequat nisi. Ullamco enim ullamco esse esse ea nostrud velit, aliquip duis eu reprehenderit culpa, velit pariatur minim laboris cupidatat sint culpa ad. Proident do magna non consequat consectetur, fugiat est ea ex incididunt.'''

class MyDocument(Document):
    def __init__(self):
        super().__init__(documentclass='book',
            document_options=['12pt', 'b5paper', 'twoside'],
            indent=True)
        self.preamble.append(Command('title', 'Blogs of Paul Graham'))
        self.preamble.append(Command('author', 'scrapy by gk'))
        self.preamble.append(Command('date', NoEscape(r'\today')))
        self.append(NoEscape(r'\maketitle'))
        self.append(NoEscape(r'\tableofcontents'))

    def fill_title(self, title, url, date):
        self.append(NoEscape(r'\chapter{%s}' % title))
        with self.create(FlushRight()):
            self.append(date)
        with self.create(FlushRight()):
            self.append(url)

    def fill_document(self, data, escape=False):
        if escape:
            self.append(data)
        else:
            self.append(NoEscape(data))
        self.append(NewPage())


doc = MyDocument()
doc.fill_title('sy', 'https://github.com', 'December 2019')
doc.fill_document(l)
doc.fill_title('gk', 'https://github.com/2', 'November 2019')
x = lorem.get_paragraph(count=(10), comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10), sep=os.linesep)
x = x.replace('\n', '\n\n')
doc.fill_document(x)

doc.generate_pdf('test', clean_tex=False)
tex = doc.dumps()  # The document as string in LaTeX syntax
