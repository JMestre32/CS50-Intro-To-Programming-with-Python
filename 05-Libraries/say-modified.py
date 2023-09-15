#New say, that makes my functions do the talking

import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])