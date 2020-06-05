#!/usr/bin/env python3
import os, sys
import argparse


def apply_changes(filepath):
    """
    Sequentially renames every file within the folder. 
    """
    try:
        # Attempt to use the given file directory
        os.chdir(filepath)

        # Filter by files only
        filelist = [f for f in os.listdir() if os.path.isfile(f)]

        n_files = len(filelist)
        # Set total number of digits in order to posterior fill the filename with zeros
        n_digits = len(str(n_files))

        for i, _file in enumerate(filelist):
            # Get the file extension
            _, file_ext = os.path.splitext(_file)
            # Rename the file
            numeric_name = str(i + 1).zfill(n_digits)
            new_name = f"{numeric_name}{file_ext}"
            os.rename(_file, new_name)

    except FileNotFoundError:
        print("No such folder. Try again.")


def main():
    # Create an argument parser in order to allow CLI instructions
    parser = argparse.ArgumentParser(description="A simple sequential bulk-renaming tool")
    # Allow to pass the filename as an input argument
    parser.add_argument('-i', '--input', help="Target directory path in order to perform changes")
    # Assign the strings as namespace's attributes
    args = parser.parse_args()

    # Display help if no argument is provided
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    # Performs the default operation
    if args.input:
        apply_changes(args.input)


if __name__ == "__main__":
    main()
