# Afvalophaaldata

(English documentation is found below.)


## 1 Inleiding

In Nederland kun je met een website of app zien wanneer je huisvuil wordt
opgehaald. Het gebruik van een dergelijke website kan omslachtig zijn en een app
vereist rechten op je mobiele apparaat die je privacy niet kunnen waarborgen.
Mede hierdoor is ook een beweging om zo min mogelijk propriëtaire (en mogelijk
schadelijke) apps geïnstalleerd te hebben.

Dit project biedt de afvalophaaldata voor jouw adres aan die je kan toevoegen
als een online kalender op je computer of mobiel apparaat. Deze integratie – die
ook notificaties kan geven – maakt afstemming met andere afspraken makkelijker
en je hoeft geen vuilnisapp meer op je smartphone of tablet te installeren.


## 2 Indruk

Om een idee te krijgen hoe afvalophaaldata in je kalender eruit ziet, staan
hieronder twee voorbeelden. De eerste is van op een mobiel apparaat en de tweede
van op een computer.

[<img alt="example mobile" src="images/example-etar-cropped.png?raw=true" width="50%" />](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-etar-cropped.png)

[![example](images/example-thunderbird-cropped.png?raw=true)](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-thunderbird-cropped.png)


## 3 Gebruik

De kalenders hier zijn in iCalendar-formaat (.ics) en zijn te gebruiken door
de volgende drie stappen te volgen:
1. Vind de link van de afvalophaalkalender voor jouw adres.
2. Indien nodig, installeer een kalendersoftware.
3. Voeg deze link toe aan je kalendersoftware.


### 3.1 Vind de link voor jouw adres

In de map genaamd [ics](ics) zijn de kalenders te vinden. Voor elke postcode is
er een bestand README.md met een overzicht van alle kalenders. Dit is de meest
makkelijke manier om een specifieke kalender te vinden en toe te voegen aan
kalendersoftware.

De links van de kalenders hebben de volgende opbouw:
1. `https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/`
2. `DDDD/` (decimalen van de postcode, bijvoorbeeld `3531`)
3. `LL/` (letters van de postcode, bijvoorbeeld `EB`)
4. `N` (decimalen van het huisnummer, bijvoorbeeld `2`)
5. `-EEE` (optionele huisnummertoevoeging, bijvoorbeeld `BSA` of `BS`)
6. `_HHMM` (optionele notificatie, `_2130` avond ervoor, `_0700` in de ochtend)
7. `.ics`

Alleen bovenstaande twee specifieke notificaties zijn beschikbaar. Voorbeelden
van links zijn:
* voor postcode `3531 EB` op huisnummer `2` zonder notificatie<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2.ics`
* voor postcode `3531 EB` op huisnummer `2` met een notificatie in de ochtend om 07.00<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_0700.ics`
* voor postcode `3531 EB` op huisnummer `2` met een notificatie de avond ervoor om 21.30<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_2130.ics`
* voor postcode `3531 EB` op huisnummer `2` toevoeging `BS` met een notificatie de avond ervoor om 21.30<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BS_2130.ics`
* voor postcode `3531 EB` op huisnummer `2` toevoeging `BSA` met een notificatie de avond ervoor om 21.30<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BSA_2130.ics`

Als je postcode er niet bijstaat, dien een verzoek in via een
[issue](https://github.com/PanderMusubi/afvalophaaldata/issues) maar om
privacyredenen, noem alleen je postcode en **niet** je huisnummer. Indien
mogelijk, voeg ook de website toe van de organisatie waar jouw afvalophaaldata
zijn te vinden. Daarn worden er kalender gemaakt voor alle huisnummers met die
postcode.


### 3.2 Installeer kalendersoftware

Afvalophaalkalenders zijn weer te geven met:

| Naam              | Android | iOS | macOS | Windows | Linux | Webinterface |
|-------------------|:-------:|:---:|:-----:|:-------:|:-----:|:------------:|
| Google Calendar   | [✔](https://play.google.com/store/apps/details?id=com.google.android.calendar) | - | - | - | - | [✔](https://google.com/calendar) |
| ICSx⁵             | [✔](https://play.google.com/store/apps/details?id=at.bitfire.icsdroid) | - | - | - | - | - |
| CalDAV-Sync       | [✔](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib) | - | - | - | - | - |
| iCloud Calendar   | - | [✔](https://www.apple.com/icloud/#ccm) | - | - | - | - |
| Thunderbird       | - | - | [✔](https://www.thunderbird.net) | [✔](https://www.thunderbird.net) | [✔](https://www.thunderbird.net) | - |
| Apple Calendar    | - | - | [✔](https://www.apple.com/macos/what-is) | - | - | - |
| Microsoft Outlook | - | - | - | [✔](https://products.office.com/outlook) | - | [✔](https://outlook.com) |

De vinkjes in de tabel hebben een link naar de software. ICSx⁵ is ook te vinden
in de [F-Droid](https://f-droid.org/repository/browse/?fdfilter=calendar&fdid=at.bitfire.icsdroid)
appstore. Gebruik **geen** software die alleen maar ICS-bestanden kan importeren of
exporteren.


### 3.3 Voeg jouw link toe aan kalendersoftware



De meeste kalendersoftware kan deze afvaalophaaldata weergeven in een kleur naar uw keuze. In sommige software is het ook mogelijk en een onderscheidende kleur in te stellen voor de kalendercategorie `Afvalophaal`.

Warning: Please, do **not** import these ICS files into your calendar as they will be added only once and never get updated. Add these calendars as a shared (read-only) network calendar. These calendars do not need frequent updates, however, sometimes bugs are fixed, functionality is added or garbage collection change due to holidays or local events. Most software offer a daily update frequency, which is fine for these calendars. Syncing should also configured to take place only from server to client, computer or phone.


## 4 Onderhoud

### 4.1

<!--Kalender die zijn aangemaakt kunnen gevalideerd worden met:
* [postcode en huisnummer](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3524%2FDZ%2F172.ics)
* [postcode, huisnummer en toevoeging](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FVX%2F90-BS.ics)
* [postcode, huisnummer en notificatie](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_0700.ics)
* [postcode, huisnummer en notificatie de avond ervoor](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_2130.ics)-->

Om huisnummers voor een postcode toe voegen, ga naar https://www.postcode.nl/POSTCODE waar POSTCODE een Nederlandse postcode is zonder een spatie.


### 4.2 Notificaties in Thunderbird

Voor de kalender in Thunderbird, Lightning, is er een bug met notificaties voor alleen-lezen kalenders. Stem, voeg zinvol commentaar toe, fiks of maak een donatie via [Bounty Source](https://www.bountysource.com/teams/thunderbird/issues) voor de volgende gerelateerde bugs:
* https://bugzilla.mozilla.org/show_bug.cgi?id=375209
* https://bugzilla.mozilla.org/show_bug.cgi?id=496889
* https://bugzilla.mozilla.org/show_bug.cgi?id=702206
* https://bugzilla.mozilla.org/show_bug.cgi?id=861594

De workaround voor Thunderbird is om te gaan naar Preferences / Calendar / Reminders en "Show missed reminders" uit te zetten.


## 5 Zie ook

Zie ook:
* https://github.com/PanderMusubi/lunar-phase-calendar
* https://github.com/PanderMusubi/dutch-holidays

Voor Androidgebruikers, zie ook de alternatieve kalenderapp Etar in de appstores [Google Play](https://play.google.com/store/apps/details?id=ws.xsoh.etar) en [F-Droid](https://f-droid.org/repository/browse/?fdid=ws.xsoh.etar).


# Garbage Collection Dates

(Nederlandse documentatie is hierboven te vinden.)


## 1 Introduction

In the Netherlands, you can use a website or app to see when your garbage will
be collected at your house. The use of such website can be time-consuming and an
app demands rights on your mobile device which cannot guarantee your privacy.
Partly because of this, there is also a movement to install as less of these
propietary (and potentially harmful) apps as possible.

This project offers garbage collection data for jour address which you can add
as an online calendar on your computer or mobile device. This integration –
which also supports notifications – improves the coordination with other
appointments and you do not have to install a garbage app on your smartphone or
tablet.


## 2 Impression

To get an idea how gabarge collection dates look like, below are two examples.
The first of on a mobile device and the second on a computer.

[<img alt="example mobile" src="images/example-etar-cropped.png?raw=true" width="50%" />](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-etar-cropped.png)

[![example](images/example-thunderbird-cropped.png?raw=true)](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-thunderbird-cropped.png)


## 3 Usage

the calendars here are in iCalendar format (.ics) and can be used by following
next three steps:
1. Find the link for the garbage collection calendar for your address.
2. If needed, install calendar software.
3. Add this link to your calendar software.


### 3.1 Find the link for your address

See the directory [ics](ics) for available calendars. For every postcode, there
is a file called README.md with an overview of the calendars for that postcode.
This is the moest easy way to find your calendar.

The links to the calendars have the following structure:
1. `https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/`
2. `DDDD/` (decimals from postcode, e.g. `3531`)
3. `LL/` (letters from postcode, e.g. `EB`)
4. `N` (decimals from house number, e.g. `2`)
5. `-EEE` (optional house number extension, e.g. `BSA` or `BS`)
6. `_HHMM` (optional notification, `2130` evening before, `0700` for morning)
7. `.ics`

Note that only two exact notifications are available. The above results in 
he following examples:
* for postcode `3531 EB` at house number `2` without a notification<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2.ics`
* for postcode `3531 EB` at house number `2` with a notification in the morning at 07:00<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_0700.ics`
* for postcode `3531 EB` at house number `2` with a notification evening before at 21:30<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2_2130.ics`
* for postcode `3531 EB` at house number `2` extension `BS` with a notification evening before at 21:30<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BS_2130.ics`
* for postcode `3531 EB` at house number `2` extension `BSA` with a notification evening before at 21:30<br />`https://raw.github.com/PanderMusubi/afvalophaaldata/master/ics/3531/EB/2-BSA_2130.ics`

If your postcode is missing, please request it via an
[issue](https://github.com/PanderMusubi/afvalophaaldata/issues) but for privacy
reasons list **only** your postcode and not any house numbers. If possible, also
add the website where your garbage collection data can be found. Then calendars
for all house numbers of that postcode will be added.


### 3.2 Install calendar software


### 3.3 Add your link to calendar software

Probably, your system already has calendar software installed. If that is not
the case, please use a calander from the list below.


#### Desktop or laptop

Garbage collection calendars can be show in:

| Name              | Android | iOS | macOS | Windows | Linux | Web interface |
|-------------------|:-------:|:---:|:-----:|:-------:|:-----:|:------------:|
| Google Calendar   | [✔](https://play.google.com/store/apps/details?id=com.google.android.calendar) | - | - | - | - | [✔](https://google.com/calendar) |
| ICSx⁵             | [✔](https://play.google.com/store/apps/details?id=at.bitfire.icsdroid) | - | - | - | - | - |
| CalDAV-Sync       | [✔](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib) | - | - | - | - | - |
| iCloud Calendar   | - | [✔](https://www.apple.com/icloud/#ccm) | - | - | - | - |
| Thunderbird       | - | - | [✔](https://www.thunderbird.net) | [✔](https://www.thunderbird.net) | [✔](https://www.thunderbird.net) | - |
| Apple Calendar    | - | - | [✔](https://www.apple.com/macos/what-is) | - | - | - |
| Microsoft Outlook | - | - | - | [✔](https://products.office.com/outlook) | - | [✔](https://outlook.com) |

Check marks in the table have links to the software. ICSx⁵ can also be found in
the [F-Droid](https://f-droid.org/repository/browse/?fdfilter=calendar&fdid=at.bitfire.icsdroid)
app store. Do **not** use software that can only import or export ICS files.


## Calendars

Most calendar
software can show the garbage collection dates in a color of your choice.
Also in some software, a distinction in color can be configured according to the
calendar category `Afvalophaal` to which all the dates belong.

Warning: Please, do **not** click on the links of these ICS files. This might
download the calendar or show it in the browser. Both will not work. Also,
importing a calendar will lead to adding dates only once and will not update
these.

Add calendars by copying the link and add them as a shared (read-only) network
calendar. These calendars do not need frequent updates, however, sometimes bugs
are fixed, functionality is added or garbage collection change due to holidays
or local events. Most software offer a daily update frequency, which is fine for
these calendars. Syncing should also configured to take place only from server
to client, computer or phone.


## 4 Maintenance

### 4.1

<!--Calendars that have been generated can be validated by:
* [postcode and number](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3524%2FDZ%2F172.ics)
* [postcode, number and extension](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FVX%2F90-BS.ics)
* [postcode, number and notification in the morning](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_0700.ics)
* [postcode, number and notification in the evening before](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_2130.ics)-->

Add all house numbers for a postcode via https://www.postcode.nl/POSTCODE where POSTCODE is a Dutch postcode without a space.

See https://postcode.nl note that often bijeenkomstfunctie, industriefunctie
and/or winkelfunctie are not supported for garbage collection as the need
to use a commercial garbage service.



### 4.2 Notifications in Thunderbird

For Thunderbird calender, Lightning, there is a bug with notifications for read-only calendars. Please vote, add a useful comment, fix or pledge a bounty via [Bounty Source](https://www.bountysource.com/teams/thunderbird/issues) for the following related bugs:
* https://bugzilla.mozilla.org/show_bug.cgi?id=375209
* https://bugzilla.mozilla.org/show_bug.cgi?id=496889
* https://bugzilla.mozilla.org/show_bug.cgi?id=702206
* https://bugzilla.mozilla.org/show_bug.cgi?id=861594

The workaround for Thunderbird is to go to Preferences / Calendar / Reminders and disable "Show missed reminders".


## 5 See also

Please, see also:
* https://github.com/PanderMusubi/lunar-phase-calendar
* https://github.com/PanderMusubi/dutch-holidays

For Android users, see also the alternative calendar app Etar from [Google Play](https://play.google.com/store/apps/details?id=ws.xsoh.etar) or [F-Droid](https://f-droid.org/repository/browse/?fdid=ws.xsoh.etar).

