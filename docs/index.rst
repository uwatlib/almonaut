Welcome to Almonaut’s documentation!
====================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   quickstart
   client
   acquisitions_models
   electronic_resources_models

**Almonaut** (*`Ahl-muh-naut*) is a Python library for interacting with
the Ex Libris Alma\ :sup:`©` API. It provides a number of methods which
facilitate handling Alma\ :sup:`©` API data in Python dot notation.

*Almonaut* is built on two excellent Python libraries: the
`Requests <https://github.com/psf/requests>`_ HTTP library and
`pydantic <https://github.com/pydantic/pydantic>`_ for parsing and
validation.

.. note::

   This is a new project under active development. Its API is subject to
   change.

.. warning::

   Ex Libris customers are assigned a limited number of calls to the
   Alma\ :sup:`©` API per day. Some *Almonaut* methods, if used with
   particular combinations of parameters (*e.g.* ``all_records=True``),
   could result in a large number of API calls.

Current State
#############

=================================== =========== ===========
Alma\ :sup:`©` API Area             Read        Write
=================================== =========== ===========
Acquisitions                        ✔           ✖ (planned)
Analytics                           ✖ (planned) n/a
Bibliographic Records and Inventory ✖ (planned) ✖ (planned)
Electronic Resources                ✔           ✖ (planned)
=================================== =========== ===========

Indices
#######

* :ref:`genindex`
* :ref:`modindex`
