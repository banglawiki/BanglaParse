"""Banglaparse command line interface."""
import sys
import banglaparse
from argparse import ArgumentParser
from ._compat import *

parser = ArgumentParser(usage="%s -m banglaparse [options] filename" % sys.executable, description="Banglaparse command line interface.", epilog="If no filename specified, use STDIN instead.")
parser.add_argument("-d", "--delimiter", metavar="DELIM", default=' / ',
                    nargs='?', const=' ',
                    help="use DELIM instead of ' / ' for word delimiter; or a space if it is used without DELIM")
parser.add_argument("-p", "--pos", metavar="DELIM", nargs='?', const='_',
                    help="enable POS tagging; if DELIM is specified, use DELIM instead of '_' for POS delimiter")
parser.add_argument("-D", "--dict", help="use DICT as dictionary")
parser.add_argument("-u", "--user-dict",
                    help="use USER_DICT together with the default dictionary or DICT (if specified)")
parser.add_argument("-a", "--cut-all",
                    action="store_true", dest="cutall", default=False,
                    help="full pattern cutting (ignored with POS tagging)")
parser.add_argument("-n", "--no-hmm", dest="hmm", action="store_false",
                    default=True, help="don't use the Hidden Markov Model")
parser.add_argument("-q", "--quiet", action="store_true", default=False,
                    help="don't print loading messages to stderr")
parser.add_argument("-V", '--version', action='version',
                    version="Banglaparse " + banglaparse.__version__)
parser.add_argument("filename", nargs='?', help="input file")

args = parser.parse_args()

if args.quiet:
    banglaparse.setLogLevel(60)
if args.pos:
    import banglaparse.posseg
    posdelim = args.pos
    def cutfunc(sentence, _, HMM=True):
        for w, f in banglaparse.posseg.cut(sentence, HMM):
            yield w + posdelim + f
else:
    cutfunc = banglaparse.cut

delim = text_type(args.delimiter)
cutall = args.cutall
hmm = args.hmm
fp = open(args.filename, 'r') if args.filename else sys.stdin

if args.dict:
    banglaparse.initialize(args.dict)
else:
    banglaparse.initialize()
if args.user_dict:
    banglaparse.load_userdict(args.user_dict)

ln = fp.readline()
while ln:
    l = ln.rstrip('\r\n')
    result = delim.join(cutfunc(ln.rstrip('\r\n'), cutall, hmm))
    if PY2:
        result = result.encode(default_encoding)
    print(result)
    ln = fp.readline()

fp.close()
