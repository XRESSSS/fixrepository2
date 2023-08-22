from function import convert_meters_to_inches


def test_meter_to_inches_converter_int():
    expected_result = 39.370100
    meters = 1
    actual_result = convert_meters_to_inches(meters)
    assert actual_result == expected_result
    assert type(actual_result) == float
    assert ''


def test_meter_to_inches_converter_float():
    expected_result = 13.779535
    meters = 0.35
    actual_result = convert_meters_to_inches(meters)
    assert actual_result == expected_result
    assert type(actual_result) == int
    assert ''
