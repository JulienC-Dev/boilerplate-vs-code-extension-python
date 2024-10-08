"""
root : account
myapp -p update_account.json
"""

import json
import os
import argparse

def dump_json(content:dict, path)->None:
    with open(path, 'w') as f:
        json.dump(content, f)
    return None

def load_json(path:str)->dict:
    with open(path, 'r') as f:
        return json.load(f)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', type=str, help='Relative path for updating the account', required=True)
    return parser.parse_args()

def is_valid_path(path:str)->bool:
    return os.path.exists(path)

def main()->int:
  args = get_args()
  if not is_valid_path(args.path):
    print('File not found')
    return 1
  update_account = load_json(args.path)
  dump_json(update_account, args.path)
  print("Account updated successfully")
  return 0

if __name__ == '__main__':
  main()

