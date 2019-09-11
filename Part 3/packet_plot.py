#! /usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np
import packet_digest
import sys

urls=[
  'https://en.wikipedia.org/wiki/Cat',
  'https://en.wikipedia.org/wiki/Dog',
  'https://en.wikipedia.org/wiki/Egress_filtering',
  'http://web.mit.edu/',
  'http://www.unm.edu/',
  'https://cmu.edu/',
  'https://www.berkeley.edu/',
  'https://www.utexas.edu/',
  'https://www.asu.edu/',
  'https://www.utdallas.edu/'
]

websites_short = ['Cat', 'Dog', 'Egress', 'MIT', 'UNM', 'CMU', 'UCB', 'UT', 'ASU', 'UTD']

if len(sys.argv) < 2:
    print("ERROR: no files specified")
    exit()
web_digests = list()
for i in range(1, len(sys.argv)):
    web_digests.append(packet_digest.digest_file(sys.argv[i]))


ffx_avg_lens = [packet_digest.find_avg_len(key, web_digests[0]) for key in urls]
ffx_avg_sents = [packet_digest.find_avg_sent(key, web_digests[0]) for key in urls]

tor_avg_lens = [packet_digest.find_avg_len(key, web_digests[1]) for key in urls]
tor_avg_sents = [packet_digest.find_avg_sent(key, web_digests[1]) for key in urls]

vpn_avg_lens = [packet_digest.find_avg_len(key, web_digests[2]) for key in urls]
vpn_avg_sents = [packet_digest.find_avg_sent(key, web_digests[2]) for key in urls]

# create plot
len_plot = plt.figure(1)
index = np.arange(len(urls))
bar_width = 0.3
opacity = 0.8

rects1 = plt.bar(index, ffx_avg_lens, bar_width,
alpha=opacity,
color='b',
label='ffx')

rects2 = plt.bar(index + bar_width, tor_avg_lens, bar_width,
alpha=opacity,
color='g',
label='tor')

rects3 = plt.bar(index + bar_width * 2, vpn_avg_lens, bar_width,
alpha=opacity,
color='r',
label='vpn')

plt.xlabel('website')
plt.ylabel('packet length')
plt.xticks(index + bar_width, websites_short)
plt.legend()

# plt.tight_layout()
len_plot = plt.figure(2)
index = np.arange(len(urls))
bar_width = 0.3
opacity = 0.8

rects1 = plt.bar(index, ffx_avg_sents, bar_width,
alpha=opacity,
color='b',
label='ffx')

rects2 = plt.bar(index + bar_width, tor_avg_sents, bar_width,
alpha=opacity,
color='g',
label='tor')

rects3 = plt.bar(index + bar_width * 2, vpn_avg_sents, bar_width,
alpha=opacity,
color='r',
label='vpn')

plt.xlabel('website')
plt.ylabel('packes sent')
plt.xticks(index + bar_width, websites_short)
plt.legend()

plt.show()

