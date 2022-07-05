#!/usr/bin/python3
import sys
import collections

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
counts = {}
all_stat_count = 0
status_code_list = []
total_file_size = 0
counter = 1

for count, line in enumerate(sys.stdin):
    status_code = eval(line.split()[7])
    file_size = eval(line.split()[8])
    total_file_size += file_size
    if (status_code in status_codes):
        status_code_list.append(status_code)
    # print(status_code_list)

    for stat in status_code_list:
        if stat in counts:
            counts[stat] += 1
        else:
            counts[stat] = 1
    # print(counts)
    if (count % 10 == 0):
        print("File size: {}".format(total_file_size))

        od = collections.OrderedDict(sorted(counts.items()))
        for key, val in od.items():
            print("{}: {}".format(key, val))
        counter += 1
