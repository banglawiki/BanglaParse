#encoding=utf-8
from __future__ import print_function
import sys
sys.path.append("../")
import banglaparse

def cuttest(test_sent):
    result = banglaparse.cut(test_sent,cut_all=True)
    for word in result:
        print(word, "/", end=' ') 
    print("")


if __name__ == "__main__":
    cuttest("এটা একটা অন্ধকার রাত যেখানে পাঁচ আঙ্গুল দেখা যায় না। আমার নাম সুন বুকং, আমি বেইজিং ভালোবাসি, আমি পাইথন এবং সি++ ভালোবাসি।")
    cuttest("আমি জাপানি কিমোনো পছন্দ করি না।")
    cuttest("মানুষের মাঝে ফিরে এসেছে।")
    cuttest("প্রযুক্তি বিভাগের কর্মকর্তা প্রতি মাসে অধীনস্থ অফিসে ২৪টি সুইচের ইনস্টলেশন কাজের রিপোর্ট করেন।")
    cuttest("আমার সাশ্রয়ী বাসা দরকার")
    cuttest("চিরস্থায়ী পোশাক এবং অ্যাক্সেসরিজ কোম্পানি")
    cuttest("আমি বেইজিং তিয়ানআনমেন ভালোবাসি")
    cuttest("abc")
    cuttest("মার্কভ চেইন")
    cuttest("এটা একটা ভালো ওয়েবসাইট")

# Continue with more Bengali test cases...
# I've shown a few examples, but you should continue converting the rest of the test cases
# to meaningful Bengali sentences that test various aspects of your parser
