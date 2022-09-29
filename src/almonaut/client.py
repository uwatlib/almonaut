# Copyright 2022 University of Waterloo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib.parse import urljoin

import json
import logging

from almonaut.session import AlmaApiSession
from almonaut.exceptions import handle_error_response

from almonaut.acquisitions import acquisitions_models
from almonaut.electronic_resources import electronic_resources_models

logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.WARNING)


class AlmaApiClient(object):
    """The Alma API client.

    :param api_key: The Alma API key to use.
    :param host: Hostname of the Alma API instance.
    :param url_prefix: Prefix before the API version.
    :param version: API version to use.
    """

    def __init__(self,
                 api_key: str,
                 host: str = 'https://api-ca.hosted.exlibrisgroup.com',
                 url_prefix: str = 'almaws',
                 version: str = 'v1'):
        """Instantiate a new API client."""
        self.api_key = api_key
        self.host = host
        self.url_prefix = url_prefix
        self.version = version
        self.session = AlmaApiSession()

    def _request(self, limit=5, offset=0):
        """Execute an API request."""
        rel_url = "/".join((self.url_prefix, self.version, self.end_point))
        target_url = urljoin(self.host, rel_url)
        params = {'apikey': self.api_key, 'format': self.format_,
                  'limit': limit, 'offset': offset}
        params = {**params, **self.extra_params}
        response = self.session.request(self.method, target_url,
                                        params=params)
        logging.info("************* API hit ***************")
        logging.debug(response.url)
        if response.status_code >= 400:
            handle_error_response(response)
        else:
            return response

    def _get_records(self, end_point=None, format_='json',
                     limit=5, all_records=False, extra_params=None,
                     data_dict_key=None):
        """Retrieve records for a query.

        If the number of records for the query exceeds the limit, make multiple
        API calls until all records for the query are retrieved.
        """
        self.end_point = end_point
        self.format_ = format_
        self.extra_params = extra_params
        self.method = 'GET'

        response = self._request(limit=limit, offset=0)
        if type(json.loads(response.content)) == dict:
            response_json = json.loads(response.content)
            if 'total_record_count' in response_json:
                total_records = response_json['total_record_count']
            else:
                total_records = 1

        if total_records == 0:
            return
        elif not all_records:
            return response.content
        else:
            records_requested = limit
            limit = 50
            while records_requested < total_records:
                subsequent_response = self._request(limit=limit,
                                                    offset=records_requested)
                records_requested += limit
                if type(json.loads(subsequent_response.content)) == dict:
                    subsequent_response_json = json.loads(subsequent_response.content)
                    response_json[data_dict_key] += subsequent_response_json[data_dict_key]
            back_to_str = json.dumps(response_json)

            return back_to_str

    # API methods

    # acquisitions

    def get_fund(self, id_: str, format_: str = 'json') -> acquisitions_models.Fund:
        r"""Get a fund record.

        :param id\_: Alma fund ID.
        :param format\_: Format of the raw returned data.

        The ``extra_params`` dict can include:

        view
          brief|full
        """
        end_point = f"acq/funds/{id_}"
        extra_params = {'view': 'full'}
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=1,
                                   all_records=False,
                                   extra_params=extra_params
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.Fund.parse_raw(result)

    def get_funds(self, format_: str = 'json', limit: int = 5,
                  all_records: bool = False, extra_params={}) -> acquisitions_models.Funds:
        r"""Get fund records.

        :param format\_: Format of the raw returned data.
        :param limit: The maximum number of records to be returned.
        :param all_records: Whether or not all matching records should be returned (overrides ``limit``).
        :param extra_params: Additional parameters.

        The ``extra_params`` dict can include:

        view
          brief|full
        """
        extra_params['view'] = 'full'
        result = self._get_records(end_point='acq/funds',
                                   format_=format_,
                                   limit=limit,
                                   all_records=all_records,
                                   extra_params=extra_params,
                                   data_dict_key='fund'
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.Funds.parse_raw(result)

    def get_fund_transactions(self, fund_id: str, format_: str = 'json',
                              limit: int = 5, all_records: bool = False,
                              extra_params={}) -> acquisitions_models.FundTransactions:
        r"""Get fund transaction records.

        :param fund_id: Alma fund ID.
        :param format\_: Format of the raw returned data.
        :param limit: The maximum number of records to be returned.
        :param all_records: Whether or not all matching records should be returned (overrides ``limit``).
        :param extra_params: Additional parameters.
        """
        end_point = f"acq/funds/{fund_id}/transactions"
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=limit,
                                   all_records=all_records,
                                   extra_params=extra_params,
                                   data_dict_key='fund_transaction'
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.FundTransactions.parse_raw(result)

    def get_invoice(self, invoice_id: str, format_: str = 'json') -> acquisitions_models.Invoice:
        r"""Get an invoice record.

        :param invoice_id: Alma invoice ID.
        :param format\_: Format of the raw returned data.

        The ``extra_params`` dict can include:

        expand
          attachments|none
        view
          brief|full
        """
        end_point = f"acq/invoices/{invoice_id}"
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=1,
                                   all_records=False,
                                   extra_params={}
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.Invoice.parse_raw(result)

    def get_invoices(self, format_: str = 'json', limit: int = 5,
                     all_records: bool = False, extra_params={}) -> acquisitions_models.Invoices:
        r"""Get invoice records.

        :param format\_: Format of the raw returned data.
        :param limit: The maximum number of records to be returned.
        :param all_records: Whether or not all matching records should be returned (overrides ``limit``).
        :param extra_params: Additional parameters.

        The ``extra_params`` dict can include:

        base_status
          ACTIVE|All|CLOSED
        creation_form
          (various)
        expand
          attachments|none
        invoice_workflow_status
          (various)
        owner
          (invoice owner: can be the institution code or a library code)
        view
          brief|full
        """
        end_point = 'acq/invoices/'
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=limit,
                                   all_records=all_records,
                                   extra_params=extra_params,
                                   data_dict_key='invoice'
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.Invoices.parse_raw(result)

    def get_invoice_line(self, invoice_id: str, invoice_line_id: str,
                         format_: str = 'json') -> acquisitions_models.InvoiceLine:
        r"""Get an invoice line record.

        :param invoice_id: Alma invoice ID.
        :param invoice_line_id: Alma invoice line ID.
        :param format\_: Format of the raw returned data.
        """
        end_point = f"acq/invoices/{invoice_id}/lines/{invoice_line_id}"
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=1,
                                   all_records=False,
                                   extra_params={}
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.InvoiceLine.parse_raw(result)

    def get_invoice_lines(self, invoice_id: str, format_: str = 'json',
                          limit: int = 5, all_records: bool = False,
                          extra_params={}) -> acquisitions_models.InvoiceLines:
        r"""Get invoice line records.

        :param invoice_id: Alma invoice ID.
        :param format\_: Format of the raw returned data.
        :param limit: The maximum number of records to be returned.
        :param all_records: Whether or not all matching records should be returned (overrides ``limit``).
        :param extra_params: Additional parameters.
        """
        end_point = f"acq/invoices/{invoice_id}/lines"
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=limit,
                                   all_records=all_records,
                                   extra_params=extra_params,
                                   data_dict_key='invoice_line'
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.InvoiceLines.parse_raw(result)

    def get_license(self, code: str, format_: str = 'json') -> acquisitions_models.License:
        r"""Get a license record.

        :param code: Alma license code.
        :param format\_: Format of the raw returned data.

        The ``extra_params`` dict can include:

        expand
          attachments|none
        include_blank_terms
          true|false
        """
        end_point = f"acq/licenses/{code}"
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=1,
                                   all_records=False,
                                   extra_params={}
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.License.parse_raw(result)

    def get_licenses(self, format_: str = 'json', limit: int = 5,
                     all_records: bool = False, extra_params={}) -> acquisitions_models.Licenses:
        r"""Get license records.

        :param format\_: Format of the raw returned data.
        :param limit: The maximum number of records to be returned.
        :param all_records: Whether or not all matching records should be returned (overrides ``limit``).
        :param extra_params: Additional parameters.
        """
        # extra_params['expand'] = 'attachments'
        end_point = 'acq/licenses'
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=limit,
                                   all_records=all_records,
                                   extra_params=extra_params,
                                   data_dict_key='license'
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.Licenses.parse_raw(result)

    def get_po_line(self, number: str, format_: str = 'json') -> acquisitions_models.PoLine:
        r"""Get a PO Line record.

        :param number: Alma PO Line number.
        :param format\_: Format of the raw returned data.
        """
        end_point = f"acq/po-lines/{number}"
        # extra_params['expand'] = 'notes'
        # extra_params['expand'] = 'locations, notes'
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=1,
                                   all_records=False,
                                   extra_params={},
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.PoLine.parse_raw(result)

    def get_po_lines(self, format_: str = 'json', limit: int = 5,
                     all_records: bool = False, extra_params={}) -> acquisitions_models.PoLines:
        r"""Get PO Line records.

        :param format\_: Format of the raw returned data.
        :param limit: The maximum number of records to be returned.
        :param all_records: Whether or not all matching records should be returned (overrides ``limit``).
        :param extra_params: Additional parameters.

        The ``extra_params`` dict can include:

        acquisition_method
          PURCHASE|ALL
        expand
          locations|notes|locations, notes
        status
          ACTIVE|ALL|ALL_WITH_CLOSED|CANCELLED|CLOSED
        q
          *e.g.:* number~123456, po_number~PO123, title~spenser
        """
        end_point = 'acq/po-lines'
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=limit,
                                   all_records=all_records,
                                   extra_params=extra_params,
                                   data_dict_key='po_line'
                                   )
        if result:
            logging.debug(result)
            return acquisitions_models.PoLines.parse_raw(result)

    # e-resources

    def get_electronic_collection(self, collection_id: str,
                                  format_: str = 'json') -> electronic_resources_models.ElectronicCollection:
        r"""Get an Electronic Collection record.

        :param collection_id: Alma electronic collection ID.
        :param format\_: Format of the raw returned data.
        """
        result = self._get_records(end_point=f"electronic/e-collections/{collection_id}",
                                   format_=format_,
                                   limit=1,
                                   all_records=False,
                                   extra_params={}
                                   )
        if result:
            logging.debug(result)
            return electronic_resources_models.ElectronicCollection.parse_raw(result)

    def get_electronic_collections(self, format_: str = 'json', limit: int = 5,
                                   all_records: bool = False, extra_params={}) -> electronic_resources_models.ElectronicCollections:
        r"""Get Electronic Collection records.

        :param format\_: Format of the raw returned data.
        :param limit: The maximum number of records to be returned.
        :param all_records: Whether or not all matching records should be returned (overrides ``limit``).
        :param extra_params: Additional parameters.
        """
        result = self._get_records(end_point='electronic/e-collections',
                                   format_=format_,
                                   limit=limit,
                                   all_records=all_records,
                                   extra_params=extra_params,
                                   data_dict_key='electronic_collection'
                                   )
        if result:
            logging.debug(result)
            return electronic_resources_models.ElectronicCollections.parse_raw(result)

    def get_electronic_service(self, collection_id: str, service_id: str,
                               format_: str = 'json') -> electronic_resources_models.ElectronicService:
        r"""Get an Electronic Service record.

        :param collection_id: Alma electronic collection ID.
        :param service_id: Alma electronic service ID.
        :param format\_: Format of the raw returned data.
        """
        end_point = f"electronic/e-collections/{collection_id}/e-services/{service_id}"
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=1,
                                   all_records=False,
                                   extra_params={}
                                   )
        if result:
            logging.debug(result)
            return electronic_resources_models.ElectronicService.parse_raw(result)

    def get_electronic_services(self, collection_id: str,
                                format_: str = 'json', limit: int = 5,
                                all_records: bool = False, extra_params={}) -> electronic_resources_models.ElectronicServices:
        r"""Get Electronic Service records.

        :param collection_id: Alma electronic collection ID.
        :param format\_: Format of the raw returned data.
        :param limit: The maximum number of records to be returned.
        :param all_records: Whether or not all matching records should be returned (overrides ``limit``).
        :param extra_params: Additional parameters.
        """
        end_point = f"electronic/e-collections/{collection_id}/e-services"
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=limit,
                                   all_records=all_records,
                                   extra_params=extra_params,
                                   data_dict_key='electronic_service'
                                   )
        if result:
            logging.debug(result)
            return electronic_resources_models.ElectronicServices.parse_raw(result)

    def get_portfolio(self, collection_id: str, service_id: str,
                      portfolio_id: str, format_: str = 'json') -> electronic_resources_models.Portfolio:
        r"""Get a Portfolio record.

        :param collection_id: Alma electronic collection ID.
        :param service_id: Alma electronic service ID.
        :param portfolio_id: Alma portfolio ID.
        :param format\_: Format of the raw returned data.
        """
        end_point = f"electronic/e-collections/{collection_id}/e-services/{service_id}/portfolios/{portfolio_id}"
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=1,
                                   all_records=False,
                                   extra_params={}
                                   )
        if result:
            logging.debug(result)
            return electronic_resources_models.Portfolio.parse_raw(result)

    def get_portfolios(self, collection_id: str, service_id: str,
                       format_: str = 'json', limit: int = 5,
                       all_records: bool = False, extra_params={}) -> electronic_resources_models.Portfolios:
        r"""Get Portfolio records.

        :param collection_id: Alma electronic collection ID.
        :param service_id: Alma electronic service ID.
        :param format\_: Format of the raw returned data.
        :param limit: The maximum number of records to be returned.
        :param all_records: Whether or not all matching records should be returned (overrides ``limit``).
        :param extra_params: Additional parameters.
        """
        end_point = f"electronic/e-collections/{collection_id}/e-services/{service_id}/portfolios"
        result = self._get_records(end_point=end_point,
                                   format_=format_,
                                   limit=limit,
                                   all_records=all_records,
                                   extra_params=extra_params,
                                   data_dict_key='portfolio'
                                   )
        if result:
            logging.debug(result)
            return electronic_resources_models.Portfolios.parse_raw(result)
