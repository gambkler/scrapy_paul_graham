# scrapy_paul_graham

## index

1. `http://paulgraham.com/articles.html`
2. `$x('//font/a')`

## article

save original html and cleaned article

1. `$x('//font[@size="2" and @face="verdana"]')`
2. usually return two selector, use the first
3. delete `<table>`
4. treat `<br>` as newline, sometimes as paragraph separator (double br)
5. delete `\n`?
6. treat `<b>` as subtitle
7. treat `<hr>` as seperate line
8. highlight `<a>`
9. remove all `<element>`, expect elements: font, a, br, b
10. html.escape, html.unescape

```shell
scrapy shell http://www.paulgraham.com/articles.html
scrapy startproject paulgraham
scrapy genspider test paulgraham.com
scrapy crawl test
scrapy crawl test -s CLOSESPIDER_ITEMCOUNT=3
scrapy crawl basic -o items.jl
```

## latex

pylatex

```txt
https://www.ctan.org
which additionally contains
lastpage.ins            The installation file.
lastpage.drv            The driver to generate the documentation.
lastpage.sty            The .style file.
lastpage209.sty         The .style file for L A TEX2.09 only.
lastpage-example.tex    The example file.
```
