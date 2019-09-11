#! /usr/bin/env python

import csv
import sys


class PacketInfo():
    def __init__(self, website, p_sent, p_len):
        self.website = website
        self.p_sent = int(p_sent)
        self.p_len = float(p_len)
    def __str__(self):
        return 'site: ' + self.website + '\npackets sent: ' + str(self.p_sent) + '\navg packet length: ' + str(self.p_len) + '\n'

def find_avg_len(key, website_pdigest):
    if key in website_pdigest:
        sum_len = sum([info.p_len for info in website_pdigest[key]])
        return sum_len / len(website_pdigest[key])
def find_avg_sent(key, website_pdigest):
    if key in website_pdigest:
        sent = sum([info.p_sent for info in website_pdigest[key]])
        return sent / len(website_pdigest[key])
def digest_file(filename):
    website_pdigest = dict()
    packet_info = list()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if len(row) == 1:
                website = row[0]
                packet_info = list()
            else:
                if len(row) == 3:
                    packet_info.append(PacketInfo(website, row[1], row[2]))
            website_pdigest[website] = packet_info
            #print(row)
    return website_pdigest


# if len(sys.argv) < 2:
#     "NO file spec"
#     exit()

# web = digest_file(sys.argv[1])
# avg_lens = [find_avg_len(key, web) for key in urls]
# avg_sents = [find_avg_sent(key, web) for key in urls]


# # create plot
# fig, ax = plt.subplots()
# index = np.arange(len(urls))
# bar_width = 0.35
# opacity = 0.8

# rects1 = plt.bar(index, avg_lens, bar_width,
# alpha=opacity,
# color='b',
# label='ffx')

# # rects2 = plt.bar(index + bar_width, means_guido, bar_width,
# # alpha=opacity,
# # color='g',
# # label='tor')

# # rects3 = plt.bar(index + bar_width, means_guido, bar_width,
# # alpha=opacity,
# # color='r',
# # label='vpn')

# plt.xlabel('website')
# plt.ylabel('packet length')
# plt.xticks(index + bar_width, websites_short)
# plt.legend()

# plt.tight_layout()
# plt.show()