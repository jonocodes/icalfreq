# icalfreq

This application serves a simple subscribable calendar in [iCalendar](https://icalendar.org/) format. Subscribe to the calendar with various calendar clients (Google, Outlook, etc) to see the frequency of the sync in each of those clients.

## Use

Start with:

    ./manage.py runserver 0.0.0.0:8002

Use a URL like this in your client:

http://localhost:8002/freq/cal?jono+gcal

Adding any metadata after the question mark can be helpful for logging purposes when filtering results.

Example of viewing/filtering the log:

http://localhost:8002/freq/log?filter=gcal

    FETCH, 2018-10-12 05:42:36, /freq/cal, jono+gcal, Google-Calendar-Importer
    FETCH, 2018-10-13 08:34:32, /freq/cal, jono+gcal, Google-Calendar-Importer
    FETCH, 2018-10-13 23:50:25, /freq/cal, jono+gcal, Google-Calendar-Importer
    FETCH, 2018-10-14 14:39:03, /freq/cal, jono+gcal, Google-Calendar-Importer
    FETCH, 2018-10-15 04:52:34, /freq/cal, jono+gcal, Google-Calendar-Importer
    FETCH, 2018-10-15 17:30:21, /freq/cal, jono+gcal, Google-Calendar-Importer

The log is in CSV format so you can paste it into a spreadsheet for analysis.

Example output: [sample.log](sample.log)

## Results

I ran this in October 2018 for a few days and got these preliminary data points:

* Google Calendar (user1) syncs: 25 hours, 15 hours, 15 hours, 8 hours
* Google Calendar (user2) syncs: 26 hours, 14 hours, 12 hours, 13 hours
* Desktop Apple mail: 2 days, 10 minutes (probably only syncs on use, not in background)
* iPhone Calendar: 1 minute to 3 hours (frequent but unpredictable, maybe due to mobile optimizations)
* outlook.live.com calendar: never updated
* Thunderbird/Lightning, Evolution: every 30 minutes
