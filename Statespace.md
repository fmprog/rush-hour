State space

Opdracht 1
Een student heeft 12 verschillende vakken van 2 uur welke geroosterd moeten worden van maandag t/m vrijdag in tijdsloten 9-11, 11-13, 13-15, 15-17. Hoeveel verschillende roosters zijn er mogelijk voor deze student zonder overlap van vakken?

* n = 20 omdat er 4 x 5 = 20 tijdsloten zijn en r = 12 (vakken).
* Order does not matter & repetition does not matter 
* => n! / (r!(n-r)!) = 20! / (12!8!) = 125970 verschillende roosters mogelijk.

Opdracht 2
Je fietst door Manhattan, New York en kunt bij elk kruispunt linksaf, rechtsaf of rechtdoor. Hoeveel verschillende routes kun je rijden vanaf een gegeven beginpunt en richting met daarin 20 kruispunten?

* Repetition matters & order matters.
* 3 opties voor een route met 20 kruispunten dus n= 3 en r = 20.
* => 3^20 = 3486784401 verschillende routes.

Opdracht 3
Er moeten 50 dozen met flesjes water, 50 dozen fruit, en 30 dozen broodjes worden vervoerd. In de bestelbus passen 25 dozen. Hoeveel verschillende ladingen kun je in de eerste rijtje meenemen als je een volle lading meeneemt?

* Er zijn 3 opties en 25 plekken, dus n = 3 en r = 25.
* Order does not matter & repetition does matter.
* => (r+n-1)! / (r!(n-1)!) = 27!/(2*25!) = 351 verschillende ladingen.

Opdracht 4
Om af te studeren moet een student 30 vakken hebben afgerond, maar een student mag er ook meer doen. Een student kan daarbij kiezen uit 110 verschillende aangeboden vakken. Op hoeveel verschillende manieren kan een student afstuderen met 30, 31 of 32 vakken?

* n=110 opties en r1= 30, r2 = 31 en r3 = 32
* Order does not matter & repetition does not matter.
* 
* => n! / (r!(n-r)!) => n! / (r1!(n-r1)!) + n! / (r2!(n-r2)!) + n! / (r3!(n-r3)!) 
* = 110!/(30!80!) + 110!/(31!79!) + 110!/(32!78!) 
* =  8.3662309e+26 + 2.1590273e+27 + 5.3300987e+27 verschillende manieren.

Opdracht 5
Een loterij heeft balletjes A t/m Z waaruit een notaris op volgorde 7 willekeurige balletjes trekt zonder terugleggen. Wat is de kans dat het lot met DBFAECG wint?

* Er zijn 26 opties en er worden 7 balletjes getrokken, dus n = 26 en r = 7.
* The order matters & repetition does not matter.
* n! / (n-r!) = 26! / 19! = 3315312000
* De kans dat het lot met DBFAECG wint = 1 /  3315312000 = 3.0163074e-10

Opdracht 6
Opnieuw moeten 50 dozen met flesjes water, 50 dozen fruit, en 30 dozen broodjes worden vervoerd. Je hebt nu een vrachtwagen waarin 45 dozen passen. Hoeveel verschillende ladingen kun je nu in de eerste ritje meenemen als je een volle lading meeneemt?

* …

Opdracht 7
Geef (de bovengrens van) de grootte van de state-space van de gekozen case.
Welke case heb je gekozen?
* Rush Hour
Welke variabelen zijn er in de case?
* breedte veld
* aantal auto's
* grootte auto
* positie auto (x, y)
* positie exit
* start posities
Beschrijf de eventuele versimpelende aannames die je maakt en waarom de werkelijke state-space grootte hier dan gegarandeerd nooit boven ligt.
* We zullen een aanname maken over het maximale aantal auto's op de grid.
* We nemen aan dat de maximale grid grootte 12x12 = 144 is en we nemen aan dat ons speelveld vierkant is.
* De minimale auto lengte = 2 dus daarom zal het maximale aantal autos 72 zijn als het bord volledig gevuld is. we nemen daarom aan dat het max aantal auto's gelijk is aan:
* (breedte veld^2 / 2) - 2.
Geef de formule voor de berekening van (de bovengrens van) de grootte van de state-space van je case.
* Order matters and repetition matters
* Dus de formule voor de berekening van de bovengrens van de grootte van de state-space is n^r.
* r = aantal keuzes = 70
* n = mogelijkheden  = 2
* auto's^2 =70^2
Laat in een klein voorbeeld zien dat de formule klopt:
cid:F31177DC-411D-4ADD-B683-CC51E7A397A8![image](https://user-images.githubusercontent.com/90259648/149357869-af0a58df-e510-4051-bcde-d9a2c8d491c5.png)
In dit voorbeeld kijken we naar een grid van 3x3 met daarin 3 auto's. Deze voertuigen zijn allemaal horizontaal geplaatst.

Bereken de grootte van de state-space voor één of meer van de probleem-instanties in de case.

