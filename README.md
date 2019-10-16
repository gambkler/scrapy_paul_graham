# scrapy_paul_graham

## index
1. `http://paulgraham.com/articles.html`
2. `$x('//font/a')`

## article
save original html and cleaned article
1. `$x('//font[@size="2" and @face="verdana"]')`
2. delete `<table>`
3. treat `<br>` as newline, sometimes as paragraph separator (double br)
4. delete `\n`?
5. treat `<b>` as subtitle
6. highlight `<a>`
7. remove all `<element>`, expect elements: font, a, br, b
8. html.escape, html.unescape
