import os
import sys

def find_codebase(mypath, codebase_rootfile):
    root, branch = mypath, 'nonempty'
    while branch:
        if os.path.exists(os.path.join(root, codebase_rootfile)):
            codebase_root = os.path.dirname(root)
            return codebase_root
        root, branch = os.path.split(root)

def main(codebase_rootfile):
    thisfile = os.path.abspath(sys.modules[__name__].__file__)
    mypath = os.path.dirname(thisfile)
    codebase_root = find_codebase(mypath, codebase_rootfile)

    if codebase_root:
        if codebase_root not in sys.path:
#            print "Add:", codebase_root
#            sys.path.append(codebase_root)
            sys.path.insert(0, codebase_root)
#    else:
#        raise ImportError("Failed to locate %s by searching from %s up the tree" %
#                          (codebase_rootfile, mypath))

codebase_rootfile = '.codebase_root'
main(codebase_rootfile)
