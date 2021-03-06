#!/usr/bin/python

import sys
import os.path
sys.path.append(os.path.dirname(__file__))

def read_device():
	device_counts = {}
	with open("id_ip_countTest.txt", "r") as f:
		lines = f.readlines()
	for line in lines:
		line = line.strip()
		words = line.split('\t')
		day, device_id = words[0], words[1]
		ip_count, id_count = words[2], words[3]
		key = "%s,%s" % (day, device_id)
		device_counts[key] = (ip_count, id_count)
	return device_counts

device_dict = read_device()

for line in sys.stdin:
	line = line.strip()
	words = line.split(",")
	if len(words) == 23 and words[0] != "id":
			time = words[1]
			day = time[4:6]
			device_id = words[10]
			if device_id != "a99f214a" and device_id != "c357dbff":
				key = "%s,%s" % (day, device_id)
				if key in device_dict:
					print "%s,%s,%s" % (line, device_dict[key][0], device_dict[key][1])
				elif key not in device_dict:  #shouldn't be used at all
					print "%s,%s,%s" % (line, "1", "1")
			elif device_id == "a99f214a" or device_id == "c357dbff":  #then the device_id is an unknown id
				print "%s,%s,%s" % (line, "1", "1")  #assume the counts are just 1 if unknown id
