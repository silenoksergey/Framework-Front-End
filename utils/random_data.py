import random
import string


def random_prompt(length: int = 8) -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))