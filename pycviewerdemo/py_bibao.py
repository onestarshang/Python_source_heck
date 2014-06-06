#coding:utf-8
a = 1
def f():
    a = 2
    def g():
          print a
    return g

func = f()
func() #[2]
