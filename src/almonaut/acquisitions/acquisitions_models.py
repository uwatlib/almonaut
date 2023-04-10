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

# from __future__ import annotations

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from almonaut import common_validators


class AdditionalCharges(BaseModel):
    use_pro_rata: bool
    shipment: int
    overhead: int
    insurance: int
    discount: int


class Administrator(BaseModel):
    email: str
    primary_id: str
    first_name: str
    last_name: str
    link: str


class AcquisitionMethod(BaseModel):
    value: str


class AlternativeCallNumberType(BaseModel):
    value: str


class AvailableForLibrary(BaseModel):
    value: str
    desc: str


class BreakIndicator(BaseModel):
    value: str


class Currency1(BaseModel):
    # used by class Fund
    value: str


class Currency3(BaseModel):
    # used by class Invoice
    value: str


class EntityType(BaseModel):
    value: str
    desc: str


class FiscalPeriod(BaseModel):
    value: str
    desc: str


class ForeignCurrency(BaseModel):
    value: str


class FundCode1(BaseModel):
    # used by class FundDistributionItem
    value: str
    desc: Optional[str] = None


class FundCode2(BaseModel):
    # used by class
    value: str


class InterestedUser(BaseModel):
    primary_id: str
    notify_receiving_activation: bool
    hold_item: bool
    notify_renewal: bool
    notify_cancel: bool


class ItemPolicy(BaseModel):
    value: str


class Library(BaseModel):
    value: str


class License2(BaseModel):
    # used by class PoLine
    value: str
    desc: str


class LicensingAgent(BaseModel):
    value: Optional[str] = None
    desc: Optional[str] = None


class Licensor(BaseModel):
    value: Optional[str] = None
    desc: Optional[str] = None


class Location2(BaseModel):
    # used by class License
    value: str
    desc: Optional[str] = None


class MaterialType(BaseModel):
    value: str
    desc: str


class MmsId(BaseModel):
    value: str


class Note1(BaseModel):
    # used by class PoLine
    note_text: str


class Note2(BaseModel):
    # used by class Invoice
    note_text: Optional[str] = None


class OverencumbranceAllowed(BaseModel):
    value: str
    desc: str


class OverexpenditureAllowed(BaseModel):
    value: str
    desc: str


class Owner1(BaseModel):
    # used by class Fund
    value: str
    desc: str


class Owner2(BaseModel):
    # used by class PoLine
    value: str


class Owner3(BaseModel):
    # used by class Invoice
    value: str


class Parent(BaseModel):
    value: int
    link: str


class PatternType(BaseModel):
    value: str


class PaymentMethod(BaseModel):
    value: str


class PaymentStatus(BaseModel):
    value: str


class PhysicalCondition(BaseModel):
    value: str


class PhysicalMaterialType(BaseModel):
    value: str


class Policy(BaseModel):
    value: str


class Provenance(BaseModel):
    value: str


class RenewalCycle(BaseModel):
    value: Optional[str] = None


class ReportingCode(BaseModel):
    value: Optional[str] = None


class ReviewStatus(BaseModel):
    value: str
    desc: str


class SecondaryReportingCode(BaseModel):
    value: Optional[str] = None


class SourceType(BaseModel):
    value: Optional[str] = None


class Status1(BaseModel):
    # used by class Fund
    value: str
    desc: str


class Status2(BaseModel):
    # used by class License
    value: str
    desc: str


class TempCallNumberType(BaseModel):
    value: str


class TempLibrary(BaseModel):
    value: str


class TempLocation(BaseModel):
    value: str


class TempPolicy(BaseModel):
    value: str


class TertiaryReportingCode(BaseModel):
    value: Optional[str] = None


class Type1(BaseModel):
    # used by class Fund
    value: str
    desc: str


class Type2(BaseModel):
    # used by class PoLine
    value: str
    desc: str


class Type3(BaseModel):
    # used by class InvoiceVat
    value: str


class Type4(BaseModel):
    # used by class InvoiceLine
    value: str
    desc: str


class Type5(BaseModel):
    # used by class License
    value: str
    desc: str


class VatCode1(BaseModel):
    # used by class InvoiceVat
    value: str


class VatCode2(BaseModel):
    # used by class InvoiceLineVat
    value: str


class Vendor1(BaseModel):
    # used by class PoLine
    value: str
    desc: str


class Vendor2(BaseModel):
    # used by class Invoice
    value: str


class VendorReferenceNumberType(BaseModel):
    value: str


class VoucherCurrency(BaseModel):
    value: str


class Fund(BaseModel):
    id_: str = Field(..., alias='id')
    link: str
    code: str
    name: str
    external_id: Optional[str] = None
    type_: Optional[Type1] = Field(alias='type')
    entity_type: EntityType
    owner: Owner1
    status: Status1
    description: Optional[str] = None
    fiscal_period: FiscalPeriod
    currency: Currency1
    allocated_balance: float
    expended_balance: float
    cash_balance: float
    encumbered_balance: float
    available_balance: float
    available_for_libraries: List[AvailableForLibrary] = Field(..., alias='available_for_library')
    parent: Parent
    overencumbrance_allowed: OverencumbranceAllowed
    overexpenditure_allowed: OverexpenditureAllowed
    overencumbrance_warning_percent: int
    overexpenditure_warning_sum: float
    overencumbrance_limit_percent: int
    overexpenditure_limit_sum: float
    encumbrances_prior_to_fiscal_period: int
    expenditures_prior_to_fiscal_period: int
    transfers_prior_to_fiscal_period: int
    fiscal_period_end_encumbrance_grace_period: int
    fiscal_period_end_expenditure_grace_period: int


class Funds(BaseModel):
    total_record_count: int
    funds: List[Fund] = Field(..., alias='fund')


class Type6(BaseModel):
    # used by class FundTransaction
    desc: str
    value: str


class Currency5(BaseModel):
    # used by class FundTransaction
    desc: Optional[str] = None
    value: str


class PoLine2(BaseModel):
    # used by class FundTransaction
    link: str
    value: str


class InvoiceLine2(BaseModel):
    # used by class FundTransaction
    link: Optional[str] = None
    value: str


class FundTransaction(BaseModel):
    link: Optional[str] = None
    id_: str = Field(..., alias='id')
    transaction_time: date
    payment_time: Optional[str] = None
    type_: Type6 = Field(..., alias='type')
    amount: float
    currency: Currency5
    transaction_note: Optional[str] = None
    po_line: PoLine2
    invoice_line: InvoiceLine2
    reporting_code: str
    secondary_reporting_code: str
    tertiary_reporting_code: str
    fourth_reporting_code: str
    fifth_reporting_code: str

    _strip_gmt_date_z = validator('transaction_time', pre=True, allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class FundTransactions(BaseModel):
    total_record_count: int
    fund_transactions: List[FundTransaction] = Field(..., alias='fund_transaction')


class Alert(BaseModel):
    value: Optional[str] = None
    desc: str


class Currency2(BaseModel):
    # used by class Price
    value: str


class Currency4(BaseModel):
    # used by class Amount
    value: Optional[str] = None
    desc: Optional[str] = None


class PermanentLibrary(BaseModel):
    value: str


class Status3(BaseModel):
    # used by class PoLine
    value: str
    desc: str


class Price(BaseModel):
    sum_: float = Field(..., alias='sum')
    currency: Currency2


class Amount(BaseModel):
    sum_: Optional[float] = Field(alias='sum')
    currency: Currency4

    @validator('sum_', pre=True)
    def empty_string(value, field):
        if value == "":
            return None
        return value


class ResourceMetadata(BaseModel):
    mms_id: Optional[MmsId] = None
    title: Optional[str] = None
    author: Optional[str] = None
    issn: Optional[str] = None
    isbn: Optional[str] = None
    publisher: Optional[str] = None
    publication_place: Optional[str] = None
    publication_year: Optional[str] = None
    vendor_title_number: Optional[str] = None
    title_id: Optional[str] = None
    system_control_numbers: Optional[List[str]] = Field(alias='system_control_number')


class FundDistribution1(BaseModel):
    # used by class PoLine
    fund_code: FundCode1
    percent: Optional[float] = 0
    amount: Optional[Amount] = None


class Copy(BaseModel):
    link: str
    barcode: Optional[str] = None
    item_policy: ItemPolicy
    receive_date: Optional[str] = None
    enumeration_a: Optional[str] = None
    enumeration_b: Optional[str] = None
    enumeration_c: Optional[str] = None
    chronology_i: Optional[str] = None
    chronology_j: Optional[str] = None
    chronology_k: Optional[str] = None
    description: Optional[str] = None
    storage_location_id: Optional[str] = None
    is_temp_location: Optional[bool] = None
    permanent_library: Optional[PermanentLibrary] = None
    permanent_shelving_location: Optional[str] = None


class Location1(BaseModel):
    # used by class PoLine
    quantity: int
    library: Library
    shelving_location: str
    copies: List[Copy] = Field(..., alias='copy')


class PoLine(BaseModel):
    number: str
    status: Status3
    link: Optional[str] = None
    owner: Owner2
    type_: Type2 = Field(..., alias='type')
    vendor: Vendor1
    vendor_account: str
    reclaim_interval: Optional[str] = None
    expected_receipt_interval: Optional[str] = None
    claiming_interval: Optional[str] = None
    expected_activation_interval: Optional[str] = None
    subscription_interval: Optional[str] = None
    expected_activation_date: Optional[str] = None
    e_activation_due_interval: Optional[str] = None
    acquisition_method: Optional[AcquisitionMethod] = None
    no_charge: Optional[bool] = None
    rush: Optional[bool] = None
    cancellation_restriction: Optional[bool] = None
    cancellation_restriction_note: Optional[str] = None
    price: Optional[Price] = None
    discount: Optional[str] = None
    vendor_reference_number: str
    vendor_reference_number_type: Optional[VendorReferenceNumberType] = None
    source_type: SourceType
    po_number: str
    invoice_reference: Optional[str] = None
    resource_metadata: ResourceMetadata
    fund_distributions: Optional[List[FundDistribution1]] = Field(alias='fund_distribution')
    reporting_code: Optional[str] = None
    secondary_reporting_code: Optional[str] = None
    tertiary_reporting_code: Optional[str] = None
    fourth_reporting_code: Optional[str] = None
    fifth_reporting_code: Optional[str] = None
    vendor_note: Optional[str] = None
    receiving_note: Optional[str] = None
    alerts: Optional[List[Alert]] = Field(alias='alert')
    notes: Optional[List[Note1]] = Field(alias='note')
    locations: Optional[List[Location1]] = Field(alias='location')
    interested_users: Optional[List[InterestedUser]] = Field(alias='interested_user')
    license_: Optional[License2] = Field(alias='license')
    access_model: Optional[str] = None
    url: Optional[str] = None
    base_status: Optional[str] = None
    access_provider: Optional[str] = None
    manual_renewal: Optional[bool] = None
    renewal_cycle: Optional[RenewalCycle] = None
    subscription_from_date: Optional[date] = None
    subscription_to_date: Optional[date] = None
    renewal_date: Optional[date] = None
    renewal_period: Optional[str] = None
    renewal_note: Optional[str] = None
    material_type: Optional[MaterialType] = None
    expected_receipt_date: Optional[date] = None
    created_date: Optional[date] = None
    status_date: Optional[date] = None

    _strip_gmt_date_z = validator('expected_receipt_date',
                                  'created_date',
                                  'renewal_date',
                                  'status_date',
                                  'subscription_from_date',
                                  'subscription_to_date',
                                  pre=True,
                                  allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class PoLines(BaseModel):
    total_record_count: int
    po_lines: List[PoLine] = Field(..., alias='po_line')


class HoldingData(BaseModel):
    link: str
    holding_id: str
    copy_id: str
    in_temp_location: bool
    temp_library: TempLibrary
    temp_location: TempLocation
    temp_call_number_type: TempCallNumberType
    temp_call_number: str
    temp_call_number_source: str
    temp_policy: TempPolicy
    due_back_date: str


class ItemData(BaseModel):
    barcode: str
    physical_material_type: PhysicalMaterialType
    policy: Policy
    provenance: Provenance
    po_line: str
    issue_date: str
    is_magnetic: bool
    arrival_date: str
    expected_arrival_date: str
    year_of_issue: str
    enumeration_a: str
    enumeration_b: str
    enumeration_c: str
    enumeration_d: str
    enumeration_e: str
    enumeration_f: str
    enumeration_g: str
    enumeration_h: str
    chronology_i: str
    chronology_j: str
    chronology_k: str
    chronology_l: str
    chronology_m: str
    break_indicator: BreakIndicator
    pattern_type: PatternType
    linking_number: str
    description: str
    replacement_cost: int
    receiving_operator: str
    inventory_number: str
    inventory_date: str
    inventory_price: str
    receive_number: str
    weeding_number: str
    weeding_date: str
    alternative_call_number: str
    alternative_call_number_type: AlternativeCallNumberType
    alt_number_source: str
    storage_location_id: str
    pages: str
    pieces: str
    public_note: str
    fulfillment_note: str
    internal_note_1: str
    internal_note_2: str
    internal_note_3: str
    statistics_note_1: str
    statistics_note_2: str
    statistics_note_3: str
    physical_condition: PhysicalCondition


class Item(BaseModel):
    link: str
    holding_data: HoldingData
    item_data: ItemData


class PoLineItems(BaseModel):
    total_record_count: int
    items: List[Item] = Field(..., alias='item')


class InvoiceVat(BaseModel):
    report_tax: bool
    vat_per_invoice_line: bool
    vat_code: VatCode1
    percentage: int
    vat_amount: float
    type_: Type3 = Field(..., alias='type')
    expended_from_fund: bool
    vendor_tax: Optional[str] = None


class Payment(BaseModel):
    prepaid: bool
    internal_copy: bool
    export_to_erp: Optional[bool] = None
    payment_status: PaymentStatus
    voucher_date: str
    voucher_number: str
    voucher_amount: str
    voucher_currency: VoucherCurrency


class InvoiceLineVat(BaseModel):
    vat_code: VatCode2
    percentage: int
    vat_amount: int


class FundDistribution2(BaseModel):
    # used by class InvoiceLine
    fund_code: FundCode2
    percent: float
    amount: float


class InvoiceLine(BaseModel):
    link: str
    type_: Type4 = Field(..., alias='type')
    number: str
    po_line: str
    price: float
    price_note: str
    quantity: int
    vat_note: str
    check_subscription_date_overlap: bool
    fully_invoiced: bool
    subscription_from_date: Optional[date] = None
    subscription_to_date: Optional[date] = None
    additional_info: Optional[str] = None
    release_remaining_encumbrance: bool
    reporting_code: Optional[ReportingCode] = None
    secondary_reporting_code: Optional[SecondaryReportingCode] = None
    tertiary_reporting_code: Optional[TertiaryReportingCode] = None
    note: str
    invoice_line_vat: InvoiceLineVat
    fund_distributions: List[FundDistribution2] = Field(..., alias='fund_distribution')

    _strip_gmt_date_z = validator('subscription_from_date',
                                  'subscription_to_date',
                                  pre=True,
                                  allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class InvoiceLines(BaseModel):
    total_record_count: int
    invoice_lines: List[InvoiceLine] = Field(..., alias='invoice_line')


class ExplicitRatio(BaseModel):
    foreign_currency: ForeignCurrency
    rate: int


class Invoice(BaseModel):
    link: str
    number: str
    invoice_date: date
    invoice_due_date: Optional[date] = None
    vendor: Vendor2
    vendor_account: str
    total_amount: int
    currency: Currency3
    payment_method: PaymentMethod
    reference_number: str
    owner: Owner3
    additional_charges: AdditionalCharges
    invoice_vat: InvoiceVat
    # plural in 's' used for clarity instead of 'ratii'
    explicit_ratios: List[ExplicitRatio] = Field(..., alias='explicit_ratio')
    payment: Payment
    notes: List[Note2] = Field(..., alias='note')
    invoice_lines: InvoiceLines

    _strip_gmt_date_z = validator('invoice_date',
                                  'invoice_due_date',
                                  pre=True,
                                  allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class Invoices(BaseModel):
    total_record_count: int
    invoices: List[Invoice] = Field(..., alias='invoice')


class Amendments(BaseModel):
    value: int
    link: str


class Code(BaseModel):
    value: str
    desc: Optional[str] = None


class Value(BaseModel):
    value: str
    desc: Optional[str] = None


class Term(BaseModel):
    code: Code
    value: Value


class Type7(BaseModel):
    # used by class Resource
    value: str
    desc: str


class Resource(BaseModel):
    pid: str
    name: str
    type_: Type7 = Field(..., alias='type')
    link: str


class Type8(BaseModel):
    # used by class Note3
    value: str
    desc: str


class Note3(BaseModel):
    # used by class License
    content: Optional[str] = None
    creation_date: date
    created_by: str
    type_: Optional[Type8] = Field(alias='type')

    _strip_gmt_date_z = validator('creation_date', pre=True, allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class License(BaseModel):
    link: str
    code: str
    name: str
    type_: Type5 = Field(..., alias='type')
    status: Status2
    licensor: Licensor
    signed_by: Optional[str] = None
    signed_date: Optional[date] = None
    second_party_signed_by: Optional[str] = None
    second_party_signed_date: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    location: Optional[Location2] = None
    review_status: ReviewStatus
    uri: Optional[str] = None
    amendments: Optional[Amendments] = None
    licensing_agent: Optional[LicensingAgent] = None
    terms: Optional[List[Term]] = Field(alias='term')
    resources: Optional[List[Resource]] = Field(alias='resource')
    notes: Optional[List[Note3]] = Field(alias='note')
    administrators: Optional[List[Administrator]] = Field(alias='administrator')

    _strip_gmt_date_z = validator('end_date', 'signed_date', 'start_date', pre=True, allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class Licenses(BaseModel):
    total_record_count: int
    licenses: List[License] = Field(..., alias='license')
