<br />
<div align="center">
  <a href="https://github.com/idarb-oss/adaptive-cards">
    <img src="assets/adaptive-card.svg" alt="Logo" width="100" height="100">
  </a>

<h3 align="center">ms-adaptive-cards</h3>

  <p align="center">
    Implements Microsoft Adaptive Cards models to generate json data from Python.
    <br />
    <br />
    <a href="https://github.com/idarb-oss/adaptive-cards/issues">Report Bug</a>
    ·
    <a href="https://github.com/idarb-oss/adaptive-cards/issues">Request Feature</a>
  </p>
</div>

[![CI][ci-shield]][ci-url]
[![PyPi][pypi-shield]][pypi-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

---

Adaptive Cards are an open card exchange format enabling developers to exchange UI content in a common and consistent way.

Card Authors describe their content as a simple JSON object. That content can then be rendered natively inside a Host Application, automatically adapting to the look and feel of the Host.

## Goals

The goals for Adaptive Cards are:

- Portable - To any app, device, and UI framework
- Open - Libraries and schema are open source and shared
- Low cost - Easy to define, easy to consume
- Expressive - Targeted at the long tail of content that developers want to produce
- Purely declarative - No code is needed or allowed
- Automatically styled - To the Host application UX and brand guidelines

## Example

```python
from msadaptivecards.cards import AdaptiveCard
from msadaptivecards.elements import TextBlock


adaptive_card = AdaptiveCard()

text_block = TextBlock(text="Hello World")

adaptive_card.body.append(text_block)

json = adaptive_card.json(by_alias=True, exclude_none=True)
```



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[ci-shield]: https://img.shields.io/github/workflow/status/idarb-oss/adaptive-cards/CI?style=for-the-badge
[ci-url]: https://github.com/idarb-oss/adaptive-cards/actions?query=event%3Apush+branch%3Amain+workflow%3Aci
[pypi-shield]: https://img.shields.io/pypi/v/ms-adaptive-cards?style=for-the-badge
[pypi-url]: https://pypi.org/project/ms-adaptive-cards/
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
