import sys
sys.path.append('../')

import banglaparse
import banglaparse.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags_stop_words.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open(file_name, 'rb').read()

banglaparse.analyse.set_stop_words("../extra_dict/stop_words.txt")
banglaparse.analyse.set_idf_path("../extra_dict/idf.txt.big");

tags = banglaparse.analyse.extract_tags(content, topK=topK)

print(",".join(tags))
