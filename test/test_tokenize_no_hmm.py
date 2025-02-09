#encoding=utf-8
from __future__ import print_function,unicode_literals
import sys
sys.path.append("../")
import banglaparse

g_mode="default"

def cuttest(test_sent):
    global g_mode
    result = banglaparse.tokenize(test_sent,mode=g_mode,HMM=False)
    for tk in result:
        print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))


if __name__ == "__main__":
    for m in ("default","search"):
        g_mode = m
        cuttest("আমি বাংলা ভালোবাসি।")  # I love Bengali
        cuttest("ঢাকা বাংলাদেশের রাজধানী।")  # Dhaka is the capital of Bangladesh
        cuttest("আমি কম্পিউটার প্রোগ্রামিং শিখছি।")  # I am learning computer programming
        cuttest("abc")  # keeping English test
        cuttest("মাইক্রোসফট একটি সফটওয়্যার কোম্পানি।")  # Microsoft is a software company
        cuttest("বাংলা ভাষা আমার মাতৃভাষা।")  # Bengali is my mother tongue
        cuttest("আমি ভাত খাই।")  # I eat rice
        cuttest("কলকাতা একটি বড় শহর।")  # Kolkata is a big city
        cuttest("")  # empty string test
        cuttest("I love তোমাকে")  # Mixed English-Bengali text
