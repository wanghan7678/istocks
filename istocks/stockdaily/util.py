from datetime import datetime

default_null_value = 0
ak_date_format = "yyyy-mm-dd"


def to_ak_hk_code(code):
    ln = len(code)
    if ln == 4:
        return '0' + code
    elif ln == 3:
        return '00' + code
    elif ln == 2:
        return '000' + code
    elif ln == 1:
        return '0000' + code
    else:
        return code


def to_float(input_str):
    if input_str is None:
        return default_null_value
    try:
        return float(input_str)
    except ValueError:
        return default_null_value


def to_int(input_str):
    if input_str is None:
        return default_null_value
    try:
        return int(input_str)
    except ValueError:
        return default_null_value


def to_date(date_str, date_format):
    return datetime.strptime(date_str, date_format)

