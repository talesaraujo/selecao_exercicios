#!/usr/bin/env python3
import os, sys
import argparse


def apply_changes(filepath):

    try:
        os.chdir(filepath)
        filelist = [f for f in os.listdir() if os.path.isfile(f)]
        
        qty = len(filelist)
        n_digits = len(str(qty))

        for index, _file in enumerate(filelist):
            file_name, file_ext = os.path.splitext(_file)

            number_name = str(index).zfill(n_digits)
            new_name = f"{number_name}{file_ext}"

            os.rename(_file, new_name)

    except FileNotFoundError as e:
        print("No such folder. Try again.")


def main():
    
    parser = argparse.ArgumentParser(description="A simple sequential-renaming folder tool")

    parser.add_argument('-i', '--input', help="Target directory path in order to perform changes")
    
    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    if args.input:
        apply_changes(args.input)



if __name__ == "__main__":
    main()
