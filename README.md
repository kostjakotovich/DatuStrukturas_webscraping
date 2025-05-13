# Noslēguma projekts datu struktūrās


## Projekta apraksts

Noslēguma darba uzdevums ir izveidot ērtu risinājumu nepieciešamo vakanču meklēšanai Latvijas tīmekļa vietnē “visidarbi.lv” (“https://www.visidarbi.lv”). 
Projekta mērķis ir atvieglot meklēšanas procesu un nodrošināt iespēju atlasīt atbilstošus sludinājumus, pamatojoties uz lietotāja definētiem kritērijiem. 

Ir plānotas vairākas funkcijas:
- Meklēt pēc vietnes iekšējiem parametriem: 
    - vēlamā vakance, 
    - atrašanas vieta, 
    - atslēgas vārdi (piem.: sql html).
- Meklēšana pēc lietotāja parametriem, stingra meklēšana pēc amata nosaukuma, šajā piemērā tiek izmantota, lai meklētu pēc pieredzes līmeņa (piemēram: “junior”, “middle”, “senior”).
- Visa vakanču saraksta izvadīšana pēc norādītajiem parametriem
- Vakanšu saraksta sakārtošana pēc ienākumiem
- Konsoles dzēšana pirms pēdējās izvades
- Izvēlne ērtai navigācijai
- Un izeja, lai apturētu programmu

Programmas izstrādei tiek izmantots Visual Studio kods (1.100) un Python programmēšanas valoda (3.13.3).

## Šajā projektā tika izmantotas sēkojošas Python bibliotēkas:

Šajā projektā tiek izmantotas dažādas bibliotēkas, un katra no tām palīdz veikt konkrētu uzdevumu:
- BeautifulSoup - bibliotēka HTML un XML dokumentu parsēšanai Python valodā. Tā nodrošina vienkāršu un ērtu veidu, kā iegūt datus no tīmekļa lapām (piemēram, amatu nosaukumus, uzņēmumu nosaukumus, algas) no tīmekļa lapas struktūras.
- requests - tiek izmantots, lai nosūtītu HTTP pieprasījumus uz "visidarbi.lv" vietni un iegūtu HTML saturu (lapas kodu), piemēram, lai iegūtu visas vakances.
- time - moduli darbam ar laiku Python valodā. To izmanto, lai iestatītu pauzes starp meklēšanas darbībām (piemēram, pirms datu atjaunināšanas), tas nav obligāts, bet pievienots ērtības dēļ.
- urllib.parse - tiek izmantots URL kodēšanai, lai tīmekļa adresēs droši iekļautu meklēšanas parametrus. Šajā projektā tas tiek izmantots, lai apkopotu URL, pamatojoties uz vietnes iekšējiem parametriem.
- os - operētājsistēmas operācijām, piemēram, console clear atkarībā no operētājsistēmas (cls operētājsistēmai Windows, clear operētājsistēmai Unix).

- Bibliotēku instalēšanai:
pip install requests
pip install beautifulsoup4

## Izmanotās datu struktūras:

Projektā izmantotās datu struktūras:
- list - izmanto, lai uzglabātu pēc norādītajiem parametriem filtrēto vakanču sarakstu (piemēram, mainīgajā all_vacances), kurā katra vakance ir attēlota kā saraksta vienība.

- vārdnīca - izmanto, lai uzglabātu vietnes un lietotāja iekšējos filtrus (piemēram, mainīgajos website_filters un personal_filters), kur atslēgas ir parametru nosaukumi, bet vērtības ir lietotāja ievadītie atbilstošie dati.

- set - izmanto, lai uzglabātu visu vakanču saites (mainīgais seen_links), kas ļauj ātri pārbaudīt, vai konkrētā vakance jau ir apstrādāta, lai izvairītos no dublēšanās, tādējādi atrodot pēdējo lapu.

## Izstrādes metodes un soļi:

Projekta sākumā tika definēts mērķis un galvenās funkcijas. Tālāk pa soļiem tika veidoti moduļi: 
datu iegūšana (web scraping), lietotāja ievade, datu filtrēšana, šķirošana utt. 
Kods tika rakstīts un palaists Visual Studio Code vidē, izmantojot Python programmēšanas valodu.
 
Vakances tika kārtotas pēc atalgojuma, izmantojot Merge Sort algoritmu, kas nodrošina optimizētu šķirošanas veiktspēju ar laika sarežģītību O(n log n).

Turklāt programmā tika izmantots atslēgvārdu vārdnīca, kas ļauj atpazīt amatu līmeņus ne tikai angļu valodā (piemēram, Junior, Mid, Senior), bet arī latviešu valodā (piemēram, Jaunākais, Vidējais, Vecākais). Tas uzlabo meklēšanas precizitāti.

## Programmatūras izmantošanas metodes

Šajā sadaļā aprakstīts, kā gala lietotājs izmanto programmu:
- Programma tiek palaista terminālī (komandrindā).
- Lietotājs tiek aicināts ievadīt meklēšanas kritērijus: amatu, pilsētu un atslēgvārdus.
- Ir iespēja papildus filtrēt vakances pēc pieredzes līmeņa.
- Lietotājs var izvēlēties darbību no izvēlnes (piemēram, meklēt, rādīt rezultātus, kārtot pēc algas utt.).
- Rezultāti tiek parādīti konsolē, ieskaitot uzņēmuma nosaukumu, vakances nosaukumu, algu un saiti uz atbilstošo vakanci.
- Lietotājs var atkārtoti mainīt meklēšanas parametrus 
- Var iziet no programmas.

## Izmantotie rīki:
Izstrādājot šo projektu, problēmu risināšanai tika izmantoti vairāki avoti:
- YouTube palīgmateriāls: "Web Scraping with Python - Beautiful Soup Crash Course" ("https://www.youtube.com/watch?v=XVv6mJpFOb0"), autors "freeCodeCamp.org".
- Python dokumentācijas ("https://docs.python.org/3/library/os.html")
- BeautifulSoup4 dokumentācija ("https://pypi.org/project/beautifulsoup4/")
- ChatGPT - izmantots problēmu risināšanai, vakanču atlasei no visām lapām.
