def demo():
    for i in range(1,11):
        yield i
d=demo()
print(next(d))
print(next(d))
print(next(d))

import sys
li=[i for i in range(1,100000)]
li2=(i for i in range(1,100000))
print(sys.getsizedof[li])
print(sys.getsizedof[li2])
