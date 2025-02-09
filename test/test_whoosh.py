# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys,os
sys.path.append("../")
from whoosh.index import create_in,open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

from banglaparse.analyse import BengaliAnalyzer

analyzer = BengaliAnalyzer()

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
if not os.path.exists("tmp"):
    os.mkdir("tmp")

ix = create_in("tmp", schema)
writer = ix.writer()

writer.add_document(
    title="document1",
    path="/a",
    content="This is the first document we've added!"
)

writer.add_document(
    title="document2", 
    path="/b",
    content="The second one তুমি বাংলা পরীক্ষা is even more interesting! ফল খাও"
)

writer.add_document(
    title="document3",
    path="/c", 
    content="ফল কিনে এক্সপো যাও।"
)

writer.add_document(
    title="document4",
    path="/c",
    content="আইটি বিভাগের কর্মকর্তা প্রতি মাসে ২৪টি সুইচ এবং অন্যান্য প্রযুক্তিগত যন্ত্রপাতির ইনস্টলেশন কাজ তদারকি করেন"
)

writer.add_document(
    title="document5",
    path="/c",
    content="আমরা বিনিময় করি।"
)

writer.commit()
searcher = ix.searcher()
parser = QueryParser("content", schema=ix.schema)

for keyword in ("ফল এক্সপো", "তুমি", "first", "বাংলা", "সুইচ", "বিনিময়"):
    print("result of ", keyword)
    q = parser.parse(keyword)
    results = searcher.search(q)
    for hit in results:
        print(hit.highlights("content"))
    print("="*10)

for t in analyzer("আমার প্রিয় বন্ধু লিমু; আমি ঢাকা ভালোবাসি; IBM এবং Microsoft; I have a dream. this is interesting and interested me a lot"):
    print(t.text)
