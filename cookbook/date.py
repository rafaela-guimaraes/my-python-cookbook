
from datetime import datetime, date


def convert_from_date_to_datetime(dt):
    """
    Convert a date object to a datetime object

    Args:
        dt (date): Date to be converted into datetime

    Returns:
        [datetime]: Datetime object
    """
    return datetime.combine(dt, datetime.min.time())


def add_timezone_into_date(dt, timezone_name='America/Sao_Paulo'):
    """
    Add timezone info for the given datetime

    Args:
        dt (datetime): Datetime object
        timezone_name (str, optional): Timezone name. Defaults to 'America/Sao_Paulo'.
            For more options print(pytz.all_timezones)

    Returns:
        [datetime]: Datetime with timezone included
    """
    import pytz  # requirement

    timezone = pytz.timezone(timezone_name)

    return timezone.localize(dt)


def get_date_isoformat(dt, timezone='America/Sao_Paulo', mask='%Y-%m-%d %H:%M'):
    """
    Gets the iso foarmat for the given date 

    Args:
        date (string, date or datetime): A string of teh date to be converted.
        timezone (string - optional): Timezone info, Default to: 'America/Sao_Paulo'
        mask (string): A string with formating mask of the first argument
    Returns:
        [string]: isoformat of the given date
    """

    if isinstance(dt, str):
        dt = datetime.strptime(dt, mask)
    if isinstance(dt, date):
        dt = datetime.combine(dt, datetime.min.time())

    dt = add_timezone_into_date(dt)
    return dt.isoformat()


if __name__ == "__main__":
    assert get_date_isoformat(
        '2020-09-20 12:35') == '2020-09-20T00:00:00-03:00'
    assert type(convert_from_date_to_datetime(date(2020, 9, 20))) == datetime
    assert str(add_timezone_into_date(convert_from_date_to_datetime(
        date(2020, 9, 20)))) == '2020-09-20 00:00:00-03:00'
