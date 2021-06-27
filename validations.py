#!/usr/bin/env python3

def validate_user(username, minlen):
    # assert is used in situations that are not expected, but may cause our code to misbehave.
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        # use raise to check for conditions that are expected to 
        # happen during normal execution of the code.
        raise ValueError("minlen needs to be longer than 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
