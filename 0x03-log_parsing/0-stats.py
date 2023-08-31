#!/usr/bin/python3
"""Reads stdin line by line, computes and prints log metrics
"""

import re
import sys


def print_logs(total_size, cache):
    """Print total file size, and log status codes and their frequencies
    """
    print(f"File size: {total_size}")
    for code, freq in sorted(cache.items()):
        print("{}: {}".format(code, freq))


cache = {}
total_size = 0
counter = 0

try:
    pattern = (
        r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s-\s'
        r'(\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d{6}\])\s'
        r'(\"GET /projects/260 HTTP/1.1\")\s'
        r'(\d{3})\s(\d+)'
    )

    for line in sys.stdin:
        # Match whole log line and capture groups
        match = re.match(pattern, line)

        if match:
            # Store status code of request in cache
            status_code = match.group(4)
            cache[status_code] = cache.get(status_code, 0)
            cache[status_code] += 1

            # Add file size of request in variable
            file_size = int(match.group(5))
            total_size += file_size

            # Increment counter by 1
            counter += 1

        if counter == 10:
            # Print logs and reset counter
            print_logs(total_size, cache)
            counter = 0

# End infinite loop on keyboard interruption and print logs
except Exception as err:
    pass

finally:
    print_logs(total_size, cache)
