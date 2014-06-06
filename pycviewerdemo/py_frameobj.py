#coding:-utf-8

import sys

value = 3

def g():
    frame = sys._getframe()
    print 'current function is : ', frame.f_code.co_name
    caller = frame.f_back
    print 'caller function is : ', caller.f_code.co_name
    print "caller's local namespace : ", caller.f_locals
    print "caller's global namespace : ", caller.f_globals.keys()

def f():
    a = 1
    b = 2
    g()

def show():
    f()

show()



######

[frame_getter.py]
import sys
def get_current_frame():
    try:
        1/0
    except Exception, e:
        type, value, traceback = sys.exc_info()
        return traceback.tb_frame.f_back
 