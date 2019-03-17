# Afvalophaaldata

(English documentation is found below.)


## 1 Inleiding

In Nederland kun je met een website of app zien wanneer jouw huisvuil wordt
opgehaald. Het gebruik van een dergelijke website kan omslachtig zijn en een app
vereist rechten op je mobiele apparaat die je privacy niet kunnen waarborgen.
Mede hierdoor is ook een beweging om zo min mogelijk propriëtaire (en mogelijk
schadelijke) apps geïnstalleerd te hebben.

Dit project biedt de afvalophaaldata voor jouw adres aan die je kan toevoegen
als een online kalender op je computer of mobiel apparaat. Deze integratie – die
ook notificaties kan geven – maakt afstemming met andere afspraken makkelijker
en je hoeft geen vuilnisapp meer op je smartphone of tablet te installeren.

Op deze manier ben je altijd op de hoogte van wijzigingen in de reguliere
ophaaldagen vanjouw afval. Voorbeelden van hiervan zijn feestdagen of bepaalde
evenementen bij je in de buurt of wanneer er kerstbomen worden opgehaald.


## 2 Indruk

Om een idee te krijgen hoe afvalophaaldata in je kalender eruit ziet, staan
hieronder twee voorbeelden. De eerste is van op een mobiel apparaat en de tweede
van op een computer.

[<img alt="example mobile" src="images/example-etar-cropped.png?raw=true" width="50%" />](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-etar-cropped.png)

[![example](images/example-thunderbird-cropped.png?raw=true)](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-thunderbird-cropped.png)


## 3 Gebruik

De kalenders hier zijn in iCalendar-formaat (.ics) en zijn te gebruiken door
de volgende drie stappen te volgen:
1. Indien nodig, installeer een kalendersoftware.
2. Vind de link van de afvalophaalkalender voor jouw adres.
3. Voeg deze link toe aan je kalendersoftware.

**Waarschuwing:** Klik **niet** op links van afvalophaalkalenders! Je moet ze
alleen kopiëren naar kalendersoftware omdat er anders de volgende problemen
kunnen optreden:
* Je webbrowser probeert de link te openen maar weet niet wat er mee moet
gebeuren en geeft een foutmelding.
* De huidige kalender wordt gedownload, maar verder gebeurd er niets.
* De huidige kalender wordt eenmalig geïmporteerd, maar updates blijven uit.


### 3.1 Installeer kalendersoftware

Waarschijnlijk heb je al software geïnstalleerd om online kalenders te
gebruiken. Mocht dat niet het geval zijn, afvalophaalkalenders zijn weer te
geven met:

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
appstore. Gebruik **geen** software die alleen maar ICS-bestanden kan importeren.

Nogmaals, niet op de kalenderlink klikken, alleen maar de link als tekst
kopiëren!


### 3.2 Vind de link voor jouw adres

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
zijn te vinden. Daarna worden er kalenders voor je gemaakt voor alle huisnummers
met die postcode.


### 3.3 Voeg jouw link toe aan kalendersoftware

Nadat je jouw link hebt gekopieerd, plak deze bij in jouw kalendersoftware bij
het aanmaken van een (alleen-lezen) online netwerk- of ICS-kalender. Meestal kun
je dan ook instellen wanneer synchronisatie moet plaatsvinden zodat je
afvalophaalkalender up to date blijft. Zet deze op 24 uur want er zij niet
zoveel updates. Nogmaals, kies **niet** voor het (eenmalig) importeren van een
ICS-kalender want die zal zichzelf niet updaten.


## 4 Onderhoud

### 4.1 Postcodes en huisnummers

Nederlandse postcodes zijn te vinden op https://www.postcode.nl . Gebruik geen
huisnummers zonder een woonfuctie. Huisnummers met alleen een bestemming
bijeenkomstfunctie, industriefunctie en/of winkelfunctie worden hier niet
ondersteunt omdat die een commerciële afvalophaaldienst moeten gebruiken.


### 4.2 Notificaties in Thunderbird

In Thunderbird is een bug met notificaties voor alleen-lezen kalenders. Stem of
voeg zinvol commentaar toe voor de volgende gerelateerde bugs:
* https://bugzilla.mozilla.org/show_bug.cgi?id=375209
* https://bugzilla.mozilla.org/show_bug.cgi?id=496889
* https://bugzilla.mozilla.org/show_bug.cgi?id=702206
* https://bugzilla.mozilla.org/show_bug.cgi?id=861594

Als dit gebeurd, de workaround voor Thunderbird is om te gaan naar
`Preferences / Calendar / Reminders` en `Show missed reminders` uit te zetten.


<!--###4.3 Validatie

Kalender die zijn aangemaakt kunnen gevalideerd worden met:
* [postcode en huisnummer](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3524%2FDZ%2F172.ics)
* [postcode, huisnummer en toevoeging](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FVX%2F90-BS.ics)
* [postcode, huisnummer en notificatie](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_0700.ics)
* [postcode, huisnummer en notificatie de avond ervoor](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_2130.ics)-->


## 5 Zie ook

Zie ook de volgende online kalenders:
* https://github.com/PanderMusubi/lunar-phase-calendar
* https://github.com/PanderMusubi/dutch-holidays

Voor Androidgebruikers, zie ook de alternatieve kalenderapp Etar in de appstores [Google Play](https://play.google.com/store/apps/details?id=ws.xsoh.etar) en [F-Droid](https://f-droid.org/repository/browse/?fdid=ws.xsoh.etar).


## 6 Licentie

Deze software voor het maken van deze online kalenders met afvalophaaldata en
bijbehorende handleiding hebben een [MIT](LICENSE)-licentie en zijn mede
mogelijk gemaakt door de analytische vaardigheden van
[Hellebaard](http://hellebaard.nl).


# Garbage Collection Dates

(Nederlandse documentatie is hierboven te vinden.)


## 1 Introduction

In the Netherlands, you can use a website or app to see when your garbage will
be collected at your house. The use of such website can be time-consuming and an
app demands rights on your mobile device which cannot guarantee your privacy.
Partly because of this, there is also a movement to install as less of these
propietary (and potentially harmful) apps as possible.

This project offers garbage collection data for your address which you can add
as an online calendar on your computer or mobile device. This integration –
which also supports notifications – improves the coordination with other
appointments and you do not have to install a garbage app on your smartphone or
tablet.

In this way, you are always up to date of changes to the schedule of regular
collection days days of your garbage. Examples of this are public holidays or
events in your neighbourhood or when Christmas trees are being collected.


## 2 Impression

To get an idea how gabarge collection dates look like, below are two examples.
The first of on a mobile device and the second on a computer.

[<img alt="example mobile" src="images/example-etar-cropped.png?raw=true" width="50%" />](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-etar-cropped.png)

[![example](images/example-thunderbird-cropped.png?raw=true)](https://raw.github.com/PanderMusubi/afvalophaaldata/master/images/example-thunderbird-cropped.png)


## 3 Usage

the calendars here are in iCalendar format (.ics) and can be used by following
next three steps:
1. If needed, install calendar software.
2. Find the link for the garbage collection calendar for your address.
3. Add this link to your calendar software.

**Warning:** Do **not** click on links of your garbage collection calendar! Only
copy these to calendar software, because otherwise the following problems can
arise:
* Your web browser does not know what to with it and give an error message.
* Your calendar will be downloaded, but nothing will happen next.
* Your calendar will be imported once, but updates will not take place.

Again, do not click on a calender link, only copy the link as text!


### 3.1 Install calendar software

Probably, your have already software installed for using online calendars. If
that is not the case, garbage collection calendars can be show with:

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
app store. Do **not** use software that can only import ICS files.


### 3.2 Find the link for your address

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
will be added for you for all house numbers of that postcode.


### 3.3 Add your link to calendar software

After you have copied your link, please paste this in your calendar software
when adding a (read-only) online network or ICS calendar. Usually you can choose
how often synchronization has to be done to keep your garbage collection
calendar up to date. Set this to 24 hours, because there are not that many
updates. Again, do **not** choose the (one time) import of the ICS calender as
it will not update itself. 


## 4 Maintenance

### 4.1 Postcodes and house numbers

Dutch postcodes can be found with https://www.postcode.nl . Do not use house
numbers without a residence (*woonfunctie*) designation. House numbers with only
a designation of *bijeenkomstfunctie*, *industriefunctie* and/or *winkelfunctie*
will not be supported for garbage collection as these need to use a commercial
garbage collection service.


### 4.2 Notifications in Thunderbird

In Thunderbird is a bug with notifications for read-only calendars. Please vote
or add a useful comment for the following related bugs:
* https://bugzilla.mozilla.org/show_bug.cgi?id=375209
* https://bugzilla.mozilla.org/show_bug.cgi?id=496889
* https://bugzilla.mozilla.org/show_bug.cgi?id=702206
* https://bugzilla.mozilla.org/show_bug.cgi?id=861594

If this bug occurs, the workaround for Thunderbird is to go to
`Preferences / Calendar / Reminders` and disable `Show missed reminders`.


<!--### 4.3 Validation

Calendars that have been generated can be validated by:
* [postcode and number](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3524%2FDZ%2F172.ics)
* [postcode, number and extension](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FVX%2F90-BS.ics)
* [postcode, number and notification in the morning](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_0700.ics)
* [postcode, number and notification in the evening before](http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.github.com%2FPanderMusubi%2Fafvalophaaldata%2Fmaster%2Fics%2F3521%2FEC%2F17_2130.ics)-->


## 5 See also

Please, see also these other online calendars:
* https://github.com/PanderMusubi/lunar-phase-calendar
* https://github.com/PanderMusubi/dutch-holidays

For Android users, see also the alternative calendar app Etar from [Google Play](https://play.google.com/store/apps/details?id=ws.xsoh.etar) or [F-Droid](https://f-droid.org/repository/browse/?fdid=ws.xsoh.etar).


## 6 License

The software for making these online calendars with garbage collection dates and
accompanying manual have an [MIT](LICENSE) license and have been made possible
with the analytic skills of [Hellebaard](http://hellebaard.nl).

