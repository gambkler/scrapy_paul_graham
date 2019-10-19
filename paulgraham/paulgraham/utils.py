import re
import html

class CustomException(Exception):
    pass

class Cleaner:
    def __init__(self):
        self._element_table_start_tag_pattern = re.compile(r'<table.*>')
        self._element_table_end_tag_string = r'</table>'
        self._raw_newline_pattern = re.compile(r'\\n')
        self._element_br_pattern = re.compile(r'<\\?br>')
        self._all_element_tag = re.compile(r'<.*?>')
        self._blanks_pattern = re.compile(r' *\n *')
        self._join_lines_pattern = re.compile(r'(\S)\n(\S)')
        self._escaped_apostrophe_pattern = re.compile(r"\\'")
        self._multi_emptyline_pattern = re.compile(r'\n{3,}')

    def clean_from_file(self, src_file='temp.html', dst_file='test.html'):
        with open(src_file) as f:
            self._content = f.read()
        self._process()
        with open(dst_file, 'w') as f:
            f.write(self._content)

    def clean(self, content):
        self._content = content
        self._process()
        return self._content

    def _process(self):
        self._remove_element_table()
        self._remove_raw_newline()
        self._replace_element_br()
        self._remove_all_element_tag()
        self._remove_blanks()
        self._join_lines()
        self._unescape()
        self._remove_multi_emptyline()

    def _remove_element_table(self):
        for i in self._element_table_start_tag_pattern.finditer(self._content):
            start_index = i.start()
            end_index = self._content.find(self._element_table_end_tag_string) + 8
            self._content = self._content[:start_index] + self._content[end_index:]

    def _remove_raw_newline(self):
        self._content = self._raw_newline_pattern.sub(' ', self._content)

    def _replace_element_br(self):
        self._content = self._element_br_pattern.sub('\n', self._content)
    
    def _remove_all_element_tag(self):
        self._content = self._all_element_tag.sub('', self._content)
    
    def _remove_blanks(self):
        self._content = self._blanks_pattern.sub('\n', self._content)
    
    def _join_lines(self):
        # twice to join '[1]' mark
        self._content = self._join_lines_pattern.sub(r'\1 \2', self._content)
        self._content = self._join_lines_pattern.sub(r'\1 \2', self._content)
    
    def _unescape(self):
        self._content = html.unescape(self._content)
        self._content = self._escaped_apostrophe_pattern.sub("'", self._content)
    
    def _remove_multi_emptyline(self):
        self._content = self._multi_emptyline_pattern.sub('\n\n', self._content)
