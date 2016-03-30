# afvalophaaldata
Kalender met afvalophaaldata in Nederland voor postcode en huisnummer


Usage
-----

The calendars provided here are in iCalendar or ICS format. Calendar software that can display these garbage collection calendars are:
* for OS-X, Windows and Linux: [Mozilla Thunderbird](https://www.mozilla.org/thunderbird/)
* web-based and indirectly on Android too: [Google Calendar](https://google.com/calendar)
* for Android only: ICSdroid from [Google Play](https://play.google.com/store/apps/details?id=at.bitfire.icsdroid) or [F-Droid](https://f-droid.org/repository/browse/?fdfilter=calendar&fdid=at.bitfire.icsdroid)
* for OS-X only: [Calendar](https://www.apple.com/osx/apps/#calendar)
* for iOS only: [iCloud Calendar](https://www.apple.com/icloud/#ccm)
* for Windows only: [Microsoft Outlook](https://products.office.com/outlook)
* web-based: [Microsoft Outlook.com](https://outlook.com)

[![example](example.png?raw=true)](https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/example.png)

Most calendar software can show these garbage collection days to a color of your choice. Also in some software, a distinction in colour can be configured according to the calendar categories `Afvalophaal`.

Warning: Please, do **not** import these ICS files into your calendar as they will be added only once and never get updated. Add these calendars as a shared (read-only) network calendar. These calendars do not need frequent updates, however, sometimes bugs are fixed, functionality is added or garbage collection change due to holidays or local events. Most software offer a daily update frequency, which is fine for these calendars. Syncing should also configured to take place only from server to client, computer or phone.


Maintenance
-----------

Calendars that have been generated can be validated by:
* http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.githubusercontent.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2F3521VX-90-BS.ics
* http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.githubusercontent.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2F3524DZ-172.ics

Add all house numbers for a postcode via https://www.postcode.nl/POSTCODE where POSTCODE is a Dutch postcode without a space.


See also
--------

See also https://github.com/PanderMusubi/dutch-holidays
