import json
import os
import pprint
import argparse
from pathlib import Path

def process_args():
    parser = argparse.ArgumentParser(description="A utility for quicksave/load of directories")
    parser.add_argument('-c', '--command', choices=["ls", "go", "save", "rm"], required=True)
    parser.add_argument('-k', '--key')
    args = parser.parse_args()
    return args

def get_portals(args):
    with open(f'{args["PORTALS_ROOT"]}/portal-list') as f:
        data = json.load(f)
    return data

def save_portals(data, args):
    with open(f'{args["PORTALS_ROOT"]}/portal-list', 'w') as f:
        json.dump(data, f)

def ls(args):
    data = get_portals(args)
    pprint.pprint(data)

def save(args):
    cur_dir = os.getcwd()
    data = get_portals(args)
    data[args["key"]] = cur_dir
    save_portals(data, args)

def go(args):
    data = get_portals(args)
    if (args["key"] not in data):
        print(f'No entry defined for {args["key"]}.')
        exit()
     # We're gonna pass this to cd
    print(data[args["key"]])

def rm(args):
    data = get_portals(args)
    if (args["key"] not in data):
        print(f'No entry defined for {args["key"]}.')
        exit()
    del data[args["key"]]
    save_portals(data, args)

if __name__ == "__main__":
    data_file = os.getenv("PORTALS_ROOT")
    if data_file is None:
        print("Please define the PORTALS_ROOT environment variable")
        exit()
    portals_list = Path(data_file + '/portal-list')
    if not (portals_list.is_file()):
        with portals_list.open("w") as f:
            f.write("{}")

    args = vars(process_args())
    switch = {
        "go": go,
        "rm": rm,
        "save": save,
        "ls": ls
    }
    args["PORTALS_ROOT"] = data_file
    if (args["command"] in ["save", "go", "rm"] and args["key"] is None):
        print("Please specify a key")
        exit()
    switch[args["command"]](args)