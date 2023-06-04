# Beluga.

This API as the vocation to distribute and compare the best value of travel website for the moment.

The idea is to compare the best value of travel website and to give the best price to the user.

## Table of Contents
1. [How does it work](#How-does-it-work-?)
2. [Run the API](#example2)
<!-- 3. [Third Example](#third-example)
4. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom) -->

## How does it work ?
Each API is a method that return a list of dictionnary with the best value of the website.

## Run the API
Clone the project on your computer.
```bash
git clone https://github.com/OliveCh12/deals-sonar.git
```

```bash
cd deals-sonar
pip install requirement 
```
Run the project by this commannd
```bash
uvicorn main:app --reload
```

## Contributing

Add methods and the description of the methdod.

For exemple, you want to add a method to get the best price of a flight using the API of the website `https://www.google.fr/flights/

1 [ ] Add a method to get the best price of a flight using the API of the website.

### Utility functions

We provide a set of utility functions to help you to build your own method on differents topics you want to track.

### Dates functions.

`get_days_list` : return a list of days from today to the number of days you want.
```python
from utils.dates import get_days_list

print(get_days_list(3))

# -> ['2018-01-01', '2018-01-02', '2018-01-03' ... ]
```

#### Query url builder functions.