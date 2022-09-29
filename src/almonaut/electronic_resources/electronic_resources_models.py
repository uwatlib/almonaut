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


class Library1(BaseModel):
    # used by class ElectronicCollection
    value: str


class Type2(BaseModel):
    # used by class ElectronicCollection
    value: str
    desc: str


class Interface1(BaseModel):
    # used by class ElectronicCollection
    name: str


class IsSelective(BaseModel):
    value: str
    desc: Optional[str] = None


class AccessType1(BaseModel):
    # used by class ElectronicCollection
    value: str


class CounterPlatform1(BaseModel):
    # used by class ElectronicCollection
    value: str
    desc: Optional[str] = None


class PoLine1(BaseModel):
    # used by class ElectronicCollection
    value: str


class License1(BaseModel):
    # used by class ElectronicCollection
    value: str


class Number1(BaseModel):
    # used by class ElectronicCollection
    value: str


class Free2(BaseModel):
    value: str


class ProxyEnabled3(BaseModel):
    # used by class ElectronicCollection
    value: str


class Language(BaseModel):
    value: str


class MmsId1(BaseModel):
    # used by class ResourceMetadata1
    value: str


class ResourceMetadata1(BaseModel):
    # used by class ElectronicCollection
    mms_id: MmsId1


class Note2(BaseModel):
    # used by class ElectronicCollection
    content: str
    creation_date: date
    created_by: str
    type_: str = Field(..., alias='type')

    _strip_gmt_date_z = validator('creation_date', pre=True, allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class Group2(BaseModel):
    # used by class GroupSetting2
    value: str


class ProxyEnabled4(BaseModel):
    # used by class GroupSetting2
    value: str


class Portfolios2(BaseModel):
    # used by class ElectronicCollection
    value: int
    link: Optional[str] = None


class GroupSetting2(BaseModel):
    group: Group2
    proxy_enabled: ProxyEnabled4
    proxy: str
    public_name: str
    authentication_note: str
    public_note: str


class CdiUpdateFrequency(BaseModel):
    value: str
    desc: Optional[str] = None


class SearchRightsInCdi(BaseModel):
    value: str
    desc: str


class FullTextLinkingInCdi(BaseModel):
    value: str
    desc: str


class CdiNewspapersSearch(BaseModel):
    value: str
    desc: str


class FullTextRightsInCdi(BaseModel):
    value: str
    desc: str


class CdiType(BaseModel):
    value: str
    desc: str


class CdiInfo(BaseModel):
    cdi_collection_id: Optional[str] = None
    number_of_records_in_cdi: Optional[int] = None
    cdi_update_frequency: Optional[CdiUpdateFrequency] = None
    search_rights_in_cdi: Optional[SearchRightsInCdi] = None
    full_text_linking_in_cdi: Optional[FullTextLinkingInCdi] = None
    cdi_newspapers_search: Optional[CdiNewspapersSearch] = None
    provider_coverage: Optional[bool] = None
    resource_types: Optional[str] = None
    full_text_rights_in_cdi: Optional[FullTextRightsInCdi] = None
    cdi_type: Optional[CdiType] = None
    coverage_percentage: Optional[str] = None


class ElectronicCollection(BaseModel):
    id_: str = Field(..., alias='id')
    is_local = bool
    link: str
    public_name: str
    description: str
    description_override: Optional[str] = None
    internal_description: Optional[str] = None
    library: Optional[Library1] = None
    type_: Type2 = Field(..., alias='type')
    interface: Optional[Interface1] = None
    is_selective: Optional[IsSelective] = None
    access_type: Optional[AccessType1] = None
    counter_platform: CounterPlatform1
    po_line: Optional[PoLine1] = None
    activation_date: Optional[date] = None
    expected_activation_date: Optional[date] = None
    license_: Optional[License1] = Field(..., alias='license')
    number: Optional[List[Number1]] = None
    alternative_title: Optional[str] = None
    source: Optional[str] = None
    creator: Optional[str] = None
    url: Optional[str] = None
    url_override: Optional[str] = None
    free: Optional[Free2] = None
    proxy_enabled: Optional[ProxyEnabled3] = None
    proxy: Optional[str] = None
    language: Optional[Language] = None
    category: Optional[str] = None
    resource_metadata: Optional[ResourceMetadata1] = None
    authentication_note: Optional[str] = None
    public_note: Optional[str] = None
    notes: Optional[List[Note2]] = None
    group_settings: Optional[List[GroupSetting2]] = None
    portfolios: Portfolios2
    do_not_show_as_full_text_available_in_cdi_even_if_active_in_alma: Optional[bool] = None
    cdi_search_activation_status: Optional[bool] = None
    cdi_only_full_text_activation: Optional[bool] = None
    cdi_local_notes: Optional[str] = None
    cdi_info: CdiInfo

    _strip_gmt_date_z = validator('activation_date', 'expected_activation_date', pre=True, allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class ElectronicCollections(BaseModel):
    total_record_count: int
    electronic_collections: List[ElectronicCollection] = Field(..., alias='electronic_collection')


class Type1(BaseModel):
    # used by class ElectronicService
    value: str
    desc: str


class ActivationStatus(BaseModel):
    value: str
    desc: str


class ServiceTemporarilyUnavailable(BaseModel):
    value: str


class LinkResolverPlugin(BaseModel):
    value: str


class UrlType1(BaseModel):
    # used by class ElectronicService
    value: str


class UrlTypeOverride1(BaseModel):
    # used by class ElectronicService
    value: str


class Free1(BaseModel):
    # used by class ElectronicService
    value: str


class CrossrefSupported(BaseModel):
    value: str


class CrossrefEnabled(BaseModel):
    value: str


class ProxyEnabled1(BaseModel):
    # used by class ElectronicService
    value: str


class LinkingLevel(BaseModel):
    value: str


class Note1(BaseModel):
    # used by class ElectronicService
    content: str
    creation_date: date
    created_by: str
    type_: str = Field(..., alias='type')

    _strip_gmt_date_z = validator('creation_date', pre=True, allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class Group1(BaseModel):
    # used by class GroupSetting1
    value: str


class Portfolios1(BaseModel):
    # used by class ElectronicService
    value: int
    link: str


class ProxyEnabled2(BaseModel):
    # used by class GroupSetting1
    value: str


class GroupSetting1(BaseModel):
    # used by class ElectronicService
    group: Group1
    proxy_enabled: ProxyEnabled2
    proxy: str
    public_name: str
    authentication_note: str
    public_note: str


class ElectronicService(BaseModel):
    id_: str = Field(..., alias='id')
    link: str
    is_local: bool
    type_: Type1 = Field(..., alias='type')
    public_description: str
    internal_description: Optional[str] = None
    public_description_override: str
    activation_status: ActivationStatus
    activate_new_portfolios: Optional[bool] = None
    active_from_date: Optional[date] = None
    active_until_date: Optional[date] = None
    service_temporarily_unavailable: Optional[ServiceTemporarilyUnavailable] = None
    service_unavailable_date: Optional[date] = None
    service_unavailable_reason: Optional[str] = None
    parser: Optional[str] = None
    parser_override: Optional[str] = None
    parser_parameters: Optional[str] = None
    parser_parameters_override: Optional[str] = None
    link_resolver_plugin: Optional[LinkResolverPlugin] = None
    url_type: Optional[UrlType1] = None
    url_type_override: Optional[UrlTypeOverride1] = None
    dynamic_url: Optional[str] = None
    dynamic_url_override: Optional[str] = None
    free: Optional[Free1] = None
    crossref_supported: Optional[CrossrefSupported] = None
    crossref_enabled: Optional[CrossrefEnabled] = None
    proxy_enabled: Optional[ProxyEnabled1] = None
    proxy: Optional[str] = None
    linking_level: Optional[LinkingLevel] = None
    authentication_note: Optional[str] = None
    public_note: Optional[str] = None
    notes: Optional[List[Note1]] = None
    group_settings: Optional[List[GroupSetting1]] = None
    portfolios: Portfolios1

    _strip_gmt_date_z = validator('active_from_date', 'active_until_date',
                                  'service_unavailable_date', pre=True,
                                  allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class ElectronicServices(BaseModel):
    # Alma API total_record_count for this API can be null
    total_record_count: Optional[int] = None
    electronic_services: List[ElectronicService] = Field(..., alias='electronic_service')


class MmsId2(BaseModel):
    # used by class ResourceMetadata2
    link: str
    value: str


class ResourceMetadata2(BaseModel):
    # used by class Portfolio
    mms_id: MmsId2
    title: str
    author: Optional[str] = None
    issn: Optional[str] = None


class Availability(BaseModel):
    value: str
    desc: str


class MaterialType(BaseModel):
    value: str


class Library2(BaseModel):
    # used by class Portfolio
    value: str


class AccessType2(BaseModel):
    # used by class Portfolio
    value: str


class CounterPlatform2(BaseModel):
    # used by class Portfolio
    value: str


class UrlType2(BaseModel):
    # used by class LinkingDetails
    value: str


class UrlTypeOverride2(BaseModel):
    # used by class LinkingDetails
    value: str


class ProxyEnabled5(BaseModel):
    # used by class LinkingDetails
    value: str


class LinkingDetails(BaseModel):
    url: str
    url_type: UrlType2
    url_type_override: UrlTypeOverride2
    dynamic_url: str
    dynamic_url_override: str
    static_url: str
    static_url_override: str
    parser_parameters: str
    parser_parameters_override: str
    proxy_enabled: ProxyEnabled5
    proxy: str


class CoverageInUse(BaseModel):
    value: str


class FromMonth1(BaseModel):
    # used by class GlobalDateCoverageParameter
    value: str


class FromDay1(BaseModel):
    # used by class GlobalDateCoverageParameter
    value: str


class UntilMonth1(BaseModel):
    # used by class GlobalDateCoverageParameter
    value: str


class UntilDay1(BaseModel):
    # used by class GlobalDateCoverageParameter
    value: str


class GlobalDateCoverageParameter(BaseModel):
    from_year: str
    from_month: FromMonth1
    from_day: FromDay1
    from_volume: str
    from_issue: str
    until_year: str
    until_month: UntilMonth1
    until_day: UntilDay1
    until_volume: str
    until_issue: str


class FromMonth2(BaseModel):
    # used by class LocalDateCoverageParameter
    value: str


class FromDay2(BaseModel):
    # used by class LocalDateCoverageParameter
    value: str


class UntilMonth2(BaseModel):
    # used by class LocalDateCoverageParameter
    value: str


class UntilDay2(BaseModel):
    # used by class LocalDateCoverageParameter
    value: str


class LocalDateCoverageParameter(BaseModel):
    from_year: str
    from_month: FromMonth2
    from_day: FromDay2
    from_volume: str
    from_issue: str
    until_year: str
    until_month: UntilMonth2
    until_day: UntilDay2
    until_volume: str
    until_issue: str


class FromMonth3(BaseModel):
    # used by class PerpetualDateCoverageParameter
    value: str


class FromDay3(BaseModel):
    # used by class PerpetualDateCoverageParameter
    value: str


class UntilMonth3(BaseModel):
    # used by class PerpetualDateCoverageParameter
    value: str


class UntilDay3(BaseModel):
    # used by class PerpetualDateCoverageParameter
    value: str


class PerpetualDateCoverageParameter(BaseModel):
    from_year: str
    from_month: FromMonth3
    from_day: FromDay3
    from_volume: str
    from_issue: str
    until_year: str
    until_month: UntilMonth3
    until_day: UntilDay3
    until_volume: str
    until_issue: str


class EmbargoOperator1(BaseModel):
    # used by class GlobalEmbargoInformation
    value: str


class GlobalEmbargoInformation(BaseModel):
    embargo_operator: EmbargoOperator1
    number_of_years: str
    number_of_months: str


class EmbargoOperator2(BaseModel):
    # used by class LocalEmbargoInformation
    value: str


class LocalEmbargoInformation(BaseModel):
    embargo_operator: EmbargoOperator2
    number_of_years: str
    number_of_months: str


class EmbargoOperator3(BaseModel):
    # used by class PerpetualEmbargoInformation
    value: str


class PerpetualEmbargoInformation(BaseModel):
    embargo_operator: EmbargoOperator3
    number_of_years: str
    number_of_months: str


class CoverageDetails(BaseModel):
    coverage_in_use: CoverageInUse
    global_date_coverage_parameters: List[GlobalDateCoverageParameter]
    local_date_coverage_parameters: List[LocalDateCoverageParameter]
    perpetual_date_coverage_parameters: List[PerpetualDateCoverageParameter]
    global_embargo_information: GlobalEmbargoInformation
    local_embargo_information: LocalEmbargoInformation
    perpetual_embargo_information: PerpetualEmbargoInformation


class PoLine2(BaseModel):
    # used by class Portfolio
    value: str


class PublicAccessModel(BaseModel):
    value: str


class License2(BaseModel):
    # used by class Portfolio
    value: str


class Vendor(BaseModel):
    link: str
    value: str


class Interface2(BaseModel):
    # used by class Portfolio
    name: str
    vendor: Vendor


class Pda(BaseModel):
    value: str


class Number2(BaseModel):
    # used by class Portfolio
    link: str
    value: str


class Note3(BaseModel):
    # used by class Portfolio
    content: str
    creation_date: date
    created_by: str
    type_: str = Field(..., alias='type')

    _strip_gmt_date_z = validator('creation_date', pre=True, allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class Group3(BaseModel):
    # used by class GroupSetting3
    value: str


class ProxyEnabled6(BaseModel):
    # used by class GroupSetting1
    value: str


class GroupSetting3(BaseModel):
    # used by class Portfolio
    group: Group3
    proxy_enabled: ProxyEnabled6
    proxy: str
    public_name: str
    authentication_note: str
    public_note: str


class Portfolio(BaseModel):
    id_: str = Field(..., alias='id')
    link: str
    is_standalone: Optional[bool] = None
    resource_metadata: ResourceMetadata2
    electronic_collection: Optional[ElectronicCollection] = None
    availability: Availability
    material_type: Optional[MaterialType] = None
    activation_date: Optional[date] = None
    expected_activation_date: Optional[date] = None
    library: Optional[Library2] = None
    access_type: Optional[AccessType2] = None
    counter_platform: Optional[CounterPlatform2] = None
    linking_details: Optional[LinkingDetails] = None
    coverage_details: Optional[CoverageDetails] = None
    po_line: Optional[PoLine2] = None
    public_access_model: Optional[PublicAccessModel] = None
    license_: Optional[License2] = Field(..., alias='license')
    interface: Optional[Interface2] = None
    pda: Optional[Pda] = None
    number: Optional[List[Number2]] = None
    authentication_note: Optional[str] = None
    public_note: Optional[str] = None
    internal_description: Optional[str] = None
    notes: Optional[List[Note3]] = None
    group_settings: Optional[List[GroupSetting3]] = None

    _strip_gmt_date_z = validator('activation_date', 'expected_activation_date', pre=True, allow_reuse=True)(
        common_validators._strip_gmt_date_z
    )


class Portfolios(BaseModel):
    total_record_count: Optional[int] = None
    portfolios: List[Portfolio] = Field(..., alias='portfolio')
