import json
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "users.json")
with open(filename, 'r') as users_file:
  USERS = json.load(users_file)

def get_user_record(by_field, search_field) -> dict:
  """
  Searches USER by a specific field and returns
  data for that user.
  """
  
  for user in USERS:
    if user[by_field] == search_field:
      return user
  raise KeyError("Cannot find user with given criteria.")

def get_user_info(by_field, search_field) -> dict:
  """
  Searches USER by a specific field and returns
  data for that user. Excludes password.
  """
  user_record = get_user_record(by_field, search_field)
  user_info = user_record.copy()
  del user_info["password"]
  return user_info

def get_user_info_by_username(username: str) -> dict:
  return get_user_info("username", username)

def get_user_info_by_user_id(user_id: int) -> dict:
  return get_user_info("user_id", user_id)

def is_valid_login(username: str, password: str) -> bool:
  try:
    user = get_user_record("username", username)
    return user["password"] == password
  except KeyError:
    return False  

def main():
  print(is_valid_login("admin", ""))

if __name__ == "__main__":
  main()