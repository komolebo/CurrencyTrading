Data Capital Management Interview Exercise
==========================================



Your Mission
============

In this directory, you will find a "Currency Trading.pdf" file.  This file describes the core
business requirements of the application you will be constructing.

Based on those requirements, implement a RESTful web service containing the following endpoints:

GET /currencies

Return the entire matrix of available currency exchange rates as outlined in the requirements document
in JSON format

for example:

{
  "EUR": {
    "EUR": 1.00,
    "USD": 1.10,
    "CNY": 6.50,
    "RUB": 70.00
  },
  "USD": {
    "EUR": 0.90,
    "USD": 1.00,
    "CNY": 6.00,
    "RUB": 65.00
  },
  ...
}

GET /currency/{symbol}

Return all available exchange rate mappings for {symbol} in JSON format.

For example, GET /currency/EUR would return:

{
  "EUR": 1.00,
  "USD": 1.10,
  "CNY": 6.50,
  "RUB": 70.00
}

GET /sequence

Returns the shortest sequence of exchanges that yield a profit greater than 1.00% based upon the
current set of currency exchange rates, as well as the actual profit percentage in JSON format.
(This is the same information output as in the requirements pdf, only in JSON format)

For example:

{
  "profit_percent": 1.25,
  "sequence": ["EUR", "USD", "RUB"]
}

POST /currency/{symbol}

Create a new single currency exchange rate mapping.  Your controller should accept input in JSON format,
identical to the output of GET /currency/{symbol}.  The new mapping should be persisted so that it can
later be returned by a subsequent GET request to /currency/{symbol}.

If mappings already exist for {symbol}, they should not be overwritten and an appropriate HTTP status
code should be returned.

PUT /currency/{symbol}/{to}

Update a specific currency exchange rate mapping from {symbol} to {to} (e.g. for EUR to USD).  Should accept input in
JSON format based upon the JSON format used in the previously outlined API endpoints.

The updated mapping should overwrite the previous one, and be persisted as in the POST /currency/{symbol} controller.

Your web service application must at a minimum start with a set of currency exchange rate mappings loaded
from a CSV (as per the input CSV examples in the requirements document).  If you want to go the extra
mile and augment or replace that with something that attempts to pull up to date exchange rates
from an online source (e.g. Yahoo or Google), you are certainly more than welcome to, but it is not
required.

## What we'll be looking for

* Is your solution efficient and scalable? consider the number if currencies on the world are around 200, and response need to be provided very quickly to users 
* Is your code written in a way that you, or anyone else, would actually want to maintain it?
* Can we run it easily after you submit it?
* Are there tests?  Can we run them easily?
* Have you demonstrated an understanding of python and software engineering discipline?

Bonus points
=============

Be creative! This exercise is intentionally fairly open in terms of requirements and restrictions
placed upon you, so go nuts and try to impress us.  If you enhance things beyond the scope of what is
required to meet the minimal set of requirements, that's cool with us.
