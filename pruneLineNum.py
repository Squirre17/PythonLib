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
''' Description 
		: remove the chars that should pruned in the line head
		: copy code from other's text with line num in head usually annoying
		: this script aim to remove line num
''' 
# exec() serve for c file, so i dont care accurate indentation in line head
num = list(map(lambda x:str(x),list(range(0,10))))
def exec(path):
	# Dbg(f"num is {num}")
	if not os.path.exists(path):
		sys.stderr = f"[!] Oops ,open {path} failed"
		sys.exit(1)
	# not filter cmd injection , Security problem here
	# create backup
	Dbg("retain file backup")
	os.system("cp " + path + " " + path + ".bak")
	with open(path,"r+") as f:
		fl = f.readlines()
		f.close()
		head_num_l = []
		head_num = 0
		# record the num of chars that should pruned in the line head
		for i in fl:
			j = 0
			while i[j] == ' ' or (i[j] in num):
				j = j + 1
			head_num_l.append(j)
		head_num_l.sort()
		num_l_len = len(head_num_l)
		head_num = head_num_l[num_l_len//2]

		# write back to file
		f.close()
		f = open(path,"w+")
		for i in fl:
			f.write(i[head_num:])
		f.close()		
		Dbg("Done.")

def test():
	exec("/home/squ/develop/prun_headline_number/tests/test01.txt")

def usage():
	print("[usage example]: python3 src/pruneLineNum.py -p ./tests/test02.txt")

def main():
	usage()
	ap = argparse.ArgumentParser()
	ap.add_argument('-p','--path', help = 'file path')
	args = ap.parse_args()
	fp = args.path
	exec(fp)

main()
