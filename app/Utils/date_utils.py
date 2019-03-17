from dateutil.parser import parse


def try_parse_date(string):
    if not isinstance(string, str):
        return False
    try:
        return parse(string)
    except ValueError:
        return False
