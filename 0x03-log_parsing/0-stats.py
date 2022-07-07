#!/usr/bin/python3
""" Log parser """
import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_code_data = {code: 0 for code in status_codes}
total_file_size = 0
try:
    count = 0
    for line in sys.stdin:
        splitstr = line.split()
        if len(splitstr) > 6:
            total_file_size += int(splitstr[-1])
            code = splitstr[-2]
            if code in status_code_data:
                count += 1
                status_code_data[code] += 1
                if count % 10 == 0:
                    print('File size: {}'.format(total_file_size))
                    for k, v in sorted(status_code_data.items()):
                        if v != 0:
                            print('{}: {}'.format(k, v))
except KeyboardInterrupt:
    print('File size: {}'.format(total_file_size))
    for k, v in sorted(status_code_data.items()):
        if v != 0:
            print('{}: {}'.format(k, v))
    raise
else:
    print('File size: {}'.format(total_file_size))
    for k, v in sorted(status_code_data.items()):
        if v != 0:
            print('{}: {}'.format(k, v))

# status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
# counts = {}
# total_file_size = 0

# try:
#     for line in sys.stdin:
#         linesplit = line.split()
#         if len(linesplit) > 6:
#             total_file_size += eval(linesplit[-1])
#             status_code = eval(linesplit[-2])
#             if (status_code in status_codes):
#                 if status_code in counts:
#                     counts[status_code] += 1
#                 else:
#                     counts[status_code] = 1

#         if (sum(counts.values()) % 10 == 0):
#             print("File size: {}".format(total_file_size))
#             for key, val in sorted(counts.items()):
#                 print("{}: {}".format(key, val))

# except KeyboardInterrupt:
#     print('File size: {}'.format(total_file_size))
#     for key, val in sorted(counts.items()):
#         print('{}: {}'.format(key, val))
#     raise

# else:
#     print('File size: {}'.format(total_file_size))
#     for key, val in sorted(counts.items()):
#         print('{}: {}'.format(key, val))
