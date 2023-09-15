#New say, that makes my functions do the talking

import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])