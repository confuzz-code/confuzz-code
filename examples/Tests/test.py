import sys

sys.path.append( "../.." )

from confuzz import MainEngine

me = MainEngine()
#me.self_check()
me.run()