<a name="readme-top"></a>

[![Version 1.0][Version_1.0]][Version_1.0-url]    
[![License][License]][License-url]
[![Code of Conduct][Code_of_Conduct]][Code_of_Conduct-url]

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

## Code of Conduct

This project runs under the "Contributor Covenant, Version 2.1" code of conduct - see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for more details

[![Contributor Covenant Code of Conduct, Version 2.1][CC_V2]][CC_V2-url]

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
[Version_1.0-url]: https://github.com/CuzImKaviar/music_identifier/commits/main/
[License]: https://img.shields.io/badge/license-Educational%20Community%20License,%20Version%202.0-3DA639
[License-url]: https://opensource.org/license/ecl-2-0/
[Code_of_Conduct]: https://img.shields.io/badge/code%20of%20conduct-Contributor%20Covenant,%20Version%202.1-5E0D73
[Code_of_Conduct-url]: https://www.contributor-covenant.org/version/2/1/code_of_conduct/
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
[CC_V2]: https://img.shields.io/badge/Contributor%20Covenant-5E0D73?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMjU2IiBoZWlnaHQ9IjI1NiIgdmlld0JveD0iMCAwIDI1NiAyNTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+Cjx0aXRsZT5Db250cmlidXRvciBDb3ZlbmFudCBMb2dvPC90aXRsZT4KPGcgaWQ9IkNhbnZhcyI+CjxnIGlkPSJHcm91cCI+CjxnIGlkPSJTdWJ0cmFjdCI+Cjx1c2UgeGxpbms6aHJlZj0iI3BhdGgwX2ZpbGwiIGZpbGw9IiNGRkZGRkYiLz4KPC9nPgo8ZyBpZD0iU3VidHJhY3QiPgo8dXNlIHhsaW5rOmhyZWY9IiNwYXRoMV9maWxsIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg1OCAyNCkiIGZpbGw9IiNGRkZGRkYiLz4KPC9nPgo8L2c+CjwvZz4KPGRlZnM+CjxwYXRoIGlkPSJwYXRoMF9maWxsIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0gMTgyLjc4NyAxMi4yODQ2QyAxNzMuMDA1IDkuNDk0MDggMTYyLjY3NyA4IDE1MiA4QyA5MC4xNDQxIDggNDAgNTguMTQ0MSA0MCAxMjBDIDQwIDE4MS44NTYgOTAuMTQ0MSAyMzIgMTUyIDIzMkMgMTg4LjQ2NCAyMzIgMjIwLjg1NyAyMTQuNTc1IDI0MS4zMDggMTg3LjU5OEMgMjE5Ljg3IDIyOC4yNzIgMTc3LjE3MyAyNTYgMTI4IDI1NkMgNTcuMzA3NSAyNTYgMCAxOTguNjkyIDAgMTI4QyAwIDU3LjMwNzUgNTcuMzA3NSAwIDEyOCAwQyAxNDcuNjA0IDAgMTY2LjE3OSA0LjQwNzA5IDE4Mi43ODcgMTIuMjg0NloiLz4KPHBhdGggaWQ9InBhdGgxX2ZpbGwiIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTSAxMzcuMDkgOS4yMTM0MkMgMTI5Ljc1NCA3LjEyMDU2IDEyMi4wMDggNiAxMTQgNkMgNjcuNjA4MSA2IDMwIDQzLjYwODEgMzAgOTBDIDMwIDEzNi4zOTIgNjcuNjA4MSAxNzQgMTE0IDE3NEMgMTQxLjM0OCAxNzQgMTY1LjY0MyAxNjAuOTMxIDE4MC45ODEgMTQwLjY5OEMgMTY0LjkwMyAxNzEuMjA0IDEzMi44OCAxOTIgOTYgMTkyQyA0Mi45ODA3IDE5MiAwIDE0OS4wMTkgMCA5NkMgMCA0Mi45ODA3IDQyLjk4MDcgMCA5NiAwQyAxMTAuNzAzIDAgMTI0LjYzNCAzLjMwNTMxIDEzNy4wOSA5LjIxMzQyWiIvPgo8L2RlZnM+Cjwvc3ZnPgoK
[CC_V2-url]: https://www.contributor-covenant.org/version/2/1/code_of_conduct/
[ECL_V2]: https://img.shields.io/badge/Educational%20Community%20License,%20Version%202.0-414042?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPHN2ZyBoZWlnaHQ9IjI0OCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQiIHZpZXdCb3g9IjAgMCAyNTYgMjQ4IiB3aWR0aD0iMjU2IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxwYXRoIGQ9Im0xNDMuMzM3MDg4IDE2Ny44MzIwMTJjMjIuMDYyNzA1LTguNDcyNyAzMy4wODE3MjEtMzMuMjMxNDI2IDI0LjYxMTY5LTU1LjMwMTA4NC04LjQ3MDAzMS0yMi4wNjkyMTc2LTMzLjIyMTM5OC0zMy4wOTE3MDU2LTU1LjI4MzY2My0yNC42MTk0NDYyLTIyLjA2MjcwNTQgOC40NzI3MDAyLTMzLjA4MTI4MDIgMzMuMjMxODY3Mi0yNC42MTE2ODk5IDU1LjMwMTA4NDIgNC4zNDU4MzE0IDExLjMyNDQwOCAxMy4yOTEyOTA5IDIwLjI3MjI0NiAyNC42MTE2ODk5IDI0LjYxOTQ0NmwtMjguODIzNTcyOCA3NS4xMjkwNDZjLTYzLjU0MTc1NTYtMjQuMzk1OTgyLTk1LjI4MTM0OTQtOTUuNzAwMTI1LTcwLjg5MjYxMjgtMTU5LjI2MTkwNDkgMjQuMzg4NzM2Ny02My41NjE3Nzk4IDk1LjY2OTk3NTYtOTUuMzExMzc1OSAxNTkuMjExNzMxNi03MC45MTQ5NTM1czk1LjI4MTM0OSA5NS43MDAxMjQ0IDcwLjg5MjYxMyAxNTkuMjYxOTA0NGMtMTIuNTE2MjQxIDMyLjYyMDA5NC0zOC4yODI3OTYgNTguMzk0NzY4LTcwLjg5MjYxMyA3MC45MTQ5NTR6IiBmaWxsPSIjM2RhNjM5Ii8+CiAgPGcgZmlsbD0iIzFkNTMxZCI+CiAgICA8cGF0aCBkPSJtMTcyLjE2MDY2MSAyNDcuMzY4NjQzYy0uNjEyMDIxIDAtMS4yMjMxNi0uMTI3MzgtMS43OTI4ODEtLjM4MTI1Ny0xLjA2NzYyMi0uNDc1MTM3LTEuOTAyMTU1LTEuMzU1NzczLTIuMzIwNzQ0LTIuNDQ2NjVsLTI4LjgyMzU3My03NS4xMjk0ODZjLS44NzE5ODYtMi4yNzI1NTEuMjYyNjA5LTQuODIxNDU3IDIuNTM0NDQ0LTUuNjk0MTU5IDkuNTcxNTgtMy42NzU0ODUgMTcuMTM5NjYzLTEwLjg1OTg0OCAyMS4zMDkyNDYtMjAuMjI5NDkxIDQuMTcwMDI0LTkuMzY5MjAzIDQuNDQyNzY4LTE5LjgwMjM5Ny43NjgtMjkuMzc2OTk0LTcuNTg1MjY3LTE5Ljc2NTM3MjctMjkuODMxMjctMjkuNjcyNzQxNy00OS41OTA4NTctMjIuMDg0MjAzLTE5Ljc1ODcwNTYgNy41ODgwOTc5LTI5LjY2Mjk1MzUgMjkuODQxNTUzLTIyLjA3NzI0NjEgNDkuNjA2NDg1IDMuODkxOTkzMSAxMC4xNDE4NTIgMTEuOTM5MDI5MSAxOC4xOTA5ODQgMjIuMDc3MjQ2MSAyMi4wODQyMDMgMi4yNzE4MzUuODcyNzAyIDMuNDA2NDMgMy40MjE2MDggMi41MzQ0NDQgNS42OTQxNTlsLTI4LjgyMzU3MyA3NS4xMjk0ODZjLS40MTg1ODg3IDEuMDkwODc3LTEuMjUzNTYyOSAxLjk3MTUxMy0yLjMyMTE4NDIgMi40NDY2NS0xLjA2NzE4MDcuNDc2MDItMi4yNzk3NjU5LjUwNzc1NC0zLjM3MTE4MDcuMDg4NTkzLTMxLjgzMDM2MTUtMTIuMjIwOTEtNTYuOTk4MTEzNi0zNi4xMDk1NzktNzAuODY2NjE2Mi02Ny4yNjU5MTQtMTMuODY4NTAyNi0zMS4xNTU4OTUtMTQuNzc3OTQxNDktNjUuODQ5NzU3LTIuNTYwODgxMjUtOTcuNjkwMTQ5NSAxMi4yMTcwNjAyNS0zMS44NDAzOTI0IDM2LjA5ODY0Mzc1LTU3LjAxNjA3NTcgNjcuMjQ0NzIyODUtNzAuODg4OTQ4OCAzMS4xNDYwNzk1LTEzLjg3Mjg3MzAxIDY1LjgyOTAxMjUtMTQuNzgyNTk4NSA5Ny42NTkzNzM1LTIuNTYxNjg4MjQgMzEuODMwMzYxIDEyLjIyMDkxMDI0IDU2Ljk5ODExNCAzNi4xMDk1Nzg5NCA3MC44NjY2MTYgNjcuMjY1OTE0MDQgMTMuODY4NTAzIDMxLjE1NTg5NDUgMTQuNzc4MzgyIDY1Ljg0OTc1NzUgMi41NjA4ODEgOTcuNjkwMTQ5NS0xMi45NDMyMDEgMzMuNzMyMTI4LTM5LjcwNjQzNyA2MC41MDM3OTctNzMuNDI3NDk3IDczLjQ1MDYzNy0uNTA4OTE2LjE5NTY5Ny0xLjA0NDI2OC4yOTI2NjQtMS41Nzg3NC4yOTI2NjR6bS00NC4yMDI5Ni0yMzguNDI3NDE2NTZjLTE2LjQzMjkwOSAwLTMyLjgzMDU2ODUgMy40NTU1NDY0Ni00OC4yOTMyMzI4IDEwLjM0MjgzODM2LTI4Ljk5NTg1NTUgMTIuOTE1MTA0OS01MS4yMjgxOTk3IDM2LjM1MjQzNjktNjIuNjAxOTE0IDY1Ljk5NDc2NjYtMTEuMzczNzE0MjcgMjkuNjQxODg4Ni0xMC41MjY4NDMzNiA2MS45NDAyMjk2IDIuMzg0MTkyOCA5MC45NDU2NjM2IDEyLjMxMjIzNDEgMjcuNjU5MzU3IDM0LjE4ODExNyA0OS4xNjU3MjYgNjEuODg4NTUwOCA2MC45NjgzNTdsMjUuNzExNDc3Mi02Ny4wMTkwOWMtMTAuNTUzMjgxLTUuMjM0ODg4LTE4Ljg1MDE0ODUtMTQuMjkwMjcxLTIzLjEwNjk3NDctMjUuMzgxNTE3LTkuMzI3MDM2MS0yNC4zMDI5ODIgMi44NTA4MDktNTEuNjY1MjY4MSAyNy4xNDYxMzQ3LTYwLjk5NTI0MzUgMjQuMjk2NjQ3LTkuMzMwODU3IDUxLjY0ODk5MSAyLjg1MTcwNzMgNjAuOTc2NDY4IDI3LjE1NDI0ODUgNC41MTgxMTMgMTEuNzczMDk5IDQuMTgyODAyIDI0LjYwMTM3NS0uOTQ0Njg5IDM2LjEyMTQ3OS00LjUyNDcyMyAxMC4xNjc4NTctMTIuMzA1MTg0IDE4LjI0Mjk5My0yMi4xNjA1MjMgMjMuMTA2MzIybDI1LjcwODgzMyA2Ny4wMTExNTZjMjkuNDY1MTE1LTEyLjU5MTE0NyA1Mi43NTE0MjItMzYuNjk0NDY1IDY0LjI3MzYyNS02Ni43MjM3ODEgMTEuMzczNzE0LTI5LjY0MTg4OSAxMC41MjcyODQtNjEuOTQwMjI5LTIuMzg0MTkzLTkwLjk0NTIyMjUtMTIuOTExMDM2LTI5LjAwNTQzMzgtMzYuMzQwOTg0LTUxLjI0NTIyNS02NS45NzM1MzUtNjIuNjIyMDgyOC0xMy44MzEwNS01LjMxMDI1ODEtMjguMjQxMDc0LTcuOTU3ODk0MjYtNDIuNjI0MjItNy45NTc4OTQyNnoiLz4KICA8L2c+Cjwvc3ZnPg==
[ECL_V2-url]: https://opensource.org/license/ecl-2-0/
