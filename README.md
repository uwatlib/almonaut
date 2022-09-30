![Almonaut logo](./almonaut_logo_250x194.png)

# Almonaut

**Almonaut** (*\`Ahl-muh-naut*) is a Python library for interacting with
the Ex Libris Alma<sup>©</sup> API. It provides a number of methods
which facilitate handling Alma<sup>©</sup> API data in Python dot
notation.

*Almonaut* is built on two excellent Python libraries: the
[Requests](https://github.com/psf/requests) HTTP library and
[pydantic](https://github.com/pydantic/pydantic) for parsing and
validation.

<div class="note">

<div class="title">Note</div>

This is a new project under active development. Its API is subject to
change.

</div>

## Current State

| Alma<sup>©</sup> API Area           | Read        | Write       |
|-------------------------------------|-------------|-------------|
| Acquisitions                        | ✔           | ✖ (planned) |
| Analytics                           | ✖ (planned) | n/a         |
| Bibliographic Records and Inventory | ✖ (planned) | ✖ (planned) |
| Electronic Resources                | ✔           | ✖ (planned) |

## Install Almonaut

``` console
pip install almonaut
```

## Import Almonaut and instantiate an API client

``` python
from almonaut import client

alma_api_client = client.AlmaApiClient('a1b2c3myapikeyx1y2z3')

search_query = 'name~classics'
my_funds = alma_api_client.get_funds(limit=10, extra_params={'mode': 'ALL', 'q': search_query})

if len(my_funds.funds) > 0:
    for fund in my_funds.funds:
        print(f"Name: {fund.name}")
        print(f"Type: {fund.type_.desc}")
        print(f"Status: {fund.status.desc}")
        print(f"Fiscal period: {fund.fiscal_period.desc}")
```

**Note:** Substitute your own API key for the placeholder shown above.

For more information, see the [documentation](https://uwatlib.github.io/almonaut/).
