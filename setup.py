# -*- coding: utf-8 -*-
from distutils.core import setup
LONGDOC = """
banglaparse
=====

"banglaparse" (বাংলায় "তোতলানো") বাংলা পাঠ্য বিভাজন: এটি
সেরা পাইথন বাংলা শব্দ বিভাজন মডিউল হওয়ার জন্য তৈরি।

সম্পূর্ণ ডকুমেন্টেশন দেখুন ``README.md``

GitHub: https://github.com/banglawiki/banglaparse

বৈশিষ্ট্য
====

- তিনটি শব্দ বিভাজন মোড সমর্থন করে:

   - সুনির্দিষ্ট মোড: বাক্যটি সবচেয়ে নিখুঁতভাবে ভাগ করার চেষ্টা করে, যা পাঠ্য বিশ্লেষণের জন্য উপযুক্ত।
   - পূর্ণ মোড: বাক্যের সমস্ত সম্ভাব্য শব্দ শনাক্ত করে, যা খুব দ্রুত কিন্তু দ্ব্যর্থতা দূর করতে পারে না।
   - সার্চ ইঞ্জিন মোড: সুনির্দিষ্ট মোডের উপর ভিত্তি করে দীর্ঘ শব্দগুলিকে আরও বিভক্ত করে পুনরুদ্ধারের হার বাড়ায়, যা সার্চ ইঞ্জিনের জন্য উপযুক্ত।

- প্রচলিত বাংলা এবং ক্লাসিক্যাল বাংলা উভয়ই সমর্থিত
- কাস্টম অভিধান সমর্থন করে
- MIT লাইসেন্স

ইনস্টলেশন নির্দেশাবলী
========

এই কোড Python 2/3 উভয়ের সাথেই সামঞ্জস্যপূর্ণ।

- সম্পূর্ণ স্বয়ংক্রিয় ইনস্টলেশন: ``easy_install banglaparse`` অথবা ``pip install banglaparse`` / ``pip3 install banglaparse``
- আধা-স্বয়ংক্রিয় ইনস্টলেশন: প্রথমে https://pypi.python.org/pypi/banglaparse/ থেকে ডাউনলোড করুন, তারপর আনজিপ করে চালান:
   ``python setup.py install``
- ম্যানুয়াল ইনস্টলেশন: `banglaparse` ডিরেক্টরিটিকে বর্তমান ডিরেক্টরিতে বা `site-packages` ডিরেক্টরিতে রাখুন।
- ``import banglaparse`` ব্যবহার করে প্যাকেজটি আমদানি করুন।

"""

setup(name='banglaparse',
      version='0.0.1',
      description='বাংলা শব্দ বিভাজন ইউটিলিটি',
      long_description=LONGDOC,
      author='Md Sulaiman',
      author_email='dev.sulaiman@icloud.com',
      url='https://github.com/banglawiki/banglaparse',
      license="MIT",
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Bengali (Simplified)',
        'Natural Language :: Bengali (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='NLP,tokenizing,Bengali word segmentation',
      packages=['banglaparse'],
      package_dir={'banglaparse': 'banglaparse'},
      package_data={'banglaparse':['*.*','finalseg/*','analyse/*','posseg/*']}
)
