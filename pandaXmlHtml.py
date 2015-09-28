__author__ = 'ryu'
'''
To install the lxml package, have to run yum install libxslt-devel libxml2-devel first
'''
from urllib2 import urlopen
from lxml.html import parse
from pandas.io.parsers import TextParser
from pandas import DataFrame
from StringIO import StringIO
import lxml.objectify as objectify


class ReadHTML:
    def __init__(self):
        pass

    def _unpack(self, row, kind='td'):
        elts = row.findall('.//%s' % kind)
        return [self.get_text(val, kind) for val in elts]

    def get_text(self, item, kind='th'):
        if kind == 'th':
            text_items = item.findall("./div/div")
            if len(text_items) == 0:
                return item.text_content()
            else:
                return text_items[0].text_content()
        else:
            return item.text_content().strip()

    def parse_options_data(self, table):
        rows = table.findall('.//tr')
        #<thead> has 2 <tr>s
        header = self._unpack(rows[0], kind='th')
        data = [self._unpack(r, kind='td') for r in rows[2:]]
        return TextParser(data, names=header).get_chunk()

    def main(self):
        #parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))
        parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL&date=1444348800'))
        doc = parsed.getroot()
        links = doc.findall(".//a")  #xPath

        lnk = links[28]
        lnk.get('href')
        lnk.text_content()

        urls = [lnk.get('href') for lnk in doc.findall('.//a')]

        tables = doc.findall(".//table")
        calls = tables[1]
        puts = tables[2]

        '''
        rows = calls.findall(".//tr")
        print _unpack(rows[3], kind='td')
        '''

        call_data = self.parse_options_data(calls)
        put_data = self.parse_options_data(puts)

        print call_data[:10]

#ReadHTML().main()


class ReadXML:
    def __init__(self):
        pass

    def read_from_file(self):
        path = "Performance_MNR.xml"
        parsed = objectify.parse(open(path))
        root = parsed.getroot()

        data = []
        skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']
        for elt in root.INDICATOR:
            el_data = {}
            for child in elt.getchildren():
                if child.tag in skip_fields:
                    continue
                el_data[child.tag] = child.pyval
            data.append(el_data)
        print data
        perf = DataFrame(data)
        print perf

    def read_from_other(self):
        tag = '<a href="http://www.google.com">Google</a>'
        root = objectify.parse(StringIO(tag)).getroot()
        print root.get('href')
        print root.text


ReadXML().read_from_file()