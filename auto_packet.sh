#!/bin/bash

urls=(
  'https://en.wikipedia.org/wiki/Cat'
  'https://en.wikipedia.org/wiki/Dog'
  'https://en.wikipedia.org/wiki/Egress_filtering'
  'http://web.mit.edu/'
  'http://www.unm.edu/'
  'https://cmu.edu/'
  'https://www.berkeley.edu/'
  'https://www.utexas.edu/'
  'https://www.asu.edu/'
  'https://www.utdallas.edu/'
)

FILE="./vpn_packet.csv"
[ -f $FILE ] $$ rm $FILE
touch $FILE

for dir in {0..9}; do
  echo ${urls[$dir]} >> $FILE
  for f in {0..9}; do
    capinfos -zcrmT ~/Documents/lab1/part\ 3/${dir}/${f}.pcap >> $FILE
  done
  echo >> $FILE
done
