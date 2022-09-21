'''
bit represent string to decimal or hexadecimal
1000 => 8
'''
import sys
import os
import argparse 

class styles:
    RED="\033[31m"
    GREEN="\033[32m"
    YELLOW="\033[33m"
    BLUE="\033[34m"
    AMARANTH="\033[35m"
    DEFAULT="\033[0m"
    HIGHLIGHT="\033[1m"
    UNDERLINE="\033[4m"
    FLICKER="\033[5m"

def Dbg(msg):
  print(styles.AMARANTH+"[+]:"+msg+styles.DEFAULT)

check = ["0", "1"]
def calc(bitStr):
  sum = 0
  for i in bitStr:
    assert i in check
    if i == "1":
      sum = sum * 2 + 1
    else:
      sum = sum * 2
  return sum

def usage():
  print(
    styles.YELLOW + "Usage " + styles.DEFAULT + ": py ./bit2num.py 100010101\n" +
    styles.YELLOW + "   or " + styles.DEFAULT + ": hex not support yet"
  )

def main():
  usage()
  assert(len(sys.argv) == 2)
  print(calc(sys.argv[1]))

main()