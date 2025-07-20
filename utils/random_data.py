import random
import string

def random_prompt(length=8) -> str:
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))