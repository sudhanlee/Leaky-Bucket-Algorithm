#!/usr/bin/env python3

max_capacity = int(input("Enter Bucket Capacity: ")) #bucket capacity
buffer = int(input("Initial packets in bucket: ")) #remaining space in bucket
rate = int(input("Set output stream rate: ")) #output flow
while True:
	input_size = int(input("Enter input packet size: ")) #input packet

	if (buffer - rate) >= 0:
		buffer -= rate #outgoing packet
		print("Transmitted packet of rate: ",rate)
	
	if (buffer+input_size) >= max_capacity:
		# print("Packet overflowed: Packet of size",input_size,"is losed")
		print("Packet overflowed: Packet of size",buffer+input_size-max_capacity,"is losed")
		buffer = max_capacity
	else:
		buffer += input_size
	
	print("Buffer:",buffer," -- Max buffer size:",max_capacity)