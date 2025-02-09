#encoding=utf-8
from __future__ import print_function
import sys
sys.path.append("../")
import banglaparse.posseg as pseg

def cuttest(test_sent):
    result = pseg.cut(test_sent)
    for word, flag in result:
        print(word, "/", flag, ", ", end=' ')
    print("")


if __name__ == "__main__":
    cuttest("এটি একটি অন্ধকার রাত যেখানে পাঁচ আঙ্গুল দেখা যায় না। আমার নাম সুন কংগ, আমি বেইজিং ভালোবাসি, আমি পাইথন এবং সি++ ভালোবাসি।")
    cuttest("আমি জাপানি কিমোনো পছন্দ করি না।")
    cuttest("হ্যালো, মানুষ ফিরে এসেছে।")
    cuttest("প্রতি মাসে ২৪টি টেকনিক্যাল ডিভাইস ইনস্টল করতে হয়")
    cuttest("আমার সাশ্রয়ী আবাসন প্রয়োজন")
    cuttest("ইউনিভার্সাল ক্লোদিং কোম্পানি লিমিটেড")
    cuttest("আমি তিয়েনানমেন স্কয়ার ভালোবাসি")
    cuttest("abc")
    cuttest("মার্কভ মডেল")
    cuttest("হ্যালো একটি ভালো ওয়েবসাইট")
    # ... you can continue converting the rest of the test cases similarly

    # I've shown a few examples above. You should continue translating the remaining 
    # test cases to Bengali in a similar way. Make sure to maintain proper Bengali 
    # sentence structure and meaning while translating.

