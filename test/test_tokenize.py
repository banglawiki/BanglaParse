#encoding=utf-8
from __future__ import print_function,unicode_literals
import sys
sys.path.append("../")
import banglaparse

g_mode="default"

def cuttest(test_sent):
    global g_mode
    result = banglaparse.tokenize(test_sent,mode=g_mode)
    for tk in result:
        print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))


if __name__ == "__main__":
    for m in ("default","search"):
        g_mode = m
        cuttest("এটা একটি অন্ধকার রাত যেখানে আপনি আপনার হাত দেখতে পারবেন না।")
        cuttest("আমি বাংলা ভাষা ভালোবাসি।")
        cuttest("আমি ঢাকায় থাকি।")
        cuttest("বাংলাদেশ একটি সুন্দর দেশ।")
        cuttest("আমার নাম রহিম।")
        cuttest("ঢাকা বাংলাদেশের রাজধানী।")
        cuttest("abc")
        cuttest("সূর্য পূর্বদিকে ওঠে।")
        cuttest("মাইক্রোসফট একটি সফটওয়্যার কোম্পানি।")
        cuttest("আমি কম্পিউটার প্রোগ্রামিং পছন্দ করি।")
        # Add more Bengali test cases as needed
