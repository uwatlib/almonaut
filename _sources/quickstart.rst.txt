Quickstart
==========

.. note::

   In order to access the API for your instance of *Alma©*, you will need an Ex Libris `Developer Network <https://developers.exlibrisgroup.com/alma/apis/>`_ account, and you will need to generate an API key.

   Since *Almonaut* at present uses only read-only APIs, your API key should be configured to allow only read-only access. It should allow access to all areas of the API you require (``Acquisitions``, ``Electronic Resources``).

Install Almonaut
################

.. code-block:: console

   pip install almonaut

Import Almonaut and instantiate an API client
#############################################

.. code-block:: python

   from almonaut import client

   alma_api_client = client.AlmaApiClient('a1b2c3myapikeyx1y2z3')

Example: retrieve a fund by its fund ID
#######################################

.. code-block:: python

   my_fund = alma_api_client.get_fund('123456789')

   print(f"Name: {my_fund.name}")
   print(f"Type: {my_fund.type_.desc}")
   print(f"Status: {my_fund.status.desc}")
   print(f"Fiscal period: {my_fund.fiscal_period.desc}")

Example: search funds by fund name
##################################

.. code-block:: python

   search_query = 'name~classics'
   my_funds = alma_api_client.get_funds(limit=10, extra_params={'mode': 'ALL', 'q': search_query})
   
   if len(my_funds.funds) > 0:
       for fund in my_funds.funds:
           print(f"Name: {fund.name}")
           print(f"Type: {fund.type_.desc}")
           print(f"Status: {fund.status.desc}")
           print(f"Fiscal period: {fund.fiscal_period.desc}")

For all available client methods, see :doc:`client`. For all available
object attributes, see :doc:`acquisitions_models` and :doc:`electronic_resources_models`.
