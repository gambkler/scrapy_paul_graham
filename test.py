import re
import html

class CustomException(Exception):
    pass

class Cleaner:
    def __init__(self, src_file='temp.html', dst_file='test.html'):
        self._src_file_name = src_file
        self._dst_file_name = dst_file

    def start(self):
        self._src_file = open(self._src_file_name)
        self._file_content = self._src_file.read()
        self._src_file.close()
        
        self._remove_element_table()
        self._remove_newline()
        self._replace_element_br()
        self._remove_all_element_tag()
        self._remove_blanks()
        self._join_lines()
        self._unescape()

        self._dst_file = open(self._dst_file_name, 'w')
        self._dst_file.write(self._file_content)
        self._dst_file.close()

    def _remove_element_table(self):
        for i in re.finditer(r'<table.*>', self._file_content):
            start_index = i.start()
            end_index = self._file_content.find(r'</table>') + 8
            self._file_content = self._file_content[:start_index] + self._file_content[end_index:]

    def _remove_newline(self):
        self._file_content = re.sub(r'\\n', ' ', self._file_content)

    def _replace_element_br(self):
        self._file_content = re.sub(r'<\\?br>', '\n', self._file_content)
    
    def _remove_all_element_tag(self):
        self._file_content = re.sub(r'<.*?>', '', self._file_content)
    
    def _remove_blanks(self):
        self._file_content = re.sub(r' *\n *', '\n', self._file_content)
    
    def _join_lines(self):
        # twice to join '[1]' mark
        self._file_content = re.sub(r'(\S)\n(\S)', r'\1 \2', self._file_content)
        self._file_content = re.sub(r'(\S)\n(\S)', r'\1 \2', self._file_content)
    
    def _unescape(self):
        self._file_content = html.unescape(self._file_content)
        self._file_content = re.sub(r"\\'", "'", self._file_content)

c = Cleaner()
c.start()
