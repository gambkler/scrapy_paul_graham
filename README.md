# scrapy_paul_graham

## index
1. `http://paulgraham.com/articles.html`
2. `$x('//font/a')`

## article
save original html and cleaned article
1. `$x('//font[@size="2" and @face="verdana"]')`
2. usually return two selector, use the first
2. delete `<table>`
3. treat `<br>` as newline, sometimes as paragraph separator (double br)
4. delete `\n`?
5. treat `<b>` as subtitle
6. treat `<hr>` as seperate line
7. highlight `<a>`
8. remove all `<element>`, expect elements: font, a, br, b
9. html.escape, html.unescape
