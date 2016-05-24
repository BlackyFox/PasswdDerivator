#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This script aim is to derivate some strings (passwords).
Author: BlackyFox
"""

import os
import argparse
import sys
import string
import codecs

def init():
    a = [u"A", u"@", u"à", u"â", u"ä", u"Ä", u"Â", u"4"]
    b = [u"B", u"8", r"|3", r"|o"]
    c = [u"C", u"ç", r"(", r"<"]
    d = [u"D", r"|)"]
    e = [u"E", u"é", u"è", u"ê", u"ë", u"€", u"3", u"Ê", u"Ë"]
    f = [u"F", r"|="]
    g = [u"G", u"6"]
    h = [u"H", r"|-|"]
    i = [u"I", u"1", u"î", u"ï", u"Î", u"Ï", u"|", u"!"]
    j = [u"J", r"_|"]
    k = [u"K", r"|<"]
    l = [u"L", u"1"]
    m = [u"M"]
    n = [u"N"]
    o = [u"O", u"ô", u"ö", u"Ô", u"Ö", u"0"]
    p = [u"P"]
    q = [u"Q"]
    r = [u"R"]
    s = [u"S", u"$", u"5"]
    t = [u"T", u"7"]
    u = [u"U", u"ù", u"û", u"ü", u"Û", u"Ü", r"|_|"]
    v = [u"V", r"\/"]
    w = [u"W", r"\/\/"]
    x = [u"X", u"><"]
    y = [u"Y"]
    z = [u"Z", u"2"]

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
        deriv(args.input.lower(), args.input, init(), 0, f)
    with codecs.open(fi, 'r', 'utf-8') as f:
        s = SetSupDoublons(f)

    if not args.output:
        for i in s:
            print(i)
    else:
        with codecs.open(args.output, 'w', 'utf-8') as ff:
            for i in s:
                ff.write(i)
    os.remove(fi)

def deriv(s, ss, tab, begin, f):
    for i in range(begin,len(s)):
        for ii in tab[string.lowercase.index(s[i])]:
            ss = ss[:i] + ii + ss[i + 1:]
            f.write(ss + "\n")
            if (begin + 1) < (len(s)):
                deriv(s, ss, tab, begin + 1, f)
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
