from src.backend.utils.generate import *


def test_id_generate():

    # Arrange

    result = None

    # Act

    result = id_generate()
    result2 = id_generate()

    # Assert

    assert result is not None
    assert result2 is not None
    assert result != result2


def test_get_current_date():

    # Arrange

    result = None

    #  Act

    result = get_current_date()

    year = result[0:4]
    sep1 = result[4]
    month = result[5:7]
    sep2 = result[7]
    day = result[8:10]

    # Assert

    assert result is not None
    assert isinstance(result, str)
    assert isinstance(year, str)
    assert isinstance(sep1, str)
    assert isinstance(month, str)
    assert isinstance(sep2, str)
    assert isinstance(day, str)
    assert int(year) > 2000
    assert int(month) > 0 and int(month) < 13
    assert int(day) > 0 and int(day) < 32