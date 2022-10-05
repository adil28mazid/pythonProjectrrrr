# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib
'''
'''


import matplotlib.pyplot as plot
matplotlib.use('TkAgg')

sites=['http://www.google.com','www.youtube.com']

def foo(b,c):
    assert  isinstance(b,str)
    return b


def method_name():
    x = [i for i in range(1000)]
    y = [i ** 2 for i in range(1000)]
    method_name2(x, y)
    a = 'range'


def method_name2(x, y):
    plot.plot(x, y)
    plot.show()


if __name__ == '__main__':

    method_name()
## hashtag