'''
8 => 1000 
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
def calc(num):
  l = []
  while num > 0:
    l.append(num % 2)
    num = num // 2
  l.reverse()
  l = list(map(lambda x: str(x), l))
  return "".join(l)

def usage():
  print(
    styles.YELLOW + "Usage " + styles.DEFAULT + ": py ./num2bit.py 8\n" +
    styles.YELLOW + "   or " + styles.DEFAULT + ": hex not support yet"
  )

def main():
  usage()
  assert(len(sys.argv) == 2)
  assert sys.argv[1].isnumeric()
  print(calc(int(sys.argv[1])))

main()