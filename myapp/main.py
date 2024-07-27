import json
import os
import argparse

def dump_json(content:dict)->None:
    path = os.path.join(os.getcwd(), 'account.json')
    with open(path, 'w') as f:
        json.dump(content, f)
    return None

def load_json(path:str)->dict:
    path = os.path.join(os.getcwd(), 'update_account.json')
    with open(path, 'r') as f:
        return json.load(f)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--update', type=str, help='file update account', required=True)
    return parser.parse_args()

def main()->int:
  args = get_args()
  update_account = load_json(args.update)
  dump_json(update_account)
  return 0

if __name__ == '__main__':
  main()

