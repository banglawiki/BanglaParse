#encoding=utf-8
from __future__ import print_function
import sys
sys.path.append("../")
import banglaparse

def cuttest(test_sent):
    result = banglaparse.cut(test_sent)
    print("  ".join(result))

def testcase():
    cuttest("এটা একটা অন্ধকার রাত যেখানে হাত দেখা যায় না। আমি সুন নিউকং, আমি বেইজিং ভালোবাসি, আমি পাইথন এবং সি++ ভালোবাসি।")
    cuttest("আমি জাপানি কিমোনো পছন্দ করি না।")
    cuttest("বানর মানুষের জগতে ফিরে এসেছে।")
    cuttest("প্রতি মাসে কারিগরি যন্ত্রপাতি পরিদর্শন করতে হয়")
    cuttest("আমার সাশ্রয়ী বাসস্থান দরকার")
    cuttest("চিরস্থায়ী পোশাক ও অ্যাক্সেসরিজ কোম্পানি")
    cuttest("আমি বেইজিং তিয়ানআনমেন ভালোবাসি")
    cuttest("abc")
    cuttest("মার্কভ মডেল")
    cuttest("বানর একটি ভালো ওয়েবসাইট")
    
if __name__ == "__main__":
    testcase()
    banglaparse.set_dictionary("foobar.txt")
    print("================================")
    testcase()
