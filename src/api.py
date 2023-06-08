import time


def expensive_api_call() -> int:
    time.sleep(1000)
    return 123
