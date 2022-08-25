'''
convert http message format to python exploit script format
like follow:
	Host: 192.168.18.148:13333
	Upgrade-Insecure-Requests: 1
convert to:
	req += b"POST /login.action HTTP/1.1\n"
	req += b"Host: 192.168.18.148:13333\n" 

only support file path
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

def convert_msg(msgfpath, varname = "req"):
	if not os.path.exists(msgfpath):
		sys.stderr = f"[!] Oops ,open {path} failed"
		sys.exit(1)
	Dbg("retain file backup")
	os.system("cp " + msgfpath + " " + msgfpath + ".bak")
	with open (msgfpath, "r+") as f:
		fl = f.readlines()
	
	# file readed a '\n' ,need to get rid of it
	fl = list(map(
			lambda x : f"{varname} += " + "b\"" + x[:-1] + "\\n\"" ,
			fl))
	# print(fl)
	f.close()
	f = open(msgfpath, "w+")
	f.write(f"{varname}  = b\"\"\n")
	for i in fl:
		f.write(i + "\n")
	f.close()
	print("[+] done")

def usage():
	print("Usage : py ./msgConv.py -p /path/to/your/msgfile")

def main():
	usage()
	ap = argparse.ArgumentParser()
	ap.add_argument('-p','--path', help = 'message file path')
	ap.add_argument('-v','--variable', help = 'python variable name you want to use', default="req")
	args = ap.parse_args()
	fp = args.path
	var = args.variable
	convert_msg(fp)

main()