<a name="readme-top"></a>

[![Version 1.0][Version_1.0]][Version_1.0-url]
[![License][License]][License-url]

# Musik Identifizierung

Dieses Endprojekt stellt ein Userinterface mit der Sotware zur Erkennung von Musik dar.

Diese Software soll kleine Musikausschnitte entgegennehmen und diese mit Musikstücken aus der Datenbank vergleichen. Damit soll der Ausschnitt identifiziert werden.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Beschreibung

Das Endgültige Programm soll folgende Umstände berücksichtigen:
* Im Web-UI sollen Musikstücke eingelernt werden
* Im Web-UI sollen Musikstücke identifiziert werden
* Hochgeladenes Musikstück kann im Browser wiedergegeben werden

Erweiterungen:
* Aufzeichnung über Mikrofon
* Input über YouTube-Link
* Link zu identifiziertem Musikstück auf Spotify/Youtube
* Meta-Daten zu Musikstücken (Interpret, Album, etc.) bestimmen
* Albumcover des Musikstückes mit DuckDuckGo Such-API bestimmen und anzeigen
* Bestimmung & Visualisierung der beats-per-minute des Musikstückes
* History der letzten identifizierten Musikstücke
* Visualisierung der Datenbank, Fingerprints, Histogramm der Matches, Waveform des Musikstückes plotten, etc.
* Benchmarking der Anwendung (Dauer des einlernens und identifizierens)
* Deployment auf Oracle Cloud Free Tier Server

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Erste Schritte

### Abhängigkeiten

#### Programmiersprache

&emsp;[![Python 3.12.0][Python]][Python-url] 

#### Wichtigste Bibliotheken

&emsp;[![Streamlit][Streamlit]][Streamlit-url]  
&emsp;[![NumPy][NumPy]][NumPy-url]  
&emsp;[![pandas][pandas]][pandas-url]

*(für genauere Informationen siehe* [requirements.txt](requirements.txt) *)*

#### Versionsverwaltung

&emsp;[![Git][Git]][Git-url]  
&emsp;[![GitHub][GitHub]][GitHub-url]  

#### Betriebssysteme

&emsp;[![Windows 10][Windows_10]][Windows_10-url]
&emsp;[![Windows 11][Windows_11]][Windows_11-url]

#### Programmierumgebung

&emsp;[![Visual Studio Code][VS_Code]][VS_Code-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Initialisierung

Da es sich bei diesem Programm nur um ein Mockup handelt, muss die Entsprechende Programmierumgebung erst herunterlgeladen werden.
* Herunterladen und Instalieren von [Python 3.12.0](https://www.python.org/downloads/windows/)
* Herunterladen und Instalieren von [Visual Studio Code](https://code.visualstudio.com)
* Herunterladen der aktuellen Version des Projekts von [GitHub](https://github.com/CuzImKaviar/music_identifier)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Programm Ausführen

* Einrichten einer Virtuellen Pythen-Umgebung in VS Code mit  
```python -m venv .venv```
* Aktivieren der Virtuellen Pythen-Umgebung mit  
```.venv\Scripts\activate```
* Instalieren aller benötigten Biblioteken mit  
```pip install -r requirements.txt```
* Ausführen des Programms mit  
```streamlit run music_identifier.py```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Programm Schließen

* Beenden des Programs durch folgende Tastenkombination    
```Strg + C ``` bzw. ```Ctrl + C ```
* Beenden der virtuelle Pythen-Umgebung mit    
```deactivate ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Authors

Contributors names and contact info

* Sebastian Bachlechner    
&emsp;Email: <s.bachlechner@mci4me.at>
* Noel Hack    
&emsp;Email: <n.hack@mci4me.at>
* Tobias Stummer    
&emsp;Email: <t.stummer@mci4me.at>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Version History

* v1.0
    * Funktionalität hinzugefügt
* v0.1
    * Setup
    * Siehe [Commits](github.com/CuzImKaviar/Case_Study/commits/main/) für mehr Details

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Lizenz

Dieses Projekt ist lizenziert unter der "Educational Community License, Version 2.0" - siehe [LICENSE.md](LICENSE.md) für mehr Details

[![Educational Community License, Version 2.0][ECL_V2]][ECL_V2-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Referenzen

Inspiration, code snippets, etc.
* [A simple README.md template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
* [Streamlit-Income-Expense-Tracker](https://github.com/Sven-Bo/streamlit-income-expense-tracker)
* [Streamlit Switch Page](https://github.com/streamlit/streamlit/issues/4832#issuecomment-1201938174)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Version_1.0]: https://img.shields.io/badge/version-v1.0-blue
[Version_1.0-url]: https://github.com/CuzImKaviar/Case_Study/commits/main/
[License]: https://img.shields.io/badge/license-Educational%20Community%20License,%20Version%202.0-3DA639
[License-url]: https://opensource.org/license/ecl-2-0/
[Python]: https://img.shields.io/badge/python_3.12.0-FFD43B?style=for-the-badge&logo=python&logoColor=306998
[Python-url]: https://www.python.org
[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=FFFFFF
[Streamlit-url]: https://streamlit.io
[NumPy]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=FFFFFF
[NumPy-url]: https://numpy.org
[pandas]: https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=FFFFFF
[pandas-url]: https://pandas.pydata.org
[Git]: https://img.shields.io/badge/git-F1502F.svg?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com
[GitHub]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com
[Windows_10]: https://img.shields.io/badge/Windows%2010-357EC7?style=for-the-badge&logo=windows10
[Windows_10-url]: https://www.microsoft.com/de-de/software-download/windows10%20
[Windows_11]: https://img.shields.io/badge/Windows%2011-357EC7?style=for-the-badge&logo=windows11
[Windows_11-url]: https://www.microsoft.com/de-de/software-download/windows11
[VS_Code]: https://img.shields.io/badge/Visual%20Studio%20Code-444444?style=for-the-badge&logo=visualstudiocode&logoColor=007ACC
[VS_Code-url]: https://code.visualstudio.com
[ECL_V2]: https://img.shields.io/badge/Educational%20Community%20License,%20Version%202.0-414042?style=for-the-badge&logo=opensourceinitiative&logoColor=3DA639
[ECL_V2-url]: https://opensource.org/license/ecl-2-0/
