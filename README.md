<a name="readme-top"></a>

[![Version 1.0][Version_1.0]][Version_1.0-url]
[![License][License]][License-url]

# Music Identifier

This programme offers a way for recognising different songs via a user interface.

This software receives small music excerpts and compares them with songs and music pices from the database. The aim is to identify the excerpt.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Beschreibung

The programme includes the following basic implementations:
* Music tracks are to be learnt in the web UI
* Music tracks are to be identified in the web UI
* Uploaded music tracks can be played in the browser

The programme also includes the following extensions:
* Link to identified piece of music on Spotify/Youtube
* Determine metadata for music tracks (artist, album, etc.)
* Determine and display album cover of the music track with DuckDuckGo search API
* plotting the waveform of the piece of music
* Benchmarking of the application (duration of learning and identification)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## First steps

### Dependencies

#### Programming language

&emsp;[![Python 3.12.0][Python]][Python-url] 

#### Main libraries

&emsp;[![Streamlit][Streamlit]][Streamlit-url]  
&emsp;[![NumPy][NumPy]][NumPy-url]  
&emsp;[![pandas][pandas]][pandas-url]

*(for more details see* [requirements.txt](requirements.txt) *)*

#### Version control

&emsp;[![Git][Git]][Git-url]  
&emsp;[![GitHub][GitHub]][GitHub-url]  

#### Operating systems

&emsp;[![Windows 10][Windows_10]][Windows_10-url]
&emsp;[![Windows 11][Windows_11]][Windows_11-url]

#### Programming environment

&emsp;[![Visual Studio Code][VS_Code]][VS_Code-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Initialisation

As this programme is only a mockup, the corresponding programming environment must first be downloaded.
* Download and install [Python 3.12.0](https://www.python.org/downloads/windows/)
* Download and install [Visual Studio Code](https://code.visualstudio.com)
*  Download the current version of the project from [GitHub](https://github.com/CuzImKaviar/music_identifier)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Run programme

* Setting up a virtual Pythen environment in VS Code with  
```python -m venv .venv```
* Activate the virtual Pythen environment with  
```.venv\Scripts\activate```
* Install all required libraries with  
```pip install -r requirements.txt```
* Execute the programme with  
```streamlit run music_identifier.py```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Close programme

* Exit the programme with the following key combination in the terminal    
```Strg + C ``` bzw. ```Ctrl + C ```
* Exit the virtual Pythen environment with    
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
    * added functionality 
* v0.1
    * setup
    * see [Commits](github.com/CuzImKaviar/Case_Study/commits/main/) for more details

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Licence

This project is licensed under the "Educational Community License, Version 2.0" license - see [LICENSE.md](LICENSE.md) for more details

[![Educational Community License, Version 2.0][ECL_V2]][ECL_V2-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Referenzen

Inspiration, code snippets, etc.
* [A simple README.md template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)

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
