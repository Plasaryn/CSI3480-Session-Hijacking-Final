def is_valid_login(username, password):
  return all((
    username == "admin",
    password == "1234"
  ))