#!/usr/bin/python3
"""task 14 last advanced task"""


import sys


def print_stats(total_size, status_codes):
    """
    Print the statistics of log processing.

    Args:
        total_size (int): The total size of files processed.
        status_codes (dict): A dictionary mapping status codes
        to their occurrence count.
    """
    print("File size: {}".format(total_size))
    for status in sorted(status_codes.keys()):
        print("{}: {}".format(status, status_codes[status]))


if __name__ == "__main__":
    try:
        codes = {}  # Dictionary to store status codes and their counts
        tot = 0  # Variable to store total file size
        roal = 0  # Variable to count the number of lines processed
        valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

        for line in sys.stdin:
            line = line.split()

            # Extract status code and file size from the line
            stat = line[-2]
            num = int(line[-1])

            # Update total file size
            tot += num

            # Update status code count
            if stat in valid_codes:
                codes[stat] = codes.get(stat, 0) + 1

            # Increment the line count and print stats every 10 lines
            roal += 1
            if roal % 10 == 0:
                print_stats(tot, codes)

    except KeyboardInterrupt:
        # Print stats upon keyboard interruption
        print_stats(tot, codes)
        raise
