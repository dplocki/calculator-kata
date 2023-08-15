# Calculator kata

![GitHub](https://img.shields.io/github/license/dplocki/calculator-kata)
![Python 3](https://img.shields.io/badge/python-3.11-informational)
![GitHub top language](https://img.shields.io/github/languages/top/dplocki/calculator-kata)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub last commit](https://img.shields.io/github/last-commit/dplocki/calculator-kata)

## 📒 Idea

The standard [String Calculator](https://codingdojo.org/kata/StringCalculator/) kata is much simpler that this one. The task is to parse the string, find all numbers and calculate the sum. There is also the [RPN calculator](https://codingdojo.org/kata/RPN/) kata, which is closer to it.

This one is the calculator, which is parsing the input (string) as infix notated operation and return its result. In short: you can type the mathematical operation in *human way* and see the result.

## ✔️ Functionality

* adding, subtraction
* multiple, division
* power
* brackets (the round one only)
* simple validation

## ⚙️ Run

The module is ready to use:

```py
from calculator import calculate

print(calculate('32 + 45 * 34 - 23'))
```
