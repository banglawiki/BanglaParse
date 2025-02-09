#encoding=utf-8
import sys
sys.path.append("../")
import banglaparse


def cuttest(test_sent):
    result = banglaparse.cut(test_sent)
    print(" / ".join(result))


if __name__ == "__main__":
    cuttest("এটা একটা অন্ধকার রাত যেখানে পাঁচ আঙ্গুল দেখা যায় না। আমার নাম সুন কং, আমি বেইজিং ভালোবাসি, আমি পাইথন এবং সি++ ভালোবাসি।")
    cuttest("আমি জাপানি কিমোনো পছন্দ করি না।")
    cuttest("হ্যালো বন্ধু।")
    # Add more Bengali test cases here
    cuttest("আমি ঢাকায় থাকি")
    cuttest("বাংলাদেশের রাজধানী ঢাকা")
    cuttest("আমি বাংলা ভালোবাসি")
    cuttest("abc")
    cuttest("কম্পিউটার প্রোগ্রামিং")

# Remove some of the original Chinese test cases as they're not relevant
# Add more Bengali test cases based on your needs
