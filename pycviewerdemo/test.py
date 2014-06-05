#coding:utf-8

class A:

	def __init__(self):

		self.aa = 'aa'


def B():
	print 'bb'



class C:

	def __init__(self, mystr):
		self.mystr = mystr

	def test(self):

		return self.mystr
	pass

a = A()
B()

cc = C('a')
print cc.test()