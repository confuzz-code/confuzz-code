import sys
sys.path.append( "../.." )
from confuzz import MainEngine

me = MainEngine()
# me.print_options()
# me.self_check()
# me.run()
me.start_offline_analyzing()
me.failures_analyzing()
me.dump_overall_results("/usr/Desktop/CS597/confuzz/examples/Redis/confuzz_redis_confterr.csv")

