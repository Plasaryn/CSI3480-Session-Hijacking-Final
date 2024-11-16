import jwt
from users import get_user_info_by_username
import datetime

# Module Constants
SERVER_SECRET = "G5KG6mPJbnplhdGDvg0xsp83WKa17t9zhlkUMhqsXoWbz3AibS"
SESSION_TIMEOUT = datetime.timedelta(minutes=30)

class SessionExpired(KeyError):
  def __init__(self, message:str):
    super().__init__(message)

class Session(object):
  __creation_key = object()
  __active_sessions: list["Session"] = []
  __id_ctr: int = 0

  def __init__(self, username: str, creation_key, session_timeout: datetime.timedelta) -> str:
    # Assert Public Constructor is used
    assert(creation_key == Session.__creation_key)
    
    #Define Session Attributes
    self.username: str = username
    self.session_id: int = Session.__get_next_id()

    user_info: dict = get_user_info_by_username(username)
    self.user_id: int = user_info["user_id"]
    self.user_info: dict = user_info

    # Encrypt session_id
    secret_session_id: str = jwt.encode(
      {"session_id": self.session_id},
      SERVER_SECRET,
      algorithm="HS256"
    )
    self.secret_session_id: str = secret_session_id

    # Set Expiration datetime.
    self.expiration_dt = datetime.datetime.now() + session_timeout

    # Enroll self in Session.__active_sessions
    Session.__active_sessions.append(self)

  def __get_next_id() -> int:
    Session.__id_ctr += 1
    return Session.__id_ctr

  def __retire_expired_sessions(session: "Session") -> "Session":
      if datetime.datetime.now() > session.expiration_dt:
        Session.__active_sessions.remove(session)
        return None
      else:
        return session

  def __get_session(session_id: str) -> "Session":
    for session in Session.__active_sessions:
      if session.secret_session_id == session_id:
        return_session = Session.__retire_expired_sessions(session)
        return return_session
      
  def get_session_info(session_id: str) -> dict:
    session = Session.__get_session(session_id)
    if session:
      return session.user_info
    else:
      raise SessionExpired(
        f"The Session with id {session_id} has expired"
      )

  def extend_session(session_id: str) -> None:
    session = Session.__get_session(session_id)
    if session:
      session.expiration_dt = datetime.datetime.now() + SESSION_TIMEOUT
  
  def new(username) -> str:
    return Session(
      username=username,
      creation_key = Session.__creation_key,
      session_timeout=SESSION_TIMEOUT
    )