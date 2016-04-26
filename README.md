afvalophaaldata
===============

Calendar with reminders for garbage collection in the Netherlands

_Kalender met herinnering voor afvalophaaldata in Nederland_



Usage
-----

The calendars provided here are in iCalendar or ICS format. Calendar software that can display these garbage collection calendars are:
* for OS-X, Windows and Linux: [Mozilla Thunderbird](https://www.mozilla.org/thunderbird/)
* web-based and indirectly on Android too: [Google Calendar](https://google.com/calendar)
* for Android only: ICSdroid from [Google Play](https://play.google.com/store/apps/details?id=at.bitfire.icsdroid) or [F-Droid](https://f-droid.org/repository/browse/?fdfilter=calendar&fdid=at.bitfire.icsdroid)
* for Android only: CalDAV-Sync from [Google Play](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib) and soon on F-Droid too
* for OS-X only: [Calendar](https://www.apple.com/osx/apps/#calendar)
* for iOS only: [iCloud Calendar](https://www.apple.com/icloud/#ccm)
* for Windows only: [Microsoft Outlook](https://products.office.com/outlook)
* web-based: [Microsoft Outlook.com](https://outlook.com)

[<img alt="example mobile" src="example-mobile.png?raw=true" width="50%" />](https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/example-mobile.png)

[![example](example.png?raw=true)](https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/example.png)

Most calendar software can show these garbage collection days to a color of your choice. Also in some software, a distinction in color can be configured according to the calendar categories `Afvalophaal`.

Warning: Please, do **not** import these ICS files into your calendar as they will be added only once and never get updated. Add these calendars as a shared (read-only) network calendar. These calendars do not need frequent updates, however, sometimes bugs are fixed, functionality is added or garbage collection change due to holidays or local events. Most software offer a daily update frequency, which is fine for these calendars. Syncing should also configured to take place only from server to client, computer or phone.


Calendars
---------

The urls to the calendars have the following structure:
1. `https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/ics/`
2. `DDDD` (decimals from postcode, e.g. `3531`)
3. `/`
4. `LL` (letters from postcode, e.g. `EB`)
5. `/`
6. `N` (house number, e.g. `2`)
7. `-EEE` (optional extension to house number, e.g. `BSA` or `BS`)
8. `_HHMM` (optional reminder, `2130` or `2215` evening before or `0700` or `0730` for morning)
9. `.ics` 

Note that only four reminders are available. Additional reminders can be requested via an issue.

The above results in the following examples:
* https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2.ics for postcode 3531 EB at house number 2 without a reminder
* https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_0700.ics for postcode 3531 EB at house number 2 with a reminder in the morning at 07:00
* https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_2215.ics for postcode 3531 EB at house number 2 with a reminder evening before at 22:15
* https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BS_2215.ics for postcode 3531 EB at house number 2 extension BS with a reminder evening before at 22:15
* https://raw.githubusercontent.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BSA_2215.ics for postcode 3531 EB at house number 2 extension BSA with a reminder evening before at 22:15

See the directory [ics](ics) for available calendars. If your postcode is missing, please request it via an issue but for privacy reasons list **only** your postcode and not any house numbers. Calendars will be generated for all house numbers of a requested postcode.


Maintenance
-----------

Calendars that have been generated can be validated by:
* [postcode and number](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.githubusercontent.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3524%2FDZ%2F172.ics)
* [postcode, number and extension](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.githubusercontent.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FVX%2F90-BS.ics)
* [postcode, number and reminder in the morning](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.githubusercontent.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_0700.ics)
* [postcode, number and reminder in the evening before](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.githubusercontent.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_2215.ics)

Add all house numbers for a postcode via https://www.postcode.nl/POSTCODE where POSTCODE is a Dutch postcode without a space.


Reminders Thunderbird
---------------------

For Thunderbird calender, Lightning, there is a bug with reminders for read-only calendars. Please vote, add a useful comment, fix or pledge a bounty via [Bounty Source](https://www.bountysource.com/teams/thunderbird/issues) for the following related bugs:
* https://bugzilla.mozilla.org/show_bug.cgi?id=375209
* https://bugzilla.mozilla.org/show_bug.cgi?id=496889
* https://bugzilla.mozilla.org/show_bug.cgi?id=702206
* https://bugzilla.mozilla.org/show_bug.cgi?id=769118
* https://bugzilla.mozilla.org/show_bug.cgi?id=804009
* https://bugzilla.mozilla.org/show_bug.cgi?id=861594
* https://bugzilla.mozilla.org/show_bug.cgi?id=948507
* https://bugzilla.mozilla.org/show_bug.cgi?id=1067134

The workaround for Thunderbird is to go to Preferences / Calendar / Reminders and disable "Show missed reminders".


See also
--------

See also https://github.com/PanderMusubi/dutch-holidays

For Android users, see also the alternative calendar app Etar from [Google Play](https://play.google.com/store/apps/details?id=ws.xsoh.etar) or [F-Droid](https://f-droid.org/repository/browse/?fdid=ws.xsoh.etar).
