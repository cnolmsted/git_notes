#!/usr/bin/env python
"""usage: binomial.py [n] [k] [--log] [--help]
usage: binomial.py [--test] (must be the first argument if used, tests the module)

Optional arguments:
-h, --help (must be first arg)   shows this help message
--log (must be third and last arg after [n] and [k]) gives log10 of function
--test (must be only arg) runs the tests in the examples below

binomial.py defines the function choose(n,k) that 
returns the binomial coefficient of n and k which can be expressed mathematically as:
choose(n,k) = n! / (k! (n-k)!)
except it does it piecemeal so not to overload programing with giant numbers
to use it in python do: import binomial

Example output:
$ ./binomial.py 10 3 --log
n= 10
k= 3
The binomial coefficient is: 120
...and the log-base-10 of 120 is: 2.079181

Examples:
>>> logfactorial(10)
6.559763032876794
>>> log_Nfact_over_Kfact(10,10)
0
>>> log_Nfact_over_Kfact(5,6)
0
>>> log_Nfact_over_Kfact(100,50)
93.48692878224377
>>> choose(10,3)
120
>>> choose(20,20)
1
>>> choose(19,20)
1
"""
#All indentations use tab in this file.

import sys
import math
#following function takes the log of the factorial of a number
def logfactorial(intgr): 
    s = 0 
    for number in range(1, int(intgr)+1):
        s += math.log10(number)
    return(s)
#following function tests if something is an integer even if it is a string from an argument
def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
#following funciton calculates log(n!/k!)
def log_Nfact_over_Kfact(n_value,k_value):
    result = 0
    for number in range(int(k_value)+1, int(n_value)+1):
        result += math.log10(number)
    return(result)
#following function calculates log(n!/k!) - log((n-k)!)
def choose(n_value,k_value):
    result = 0 
    NminusK = int(n_value) - int(k_value)
    result += log_Nfact_over_Kfact(n_value,k_value) - logfactorial(NminusK)
    result = 10 ** result
    return(int(result))
#following gives help option
if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print(__doc__)
    sys.exit()
#this will allow one to run the tests contained within the docstring
if sys.argv[1] == "--test":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="tests the module and quits")
    args = parser.parse_args()
    if __name__ == '__main__':
        if args.test:
            import doctest
            doctest.testmod()
            sys.exit("The test is over... now, now, now, now, now, now, now, now...") #flaming lips reference
#the following runs the module if it is not a test
else:
    n = sys.argv[1] if len(sys.argv) >= 1 else 0
    k = sys.argv[2] if len(sys.argv) > 2 else 0
    arg3 = sys.argv[3] if len(sys.argv) > 3 else 0
#the above makes the arguments optional
#And the following tests if n and k options are positive integers with added snark
for arg in sys.argv[1:2]:
    if not is_intstring(arg):
        sys.exit("All arguments must be integers, punk.")
for arg in sys.argv[1:2]:
    if not int(arg) >= 0:
        sys.exit("All arguments must be positive, nimrod.")

#the following determines the output message, assuming it was properly executed
print("n= %d" % int(n))
print("k= %d" % int(k))
print("The binomial coefficient is: %d" % choose(n,k))
#remember the following only works if --log is the third argument
if arg3 == "--log":
   print("...and the log-base-10 of %d is: %f" % (choose(n,k),math.log10(choose(n,k))))