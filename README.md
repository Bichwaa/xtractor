<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

Ever finished writing a long microsoft word document that refuses to open once saved and closed?  When you try opening the file all you get is a dialog telling you the file is corrupt/broken, leaving you with no option but to start over from scratch.

This tool tries to extract  the text in files like that so that you do not have to start typing it from sctratch. Instead you get all the ext you typed in and only have to format it again in your favourite text editor.

### Built With
Currently the project has one dependecy, Python Fire, a tool by google which handles the tool's commandline interface (This will change in the future as the intention is to use the argparse internal module instead).
* [Python Fire](https://github.com/google/python-fire)


### Prerequisites

* Python3 

For development purposes, the project is best run in a virtual environment. 
[Pipenv](https://github.com/pypa/pipenv) is the project's choice but you can use python's inbuilt [venv](https://docs.python.org/3/library/venv.html) module if you wish.

* To install pipenv in Debian based OS's
```sh
$ sudo apt install pipenv
```

* To install pipenv in Windows command prompt
```sh
pip install pipenv
```
* For instructions on other platforms see [Pipenv's](https://github.com/pypa/pipenv) documentation.

<!-- GETTING STARTED -->
## Getting Started

To get started with this project clone the repo and navigate into it.

* Installing requirements:
```sh
pipenv install
```

* Activating virtual environment
```sh
pipenv shell
```


### Installation

Not production ready yet. Installation instructions will come after a Graphical User Interface is added.



<!-- USAGE EXAMPLES -->
## Usage

Easiest way to use the tool after activating the virtual environment is to run,

```sh
python xtractor
```
Which will initiate the tool in interactive mode.

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/bichwaa/xtractor/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Twitter - [moran__tz](https://twitter.com/moran__tz) 

Email - morandevelopers@gmail.com

Project Link - [https://github.com/your_username/xtractor](https://github.com/your_username/xtractor)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Python Fire](https://github.com/google/python-fire)
* [Img Shields](https://shields.io)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template#contact)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png -->