import pytz


def convert_to_us_eastern(dt):
    eastern_tz = pytz.timezone('US/Eastern')
    return dt.astimezone(eastern_tz)