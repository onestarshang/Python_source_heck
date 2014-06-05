#coding:utf-8

import sys
import inspect
import types
import dis

class PycGenerator:

	def __init__(self, pyfilepath):
		self.pyfilepath = pyfilepath

	def getpycodeobj(self):
		source = open(self.pyfilepath).read()
		co = compile(source, self.pyfilepath, 'exec')
		return co

	def getcodeobjdetails(self):
		pyobj = self.getpycodeobj()
		attrlist = dir(pyobj)
		return dir(pyobj)

ttlist = ['co_argcount',\
          # 'co_code',\
          'co_consts',\
          'co_filename',\
          'co_firstlineno',\
          'co_flags',\
          # 'co_lnotab',\
          'co_name',\
          'co_names',\
          'co_nlocals',\
          'co_stacksize',\
          'co_varnames'
          ]

xmlstr = '<?xml version="1.0"?><pycfile>'

def parse(codeobj):
	global xmlstr
	for item in codeobj.co_consts:
		if type(item) is types.CodeType:
			xmlstr +='<codeobj>'
			# print '------------'
			# print item
			# print item.co_consts
			# print dir(item)
			# print '------------'
			for t in ttlist:
				xmlstr += '<%s><![CDATA['%t
				tmpobj = getattr(item, t)
				if type(tmpobj) is types.IntType:
					xmlstr += str(tmpobj)
					xmlstr += ']]></%s>'%t
				elif type(tmpobj) is types.StringType:
					xmlstr += str(tmpobj)
					xmlstr += ']]></%s>'%t
				# elif type(tmpobj) is types.TupleType:
				# 	if tmpobj:
				# 		for tto in tmpobj:
				# 			if type(tto) is types.CodeType:
				# 				parse(tto)
							
				# 			xmlstr += '<tupletype><![CDATA['
							
				# 			if tto :
				# 				xmlstr += str(tto)
				# 				xmlstr += ']]></tupletype>'
				# 		xmlstr += ']]></%s>'%t
				else:
					print '+++++++++'
					print t
					print type(getattr(item, t))
					print getattr(item, t)
					xmlstr += ']]></%s>'%t
			# xmlstr +='</codeobj>'
			
			parse(item)
			xmlstr +='</codeobj>'
		elif item:
			xmlstr += '<%s><![CDATA[%s]]></%s>'%(str(item), str(item), str(item))
			# print '++++++++++'
			# print item
			# print '++++++++++'





if __name__ == '__main__':
	pg = PycGenerator("test.py")
	codeobj = pg.getpycodeobj()
	import dis
	dd = dis.dis(codeobj.co_code)
	print str(dd)
	print type(str(dd))
	print codeobj.co_consts
	parse(codeobj)
	xmlstr+='</pycfile>'
	# print xmlstr
	f = open('test.xml', 'w')
	f.write(xmlstr)
	f.close()
	# tmp1 = codeobj.co_consts
	# # print tmp1
	# # tmp2 = tmp1[1].co_consts
	# print tmp1[2]

	# # print tmp2[0].co_consts



	# print type(codeobj)
	# print codeobj.co_consts
	# for item in codeobj.co_consts:
	# 	if type(item) is types.CodeType:
	# 		print item.co_consts

	# memlist = inspect.getmembers(codeobj)
	# for tt in memlist:
	# 	print tt[0], tt[1]
	# print pg.getcodeobjdetails()