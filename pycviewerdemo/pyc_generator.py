#[pyc_generator.py]
import imp
import sys
import dis

def generate_pyc(name):
    fp, pathname, description = imp.find_module(name)
    try:
        imp.load_module(name, fp, pathname, description)
    finally:
        if fp:
            fp.close()


def getcompiledfile():
    source = open("test.py").read()
    co = compile(source, "test.py", 'exec')
    print dir(co)
    print type(co)
    print dis.dis(co)


getcompiledfile()
# if __name__ == '__main__':
#     # generate_pyc(sys.argv[1])
#     getcompiledfile()