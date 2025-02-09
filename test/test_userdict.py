#encoding=utf-8
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")
import banglaparse
banglaparse.load_userdict("userdict.txt")
import banglaparse.posseg as pseg

banglaparse.add_word('গ্রাফিন')  # graphene
banglaparse.add_word('ক্যাটলিন')  # Caitlyn
banglaparse.del_word('কাস্টম শব্দ')  # custom word

test_sent = (
"লি শিয়াওফু ইনোভেশন অফিসের প্রধান এবং ক্লাউড কম্পিউটিং এর একজন বিশেষজ্ঞ; বাইই শুয়াংলু কি\n"
"উদাহরণস্বরূপ আমি 'হান যু শাং জিয়ান' শিরোনাম দিয়েছি, কাস্টম ডিকশনারিতে এই শব্দটি N শ্রেণিতে যোগ করা হয়েছে\n"
"'তাইচুং' সঠিকভাবে বিভক্ত হওয়া উচিত নয়। ম্যাকে 'গ্রাফিন' বের করা যায়; এখন ক্যাটলিনও বের করা যায়।"
)
words = banglaparse.cut(test_sent)
print('/'.join(words))

print("="*40)

result = pseg.cut(test_sent)

for w in result:
    print(w.word, "/", w.flag, ", ", end=' ')

print("\n" + "="*40)

terms = banglaparse.cut('easy_install is great')
print('/'.join(terms))
terms = banglaparse.cut('পাইথন এর রেগুলার এক্সপ্রেশন ভালো')  # Python's regular expression is good
print('/'.join(terms))

print("="*40)
# test frequency tune
testlist = [
('আজ আবহাওয়া ভালো', ('আজ', 'আবহাওয়া')),  # Today weather is good
('পোস্টে রাখলে ভুল হবে।', ('পোস্টে', 'ভুল')),  # If put in post will be wrong
('আমাদের মধ্যে একজন বিশ্বাসঘাতক', ('মধ্যে', 'একজন')),  # Among us there is a traitor
]

for sent, seg in testlist:
    print('/'.join(banglaparse.cut(sent, HMM=False)))
    word = ''.join(seg)
    print('%s Before: %s, After: %s' % (word, banglaparse.get_FREQ(word), banglaparse.suggest_freq(seg, True)))
    print('/'.join(banglaparse.cut(sent, HMM=False)))
    print("-"*40)
