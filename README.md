# 🔐 Simple Auth System

A beginner Python exercise that simulates a login: it checks a username and password against a dictionary of users.

## How it works

1. Asks for a username and checks whether it exists in the dictionary.
2. If it does, asks for the password and compares it with the stored one.
3. Prints whether access is granted.

```
Enter Username: nur
Enter Password: hello
You got it! Access Granted.
```

## Run it

```bash
python simple-auth-system.py
```

## Note on security

This is a learning exercise for dictionaries and `if`/`else` logic, not real authentication. A real system would:

- Store **hashed** passwords (for example with `bcrypt` or `hashlib.scrypt`), never plain text
- Use `getpass` so the password isn't shown while typing
- Give the same message for a wrong username or a wrong password, so attackers can't tell which usernames exist
- Limit the number of login attempts
