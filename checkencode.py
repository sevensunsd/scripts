#!/usr/bin/env python
#-*-coding: utf-8-*-

'''use shell cmd file check file encode 
 print filename if encode is UTF-8 with BOM
 tested on Linux & MacOS
'''

import os
import sys
import commands

temp_dir  = []
file_list = []
bom_list  = []
def _checkEncode(filename):
    #Todo 
    #file filename
    res = commands.getstatusoutput('file {0}'.format(filename))
    if res[0]:
        print 'sys error'
        sys.exit(1)
    print res[1]
    if 'with BOM' in res[1]:
        bom_list.append(filename)

def traversalDir():
    for root, dirs, files in os.walk('.'):
        for _file in files:
            _file_path = os.path.join(root, _file)
            if os.path.exists(_file_path):
                _checkEncode(_file_path)
            else:
                print 'file %s not exists' % _file_path

if __name__ == "__main__":
    traversalDir()
    for f in bom_list:
        print "\033[0;31;40m%s\033[0m" % f