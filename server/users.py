import json
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "users.json")
with open(filename, 'r') as users_file:
  USERS = json.load(users_file)

def is_valid_login(username, password):
  for user in USERS:
    if user["username"] == username:
      return user["password"] == password
  return False

def main():
  print(is_valid_login("admin", ""))

if __name__ == "__main__":
  main()