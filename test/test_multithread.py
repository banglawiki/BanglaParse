#encoding=utf-8
import sys
import threading
sys.path.append("../")

import banglaparse

class Worker(threading.Thread):
    def run(self):
        seg_list = banglaparse.cut("আমি বেইজিং থিংহুয়া বিশ্ববিদ্যালয়ে এসেছি", cut_all=True)
        print("Full Mode:" + "/ ".join(seg_list))  #পূর্ণ মোড

        seg_list = banglaparse.cut("আমি বেইজিং থিংহুয়া বিশ্ববিদ্যালয়ে এসেছি", cut_all=False)
        print("Default Mode:" + "/ ".join(seg_list))  #ডিফল্ট মোড

        seg_list = banglaparse.cut("সে নেটইজ হ্যাংঝু রিসার্চ বিল্ডিংয়ে এসেছে")
        print(", ".join(seg_list))

        seg_list = banglaparse.cut_for_search("ছোট মিং মাস্টার্স ডিগ্রি চাইনিজ একাডেমি অফ সায়েন্সেস থেকে পাস করেছেন এবং পরে জাপানের কিয়োটো বিশ্ববিদ্যালয়ে পড়াশোনা করেছেন")  #সার্চ ইঞ্জিন মোড
        print(", ".join(seg_list))

workers = []
for i in range(10):
    worker = Worker()
    workers.append(worker)
    worker.start()

for worker in workers:
    worker.join()
