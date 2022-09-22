'''
py num2bit.py 78 20 39 17
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
  assert num > 0
  while num > 0:
    l.append(num % 2)
    num = num // 2
  l.reverse()
  l = list(map(lambda x: str(x), l))
  ret = "".join(l)
  align = ((len(ret) - 1)// 8 + 1 ) * 8 - len(ret)# align to 8
  return align * "0" + ret

def usage():
  print(
    styles.YELLOW + "Usage " + styles.DEFAULT + ": py ./num2bit.py 8 10 12\n" +
    styles.YELLOW + "   or " + styles.DEFAULT + ": hex not support yet"
  )

def main():
  usage()
  # assert(len(sys.argv) == 2)
  for i in range(1, len(sys.argv)):
    assert sys.argv[i].isnumeric()
    print(f"{sys.argv[i]} : {calc(int(sys.argv[i]))}")

main()