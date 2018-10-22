import sys

from lxml import etree

CATEGORIES = set(['article', 'inproceedings', 'proceedings', 'book', \
                  'incollection', 'phdthesis', 'mastersthesis', 'www'])
DATA_ITEMS = ['title', 'booktitle', 'year', 'journal', 'ee','url']
TABLE_SCHEMA = ['element', 'mdate', 'dblpkey', 'title', 'booktitle', \
                'year', 'journal', 'ee','url']


def write_output(paper, authors):
    arranged_fields = []
    for field in TABLE_SCHEMA:
        if field in paper and paper[field] is not None:
            arranged_fields.append(paper[field].encode('utf-8'))
        else:
            arranged_fields.append('')
    for author in authors:
            print('\t'.join(arranged_fields) + '\t' + author)


def clear_element(element):
    element.clear()
    while element.getprevious() is not None:
        del element.getparent()[0]


def extract_paper_elements(context):
    for event, element in context:
         if element.tag in CATEGORIES:
               yield element
               clear_element(element)


def fast_iter2(context):
    for element in extract_paper_elements(context):
        authors = []
        for author in element.findall('author'):
            if author is not None and author.text is not None:
                authors.append(author.text.encode('utf-8'))
            paper = {
                'element' : element.tag,
                'mdate' : element.get('mdate'),
                'dblpkey' : element.get('key')
            }
            for data_item in DATA_ITEMS:
                 data = element.find(data_item)
                 if data is not None:
                     paper[data_item] = data.text
        write_output(paper, authors)


def main():
    # Accept command line arguments

    # Parse xml input file
    for event, elemn  in etree.iterparse('/Users/derib/Downloads/dblp.xml', dtd_validation=True, events=('start', 'end')):
        print ('event ',event, ' elment ',elemn.text)


if __name__=='__main__':
    main()
