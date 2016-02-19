import re

def analyze(lines):
    arr = []
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
        elif (re.match('#\d+ .*', l)):
            scene = re.match('#\d+ (.*)', l).group(1)
        else:
            dialog = l
        arr.append({'scene': scene, 'avatar': avatar, 'dialog': dialog})
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

generate(analyze(load('templates/show_white/white.drama')))
