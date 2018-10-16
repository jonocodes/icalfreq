from django.shortcuts import render
from django.http import HttpResponse
import datetime
import logging

logger = logging.getLogger(__name__)

def _body(request):
    now = datetime.datetime.now().astimezone().strftime('%Y%m%dT%H%M%S')

    return f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//freq test ical//EN
REFRESH-INTERVAL;VALUE=DURATION:PT10M
BEGIN:VEVENT
UID:xyz
DTSTART:{now}
DTEND:{(datetime.datetime.now().astimezone()+datetime.timedelta(hours=1)).strftime('%Y%m%dT%H%M%S')}
DTSTAMP:{now}
DESCRIPTION:agent={request.META['HTTP_USER_AGENT']}
SUMMARY:Lastsync={now}
END:VEVENT
X-PUBLISHED-TTL:PT10M
X-WR-CALNAME:ical test
END:VCALENDAR
"""

def _write_log(request):
    logger.error(f"FETCH, {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S%z')}, {request.path_info}, {request.META['QUERY_STRING']}, {request.META['REMOTE_ADDR']}, {request.META['HTTP_USER_AGENT']}")

def index(request):
    return HttpResponse('visit cal or display')

def cal(request):
    _write_log(request)
    return HttpResponse(_body(request), content_type='text/calendar')

def display(request):
    _write_log(request)
    return HttpResponse(_body(request).replace('\n', '<br />\n'))

def log(request):
    file = open('django.log', 'r')
    filter = request.GET.get('filter', '')

    out = ''
    for line in file:
        if '/freq/cal' in line and filter in line:
            out += line

    return HttpResponse(out.replace('\n', '<br />\n'))
