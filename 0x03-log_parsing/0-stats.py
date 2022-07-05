#!/usr/bin/python3
""" Log parser """
import sys
# import collections

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
counts = {}
all_stat_count = 0
status_code_list = []
total_file_size = 0
count = 0

for line in sys.stdin:
    status_code = eval(line.split()[7])
    file_size = eval(line.split()[8])
    total_file_size += file_size
    count += 1
    if (status_code in status_codes):
        status_code_list.append(status_code)
    # print(total_file_size)
    # print(status_code_list)

    for stat in status_code_list:
        if stat in counts:
            counts[stat] += 1
        else:
            counts[stat] = 1

    if (count % 10 == 0):
        print("File size: {}".format(total_file_size))

        for key, val in counts.items():
            print("{}: {}".format(key, val))
