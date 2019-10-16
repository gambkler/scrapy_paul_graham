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
