from src.api import expensive_api_call


def slow_function() -> int:
    return expensive_api_call() + 1


def prints_alot(word: str) -> None:
    print(word)
    print(word)


def calls_prints_alot_n_times(number_of_times: int) -> None:
    for _ in range(number_of_times):
        prints_alot("lugia")


def does_not_call_prints_alot() -> None:
    if False:
        prints_alot("entei")
