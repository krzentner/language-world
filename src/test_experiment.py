#!/usr/bin/env python3
import argparse
import time
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--content")
    parser.add_argument("-o", "--out-file")
    parser.add_argument("--crash", action='store_true')
    return parser.parse_args()

def main():
    args = parse_args()
    time.sleep(10)
    with open(args.out_file, "w") as f:
        f.write(args.content)
    dirname = os.path.dirname(args.out_file)
    home_data = os.path.expanduser("~/data")
    os.makedirs(os.path.join(home_data, dirname), exist_ok=True)
    with open(os.path.join(home_data, args.out_file), "w") as f:
        f.write(args.content)
    if args.crash:
        import sys
        print("Time to crash!")
        sys.exit(1)

if __name__ == '__main__':
    main()
