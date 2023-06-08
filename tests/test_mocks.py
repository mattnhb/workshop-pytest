import pytest
from src.slow import slow_function, calls_prints_alot_n_times, does_not_call_prints_alot


@pytest.mark.mocks
def test_slow_function_mocked_api_call(mocker):
    mocker.patch(
        # expensive_api_call is from api.py but imported to slow.py
        "src.slow.expensive_api_call",
        return_value=123,
    )

    expected = 124
    actual = slow_function()
    assert expected == actual


@pytest.mark.mocks
def test_function_was_called_once(mocker):
    mocked_function = mocker.patch("src.slow.prints_alot")
    calls_prints_alot_n_times(1)
    mocked_function.assert_called_once()


@pytest.mark.mocks
def test_function_was_called_with(mocker):
    mocked_function = mocker.patch("src.slow.prints_alot")
    calls_prints_alot_n_times(1)
    mocked_function.assert_called_with("lugia")


@pytest.mark.mocks
def test_function_was_not_called(mocker):
    mocked_function = mocker.patch("src.slow.prints_alot")
    does_not_call_prints_alot()
    mocked_function.assert_not_called()
