#import cowsay
import sys

#if len(sys.argv) == 2:
#    cowsay.trex("hello, " + sys.argv[1])

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])