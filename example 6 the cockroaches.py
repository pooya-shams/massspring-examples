#!/usr/bin/env python3
# File: the cockroaches.py

"""
cockroaches.py

the main idea of this example was inspired by a math problem
that one of my friends once told me. it says that we have 2*n
cockroaches which are moving on a stick with constant speed.
whenever two of them reach each other, they turn around and start
moving in the other direction. if any of them reaches the end of
the stick, it will fly away and disappear. the question is what is
the maximum possible amount of collisions before they all fly away?

I tried to simulate this problem to show that his answer was wrong.
but guess what? He was all right! and I was made fun of by myself, again.
(BTW the answers is n^2, but who cares?)
"""
import massspring as ms

n = int(input("how many cockroaches? "))

assert n % 2 == 0, ValueError(
    "n must be dividable by 2 but it's value is %d" % n)

r = 20
m = 10
d = 56
_vx = 30

for i in range(-n//2, n//2):
    x = i * d + d // 2
    vx = -ms.sign(x) * _vx
    ms.mass(x=x, m=m, r=r, vx=vx, bound=False)

s = 0


def frame():
    global s
    for c in ms.collision_lis:
        if c.check_collision():
            s += 1


ms.mainloop(2, 0, frame=frame)
print(s)
