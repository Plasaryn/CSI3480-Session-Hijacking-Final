# How To Use
Users can be added to `.\server\users.json`.

`python .\server\main.py` to launch the web server.

Default host:port is `localhost:8000`

# Security Disclaimer
This is a student project developed for the purpose of demonstrating [Session Token Hijacking](https://owasp.org/www-community/attacks/Session_hijacking_attack).
As is, passwords are stored in plain text, which is unsecure. 
The session encryption key has also been posted to this repository's history, it is highly recommended to use more secure methods to store server-side secrets.

Programs are available "As-Is".
