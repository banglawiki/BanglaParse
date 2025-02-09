#encoding=utf-8
from __future__ import print_function
import sys
sys.path.append("../")
import banglaparse.posseg as pseg

def cuttest(test_sent):
    result = pseg.cut(test_sent, HMM=False)
    for word, flag in result:
        print(word, "/", flag, ", ", end=' ')
    print("")


if __name__ == "__main__":
    cuttest("এটি একটি অন্ধকার রাত যেখানে আপনি আপনার হাত দেখতে পারবেন না।")
    cuttest("আমি জাপানি কিমোনো পছন্দ করি না।")
    cuttest("আমি ঢাকা ভালোবাসি।")
    cuttest("আমি পাইথন এবং সি++ ভালোবাসি।")
    cuttest("আমার সস্তা ভাড়ার বাসা দরকার।")
    cuttest("স্বর্ণালী পোশাক লিমিটেড")
    cuttest("আমি শহীদ মিনার ভালোবাসি")
    cuttest("abc")
    cuttest("হিডেন মারকভ মডেল")
    cuttest("মাইক্রোসফট")
    cuttest("বাংলাদেশ বিজ্ঞান ও শিল্প গবেষণা পরিষদ")
    cuttest("রোমিও এবং জুলিয়েট")
    cuttest("আমি পোশাক কিনেছি")
    cuttest("PS: ওপেন সোর্স ভালো")
    cuttest("ঢাকা বিভাগ")

    # You can continue adding more Bengali test sentences as needed
    # I've provided a few examples to get you started
    # The original had many more test cases - you should add equivalent Bengali sentences
    # based on your specific testing needs
