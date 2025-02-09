# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys
import os
sys.path.append("../")
from whoosh.index import create_in,open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

from banglaparse.analyse import BengaliAnalyzer 

analyzer = BengaliAnalyzer()

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
if not os.path.exists("tmp"):
    os.mkdir("tmp")
ix = open_dir("tmp")

searcher = ix.searcher()
parser = QueryParser("content", schema=ix.schema)

# Bengali keywords instead of Chinese
for keyword in ("ফল মহিলা", "তুমি", "first", "বাংলা", "সুইচ", "বিনিময়", "শাওলিন", "কিয়াং ফেং"):
    print("result of ", keyword)
    q = parser.parse(keyword)
    results = searcher.search(q)
    for hit in results:  
        print(hit.highlights("content"))
    print("="*10)
