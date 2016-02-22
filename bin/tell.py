#!/usr/bin/env python

import re
import sys
import os.path

def analyze(lines):
    arr = []
    pics = {}
    pos, scene, avatar = 1, '', ''
    while (pos < len(lines)):
        l = lines[pos]
        dialog = ''
        pos += 1
        if (not l or re.match('//', l)):
            continue
        if (re.match('---$', l)):
            avatar = '//:0'
        elif (re.match('-.*\(.*\):$', l)):
            avatar = re.match('-.*\((.*)\):$', l).group(1)
        elif (re.match('\[(.*)\]:(.*)$', l)):
            m = re.match('\[(.*)\]:(.*)$', l)
            pics[m.group(1)] = m.group(2)
        elif (re.match('#\d+ .*', l)):
            scene = re.match('#\d+ (.*)', l).group(1)
        else:
            dialog = l
        arr.append({'scene': scene, 'avatar': avatar, 'dialog': dialog})
    arr = map(lambda x:{
        'dialog': x['dialog'],
        'scene' : pics[x['scene']] if (x['scene'] in pics) else x['scene'],
        'avatar': pics[x['avatar']] if (x['avatar'] in pics) else x['avatar']
    }, arr)
    return arr

def load(f):
    fh = open(f, 'r')
    return map(str.strip, fh.readlines())

def generate(output):
    pos = 0;
    lastavatar, lastscene = '', ''
    while (pos < len(output)):
        state = output[pos]
        if (state['dialog']):
            print '{'
            print '    dialog: "' + state['dialog'] + '",'
            if (state['avatar'] and state['avatar'] != lastavatar):
                print '    avatar: "' + state['avatar'] + '",'
                lastavatar = state['avatar']
            if (state['scene'] and state['scene'] != lastscene):
                print '    scene:  "' + state['scene'] + '",'
                lastscene = state['scene']
            print '},'
        pos += 1

if (len(sys.argv) < 2):
    print "Please specify a file name."
    exit(1)
elif (not os.path.isfile(sys.argv[1])):
    print sys.argv[1], "is not a file."
    exit(1)
else:
    generate(analyze(load(sys.argv[1])))
