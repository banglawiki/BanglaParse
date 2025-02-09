#encoding=utf-8
from __future__ import print_function
import sys
sys.path.append("../")
import banglaparse
import banglaparse.posseg as pseg
words=pseg.cut("আবার খোঁড়া আবার বোবা")
for w in words:
	print(w.word,w.flag)

