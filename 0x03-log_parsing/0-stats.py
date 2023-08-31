#!/usr/bin/python3
"""0-stats module reads stdin line by line, computes and prints log metrics"""

import re
import sys


cache = {}
total_size = 0
counter = 0


def print_logs():
    """Print total file size, and log status codes and their frequencies
    """
    print(f"File size: {total_size}")
    for code, freq in sorted(cache.items()):
        print("{}: {}".format(code, freq))


try:
    pattern = (
        r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s-\s'
        r'(\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d{6}\])\s'
        r'(\"GET /projects/260 HTTP/1.1\")\s'
        r'(\d{3})\s(\d+)'
    )

    # Start loop, counitng up to 10 lines
    while True:
        while counter < 10:
            # Read each line in standard input
            for line in sys.stdin:
                # Match whole log line and capture groups
                match = re.match(pattern, line)

                if match:
                    # Store status code of request in cache
                    status_code = int(match.group(4))
                    cache[status_code] = cache.get(status_code, 0)
                    cache[status_code] += 1

                    # Add file size of request in variable
                    file_size = int(match.group(5))
                    total_size += file_size

                    # Increment counter by 1
                    counter += 1

                # Break out of for loop on tenth iteration
                break

        # Print logs and reset counter
        print_logs()
        counter = 0

# End infinite loop on keyboard interruption and print logs
except KeyboardInterrupt:
    print_logs()
