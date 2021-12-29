import os
import tempfile
import json
import argparse

# function for writing to file
def storage_write (path, to_storage):
    with open(path, 'w') as f:
            f.write(json.dumps(to_storage))

# function for reading from file to dictionary
def storage_read (path):
    with open(storage_path, 'r') as f:
        from_storage = json.loads(f.read())
    return from_storage

# script finds directory with temp files
# and concatenates path to this directory with the file name 'storage.data'
storage_path = os.path.join(tempfile.gettempdir(),'storage.data')

# script parses arguments of command line
parser = argparse.ArgumentParser()
parser.add_argument("--key", help='Key')
parser.add_argument("--val", help='Value')
args = parser.parse_args()

# analyzes whether --val is entered
if args.val != None:
    # if --val is entered script analyzes whether file exists
    if os.path.exists(storage_path):
        # script reads content of file
        storage_dict = storage_read(storage_path)
        if args.key in storage_dict:
            # if --key is in file, then script appends list for this --key
            # and writes dictionary back to file
            storage_dict[args.key].append(args.val) 
            storage_write(storage_path, storage_dict)       
        else:
            # if it --key isn't in file then script adds {--key : --val}
            # to dictionary and writes it back to file
            storage_dict.update({args.key : [args.val]})
            storage_write(storage_path, storage_dict) 
    else:
        storage_dict = {args.key : [args.val]}
        storage_write(storage_path, storage_dict)
else:
    # if --val isn't entered, script checks presence of the file
    if os.path.exists(storage_path):
        # script reads information from file
        storage_dict = storage_read(storage_path)
        # if --key is in file scripts prints values
        if args.key in storage_dict:
            print(*storage_dict[args.key], sep=', ')
        else:
            print('None')
    else:
        print('None')