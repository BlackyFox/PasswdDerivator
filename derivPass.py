#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This script aim is to derivate some strings (passwords).
"""

import os
import argparse
import sys
import string
import codecs

def init():
    a = ["A", u"@", u"à", u"â", u"ä", u"Ä", u"Â"]
    b = ["B"]
    c = ["C", u"ç"]
    d = ["D"]
    e = ["E", u"é", u"è", u"ê", u"ë", u"€", u"3", u"Ê", u"Ë"]
    f = ["F"]
    g = ["G"]
    h = ["H"]
    i = ["I", "1", u"î", u"ï", u"Î", u"Ï"]
    j = ["J"]
    k = ["K"]
    l = ["L", "1"]
    m = ["M"]
    n = ["N"]
    o = ["O", u"ô", u"ö", u"Ô", u"Ö", u"0"]
    p = ["P"]
    q = ["Q"]
    r = ["R"]
    s = ["S", u"$"]
    t = ["T"]
    u = ["U", u"ù", u"û", u"ü", u"Û", u"Ü"]
    v = ["V", "\/"]
    w = ["W", "\/\/"]
    x = ["X"]
    y = ["Y"]
    z = ["Z"]

    rr = []
    rr.append(a)
    rr.append(b)
    rr.append(c)
    rr.append(d)
    rr.append(e)
    rr.append(f)
    rr.append(g)
    rr.append(h)
    rr.append(i)
    rr.append(j)
    rr.append(k)
    rr.append(l)
    rr.append(m)
    rr.append(n)
    rr.append(o)
    rr.append(p)
    rr.append(q)
    rr.append(r)
    rr.append(s)
    rr.append(t)
    rr.append(u)
    rr.append(v)
    rr.append(w)
    rr.append(x)
    rr.append(y)
    rr.append(z)

    return rr

def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('input', type=str, help="The string to derivate")
    parser.add_argument('-o', '--output', help="Specify a file to write the results")
    args = parser.parse_args(arguments)

    fi = "tmp_derivPass.txt"

    with codecs.open(fi, 'a', 'utf-8') as f:
        deriv(args.input, args.input, init(), 0, f)
    with codecs.open(fi, 'r', 'utf-8') as f:
        s = SetSupDoublons(f)

    if not args.output:
        for i in s:
            print(i)
    else:
        with codecs.open(args.output, 'w', 'utf-8') as ff:
            for i in s:
                ff.write(i)
    #os.remove(fi)

def deriv(s, ss, tab, begin, f):
    for i in range(begin,len(s)):
        for ii in tab[string.lowercase.index(s[i])]:
            ss = ss[:i] + ii + ss[i + 1:]
            #print(ss)
            f.write(ss + "\n")
            #print("Begin: " + str(begin) + " / Len(s): " + str(len(s)))
            if (begin + 1) < (len(s)):
                deriv(s, ss, tab, begin + 1, f)
            #ss = s
        ss = s

def _deriv(s, p, i, tab):
    print(s + " position " + p + " " + str(i))
    print(tab)

def SetSupDoublons(f):
    s = set()
    for line in f:
        if line.strip('\n'):
            s.add(line)
    return s

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
