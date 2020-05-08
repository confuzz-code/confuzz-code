Here is an example (Squid):

1. startup redis-server
```redis-server &```

2. cd into the examples/squid

3 edit the setting.json like this:

```json
{
  "software_name": "Squid",
  "conf_path": "/etc/squid/squid.conf",
  "conf_parse_mode": "PlainText",
  "misconf_mode": "Fuzzing",
  "test_mode": "Default",
  "add_new_options": true,
  "interval": 0.25,
  "log_file_path": "/var/log/squid/cache.log",
  "char2cut": 0
}
```

3. edit the squid_test.py like this:

```Python
import sys
sys.path.append( "../.." )
from confuzz import MainEngine

me = MainEngine()
me.print_options()
me.self_check()
```
run the squid_test.py to check the self-check report

```
2020-03-16 14:55:38,234  INFO: ----------Self-check Report----------
2020-03-16 14:55:42,279  INFO: Test Case ID: 1  Test Case Script: ps -ef | grep /usr/sbin/squid | grep -v grep | awk '{print $2}' | xargs kill -9  Test Case Result: True
2020-03-16 14:55:43,306  INFO: Test Case ID: 2  Test Case Script: /usr/sbin/squid -k parse  Test Case Result: True
2020-03-16 14:55:44,457  INFO: Test Case ID: 3  Test Case Script: /usr/sbin/squid -zX  Test Case Result: True
2020-03-16 14:55:47,097  INFO: Test Case ID: 4  Test Case Script: /usr/sbin/squid -N -d1  Test Case Result: True
2020-03-16 14:55:48,540  INFO: Test Case ID: 5  Test Case Script: squidclient mgr:  Test Case Result: True
2020-03-16 14:55:49,662  INFO: Test Case ID: 6  Test Case Script: /usr/sbin/squid -k shutdown  Test Case Result: True
```
If there is no failed tests, you can add the ```me.run``` to test fuzzing.

```Python
import sys
sys.path.append( "../.." )
from confuzz import MainEngine

me = MainEngine()
me.run() #The test results will be saved in Results/Fuzzing
me.failures_analyzing( [KEY] ) #analyzing the failures
me.success_analyzing([KEY])  #analyzing the passed tests
me.dump_overall_results("/Users/A/Desktop/confuzz_squid_confterr.csv") #Dump the confuzz report 
```

The report looks like 


Option Name | Mutation Name | Testcase Results | Analyzer Results | Observer4Crash | Observer4Hang | Observer4Termination
-- | -- | -- | -- | -- | -- | --
Mariadb:innodb_fast_shutdown | int_misconf3 | Fail | Bad | False | False | False
Mariadb:innodb_fast_shutdown | int_misconf4 | Fail | Bad | False | False | False

Mutation Name means the injection method.
Testcase Results: PASS or FAIL (the tests)
Analyzer Results: GOOD or BAD (log messages)
The others are not so useful for now.

Let me know if you meet any questions.