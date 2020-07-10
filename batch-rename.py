#!/usr/bin/env python
# -.- coding: utf-8 -.-
import os
import argparse
from shutil import copyfile

def main(args):
    # make dict for file name mapping
    file_map = {}
    f = open(args.index_file, 'r')
    for i in f:
        row = i.split('\t')
        file_map[row[0]] = row[1].strip()
    #print (file_map)
    if not os.path.exists(args.target_dir):
        print ('make new folder:', args.target_dir)
        os.mkdir(args.target_dir)

    for root, dirs, files in os.walk(args.source_dir):
        for i in files:
            src = os.path.join(root, i)
            dst = os.path.join(args.target_dir, file_map[i])
            print ('copy from {} to {}'.format(src, dst))
            copyfile(src, dst)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='batch rename files from map')
    parser.add_argument('source_dir', help='source dir')
    parser.add_argument('index_file', help='mapping (index) file')
    parser.add_argument('target_dir', help='target dir')

    args = parser.parse_args()
    main(args)
