# Pythonic Garage Band

**Author**: Anastasia Lebedeva
**Version**: 1.0.2

## Overview
Program which uses Python classes to model a Band made up of different kinds of musicians like Guitarist,Bassist, and Drummer. Musician base class used to handle common functionality which particular kinds of musicians will inherit.


## Getting Started
1. In terminal navigate to the folder with the pythomic_garage_band.py.
2. Run command "python .py".


## Architecture
* Python 3.7.5
* Pipenv
* Pytest


## API
1. class Musician: creates instances of the Musicians
2. class Guitarist(Musician):  inherits properties of Musician class
3. class Bassist(Musician): inherits properties of Musician class
4. class Drummer(Musician): inherits properties of Musician class
5. class Band: creates instances of the Band from the provided data_file

## Change Log

* 12/04/2019 16:12 - initial set up
* 12/04/2019 17:30 - Musician instance and Guitarist instance created
* 12/04/2019 21:30 - Musician class created
* 12/05/2019 1:27 - function create_from_data works, found "extra member" bug

