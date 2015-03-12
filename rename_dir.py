#!/usr/bin/env python
#-*-coding: utf-8-*-

'''list files & rename directorys according to some rules
move child directory's files back up to parent's
'''
import os
import os.path as os_path
#=== windows version : ===
#import random
#=== windows version end ===

def run():
    dirs = []
    files = os.listdir('.')
    for f in files:
        if os_path.isdir(f) and '_' in f:
            # mv child_dir files back up to parents_dir
            move_file(f)
            # define new name
            new_name = f.split('_')[0]
            os.rename(f, new_name)
            print '=====rename {0} to {1}'.format(f, new_name)

def move_file(dire):
    os.chdir(dire)
    files = os.listdir('.')
    for f in files:
        if os_path.isdir(f):
            fs = os.listdir(f)
            for _f in fs:
                _f_p = os_path.join(f, _f)
                if os_path.isfile(_f_p):
                    os.rename(_f_p, _f)
                    # blew works on MacOS but not on Windows
                    # it show a WindowsError:183 than means can't rename a file with exist name
                    # === windows version : ===
                    #_flag = str(random.randint(1, 100000))
                    #os.rename(_f_p, _f+_flag)
                    #os.rename(_f+_flag, _f)
                    # === windows version end === 
                    print '>>>>> move {0} back up to {1} '.format(_f, dire.split('_')[0])
            # remove empty directory
            os.rmdir(f)

    # change directory backup
    os.chdir('..')

if __name__ == "__main__":
    run()
