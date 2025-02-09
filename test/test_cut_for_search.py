#encoding=utf-8
from __future__ import print_function
import sys
sys.path.append("../")
import banglaparse

def cuttest(test_sent):
    result = banglaparse.cut_for_search(test_sent)
    for word in result:
        print(word, "/", end=' ') 
    print("")

if __name__ == "__main__":
    cuttest("এটি একটি অন্ধকার রাত যেখানে পাঁচ আঙ্গুল দেখা যায় না।")
    cuttest("আমি জাপানি কিমোনো পছন্দ করি না।")
    cuttest("বাংলাদেশ একটি সুন্দর দেশ।")
    cuttest("আমি ঢাকায় থাকি।")
    cuttest("আমার বাসা মিরপুরে।")
    cuttest("সফটওয়্যার ইঞ্জিনিয়ারিং একটি চমৎকার পেশা।")
    cuttest("আমি পাইথন এবং সি++ প্রোগ্রামিং ভালোবাসি।")
    cuttest("abc")
    cuttest("কম্পিউটার বিজ্ঞান")
    cuttest("ঢাকা বিশ্ববিদ্যালয়")
    cuttest("বাংলা ভাষা প্রসেসিং")
    # You can add more Bengali test sentences as needed
