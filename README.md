<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!--[![LinkedIn][linkedin-shield]][linkedin-url]-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/idarb-oss/adaptive-cards">
    <img src="docs/assets/adaptive-card.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">ms-adaptive-cards</h3>

  <p align="center">
    Implements Microsoft Adaptive Cards models to generate json data from Python.
    <br />
    <a href="https://github.com/idarb-oss/adaptive-cards"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/idarb-oss/adaptive-cards/issues">Report Bug</a>
    ·
    <a href="https://github.com/idarb-oss/adaptive-cards/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



## About The Project

Python implementation to create [adaptive cards](https://adaptivecards.io/) as specified from Microsoft.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

- [`Python`](https://python.org)
- [`pydantic`](https://pydantic.com) for data model modeling

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

This is an [Adaptive Cards](https://adaptivecards.io/) implementation to generate json structures according to the specification from Microsoft.


### Prerequisites

This is an example of how to list things you need to use the software and how to install them.


### Installation

- poetry

  ```sh
  poetry add adaptive-cards
  ```

- pip

  ```sh
  pip install adaptive-cards
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Roadmap

- Card Elements
  - [x] TextBlock
  - [ ] Image
  - [ ] Media
  - [ ] MediaSource
  - [ ] RichTextBlock
  - [ ] TextRun
- Containers
  - [ ] ActionSet
  - [x] Container
  - [x] ColumnSet
  - [x] Column
  - [ ] FactSet
  - [ ] Fact
  - [ ] ImageSet
  - [x] Table
  - [x] TableCell
- [ ] Actions
  - [ ] ShowCard
  - [ ] ToggleVisibility
  - [ ] TargetElement
  - [ ] Execute
- [ ] Types
  - [ ] Refersh
  - [ ] Authentication
  - [ ] TokenExchangeResource
  - [ ] AuthCardButton

See the [open issues](https://github.com/idarb-oss/adaptive-cards/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/idarb-oss/adaptive-cards.svg?style=for-the-badge
[contributors-url]: https://github.com/idarb-oss/adaptive-cards/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/idarb-oss/adaptive-cards.svg?style=for-the-badge
[forks-url]: https://github.com/idarb-oss/adaptive-cards/network/members
[stars-shield]: https://img.shields.io/github/stars/idarb-oss/adaptive-cards.svg?style=for-the-badge
[stars-url]: https://github.com/idarb-oss/adaptive-cards/stargazers
[issues-shield]: https://img.shields.io/github/issues/idarb-oss/adaptive-cards.svg?style=for-the-badge
[issues-url]: https://github.com/idarb-oss/adaptive-cards/issues
[license-shield]: https://img.shields.io/github/license/idarb-oss/adaptive-cards.svg?style=for-the-badge
[license-url]: https://github.com/idarb-oss/adaptive-cards/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[AdaptiveCards]: https://adaptivecards.io/explorer/AdaptiveCard.html
