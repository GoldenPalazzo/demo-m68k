#!/usr/bin/env python3

def hsvtorg(h,s,v):
    if s == 0:
        v = int(v*255)
        return (v,v,v)
    h = h/60
    i = int(h)
    f = h - i
    p = v*(1-s)
    q = v*(1-s*f)
    t = v*(1-s*(1-f))
    v = int(v*255)
    p = int(p*255)
    q = int(q*255)
    t = int(t*255)
    if i == 0:
        return (v,t,p)
    if i == 1:
        return (q,v,p)
    if i == 2:
        return (p,v,t)
    if i == 3:
        return (p,q,v)
    if i == 4:
        return (t,p,v)
    if i == 5:
        return (v,p,q)

with open('allcolors_palette.txt', 'w') as f:
    for i in range(0, 360, 5):
        r,g,b = hsvtorg(i, 1, 1)
        f.write(f'{r} {g} {b}\n')
