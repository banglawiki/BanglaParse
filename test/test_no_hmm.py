#encoding=utf-8
import sys
sys.path.append("../")
import banglaparse

def cuttest(test_sent):
    result = banglaparse.cut(test_sent, HMM=False)
    print(" / ".join(result))

if __name__ == "__main__":
    cuttest("আমি বাংলা ভালোবাসি।")  # I love Bengali
    cuttest("ঢাকা বাংলাদেশের রাজধানী।")  # Dhaka is the capital of Bangladesh
    cuttest("সে স্কুলে যায়।")  # He/She goes to school
    cuttest("আমার নাম কমল।")  # My name is Kamal
    cuttest("বাংলাদেশ একটি সুন্দর দেশ।")  # Bangladesh is a beautiful country
    cuttest("আমি কম্পিউটার প্রোগ্রামিং পছন্দ করি।")  # I like computer programming
    cuttest("আজ সকালে বৃষ্টি হচ্ছে।")  # It's raining this morning
    cuttest("তিনি একজন ভালো মানুষ।")  # He/She is a good person
    cuttest("আমরা বাংলায় কথা বলি।")  # We speak in Bengali
    cuttest("ABC")  # Testing English characters
    cuttest("")  # Testing empty string
