def _shiftChar(ch: str, shift: int) -> str:
    # shift character by given offset
    start, end = 32, 126
    rng = end - start + 1
    code = ord(ch)
    if code < start or code > end:
        return ch
    return chr(start + ((code - start + shift) % rng))


def encryptPassword(password: str, shift: int = 5) -> str:
    # encrypt password by shifting characters forward
    return "".join(_shiftChar(c, shift) for c in password)


def decryptPassword(ciphertext: str, shift: int = 5) -> str:
    # decrypt password by shifting characters backward."""
    return "".join(_shiftChar(c, -shift) for c in ciphertext)
