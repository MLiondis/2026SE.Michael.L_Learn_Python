import emoji
import sys

if len(sys.argv) == 2:
    print("output:", emoji.emojize(sys.argv[1]))