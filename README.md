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
[ECL_V2]: https://img.shields.io/badge/Educational%20Community%20License,%20Version%202.0-414042?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyBoZWlnaHQ9IjI0OCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQiIHZpZXdCb3g9IjAgMCAyNTYgMjQ4IiB3aWR0aD0iMjU2IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im0xNDMuMzM3MDg4IDE2Ny44MzIwMTJjMjIuMDYyNzA1LTguNDcyNyAzMy4wODE3MjEtMzMuMjMxNDI2IDI0LjYxMTY5LTU1LjMwMTA4NC04LjQ3MDAzMS0yMi4wNjkyMTc2LTMzLjIyMTM5OC0zMy4wOTE3MDU2LTU1LjI4MzY2My0yNC42MTk0NDYyLTIyLjA2MjcwNTQgOC40NzI3MDAyLTMzLjA4MTI4MDIgMzMuMjMxODY3Mi0yNC42MTE2ODk5IDU1LjMwMTA4NDIgNC4zNDU4MzE0IDExLjMyNDQwOCAxMy4yOTEyOTA5IDIwLjI3MjI0NiAyNC42MTE2ODk5IDI0LjYxOTQ0NmwtMjguODIzNTcyOCA3NS4xMjkwNDZjLTYzLjU0MTc1NTYtMjQuMzk1OTgyLTk1LjI4MTM0OTQtOTUuNzAwMTI1LTcwLjg5MjYxMjgtMTU5LjI2MTkwNDkgMjQuMzg4NzM2Ny02My41NjE3Nzk4IDk1LjY2OTk3NTYtOTUuMzExMzc1OSAxNTkuMjExNzMxNi03MC45MTQ5NTM1czk1LjI4MTM0OSA5NS43MDAxMjQ0IDcwLjg5MjYxMyAxNTkuMjYxOTA0NGMtMTIuNTE2MjQxIDMyLjYyMDA5NC0zOC4yODI3OTYgNTguMzk0NzY4LTcwLjg5MjYxMyA3MC45MTQ5NTR6IiBmaWxsPSIjM2RhNjM5Ii8+PGcgZmlsbD0iIzFkNTMxZCI+PHBhdGggZD0ibTE3Mi4xNjA2NjEgMjQ3LjM2ODY0M2MtLjYxMjAyMSAwLTEuMjIzMTYtLjEyNzM4LTEuNzkyODgxLS4zODEyNTctMS4wNjc2MjItLjQ3NTEzNy0xLjkwMjE1NS0xLjM1NTc3My0yLjMyMDc0NC0yLjQ0NjY1bC0yOC44MjM1NzMtNzUuMTI5NDg2Yy0uODcxOTg2LTIuMjcyNTUxLjI2MjYwOS00LjgyMTQ1NyAyLjUzNDQ0NC01LjY5NDE1OSA5LjU3MTU4LTMuNjc1NDg1IDE3LjEzOTY2My0xMC44NTk4NDggMjEuMzA5MjQ2LTIwLjIyOTQ5MSA0LjE3MDAyNC05LjM2OTIwMyA0LjQ0Mjc2OC0xOS44MDIzOTcuNzY4LTI5LjM3Njk5NC03LjU4NTI2Ny0xOS43NjUzNzI3LTI5LjgzMTI3LTI5LjY3Mjc0MTctNDkuNTkwODU3LTIyLjA4NDIwMy0xOS43NTg3MDU2IDcuNTg4MDk3OS0yOS42NjI5NTM1IDI5Ljg0MTU1My0yMi4wNzcyNDYxIDQ5LjYwNjQ4NSAzLjg5MTk5MzEgMTAuMTQxODUyIDExLjkzOTAyOTEgMTguMTkwOTg0IDIyLjA3NzI0NjEgMjIuMDg0MjAzIDIuMjcxODM1Ljg3MjcwMiAzLjQwNjQzIDMuNDIxNjA4IDIuNTM0NDQ0IDUuNjk0MTU5bC0yOC44MjM1NzMgNzUuMTI5NDg2Yy0uNDE4NTg4NyAxLjA5MDg3Ny0xLjI1MzU2MjkgMS45NzE1MTMtMi4zMjExODQyIDIuNDQ2NjUtMS4wNjcxODA3LjQ3NjAyLTIuMjc5NzY1OS41MDc3NTQtMy4zNzExODA3LjA4ODU5My0zMS44MzAzNjE1LTEyLjIyMDkxLTU2Ljk5ODExMzYtMzYuMTA5NTc5LTcwLjg2NjYxNjItNjcuMjY1OTE0LTEzLjg2ODUwMjYtMzEuMTU1ODk1LTE0Ljc3Nzk0MTQ5LTY1Ljg0OTc1Ny0yLjU2MDg4MTI1LTk3LjY5MDE0OTUgMTIuMjE3MDYwMjUtMzEuODQwMzkyNCAzNi4wOTg2NDM3NS01Ny4wMTYwNzU3IDY3LjI0NDcyMjg1LTcwLjg4ODk0ODggMzEuMTQ2MDc5NS0xMy44NzI4NzMwMSA2NS44MjkwMTI1LTE0Ljc4MjU5ODUgOTcuNjU5MzczNS0yLjU2MTY4ODI0IDMxLjgzMDM2MSAxMi4yMjA5MTAyNCA1Ni45OTgxMTQgMzYuMTA5NTc4OTQgNzAuODY2NjE2IDY3LjI2NTkxNDA0IDEzLjg2ODUwMyAzMS4xNTU4OTQ1IDE0Ljc3ODM4MiA2NS44NDk3NTc1IDIuNTYwODgxIDk3LjY5MDE0OTUtMTIuOTQzMjAxIDMzLjczMjEyOC0zOS43MDY0MzcgNjAuNTAzNzk3LTczLjQyNzQ5NyA3My40NTA2MzctLjUwODkxNi4xOTU2OTctMS4wNDQyNjguMjkyNjY0LTEuNTc4NzQuMjkyNjY0em0tNDQuMjAyOTYtMjM4LjQyNzQxNjU2Yy0xNi40MzI5MDkgMC0zMi44MzA1Njg1IDMuNDU1NTQ2NDYtNDguMjkzMjMyOCAxMC4zNDI4MzgzNi0yOC45OTU4NTU1IDEyLjkxNTEwNDktNTEuMjI4MTk5NyAzNi4zNTI0MzY5LTYyLjYwMTkxNCA2NS45OTQ3NjY2LTExLjM3MzcxNDI3IDI5LjY0MTg4ODYtMTAuNTI2ODQzMzYgNjEuOTQwMjI5NiAyLjM4NDE5MjggOTAuOTQ1NjYzNiAxMi4zMTIyMzQxIDI3LjY1OTM1NyAzNC4xODgxMTcgNDkuMTY1NzI2IDYxLjg4ODU1MDggNjAuOTY4MzU3bDI1LjcxMTQ3NzItNjcuMDE5MDljLTEwLjU1MzI4MS01LjIzNDg4OC0xOC44NTAxNDg1LTE0LjI5MDI3MS0yMy4xMDY5NzQ3LTI1LjM4MTUxNy05LjMyNzAzNjEtMjQuMzAyOTgyIDIuODUwODA5LTUxLjY2NTI2ODEgMjcuMTQ2MTM0Ny02MC45OTUyNDM1IDI0LjI5NjY0Ny05LjMzMDg1NyA1MS42NDg5OTEgMi44NTE3MDczIDYwLjk3NjQ2OCAyNy4xNTQyNDg1IDQuNTE4MTEzIDExLjc3MzA5OSA0LjE4MjgwMiAyNC42MDEzNzUtLjk0NDY4OSAzNi4xMjE0NzktNC41MjQ3MjMgMTAuMTY3ODU3LTEyLjMwNTE4NCAxOC4yNDI5OTMtMjIuMTYwNTIzIDIzLjEwNjMyMmwyNS43MDg4MzMgNjcuMDExMTU2YzI5LjQ2NTExNS0xMi41OTExNDcgNTIuNzUxNDIyLTM2LjY5NDQ2NSA2NC4yNzM2MjUtNjYuNzIzNzgxIDExLjM3MzcxNC0yOS42NDE4ODkgMTAuNTI3Mjg0LTYxLjk0MDIyOS0yLjM4NDE5My05MC45NDUyMjI1LTEyLjkxMTAzNi0yOS4wMDU0MzM4LTM2LjM0MDk4NC01MS4yNDUyMjUtNjUuOTczNTM1LTYyLjYyMjA4MjgtMTMuODMxMDUtNS4zMTAyNTgxLTI4LjI0MTA3NC03Ljk1Nzg5NDI2LTQyLjYyNDIyLTcuOTU3ODk0MjZ6Ii8+PHBhdGggZD0ibTIzNy43NDEzMTggMjI5LjU3NDc1NWMtMS41OTY5OTcgMS42MzMyOTMtMi4zOTU0ODQgMy41NzA1My0yLjM5NTQ4NCA1LjgxMTc3MSAwIDIuMzIyOTA1LjgxMjA5NyA0LjI5NjQzNyAyLjQzNjMxNiA1LjkyMDY1NiAxLjYxNTE0NSAxLjYyNDIxOCAzLjU2NTk5MyAyLjQzNjMxNSA1Ljg1MjYwMiAyLjQzNjMxNSAyLjI3NzUzNiAwIDQuMjIzODQ3LS44MTY2MzQgNS44Mzg5OTItMi40NDk5MjYgMS42MTUxNDUtMS42NDIzNjcgMi40MjI3MDUtMy42MTEzNjIgMi40MjI3MDUtNS45MDcwNDUgMC0yLjIzMjE2Ny0uODAzMDIzLTQuMTY5NDA0LTIuNDA5MDk0LTUuODExNzcxLTEuNjI0MjE5LTEuNjY5NTg4LTMuNTc1MDY3LTIuNTA0MzY5LTUuODUyNjAzLTIuNTA0MzY5LTIuMzA0NzU3IDAtNC4yNjkyMTUuODM0NzgxLTUuODkzNDM0IDIuNTA0MzY5em0xMi45MTY1NTcgMTMuMDExODMzYy0xLjk1MDg3NyAxLjg4NzM2LTQuMjkxODk1IDIuODMxMDI2LTcuMDIzMTIzIDIuODMxMDI2LTIuODIxOTY2IDAtNS4xOTkyNzktLjk2NjM1LTcuMTMyMDA4LTIuODk5MDgtMS45MzI3My0xLjkzMjcyOS0yLjg5OTA4LTQuMzEwMDQyLTIuODk5MDgtNy4xMzIwMDggMC0yLjkzMDg1MyAxLjA0MzQ3Ny01LjM2NzE0NSAzLjEzMDQ2Mi03LjMwODk0OCAxLjk1OTk1MS0xLjgxNDc2OSA0LjI2MDEzNy0yLjcyMjE0MSA2LjkwMDYyNi0yLjcyMjE0MSAyLjc2NzUyNCAwIDUuMTMxMjI2Ljk3OTk2MSA3LjA5MTE3NyAyLjkzOTkxMnMyLjkzOTkxMiA0LjMyMzY1MyAyLjkzOTkxMiA3LjA5MTE3N2MwIDIuODQ5MTg4LTEuMDAyNjQ2IDUuMjQ5MTg0LTMuMDA3OTY2IDcuMjAwMDYyem0tNi4xMTEyMDYtMTAuNTQ4Mjk1Yy0uMzk5MjQ5LS4xNTQyNTYtLjk2MTgxOS0uMjMxMzgyLTEuNjg3NzI3LS4yMzEzODJoLS43MDc3NTZ2My4yMjU3MzZoMS4xMjk2ODhjLjY4MDUzOSAwIDEuMjExMzUxLS4xMzYxMDUgMS41OTI0NTItLjQwODMyMS4zODExMDItLjI3MjIxNS41NzE2NS0uNzEyMjkuNTcxNjUtMS4zMjAyMzhzLS4yOTk0MzMtMS4wMjk4NzUtLjg5ODMwNy0xLjI2NTc5NXptLTUuMzA4MTc0IDguOTI4NjIxdi0xMS4xMTk5NDVjLjY4OTYxMyAwIDEuNzIxNzQ3LjAwMjI2OSAzLjA5NjQzNS4wMDY4MDZzMi4xMzkxNDguMDExMzQyIDIuMjkzNDA0LjAyMDQxNmMuODgwMTYzLjA2MzUxNyAxLjYxMDU5Ny4yNTQwNjUgMi4xOTEzMjMuNTcxNjQ5Ljk4OTA0OS41NDQ0MzEgMS40ODM1NjcgMS40MjkxMTggMS40ODM1NjcgMi42NTQwODggMCAuOTM0NjA2LS4yNjA4NyAxLjYxMDU5Ny0uNzgyNjE2IDIuMDI3OTk0cy0xLjE2MzcxMS42NjY5MjQtMS45MjU5MTQuNzQ4NTg5Yy42OTg2ODYuMTQ1MTgyIDEuMjI0OTYxLjM1ODQxNCAxLjU3ODg0MS42Mzk3MDMuNjUzMzE3LjUyNjI4My45Nzk5NzEgMS4zNTY1MjguOTc5OTcxIDIuNDkwNzU5di45OTM1ODFjMCAuMTA4ODg2LjAwNjgwNS4yMTc3NzEuMDIwNDE2LjMyNjY1N3MuMDM4NTYzLjIxNzc3MS4wNzQ4NTkuMzI2NjU3bC4wOTUyNzUuMzEzMDQ2aC0yLjc3NjU4NGMtLjA5MDczOC0uMzUzODgtLjE0OTcxNy0uODY2NTQ1LS4xNzY5MzktMS41MzgwMS0uMDI3MjIxLS42NzE0NjQtLjA4NjIwMS0xLjEyNTE1LS4xNzY5MzktMS4zNjEwNy0uMTQ1MTgyLS4zOTAxNzUtLjQxNzM5My0uNjYyMzg3LS44MTY2NDItLjgxNjY0Mi0uMjE3NzczLS4wOTA3MzgtLjU0ODk2My0uMTQ5NzE4LS45OTM1ODItLjE3NjkzOWwtLjYzOTcwMy0uMDQwODMyaC0uNjEyNDgxdjMuOTMzNDkzeiIvPjwvZz48L3N2Zz4=
[ECL_V2-url]: https://opensource.org/license/ecl-2-0/
