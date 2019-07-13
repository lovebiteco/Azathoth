from datetime import timedelta
from dateutil.parser import parse
from django.conf import settings
from django.utils import timezone
import datetime
import math
import pytz

import logging
logger = logging.getLogger(__name__)

epoch = datetime.datetime.utcfromtimestamp(0)

def get_default_timezone():
    # this should come from the user but is hard coded for now
    return settings.DEFAULT_TIME_ZONE

def convert_datetime_naive_string(date_string):
    try:
        from_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M")
        local_tz = pytz.timezone('Europe/London')
        return from_date.replace(tzinfo=local_tz).astimezone(local_tz)
    except:
        return None

def convert_iso_string_to_utc_datetime(iso_string):
    if iso_string is None:
        return iso_string
    d = parse(iso_string)
    return pytz.UTC.normalize(d)

def convert_iso_string_to_local_datetime(iso_string):
    if iso_string is None:
        return iso_string
    d = parse(iso_string)
    return timezone.localtime(d)

def convert_datetime_to_iso_string(datetime_with_tzinfo):
    if datetime_with_tzinfo is None:
        return None
    return datetime_with_tzinfo.isoformat()

def today_in_local_timezone():
    return timezone.localtime(timezone.now())

def today_in_utc():
    return pytz.UTC.normalize(today_in_local_timezone())

def today_in_default_timezone():
    return utc_datetime_as_default_timezone(today_in_utc())

def default_datetime_as_utc_timezone(date):
    old_timezone = pytz.timezone(get_default_timezone())
    new_timezone = pytz.timezone("UTC")
    return old_timezone.localize(date.replace(tzinfo=None)).astimezone(new_timezone)

def utc_datetime_as_default_timezone(date):
    old_timezone = pytz.timezone("UTC")
    new_timezone = pytz.timezone(get_default_timezone())
    return old_timezone.localize(date.replace(tzinfo=None)).astimezone(new_timezone)

def naive_datetime_as_default_timezone(naive_date):
    return datetime.datetime.strptime(naive_date, '%d%m%Y').replace(
        tzinfo=pytz.timezone(get_default_timezone())
    )

def get_start_of_day(day):
    start_day = datetime.datetime.combine(
        day.date(),
        day.time().min
    )
    return start_day

def get_week_start_and_end_datetimes(week_start_datetime=None):
    if not week_start_datetime:
        week_start_datetime = today_in_utc()
    start_datetime = datetime.datetime.combine(
        week_start_datetime.date(),
        week_start_datetime.time().min
    )
    next_week = week_start_datetime + timedelta(days=7)
    end_datetime = datetime.datetime.combine(next_week.date(), next_week.time().max)
    return start_datetime, end_datetime

def get_default_week_start_and_end_datetimes(week_start_datetime=None):
    if not week_start_datetime:
        week_start_datetime = utc_datetime_as_default_timezone(today_in_utc())
    return get_week_start_and_end_datetimes(week_start_datetime)

def get_day_start_and_end_datetimes(day_datetime=None):
    if not day_datetime:
        day_datetime = today_in_utc()
    start_datetime = datetime.datetime.combine(
        day_datetime.date(), day_datetime.time().min
    )
    end_datetime = datetime.datetime.combine(
        day_datetime.date(), day_datetime.time().max
    )
    return start_datetime, end_datetime

def get_default_day_start_and_end_datetimes(day_datetime=None):
    if not day_datetime:
        day_datetime = utc_datetime_as_default_timezone(today_in_utc())
    return get_day_start_and_end_datetimes(day_datetime)

def get_utc_start_and_end_datetimes_for_default_datetime(date):
    start_day, end_day = get_default_day_start_and_end_datetimes(date)
    utc_start_day = default_datetime_as_utc_timezone(start_day)
    utc_end_day = default_datetime_as_utc_timezone(end_day)
    return utc_start_day, utc_end_day

def human_time(*args, **kwargs):
    secs = float(datetime.timedelta(*args, **kwargs).total_seconds())
    units = [("", 3600)]
    parts = []
    for unit, mul in units:
        if secs / mul >= 1 or mul == 1:
            if mul > 1:
                n = int(math.floor(secs / mul))
                secs -= n * mul
            else:
                n = secs if secs != int(secs) else int(secs)
            parts.append("%s %s%s" % (n, unit, "" if n == 1 else ""))
    return ", ".join(parts)

def unix_time_millis(dt):
    dt = dt.replace(tzinfo=pytz.UTC)
    epoch_aware = epoch.replace(tzinfo=pytz.UTC)
    return (dt - epoch_aware).total_seconds() * 1000.0