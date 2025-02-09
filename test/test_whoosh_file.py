# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys
import os
sys.path.append("../")
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser

from banglaparse.analyse import BengaliAnalyzer

analyzer = BengaliAnalyzer()

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
if not os.path.exists("tmp"):
    os.mkdir("tmp")
ix = create_in("tmp", schema)
writer = ix.writer()

file_name = sys.argv[1]

with open(file_name, "rb") as inf:
    i = 0
    for line in inf:
        i += 1
        writer.add_document(
            title="line"+str(i),
            path="/a",
            content=line.decode('utf-8', 'ignore')  # Changed from 'gbk' to 'utf-8'
        )
writer.commit()

searcher = ix.searcher()
parser = QueryParser("content", schema=ix.schema)

# Changed Chinese keywords to Bengali examples
for keyword in ("ফল", "তুমি", "প্রথম", "বাংলা", "রাউটার", "বিনিময়"):
    print("result of " + keyword)
    q = parser.parse(keyword)
    results = searcher.search(q)
    for hit in results:
        print(hit.highlights("content"))
    print("="*10)
