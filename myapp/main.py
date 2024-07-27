import json
import os

class Account():
  def __init__(self, montant, max_position):
    self.montant = montant
    self.position = 0
    self.max_position = max_position
  
  def __str__(self):
    return f'Account: {self.montant} - position: {self.position} - max_position: {self.max_position}'
  
  def get_montant(self):
    return self.montant
  
  def add_position(self, montant):
    self.position += 1
    self.montant -= montant

  def get_position(self):
    return self.position
  
  def is_max_position(self):
    return self.position >= self.max_position

def dump_json(content:dict):
    path = os.path.join(os.getcwd(), 'account.json')
    with open(path, 'w') as f:
        json.dump(content, f)

def main()->int:
  a = Account(1000, 3)
  dump_json(a.__dict__)
  return 0

if __name__ == '__main__':
  main()

