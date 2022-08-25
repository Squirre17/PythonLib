#!/bin/python
'''
	Aim to convert the opcode file compiled by solc to pure bin file 
	for facilitating IDA analyse
'''
def num2byte_1(n):
	assert (n >> 8) == 0
	return n.to_bytes(1, "little")

# opcode.bin file and pure bin file will be stored
def convert(opf, binf):
	f = open(opf, 'r')
	opcode = f.read()
	f.close()

	print(f"opcode is {opcode}")
	arr = []
	i = 0
	while i < len(opcode):
		arr.append(int(opcode[i:i+2], 16))# str2int
		i += 2
	
	arr = list(map(lambda x: num2byte_1(x), arr))# int2byte
	out = b"".join(arr) 
	print(out)
	f = open(binf, 'wb')
	f.write(out)
	f.close()


convert("./e_sol_Storage.bin", "tmp.bin")

