Afvalophaaldata
===============

(English documentation is found below.)

Kalender met herinnering voor afvalophaaldata in Nederland


## Gebruik

De kalenders hier zijn in iCalendar of ICS-formaat. Kalendersoftware die de afvalophaaldatakalenders kunnen weergeven zijn:
* voor OS-X, Windows en Linux: [Mozilla Thunderbird](https://www.mozilla.org/thunderbird/)
* web-based and indirectly on Android too: [Google Calendar](https://google.com/calendar)
* voor alleen Android: ICSdroid in [Google Play](https://play.google.com/store/apps/details?id=at.bitfire.icsdroid) en [F-Droid](https://f-droid.org/repository/browse/?fdfilter=calendar&fdid=at.bitfire.icsdroid)
* voor alleen Android: CalDAV-Sync in [Google Play](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib) en binnenkort ook in F-Droid
* voor alleen OS-X: [Calendar](https://www.apple.com/osx/apps/#calendar)
* voor alleen iOS: [iCloud Calendar](https://www.apple.com/icloud/#ccm)
* voor alleen Windows: [Microsoft Outlook](https://products.office.com/outlook)
* web-based: [Microsoft Outlook.com](https://outlook.com)

[<img alt="example mobile" src="images/example-etar.png?raw=true" width="50%" />](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-etar.png)

De meeste kalendersoftware kan deze afvaalophaaldata weergeven in een kleur naar uw keuze. In sommige software is het ook mogelijk en een onderscheidende kleur in te stellen voor de kalendercategorie `Afvalophaal`.

[![example](images/example-thunderbird.png?raw=true)](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-thunderbird.png)

Warning: Please, do **not** import these ICS files into your calendar as they will be added only once and never get updated. Add these calendars as a shared (read-only) network calendar. These calendars do not need frequent updates, however, sometimes bugs are fixed, functionality is added or garbage collection change due to holidays or local events. Most software offer a daily update frequency, which is fine for these calendars. Syncing should also configured to take place only from server to client, computer or phone.


## Kalenders

In de map genaamd [ics](ics) zijn de kalenders te vinden. Voor elke postcode is er een bestand README.md met een overzicht van alle kalenders, inclusief bijbehorende QR-codes. Dit is de meest makkelijke manier om een specifieke kalender te vinden en toe te voegen aan kalendersoftware.

De URL's van de kalenders hebben de volgende opbouw:
1. `https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/`
2. `DDDD` (decimalen van de postcode, bijvoorbeeld `3531`)
3. `/`
4. `LL` (letters van de postcode, bijvoorbeeld `EB`)
5. `/`
6. `N` (decimalen van het huisnummer, bijvoorbeeld `2`)
7. `-EEE` (optionele toevoeging van het huisnummer, bijvoorbeeld `BSA` of `BS`)
8. `_HHMM` (optionele herinnering, `2130` avond ervoor of `0700` in de ochtend)
9. `.ics`

Aleen bovenstaande vier herinneringen zijn beschikbaar. Additionele herinneringen kunnen op verzoek via een issue worden toegevoegd.

Bovenstaande resulteert in de volgende voorbeelden:
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2.ics voor postcode `3531 EB` op huisnummer `2` zonder herinnering
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_0700.ics voor postcode `3531 EB` op huisnummer `2` met een herinnering in de ochtend om 07.00 uur
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_2130.ics voor postcode `3531 EB` op huisnummer `2` met een herinnering de avond ervoor om 21.30 uur
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BS_2130.ics voor postcode `3531 EB` op huisnummer `2` toevoeging `BS` met een herinnering de avond ervoor om 21.30 uur
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BSA_2130.ics voor postcode `3531 EB` op huisnummer `2` toevoeging `BSA` met een herinnering de avond ervoor om 21.30 uur

See the directory [ics](ics) for available calendars. If your postcode is missing, please request it via an issue but for privacy reasons list **only** your postcode and not any house numbers. Calendars will be generated for all house numbers of a requested postcode.


## Onderhoud

Kalender die zijn aangemaakt kunnen gevalideerd worden met:
* [postcode en huisnummer](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3524%2FDZ%2F172.ics)
* [postcode, huisnummer en toevoeging](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FVX%2F90-BS.ics)
* [postcode, huisnummer en herinnering](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_0700.ics)
* [postcode, huisnummer en herinnering de avond ervoor](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_2130.ics)

Om huisnummers voor een postcode toe voegen, ga naar https://www.postcode.nl/POSTCODE waar POSTCODE een Nederlandse postcode is zonder een spatie.


## Herinneringen in Thunderbird

Voor de kalender in Thunderbird, Lightning, is er een bug met herinneringen voor alleen-lezen kalenders. Stem, voeg zinvol commentaar toe, fiks of maak een donatie via [Bounty Source](https://www.bountysource.com/teams/thunderbird/issues) voor de volgende gerelateerde bugs:
* https://bugzilla.mozilla.org/show_bug.cgi?id=375209
* https://bugzilla.mozilla.org/show_bug.cgi?id=496889
* https://bugzilla.mozilla.org/show_bug.cgi?id=702206
* https://bugzilla.mozilla.org/show_bug.cgi?id=769118
* https://bugzilla.mozilla.org/show_bug.cgi?id=804009
* https://bugzilla.mozilla.org/show_bug.cgi?id=861594

De workaround voor Thunderbird is om te gaan naar Preferences / Calendar / Reminders en "Show missed reminders" uit te zetten.


## Zie ook

Zie ook:
* https://github.com/PanderMusubi/lunar-phase-calendar
* https://github.com/PanderMusubi/dutch-holidays

Voor Androidgebruikers, zie ook de alternatieve kalenderapp Etar in de appstores [Google Play](https://play.google.com/store/apps/details?id=ws.xsoh.etar) en [F-Droid](https://f-droid.org/repository/browse/?fdid=ws.xsoh.etar).


# Garbage Collection Dates

Calendar with reminders for garbage collection in the Netherlands


## Usage

The calendars provided here are in iCalendar or ICS format. Calendar software that can display these garbage collection calendars are:
* for OS-X, Windows and Linux: [Mozilla Thunderbird](https://www.mozilla.org/thunderbird/)
* web-based and indirectly on Android too: [Google Calendar](https://google.com/calendar)
* for Android only: ICSdroid from [Google Play](https://play.google.com/store/apps/details?id=at.bitfire.icsdroid) and [F-Droid](https://f-droid.org/repository/browse/?fdfilter=calendar&fdid=at.bitfire.icsdroid)
* for Android only: CalDAV-Sync from [Google Play](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib) and soon on F-Droid too
* for OS-X only: [Calendar](https://www.apple.com/osx/apps/#calendar)
* for iOS only: [iCloud Calendar](https://www.apple.com/icloud/#ccm)
* for Windows only: [Microsoft Outlook](https://products.office.com/outlook)
* web-based: [Microsoft Outlook.com](https://outlook.com)

[<img alt="example mobile" src="images/example-etar.png?raw=true" width="50%" />](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-etar.png)

Most calendar software can show these garbage collection days to a color of your choice. Also in some software, a distinction in color can be configured according to the calendar category `Afvalophaal`.

[![example](images/example-thunderbird.png?raw=true)](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-thunderbird.png)

Warning: Please, do **not** import these ICS files into your calendar as they will be added only once and never get updated. Add these calendars as a shared (read-only) network calendar. These calendars do not need frequent updates, however, sometimes bugs are fixed, functionality is added or garbage collection change due to holidays or local events. Most software offer a daily update frequency, which is fine for these calendars. Syncing should also configured to take place only from server to client, computer or phone.


## Calendars

In de map genaamd [ics](ics) zijn de kalenders te vinden. Voor elke postcode is er een bestand README.md met een overzicht van alle kalenders, inclusief bijbehorende QR-codes. Dit is de meest makkelijke manier om een specifieke kalender te vinden en toe te voegen aan kalendersoftware.

The urls to the calendars have the following structure:
1. `https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/`
2. `DDDD` (decimals from postcode, e.g. `3531`)
3. `/`
4. `LL` (letters from postcode, e.g. `EB`)
5. `/`
6. `N` (decimals from house number, e.g. `2`)
7. `-EEE` (optional extension to house number, e.g. `BSA` or `BS`)
8. `_HHMM` (optional reminder, `2130` evening before or `0700` for morning)
9. `.ics`

Note that only four reminders are available. Additional reminders can be requested via an issue.

The above results in the following examples:
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2.ics for postcode 3531 EB at house number 2 without a reminder
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_0700.ics for postcode 3531 EB at house number 2 with a reminder in the morning at 07:00
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_2130.ics for postcode 3531 EB at house number 2 with a reminder evening before at 21:30
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BS_2130.ics for postcode 3531 EB at house number 2 extension BS with a reminder evening before at 21:30
* https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BSA_2130.ics for postcode 3531 EB at house number 2 extension BSA with a reminder evening before at 21:30

See the directory [ics](ics) for available calendars. If your postcode is missing, please request it via an issue but for privacy reasons list **only** your postcode and not any house numbers. Calendars will be generated for all house numbers of a requested postcode.


## Maintenance

Calendars that have been generated can be validated by:
* [postcode and number](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3524%2FDZ%2F172.ics)
* [postcode, number and extension](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FVX%2F90-BS.ics)
* [postcode, number and reminder in the morning](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_0700.ics)
* [postcode, number and reminder in the evening before](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_2130.ics)

Add all house numbers for a postcode via https://www.postcode.nl/POSTCODE where POSTCODE is a Dutch postcode without a space.


## Reminders in Thunderbird

For Thunderbird calender, Lightning, there is a bug with reminders for read-only calendars. Please vote, add a useful comment, fix or pledge a bounty via [Bounty Source](https://www.bountysource.com/teams/thunderbird/issues) for the following related bugs:
* https://bugzilla.mozilla.org/show_bug.cgi?id=375209
* https://bugzilla.mozilla.org/show_bug.cgi?id=496889
* https://bugzilla.mozilla.org/show_bug.cgi?id=702206
* https://bugzilla.mozilla.org/show_bug.cgi?id=769118
* https://bugzilla.mozilla.org/show_bug.cgi?id=804009
* https://bugzilla.mozilla.org/show_bug.cgi?id=861594

The workaround for Thunderbird is to go to Preferences / Calendar / Reminders and disable "Show missed reminders".


## See also

Please, see also:
* https://github.com/PanderMusubi/lunar-phase-calendar
* https://github.com/PanderMusubi/dutch-holidays

For Android users, see also the alternative calendar app Etar from [Google Play](https://play.google.com/store/apps/details?id=ws.xsoh.etar) or [F-Droid](https://f-droid.org/repository/browse/?fdid=ws.xsoh.etar).

