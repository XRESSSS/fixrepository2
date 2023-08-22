import constans

data = 876
result = 243

def CONSTANTS_VALUE():
    return {
        'INCHES_IN_METER': 39.370100,
    }

def convert_meters_to_inches(meters_co_convert: int | float) -> float:
    """
    po kaify mne, ponyal?
    asdfghjkl
    """
    result = constans.CONSTANTS_METRIC['INCHES_IN_METER'] * meters_co_convert
    abs_result = abs(result)
    return abs_result


if __name__ == '__name__':
    print(f'you dayn{__file__}')
