#-*- coding:utf-8 -*-

import os

here = os.path.dirname(os.path.abspath(__file__))
files = filter(lambda x: x[:3] == 'day' and x[-5:] == '.html', os.listdir(here))

day =  len(files)


def make_dropdown_menu(day, now):
    res = '<div class="dropdown-menu" aria-labelledby="dropdown01">\n'
    res += '\t' * 6 + '<a class="dropdown-item" href="index.html">Top</a>\n'
    for i in range(1,day+1):
        if i == now:
            res += '\t'*6 + '<a class="dropdown-item disabled" href="#">Day%d</a>\n'%i
        else:
            res += '\t'*6 + '<a class="dropdown-item" href="day%d.html">Day%d</a>\n'%(i,i)

    res += '\t'*5 + '</div>'

    return res

for file in files:
    print file
    now = int(file.replace('day','').replace('.html',''))
    file = os.path.join(here,file)
    with open(file, "r") as f:
        source = f.read()
        begin = source.find('<div class="dropdown-menu" aria-labelledby="dropdown01">')
        end = source[begin:].find("</div>") + begin + 6

    with open(file, "w") as f:
        f.write(source[:begin] + make_dropdown_menu(day, now) + source[end:])


######################
# just run 
# python auto_maker.py
# 
#
#
