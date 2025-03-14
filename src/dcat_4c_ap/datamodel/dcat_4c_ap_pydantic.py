from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'nfdi4c',
     'default_range': 'string',
     'description': 'This is an extension of the DCAT Application Profile in '
                    'LinkML. It is intended to be used by NFDI4Chem & NFDI4Cat as '
                    'a core that can further be extended in profiles to provide '
                    'domain specific metadata for a dataset.',
     'id': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap',
     'imports': ['linkml:types', 'dcat_4nfdi_ap'],
     'license': 'CC-BY 4.0',
     'name': 'dcat-4C-ap',
     'prefixes': {'BFO': {'prefix_prefix': 'BFO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/BFO_'},
                  'CHEBI': {'prefix_prefix': 'CHEBI',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/CHEBI_'},
                  'CHEMINF': {'prefix_prefix': 'CHEMINF',
                              'prefix_reference': 'http://semanticscience.org/resource/CHEMINF_'},
                  'CHMO': {'prefix_prefix': 'CHMO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/CHMO_'},
                  'FOODON': {'prefix_prefix': 'FOODON',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/FOODON_'},
                  'IAO': {'prefix_prefix': 'IAO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/IAO_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'NMR': {'prefix_prefix': 'NMR',
                          'prefix_reference': 'http://nmrML.org/nmrCV#NMR:'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'RO': {'prefix_prefix': 'RO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/RO_'},
                  'RXNO': {'prefix_prefix': 'RXNO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/RXNO_'},
                  'SIO': {'prefix_prefix': 'SIO',
                          'prefix_reference': 'http://semanticscience.org/resource/SIO_'},
                  'T4FS': {'prefix_prefix': 'T4FS',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/T4FS_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'doi': {'prefix_prefix': 'doi',
                          'prefix_reference': 'https://doi.org/'},
                  'ex': {'prefix_prefix': 'ex',
                         'prefix_reference': 'http://example.org/'},
                  'foaf': {'prefix_prefix': 'foaf',
                           'prefix_reference': 'http://xmlns.com/foaf/0.1/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nfdi': {'prefix_prefix': 'nfdi',
                           'prefix_reference': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/'},
                  'nfdi4c': {'prefix_prefix': 'nfdi4c',
                             'prefix_reference': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'sosa': {'prefix_prefix': 'sosa',
                           'prefix_reference': 'http://www.w3.org/ns/sosa/'},
                  'vcard': {'prefix_prefix': 'vcard',
                            'prefix_reference': 'http://www.w3.org/2006/vcard/ns#'}},
     'see_also': ['https://StroemPhi.github.io/dcat-NFDI-ap',
                  'https://github.com/HendrikBorgelt/DCAT-ap_as_LinkML_template/blob/main/src/dcatlinkml/schema/dcatlinkml.yaml',
                  'https://gitlab.com/opensourcelab/scientificdata/scidats/-/blob/feature/linkml-schemata/schemata/metadata_model_scidats_dcat_ap.yaml?ref_type=heads'],
     'source_file': 'src/dcat_4c_ap/schema/dcat_4c_ap.yaml',
     'title': 'DCAT-4C-AP'} )

class DatasetThemes(str, Enum):
    Agriculture_fisheries_forestry_and_food = "Agriculture, fisheries, forestry and food"
    Economy_and_finance = "Economy and finance"
    Education_culture_and_sport = "Education, culture and sport"
    Energy = "Energy"
    Environment = "Environment"
    Government_and_public_sector = "Government and public sector"
    Health = "Health"
    International_issues = "International issues"
    Justice_legal_system_and_public_safety = "Justice, legal system and public safety"
    Provisional_data = "Provisional data"
    Regions_and_cities = "Regions and cities"
    Population_and_society = "Population and society"
    Science_and_technology = "Science and technology"
    Transport = "Transport"


class TopLevelMediaTypes(str, Enum):
    application = "application"
    audio = "audio"
    example = "example"
    font = "font"
    haptics = "haptics"
    image = "image"
    message = "message"
    model = "model"
    multipart = "multipart"
    text = "text"
    video = "video"


class QUDTQuantityKindEnum(str):
    """
    Possible kinds of quantifiable attribute types provided as QUDT QualityKind instances.
    """
    pass


class QUDTUnitEnum(str):
    """
    Possible kinds of QUDT unit instances.
    """
    pass


class NMRAssayEnum(str, Enum):
    """
    NMR types from the Chemical Methods Ontology
    """
    # Spectroscopy where the energy states of 13C nuclei placed in a static magnetic field are interrogated by inducing transitions between the states via radio frequency irradiation. Each experiment consists of a sequence of radio frequency pulses with delay periods in between them.
    number_13C_nuclear_magnetic_resonance_spectroscopy = "CHMO:0000595"



class Activity(ConfiguredBaseModel):
    """
    See [DCAT-AP specs:Activity](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Activity)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'prov:Activity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Catalogue(ConfiguredBaseModel):
    """
    See [DCAT-AP specs:Catalogue](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Catalogue)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcat:Catalog',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'applicable_legislation': {'description': 'The legislation '
                                                                  'that mandates the '
                                                                  'creation or '
                                                                  'management of the '
                                                                  'Catalog.',
                                                   'inlined_as_list': True,
                                                   'multivalued': True,
                                                   'name': 'applicable_legislation',
                                                   'range': 'LegalResource',
                                                   'required': False,
                                                   'slot_uri': 'dcatap:applicableLegislation'},
                        'catalogue': {'description': 'A catalogue whose contents are '
                                                     'of interest in the context of '
                                                     'this catalogue.',
                                      'inlined_as_list': True,
                                      'multivalued': True,
                                      'name': 'catalogue',
                                      'range': 'Catalogue',
                                      'required': False,
                                      'slot_uri': 'dcat:catalog'},
                        'creator': {'description': 'An entity responsible for the '
                                                   'creation of the catalogue.',
                                    'inlined_as_list': True,
                                    'multivalued': False,
                                    'name': 'creator',
                                    'range': 'Agent',
                                    'required': False,
                                    'slot_uri': 'dcterms:creator'},
                        'description': {'description': 'A free-text account of the '
                                                       'Catalogue.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'description',
                                        'range': 'string',
                                        'required': True,
                                        'slot_uri': 'dcterms:description'},
                        'geographical_coverage': {'description': 'A geographical area '
                                                                 'covered by the '
                                                                 'Catalogue.',
                                                  'inlined_as_list': True,
                                                  'multivalued': True,
                                                  'name': 'geographical_coverage',
                                                  'range': 'Location',
                                                  'required': False,
                                                  'slot_uri': 'dcterms:spatial'},
                        'has_dataset': {'description': 'A Dataset that is part of the '
                                                       'Catalogue.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'has_dataset',
                                        'range': 'Dataset',
                                        'required': False,
                                        'slot_uri': 'dcat:dataset'},
                        'has_part': {'description': 'A related Catalogue that is part '
                                                    'of the described Catalogue.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'has_part',
                                     'range': 'Catalogue',
                                     'required': False,
                                     'slot_uri': 'dcterms:hasPart'},
                        'homepage': {'description': 'A web page that acts as the main '
                                                    'page for the Catalogue.',
                                     'inlined_as_list': True,
                                     'multivalued': False,
                                     'name': 'homepage',
                                     'range': 'Document',
                                     'recommended': True,
                                     'required': False,
                                     'slot_uri': 'foaf:homepage'},
                        'language': {'description': 'A language used in the textual '
                                                    'metadata describing titles, '
                                                    'descriptions, etc. of the '
                                                    'Datasets in the Catalogue.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'language',
                                     'range': 'LinguisticSystem',
                                     'recommended': True,
                                     'required': False,
                                     'slot_uri': 'dcterms:language'},
                        'licence': {'description': 'A licence under which the '
                                                   'Catalogue can be used or reused.',
                                    'inlined_as_list': True,
                                    'multivalued': False,
                                    'name': 'licence',
                                    'range': 'LicenseDocument',
                                    'required': False,
                                    'slot_uri': 'dcterms:license'},
                        'modification_date': {'description': 'The most recent date on '
                                                             'which the Catalogue was '
                                                             'modified.',
                                              'inlined_as_list': False,
                                              'multivalued': False,
                                              'name': 'modification_date',
                                              'range': 'string',
                                              'recommended': True,
                                              'required': False,
                                              'slot_uri': 'dcterms:modified'},
                        'publisher': {'description': 'An entity (organisation) '
                                                     'responsible for making the '
                                                     'Catalogue available.',
                                      'inlined_as_list': True,
                                      'multivalued': False,
                                      'name': 'publisher',
                                      'range': 'Agent',
                                      'required': True,
                                      'slot_uri': 'dcterms:publisher'},
                        'record': {'description': 'A Catalogue Record that is part of '
                                                  'the Catalogue.',
                                   'inlined_as_list': True,
                                   'multivalued': True,
                                   'name': 'record',
                                   'range': 'CatalogueRecord',
                                   'required': False,
                                   'slot_uri': 'dcat:record'},
                        'release_date': {'description': 'The date of formal issuance '
                                                        '(e.g., publication) of the '
                                                        'Catalogue.',
                                         'inlined_as_list': False,
                                         'multivalued': False,
                                         'name': 'release_date',
                                         'range': 'string',
                                         'recommended': True,
                                         'required': False,
                                         'slot_uri': 'dcterms:issued'},
                        'rights': {'description': 'A statement that specifies rights '
                                                  'associated with the Catalogue.',
                                   'inlined_as_list': True,
                                   'multivalued': False,
                                   'name': 'rights',
                                   'range': 'RightsStatement',
                                   'required': False,
                                   'slot_uri': 'dcterms:rights'},
                        'service': {'description': 'A site or end-point (Data Service) '
                                                   'that is listed in the Catalogue.',
                                    'inlined_as_list': True,
                                    'multivalued': True,
                                    'name': 'service',
                                    'range': 'DataService',
                                    'required': False,
                                    'slot_uri': 'dcat:service'},
                        'temporal_coverage': {'description': 'A temporal period that '
                                                             'the Catalogue covers.',
                                              'inlined_as_list': True,
                                              'multivalued': True,
                                              'name': 'temporal_coverage',
                                              'range': 'PeriodOfTime',
                                              'required': False,
                                              'slot_uri': 'dcterms:temporal'},
                        'themes': {'description': 'A knowledge organization system '
                                                  'used to classify the Resources that '
                                                  'are in the Catalogue.',
                                   'inlined_as_list': True,
                                   'multivalued': True,
                                   'name': 'themes',
                                   'range': 'ConceptScheme',
                                   'recommended': True,
                                   'required': False,
                                   'slot_uri': 'dcat:themeTaxonomy'},
                        'title': {'description': 'A name given to the Catalogue.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dcterms:title'}}})

    applicable_legislation: Optional[List[LegalResource]] = Field(default=None, description="""The legislation that mandates the creation or management of the Catalog.""", json_schema_extra = { "linkml_meta": {'alias': 'applicable_legislation',
         'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    catalogue: Optional[List[Catalogue]] = Field(default=None, description="""A catalogue whose contents are of interest in the context of this catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'catalogue', 'domain_of': ['Catalogue'], 'slot_uri': 'dcat:catalog'} })
    creator: Optional[Agent] = Field(default=None, description="""An entity responsible for the creation of the catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Catalogue', 'Dataset'],
         'slot_uri': 'dcterms:creator'} })
    description: List[str] = Field(default=..., description="""A free-text account of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    geographical_coverage: Optional[List[Location]] = Field(default=None, description="""A geographical area covered by the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'geographical_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:spatial'} })
    has_dataset: Optional[List[Dataset]] = Field(default=None, description="""A Dataset that is part of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'has_dataset', 'domain_of': ['Catalogue'], 'slot_uri': 'dcat:dataset'} })
    has_part: Optional[List[Catalogue]] = Field(default=None, description="""A related Catalogue that is part of the described Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    homepage: Optional[Document] = Field(default=None, description="""A web page that acts as the main page for the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'homepage',
         'domain_of': ['Catalogue'],
         'recommended': True,
         'slot_uri': 'foaf:homepage'} })
    language: Optional[List[LinguisticSystem]] = Field(default=None, description="""A language used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'language',
         'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'recommended': True,
         'slot_uri': 'dcterms:language'} })
    licence: Optional[LicenseDocument] = Field(default=None, description="""A licence under which the Catalogue can be used or reused.""", json_schema_extra = { "linkml_meta": {'alias': 'licence',
         'domain_of': ['Catalogue', 'DataService', 'Distribution'],
         'slot_uri': 'dcterms:license'} })
    modification_date: Optional[str] = Field(default=None, description="""The most recent date on which the Catalogue was modified.""", json_schema_extra = { "linkml_meta": {'alias': 'modification_date',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'recommended': True,
         'slot_uri': 'dcterms:modified'} })
    publisher: Agent = Field(default=..., description="""An entity (organisation) responsible for making the Catalogue available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:publisher'} })
    record: Optional[List[CatalogueRecord]] = Field(default=None, description="""A Catalogue Record that is part of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'record', 'domain_of': ['Catalogue'], 'slot_uri': 'dcat:record'} })
    release_date: Optional[str] = Field(default=None, description="""The date of formal issuance (e.g., publication) of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'recommended': True,
         'slot_uri': 'dcterms:issued'} })
    rights: Optional[RightsStatement] = Field(default=None, description="""A statement that specifies rights associated with the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'rights',
         'domain_of': ['Catalogue', 'Distribution'],
         'slot_uri': 'dcterms:rights'} })
    service: Optional[List[DataService]] = Field(default=None, description="""A site or end-point (Data Service) that is listed in the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'service', 'domain_of': ['Catalogue'], 'slot_uri': 'dcat:service'} })
    temporal_coverage: Optional[List[PeriodOfTime]] = Field(default=None, description="""A temporal period that the Catalogue covers.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:temporal'} })
    themes: Optional[List[ConceptScheme]] = Field(default=None, description="""A knowledge organization system used to classify the Resources that are in the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'themes',
         'domain_of': ['Catalogue'],
         'recommended': True,
         'slot_uri': 'dcat:themeTaxonomy'} })
    title: List[str] = Field(default=..., description="""A name given to the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })


class CatalogueRecord(ConfiguredBaseModel):
    """
    See [DCAT-AP specs:CatalogueRecord](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#CatalogueRecord)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcat:CatalogRecord',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'application_profile': {'description': 'An Application Profile '
                                                               'that the Catalogued '
                                                               'Resource&#39;s '
                                                               'metadata conforms to.',
                                                'inlined_as_list': True,
                                                'multivalued': True,
                                                'name': 'application_profile',
                                                'range': 'Standard',
                                                'recommended': True,
                                                'required': False,
                                                'slot_uri': 'dcterms:conformsTo'},
                        'change_type': {'description': 'The status of the catalogue '
                                                       'record in the context of '
                                                       'editorial flow of the dataset '
                                                       'and data service descriptions.',
                                        'inlined_as_list': True,
                                        'multivalued': False,
                                        'name': 'change_type',
                                        'range': 'Concept',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'adms:status'},
                        'description': {'description': 'A free-text account of the '
                                                       'record. This property can be '
                                                       'repeated for parallel language '
                                                       'versions of the description.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'description',
                                        'range': 'string',
                                        'required': False,
                                        'slot_uri': 'dcterms:description'},
                        'language': {'description': 'A language used in the textual '
                                                    'metadata describing titles, '
                                                    'descriptions, etc. of the '
                                                    'Catalogued Resource.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'language',
                                     'range': 'LinguisticSystem',
                                     'required': False,
                                     'slot_uri': 'dcterms:language'},
                        'listing_date': {'description': 'The date on which the '
                                                        'description of the Resource '
                                                        'was included in the '
                                                        'Catalogue.',
                                         'inlined_as_list': True,
                                         'multivalued': False,
                                         'name': 'listing_date',
                                         'range': 'string',
                                         'recommended': True,
                                         'required': False,
                                         'slot_uri': 'dcterms:issued'},
                        'modification_date': {'description': 'The most recent date on '
                                                             'which the Catalogue '
                                                             'entry was changed or '
                                                             'modified.',
                                              'inlined_as_list': False,
                                              'multivalued': False,
                                              'name': 'modification_date',
                                              'range': 'string',
                                              'required': True,
                                              'slot_uri': 'dcterms:modified'},
                        'primary_topic': {'description': 'A link to the Dataset, Data '
                                                         'service or Catalog described '
                                                         'in the record.',
                                          'inlined_as_list': False,
                                          'multivalued': False,
                                          'name': 'primary_topic',
                                          'range': 'CataloguedResource',
                                          'required': True,
                                          'slot_uri': 'foaf:primaryTopic'},
                        'source_metadata': {'description': 'The original metadata that '
                                                           'was used in creating '
                                                           'metadata for the Dataset, '
                                                           'Data Service or Dataset '
                                                           'Series.',
                                            'inlined_as_list': True,
                                            'multivalued': False,
                                            'name': 'source_metadata',
                                            'range': 'CatalogueRecord',
                                            'required': False,
                                            'slot_uri': 'dcterms:source'},
                        'title': {'description': 'A name given to the Catalogue '
                                                 'Record.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': False,
                                  'slot_uri': 'dcterms:title'}}})

    application_profile: Optional[List[Standard]] = Field(default=None, description="""An Application Profile that the Catalogued Resource&#39;s metadata conforms to.""", json_schema_extra = { "linkml_meta": {'alias': 'application_profile',
         'domain_of': ['CatalogueRecord'],
         'recommended': True,
         'slot_uri': 'dcterms:conformsTo'} })
    change_type: Optional[Concept] = Field(default=None, description="""The status of the catalogue record in the context of editorial flow of the dataset and data service descriptions.""", json_schema_extra = { "linkml_meta": {'alias': 'change_type',
         'domain_of': ['CatalogueRecord'],
         'recommended': True,
         'slot_uri': 'adms:status'} })
    description: Optional[List[str]] = Field(default=None, description="""A free-text account of the record. This property can be repeated for parallel language versions of the description.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    language: Optional[List[LinguisticSystem]] = Field(default=None, description="""A language used in the textual metadata describing titles, descriptions, etc. of the Catalogued Resource.""", json_schema_extra = { "linkml_meta": {'alias': 'language',
         'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dcterms:language'} })
    listing_date: Optional[str] = Field(default=None, description="""The date on which the description of the Resource was included in the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'listing_date',
         'domain_of': ['CatalogueRecord'],
         'recommended': True,
         'slot_uri': 'dcterms:issued'} })
    modification_date: str = Field(default=..., description="""The most recent date on which the Catalogue entry was changed or modified.""", json_schema_extra = { "linkml_meta": {'alias': 'modification_date',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcterms:modified'} })
    primary_topic: CataloguedResource = Field(default=..., description="""A link to the Dataset, Data service or Catalog described in the record.""", json_schema_extra = { "linkml_meta": {'alias': 'primary_topic',
         'domain_of': ['CatalogueRecord'],
         'slot_uri': 'foaf:primaryTopic'} })
    source_metadata: Optional[CatalogueRecord] = Field(default=None, description="""The original metadata that was used in creating metadata for the Dataset, Data Service or Dataset Series.""", json_schema_extra = { "linkml_meta": {'alias': 'source_metadata',
         'domain_of': ['CatalogueRecord'],
         'slot_uri': 'dcterms:source'} })
    title: Optional[List[str]] = Field(default=None, description="""A name given to the Catalogue Record.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })


class CataloguedResource(ConfiguredBaseModel):
    """
    See [DCAT-AP specs:CataloguedResource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#CataloguedResource)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'dcat:Resource',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class DataService(ConfiguredBaseModel):
    """
    See [DCAT-AP specs:DataService](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DataService)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcat:DataService',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'access_rights': {'description': 'Information regarding access '
                                                         'or restrictions based on '
                                                         'privacy, security, or other '
                                                         'policies.',
                                          'inlined_as_list': True,
                                          'multivalued': False,
                                          'name': 'access_rights',
                                          'range': 'RightsStatement',
                                          'required': False,
                                          'slot_uri': 'dcterms:accessRights'},
                        'applicable_legislation': {'description': 'The legislation '
                                                                  'that mandates the '
                                                                  'creation or '
                                                                  'management of the '
                                                                  'Data Service.',
                                                   'inlined_as_list': True,
                                                   'multivalued': True,
                                                   'name': 'applicable_legislation',
                                                   'range': 'LegalResource',
                                                   'required': False,
                                                   'slot_uri': 'dcatap:applicableLegislation'},
                        'conforms_to': {'description': 'An established (technical) '
                                                       'standard to which the Data '
                                                       'Service conforms.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'conforms_to',
                                        'range': 'Standard',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'dcterms:conformsTo'},
                        'contact_point': {'description': 'Contact information that can '
                                                         'be used for sending comments '
                                                         'about the Data Service.',
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'contact_point',
                                          'range': 'Kind',
                                          'recommended': True,
                                          'required': False,
                                          'slot_uri': 'dcat:contactPoint'},
                        'description': {'description': 'A free-text account of the '
                                                       'Data Service.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'description',
                                        'range': 'string',
                                        'required': False,
                                        'slot_uri': 'dcterms:description'},
                        'documentation': {'description': 'A page or document about '
                                                         'this Data Service',
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'documentation',
                                          'range': 'Document',
                                          'required': False,
                                          'slot_uri': 'foaf:page'},
                        'endpoint_URL': {'description': 'The root location or primary '
                                                        'endpoint of the service (an '
                                                        'IRI).',
                                         'inlined_as_list': True,
                                         'multivalued': True,
                                         'name': 'endpoint_URL',
                                         'range': 'Resource',
                                         'required': True,
                                         'slot_uri': 'dcat:endpointURL'},
                        'endpoint_description': {'description': 'A description of the '
                                                                'services available '
                                                                'via the end-points, '
                                                                'including their '
                                                                'operations, '
                                                                'parameters etc.',
                                                 'inlined_as_list': True,
                                                 'multivalued': True,
                                                 'name': 'endpoint_description',
                                                 'range': 'Resource',
                                                 'recommended': True,
                                                 'required': False,
                                                 'slot_uri': 'dcat:endpointDescription'},
                        'format': {'description': 'The structure that can be returned '
                                                  'by querying the endpointURL.',
                                   'inlined_as_list': True,
                                   'multivalued': True,
                                   'name': 'format',
                                   'range': 'MediaTypeOrExtent',
                                   'required': False,
                                   'slot_uri': 'dcterms:format'},
                        'keyword': {'description': 'A keyword or tag describing the '
                                                   'Data Service.',
                                    'inlined_as_list': True,
                                    'multivalued': True,
                                    'name': 'keyword',
                                    'range': 'string',
                                    'recommended': True,
                                    'required': False,
                                    'slot_uri': 'dcat:keyword'},
                        'landing_page': {'description': 'A web page that provides '
                                                        'access to the Data Service '
                                                        'and/or additional '
                                                        'information.',
                                         'inlined_as_list': True,
                                         'multivalued': True,
                                         'name': 'landing_page',
                                         'range': 'Document',
                                         'required': False,
                                         'slot_uri': 'dcat:landingPage'},
                        'licence': {'description': 'A licence under which the Data '
                                                   'service is made available.',
                                    'inlined_as_list': True,
                                    'multivalued': False,
                                    'name': 'licence',
                                    'range': 'LicenseDocument',
                                    'required': False,
                                    'slot_uri': 'dcterms:license'},
                        'publisher': {'description': 'An entity (organisation) '
                                                     'responsible for making the Data '
                                                     'Service available.',
                                      'inlined_as_list': True,
                                      'multivalued': False,
                                      'name': 'publisher',
                                      'range': 'Agent',
                                      'required': False,
                                      'slot_uri': 'dcterms:publisher'},
                        'serves_dataset': {'description': 'This property refers to a '
                                                          'collection of data that '
                                                          'this data service can '
                                                          'distribute.',
                                           'inlined_as_list': True,
                                           'multivalued': True,
                                           'name': 'serves_dataset',
                                           'range': 'Dataset',
                                           'required': False,
                                           'slot_uri': 'dcat:servesDataset'},
                        'theme': {'description': 'A category of the Data Service.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'theme',
                                  'range': 'Concept',
                                  'recommended': True,
                                  'required': False,
                                  'slot_uri': 'dcat:theme'},
                        'title': {'description': 'A name given to the Data Service.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dcterms:title'}}})

    access_rights: Optional[RightsStatement] = Field(default=None, description="""Information regarding access or restrictions based on privacy, security, or other policies.""", json_schema_extra = { "linkml_meta": {'alias': 'access_rights',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcterms:accessRights'} })
    applicable_legislation: Optional[List[LegalResource]] = Field(default=None, description="""The legislation that mandates the creation or management of the Data Service.""", json_schema_extra = { "linkml_meta": {'alias': 'applicable_legislation',
         'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    conforms_to: Optional[List[Standard]] = Field(default=None, description="""An established (technical) standard to which the Data Service conforms.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcterms:conformsTo'} })
    contact_point: Optional[List[Kind]] = Field(default=None, description="""Contact information that can be used for sending comments about the Data Service.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_point',
         'domain_of': ['DataService', 'Dataset', 'DatasetSeries'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    description: Optional[List[str]] = Field(default=None, description="""A free-text account of the Data Service.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    documentation: Optional[List[Document]] = Field(default=None, description="""A page or document about this Data Service""", json_schema_extra = { "linkml_meta": {'alias': 'documentation',
         'domain_of': ['DataService', 'Dataset', 'Distribution'],
         'slot_uri': 'foaf:page'} })
    endpoint_URL: List[Resource] = Field(default=..., description="""The root location or primary endpoint of the service (an IRI).""", json_schema_extra = { "linkml_meta": {'alias': 'endpoint_URL',
         'domain_of': ['DataService'],
         'slot_uri': 'dcat:endpointURL'} })
    endpoint_description: Optional[List[Resource]] = Field(default=None, description="""A description of the services available via the end-points, including their operations, parameters etc.""", json_schema_extra = { "linkml_meta": {'alias': 'endpoint_description',
         'domain_of': ['DataService'],
         'recommended': True,
         'slot_uri': 'dcat:endpointDescription'} })
    format: Optional[List[MediaTypeOrExtent]] = Field(default=None, description="""The structure that can be returned by querying the endpointURL.""", json_schema_extra = { "linkml_meta": {'alias': 'format',
         'domain_of': ['DataService', 'Distribution'],
         'slot_uri': 'dcterms:format'} })
    keyword: Optional[List[str]] = Field(default=None, description="""A keyword or tag describing the Data Service.""", json_schema_extra = { "linkml_meta": {'alias': 'keyword',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:keyword'} })
    landing_page: Optional[List[Document]] = Field(default=None, description="""A web page that provides access to the Data Service and/or additional information.""", json_schema_extra = { "linkml_meta": {'alias': 'landing_page',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcat:landingPage'} })
    licence: Optional[LicenseDocument] = Field(default=None, description="""A licence under which the Data service is made available.""", json_schema_extra = { "linkml_meta": {'alias': 'licence',
         'domain_of': ['Catalogue', 'DataService', 'Distribution'],
         'slot_uri': 'dcterms:license'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity (organisation) responsible for making the Data Service available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:publisher'} })
    serves_dataset: Optional[List[Dataset]] = Field(default=None, description="""This property refers to a collection of data that this data service can distribute.""", json_schema_extra = { "linkml_meta": {'alias': 'serves_dataset',
         'domain_of': ['DataService'],
         'slot_uri': 'dcat:servesDataset'} })
    theme: Optional[List[Concept]] = Field(default=None, description="""A category of the Data Service.""", json_schema_extra = { "linkml_meta": {'alias': 'theme',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:theme'} })
    title: List[str] = Field(default=..., description="""A name given to the Data Service.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })


class Dataset(ConfiguredBaseModel):
    """
    See [DCAT-AP specs:Dataset](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Dataset)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcat:Dataset',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'access_rights': {'description': 'Information that indicates '
                                                         'whether the Dataset is '
                                                         'publicly accessible, has '
                                                         'access restrictions or is '
                                                         'not public.',
                                          'inlined_as_list': True,
                                          'multivalued': False,
                                          'name': 'access_rights',
                                          'range': 'RightsStatement',
                                          'required': False,
                                          'slot_uri': 'dcterms:accessRights'},
                        'applicable_legislation': {'description': 'The legislation '
                                                                  'that mandates the '
                                                                  'creation or '
                                                                  'management of the '
                                                                  'Dataset.',
                                                   'inlined_as_list': True,
                                                   'multivalued': True,
                                                   'name': 'applicable_legislation',
                                                   'range': 'LegalResource',
                                                   'required': False,
                                                   'slot_uri': 'dcatap:applicableLegislation'},
                        'conforms_to': {'description': 'An implementing rule or other '
                                                       'specification.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'conforms_to',
                                        'range': 'Standard',
                                        'required': False,
                                        'slot_uri': 'dcterms:conformsTo'},
                        'contact_point': {'description': 'Contact information that can '
                                                         'be used for sending comments '
                                                         'about the Dataset.',
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'contact_point',
                                          'range': 'Kind',
                                          'recommended': True,
                                          'required': False,
                                          'slot_uri': 'dcat:contactPoint'},
                        'creator': {'description': 'An entity responsible for '
                                                   'producing the dataset.',
                                    'inlined_as_list': True,
                                    'multivalued': True,
                                    'name': 'creator',
                                    'range': 'Agent',
                                    'required': False,
                                    'slot_uri': 'dcterms:creator'},
                        'dataset_distribution': {'description': 'An available '
                                                                'Distribution for the '
                                                                'Dataset.',
                                                 'inlined_as_list': True,
                                                 'multivalued': True,
                                                 'name': 'dataset_distribution',
                                                 'range': 'Distribution',
                                                 'required': False,
                                                 'slot_uri': 'dcat:distribution'},
                        'description': {'description': 'A free-text account of the '
                                                       'Dataset.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'description',
                                        'range': 'string',
                                        'required': True,
                                        'slot_uri': 'dcterms:description'},
                        'documentation': {'description': 'A page or document about '
                                                         'this Dataset.',
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'documentation',
                                          'range': 'Document',
                                          'required': False,
                                          'slot_uri': 'foaf:page'},
                        'frequency': {'description': 'The frequency at which the '
                                                     'Dataset is updated.',
                                      'inlined_as_list': False,
                                      'multivalued': False,
                                      'name': 'frequency',
                                      'range': 'Frequency',
                                      'required': False,
                                      'slot_uri': 'dcterms:accrualPeriodicity'},
                        'geographical_coverage': {'description': 'A geographic region '
                                                                 'that is covered by '
                                                                 'the Dataset.',
                                                  'inlined_as_list': True,
                                                  'multivalued': True,
                                                  'name': 'geographical_coverage',
                                                  'range': 'Location',
                                                  'required': False,
                                                  'slot_uri': 'dcterms:spatial'},
                        'has_version': {'description': 'A related Dataset that is a '
                                                       'version, edition, or '
                                                       'adaptation of the described '
                                                       'Dataset.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'has_version',
                                        'range': 'Dataset',
                                        'required': False,
                                        'slot_uri': 'dcat:hasVersion'},
                        'identifier': {'description': 'The main identifier for the '
                                                      'Dataset, e.g. the URI or other '
                                                      'unique identifier in the '
                                                      'context of the Catalogue.',
                                       'inlined_as_list': True,
                                       'multivalued': True,
                                       'name': 'identifier',
                                       'range': 'uri',
                                       'required': False,
                                       'slot_uri': 'dcterms:identifier'},
                        'in_series': {'description': 'A dataset series of which the '
                                                     'dataset is part.',
                                      'inlined_as_list': True,
                                      'multivalued': True,
                                      'name': 'in_series',
                                      'range': 'DatasetSeries',
                                      'required': False,
                                      'slot_uri': 'dcat:inSeries'},
                        'is_referenced_by': {'description': 'A related resource, such '
                                                            'as a publication, that '
                                                            'references, cites, or '
                                                            'otherwise points to the '
                                                            'dataset.',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'is_referenced_by',
                                             'range': 'Resource',
                                             'required': False,
                                             'slot_uri': 'dcterms:isReferencedBy'},
                        'keyword': {'description': 'A keyword or tag describing the '
                                                   'Dataset.',
                                    'inlined_as_list': True,
                                    'multivalued': True,
                                    'name': 'keyword',
                                    'range': 'string',
                                    'recommended': True,
                                    'required': False,
                                    'slot_uri': 'dcat:keyword'},
                        'landing_page': {'description': 'A web page that provides '
                                                        'access to the Dataset, its '
                                                        'Distributions and/or '
                                                        'additional information.',
                                         'inlined_as_list': True,
                                         'multivalued': True,
                                         'name': 'landing_page',
                                         'range': 'Document',
                                         'required': False,
                                         'slot_uri': 'dcat:landingPage'},
                        'language': {'description': 'A language of the Dataset.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'language',
                                     'range': 'LinguisticSystem',
                                     'required': False,
                                     'slot_uri': 'dcterms:language'},
                        'modification_date': {'description': 'The most recent date on '
                                                             'which the Dataset was '
                                                             'changed or modified.',
                                              'inlined_as_list': False,
                                              'multivalued': False,
                                              'name': 'modification_date',
                                              'range': 'string',
                                              'required': False,
                                              'slot_uri': 'dcterms:modified'},
                        'other_identifier': {'description': 'A secondary identifier of '
                                                            'the Dataset',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'other_identifier',
                                             'range': 'Identifier',
                                             'required': False,
                                             'slot_uri': 'adms:identifier'},
                        'provenance': {'description': 'A statement about the lineage '
                                                      'of a Dataset.',
                                       'inlined_as_list': True,
                                       'multivalued': True,
                                       'name': 'provenance',
                                       'range': 'ProvenanceStatement',
                                       'required': False,
                                       'slot_uri': 'dcterms:provenance'},
                        'publisher': {'description': 'An entity (organisation) '
                                                     'responsible for making the '
                                                     'Dataset available.',
                                      'inlined_as_list': True,
                                      'multivalued': False,
                                      'name': 'publisher',
                                      'range': 'Agent',
                                      'required': False,
                                      'slot_uri': 'dcterms:publisher'},
                        'qualified_attribution': {'description': 'An Agent having some '
                                                                 'form of '
                                                                 'responsibility for '
                                                                 'the resource.',
                                                  'inlined_as_list': True,
                                                  'multivalued': True,
                                                  'name': 'qualified_attribution',
                                                  'range': 'Attribution',
                                                  'required': False,
                                                  'slot_uri': 'prov:qualifiedAttribution'},
                        'qualified_relation': {'description': 'A description of a '
                                                              'relationship with '
                                                              'another resource.',
                                               'inlined_as_list': True,
                                               'multivalued': True,
                                               'name': 'qualified_relation',
                                               'range': 'Relationship',
                                               'required': False,
                                               'slot_uri': 'dcat:qualifiedRelation'},
                        'related_resource': {'description': 'A related resource.',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'related_resource',
                                             'range': 'Resource',
                                             'required': False,
                                             'slot_uri': 'dcterms:relation'},
                        'release_date': {'description': 'The date of formal issuance '
                                                        '(e.g., publication) of the '
                                                        'Dataset.',
                                         'inlined_as_list': False,
                                         'multivalued': False,
                                         'name': 'release_date',
                                         'range': 'string',
                                         'required': False,
                                         'slot_uri': 'dcterms:issued'},
                        'sample': {'description': 'A sample distribution of the '
                                                  'dataset.',
                                   'inlined_as_list': True,
                                   'multivalued': True,
                                   'name': 'sample',
                                   'range': 'Distribution',
                                   'required': False,
                                   'slot_uri': 'adms:sample'},
                        'source': {'description': 'A related Dataset from which the '
                                                  'described Dataset is derived.',
                                   'inlined_as_list': True,
                                   'multivalued': True,
                                   'name': 'source',
                                   'range': 'Dataset',
                                   'required': False,
                                   'slot_uri': 'dcterms:source'},
                        'spatial_resolution': {'description': 'The minimum spatial '
                                                              'separation resolvable '
                                                              'in a dataset, measured '
                                                              'in meters.',
                                               'inlined_as_list': False,
                                               'multivalued': False,
                                               'name': 'spatial_resolution',
                                               'range': 'decimal',
                                               'required': False,
                                               'slot_uri': 'dcat:spatialResolutionInMeters'},
                        'temporal_coverage': {'description': 'A temporal period that '
                                                             'the Dataset covers.',
                                              'inlined_as_list': True,
                                              'multivalued': True,
                                              'name': 'temporal_coverage',
                                              'range': 'PeriodOfTime',
                                              'required': False,
                                              'slot_uri': 'dcterms:temporal'},
                        'temporal_resolution': {'description': 'The minimum time '
                                                               'period resolvable in '
                                                               'the dataset.',
                                                'inlined_as_list': True,
                                                'multivalued': False,
                                                'name': 'temporal_resolution',
                                                'range': 'duration',
                                                'required': False,
                                                'slot_uri': 'dcat:temporalResolution'},
                        'theme': {'description': 'A category of the Dataset.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'theme',
                                  'range': 'Concept',
                                  'recommended': True,
                                  'required': False,
                                  'slot_uri': 'dcat:theme'},
                        'title': {'description': 'A name given to the Dataset.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dcterms:title'},
                        'type': {'description': 'A type of the Dataset.',
                                 'inlined_as_list': True,
                                 'multivalued': True,
                                 'name': 'type',
                                 'range': 'Concept',
                                 'required': False,
                                 'slot_uri': 'dcterms:type'},
                        'version': {'description': 'The version indicator (name or '
                                                   'identifier) of a resource.',
                                    'inlined_as_list': True,
                                    'multivalued': False,
                                    'name': 'version',
                                    'range': 'string',
                                    'required': False,
                                    'slot_uri': 'dcat:version'},
                        'version_notes': {'description': 'A description of the '
                                                         'differences between this '
                                                         'version and a previous '
                                                         'version of the Dataset.',
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'version_notes',
                                          'range': 'string',
                                          'required': False,
                                          'slot_uri': 'adms:versionNotes'},
                        'was_generated_by': {'description': 'An activity that '
                                                            'generated, or provides '
                                                            'the business context for, '
                                                            'the creation of the '
                                                            'dataset.',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'was_generated_by',
                                             'range': 'Activity',
                                             'required': False,
                                             'slot_uri': 'prov:wasGeneratedBy'}}})

    access_rights: Optional[RightsStatement] = Field(default=None, description="""Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public.""", json_schema_extra = { "linkml_meta": {'alias': 'access_rights',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcterms:accessRights'} })
    applicable_legislation: Optional[List[LegalResource]] = Field(default=None, description="""The legislation that mandates the creation or management of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'applicable_legislation',
         'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    conforms_to: Optional[List[Standard]] = Field(default=None, description="""An implementing rule or other specification.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcterms:conformsTo'} })
    contact_point: Optional[List[Kind]] = Field(default=None, description="""Contact information that can be used for sending comments about the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_point',
         'domain_of': ['DataService', 'Dataset', 'DatasetSeries'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    creator: Optional[List[Agent]] = Field(default=None, description="""An entity responsible for producing the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Catalogue', 'Dataset'],
         'slot_uri': 'dcterms:creator'} })
    dataset_distribution: Optional[List[Distribution]] = Field(default=None, description="""An available Distribution for the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_distribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:distribution'} })
    description: List[str] = Field(default=..., description="""A free-text account of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    documentation: Optional[List[Document]] = Field(default=None, description="""A page or document about this Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'documentation',
         'domain_of': ['DataService', 'Dataset', 'Distribution'],
         'slot_uri': 'foaf:page'} })
    frequency: Optional[Frequency] = Field(default=None, description="""The frequency at which the Dataset is updated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'domain_of': ['Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:accrualPeriodicity'} })
    geographical_coverage: Optional[List[Location]] = Field(default=None, description="""A geographic region that is covered by the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'geographical_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:spatial'} })
    has_version: Optional[List[Dataset]] = Field(default=None, description="""A related Dataset that is a version, edition, or adaptation of the described Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_version',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:hasVersion'} })
    identifier: Optional[List[str]] = Field(default=None, description="""The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:identifier'} })
    in_series: Optional[List[DatasetSeries]] = Field(default=None, description="""A dataset series of which the dataset is part.""", json_schema_extra = { "linkml_meta": {'alias': 'in_series', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:inSeries'} })
    is_referenced_by: Optional[List[Resource]] = Field(default=None, description="""A related resource, such as a publication, that references, cites, or otherwise points to the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'is_referenced_by',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:isReferencedBy'} })
    keyword: Optional[List[str]] = Field(default=None, description="""A keyword or tag describing the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'keyword',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:keyword'} })
    landing_page: Optional[List[Document]] = Field(default=None, description="""A web page that provides access to the Dataset, its Distributions and/or additional information.""", json_schema_extra = { "linkml_meta": {'alias': 'landing_page',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcat:landingPage'} })
    language: Optional[List[LinguisticSystem]] = Field(default=None, description="""A language of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'language',
         'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dcterms:language'} })
    modification_date: Optional[str] = Field(default=None, description="""The most recent date on which the Dataset was changed or modified.""", json_schema_extra = { "linkml_meta": {'alias': 'modification_date',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcterms:modified'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the Dataset""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    provenance: Optional[List[ProvenanceStatement]] = Field(default=None, description="""A statement about the lineage of a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'provenance',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:provenance'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity (organisation) responsible for making the Dataset available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:publisher'} })
    qualified_attribution: Optional[List[Attribution]] = Field(default=None, description="""An Agent having some form of responsibility for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'qualified_attribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'prov:qualifiedAttribution'} })
    qualified_relation: Optional[List[Relationship]] = Field(default=None, description="""A description of a relationship with another resource.""", json_schema_extra = { "linkml_meta": {'alias': 'qualified_relation',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:qualifiedRelation'} })
    related_resource: Optional[List[Resource]] = Field(default=None, description="""A related resource.""", json_schema_extra = { "linkml_meta": {'alias': 'related_resource',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:relation'} })
    release_date: Optional[str] = Field(default=None, description="""The date of formal issuance (e.g., publication) of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dcterms:issued'} })
    sample: Optional[List[Distribution]] = Field(default=None, description="""A sample distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'sample', 'domain_of': ['Dataset'], 'slot_uri': 'adms:sample'} })
    source: Optional[List[Dataset]] = Field(default=None, description="""A related Dataset from which the described Dataset is derived.""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['Dataset'], 'slot_uri': 'dcterms:source'} })
    spatial_resolution: Optional[Decimal] = Field(default=None, description="""The minimum spatial separation resolvable in a dataset, measured in meters.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:spatialResolutionInMeters'} })
    temporal_coverage: Optional[List[PeriodOfTime]] = Field(default=None, description="""A temporal period that the Dataset covers.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:temporal'} })
    temporal_resolution: Optional[str] = Field(default=None, description="""The minimum time period resolvable in the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:temporalResolution'} })
    theme: Optional[List[Concept]] = Field(default=None, description="""A category of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'theme',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:theme'} })
    title: List[str] = Field(default=..., description="""A name given to the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    type: Optional[List[Concept]] = Field(default=None, description="""A type of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    version: Optional[str] = Field(default=None, description="""The version indicator (name or identifier) of a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:version'} })
    version_notes: Optional[List[str]] = Field(default=None, description="""A description of the differences between this version and a previous version of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'version_notes',
         'domain_of': ['Dataset'],
         'slot_uri': 'adms:versionNotes'} })
    was_generated_by: Optional[List[Activity]] = Field(default=None, description="""An activity that generated, or provides the business context for, the creation of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Dataset', 'EvaluatedEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })


class DatasetSeries(ConfiguredBaseModel):
    """
    See [DCAT-AP specs:DatasetSeries](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DatasetSeries)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcat:DatasetSeries',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'applicable_legislation': {'description': 'The legislation '
                                                                  'that mandates the '
                                                                  'creation or '
                                                                  'management of the '
                                                                  'Dataset Series.',
                                                   'inlined_as_list': True,
                                                   'multivalued': True,
                                                   'name': 'applicable_legislation',
                                                   'range': 'LegalResource',
                                                   'required': False,
                                                   'slot_uri': 'dcatap:applicableLegislation'},
                        'contact_point': {'description': 'Contact information that can '
                                                         'be used for sending comments '
                                                         'about the Dataset Series.',
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'contact_point',
                                          'range': 'Kind',
                                          'required': False,
                                          'slot_uri': 'dcat:contactPoint'},
                        'description': {'description': 'A free-text account of the '
                                                       'Dataset Series.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'description',
                                        'range': 'string',
                                        'required': True,
                                        'slot_uri': 'dcterms:description'},
                        'frequency': {'description': 'The frequency at which the '
                                                     'Dataset Series is updated.',
                                      'inlined_as_list': False,
                                      'multivalued': False,
                                      'name': 'frequency',
                                      'range': 'Frequency',
                                      'required': False,
                                      'slot_uri': 'dcterms:accrualPeriodicity'},
                        'geographical_coverage': {'description': 'A geographic region '
                                                                 'that is covered by '
                                                                 'the Dataset Series.',
                                                  'inlined_as_list': True,
                                                  'multivalued': True,
                                                  'name': 'geographical_coverage',
                                                  'range': 'Location',
                                                  'required': False,
                                                  'slot_uri': 'dcterms:spatial'},
                        'modification_date': {'description': 'The most recent date on '
                                                             'which the Dataset Series '
                                                             'was changed or modified.',
                                              'inlined_as_list': False,
                                              'multivalued': False,
                                              'name': 'modification_date',
                                              'range': 'string',
                                              'required': False,
                                              'slot_uri': 'dcterms:modified'},
                        'publisher': {'description': 'An entity (organisation) '
                                                     'responsible for ensuring the '
                                                     'coherency of the Dataset Series ',
                                      'inlined_as_list': True,
                                      'multivalued': False,
                                      'name': 'publisher',
                                      'range': 'Agent',
                                      'required': False,
                                      'slot_uri': 'dcterms:publisher'},
                        'release_date': {'description': 'The date of formal issuance '
                                                        '(e.g., publication) of the '
                                                        'Dataset Series.',
                                         'inlined_as_list': False,
                                         'multivalued': False,
                                         'name': 'release_date',
                                         'range': 'string',
                                         'required': False,
                                         'slot_uri': 'dcterms:issued'},
                        'temporal_coverage': {'description': 'A temporal period that '
                                                             'the Dataset Series '
                                                             'covers.',
                                              'inlined_as_list': True,
                                              'multivalued': True,
                                              'name': 'temporal_coverage',
                                              'range': 'PeriodOfTime',
                                              'required': False,
                                              'slot_uri': 'dcterms:temporal'},
                        'title': {'description': 'A name given to the Dataset Series.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dcterms:title'}}})

    applicable_legislation: Optional[List[LegalResource]] = Field(default=None, description="""The legislation that mandates the creation or management of the Dataset Series.""", json_schema_extra = { "linkml_meta": {'alias': 'applicable_legislation',
         'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    contact_point: Optional[List[Kind]] = Field(default=None, description="""Contact information that can be used for sending comments about the Dataset Series.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_point',
         'domain_of': ['DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcat:contactPoint'} })
    description: List[str] = Field(default=..., description="""A free-text account of the Dataset Series.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    frequency: Optional[Frequency] = Field(default=None, description="""The frequency at which the Dataset Series is updated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'domain_of': ['Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:accrualPeriodicity'} })
    geographical_coverage: Optional[List[Location]] = Field(default=None, description="""A geographic region that is covered by the Dataset Series.""", json_schema_extra = { "linkml_meta": {'alias': 'geographical_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:spatial'} })
    modification_date: Optional[str] = Field(default=None, description="""The most recent date on which the Dataset Series was changed or modified.""", json_schema_extra = { "linkml_meta": {'alias': 'modification_date',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcterms:modified'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity (organisation) responsible for ensuring the coherency of the Dataset Series """, json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:publisher'} })
    release_date: Optional[str] = Field(default=None, description="""The date of formal issuance (e.g., publication) of the Dataset Series.""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dcterms:issued'} })
    temporal_coverage: Optional[List[PeriodOfTime]] = Field(default=None, description="""A temporal period that the Dataset Series covers.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:temporal'} })
    title: List[str] = Field(default=..., description="""A name given to the Dataset Series.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })


class Distribution(ConfiguredBaseModel):
    """
    See [DCAT-AP specs:Distribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcat:Distribution',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'access_URL': {'description': 'A URL that gives access to a '
                                                      'Distribution of the Dataset.',
                                       'inlined_as_list': True,
                                       'multivalued': True,
                                       'name': 'access_URL',
                                       'range': 'Resource',
                                       'required': True,
                                       'slot_uri': 'dcat:accessURL'},
                        'access_service': {'description': 'A data service that gives '
                                                          'access to the distribution '
                                                          'of the dataset.',
                                           'inlined_as_list': True,
                                           'multivalued': True,
                                           'name': 'access_service',
                                           'range': 'DataService',
                                           'required': False,
                                           'slot_uri': 'dcat:accessService'},
                        'applicable_legislation': {'description': 'The legislation '
                                                                  'that mandates the '
                                                                  'creation or '
                                                                  'management of the '
                                                                  'Distribution.',
                                                   'inlined_as_list': True,
                                                   'multivalued': True,
                                                   'name': 'applicable_legislation',
                                                   'range': 'LegalResource',
                                                   'required': False,
                                                   'slot_uri': 'dcatap:applicableLegislation'},
                        'availability': {'description': 'An indication how long it is '
                                                        'planned to keep the '
                                                        'Distribution of the Dataset '
                                                        'available.',
                                         'inlined_as_list': False,
                                         'multivalued': False,
                                         'name': 'availability',
                                         'range': 'Concept',
                                         'recommended': True,
                                         'required': False,
                                         'slot_uri': 'dcatap:availability'},
                        'byte_size': {'description': 'The size of a Distribution in '
                                                     'bytes.',
                                      'inlined_as_list': False,
                                      'multivalued': False,
                                      'name': 'byte_size',
                                      'range': 'nonNegativeInteger',
                                      'required': False,
                                      'slot_uri': 'dcat:byteSize'},
                        'checksum': {'description': 'A mechanism that can be used to '
                                                    'verify that the contents of a '
                                                    'distribution have not changed.',
                                     'inlined_as_list': True,
                                     'multivalued': False,
                                     'name': 'checksum',
                                     'range': 'Checksum',
                                     'required': False,
                                     'slot_uri': 'spdx:checksum'},
                        'compression_format': {'description': 'The format of the file '
                                                              'in which the data is '
                                                              'contained in a '
                                                              'compressed form, e.g. '
                                                              'to reduce the size of '
                                                              'the downloadable file.',
                                               'inlined_as_list': True,
                                               'multivalued': False,
                                               'name': 'compression_format',
                                               'range': 'MediaType',
                                               'required': False,
                                               'slot_uri': 'dcat:compressFormat'},
                        'description': {'description': 'A free-text account of the '
                                                       'Distribution.',
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'description',
                                        'range': 'string',
                                        'recommended': True,
                                        'required': False,
                                        'slot_uri': 'dcterms:description'},
                        'documentation': {'description': 'A page or document about '
                                                         'this Distribution.',
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'documentation',
                                          'range': 'Document',
                                          'required': False,
                                          'slot_uri': 'foaf:page'},
                        'download_URL': {'description': 'A URL that is a direct link '
                                                        'to a downloadable file in a '
                                                        'given format.',
                                         'inlined_as_list': True,
                                         'multivalued': True,
                                         'name': 'download_URL',
                                         'range': 'Resource',
                                         'required': False,
                                         'slot_uri': 'dcat:downloadURL'},
                        'format': {'description': 'The file format of the '
                                                  'Distribution.',
                                   'inlined_as_list': True,
                                   'multivalued': False,
                                   'name': 'format',
                                   'range': 'MediaTypeOrExtent',
                                   'recommended': True,
                                   'required': False,
                                   'slot_uri': 'dcterms:format'},
                        'has_policy': {'description': 'The policy expressing the '
                                                      'rights associated with the '
                                                      'distribution if using the '
                                                      '[[ODRL]] vocabulary.',
                                       'inlined_as_list': True,
                                       'multivalued': False,
                                       'name': 'has_policy',
                                       'range': 'Policy',
                                       'required': False,
                                       'slot_uri': 'odrl:hasPolicy'},
                        'language': {'description': 'A language used in the '
                                                    'Distribution.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'language',
                                     'range': 'LinguisticSystem',
                                     'required': False,
                                     'slot_uri': 'dcterms:language'},
                        'licence': {'description': 'A licence under which the '
                                                   'Distribution is made available.',
                                    'inlined_as_list': True,
                                    'multivalued': False,
                                    'name': 'licence',
                                    'range': 'LicenseDocument',
                                    'required': False,
                                    'slot_uri': 'dcterms:license'},
                        'linked_schemas': {'description': 'An established schema to '
                                                          'which the described '
                                                          'Distribution conforms.',
                                           'inlined_as_list': True,
                                           'multivalued': True,
                                           'name': 'linked_schemas',
                                           'range': 'Standard',
                                           'required': False,
                                           'slot_uri': 'dcterms:conformsTo'},
                        'media_type': {'description': 'The media type of the '
                                                      'Distribution as defined in the '
                                                      'official register of media '
                                                      'types managed by IANA.',
                                       'inlined_as_list': False,
                                       'multivalued': False,
                                       'name': 'media_type',
                                       'range': 'MediaType',
                                       'required': False,
                                       'slot_uri': 'dcat:mediaType'},
                        'modification_date': {'description': 'The most recent date on '
                                                             'which the Distribution '
                                                             'was changed or modified.',
                                              'inlined_as_list': False,
                                              'multivalued': False,
                                              'name': 'modification_date',
                                              'range': 'string',
                                              'required': False,
                                              'slot_uri': 'dcterms:modified'},
                        'packaging_format': {'description': 'The format of the file in '
                                                            'which one or more data '
                                                            'files are grouped '
                                                            'together, e.g. to enable '
                                                            'a set of related files to '
                                                            'be downloaded together.',
                                             'inlined_as_list': True,
                                             'multivalued': False,
                                             'name': 'packaging_format',
                                             'range': 'MediaType',
                                             'required': False,
                                             'slot_uri': 'dcat:packageFormat'},
                        'release_date': {'description': 'The date of formal issuance '
                                                        '(e.g., publication) of the '
                                                        'Distribution.',
                                         'inlined_as_list': False,
                                         'multivalued': False,
                                         'name': 'release_date',
                                         'range': 'string',
                                         'required': False,
                                         'slot_uri': 'dcterms:issued'},
                        'rights': {'description': 'A statement that specifies rights '
                                                  'associated with the Distribution.',
                                   'inlined_as_list': True,
                                   'multivalued': False,
                                   'name': 'rights',
                                   'range': 'RightsStatement',
                                   'required': False,
                                   'slot_uri': 'dcterms:rights'},
                        'spatial_resolution': {'description': 'The minimum spatial '
                                                              'separation resolvable '
                                                              'in a dataset '
                                                              'distribution, measured '
                                                              'in meters.',
                                               'inlined_as_list': False,
                                               'multivalued': False,
                                               'name': 'spatial_resolution',
                                               'range': 'decimal',
                                               'required': False,
                                               'slot_uri': 'dcat:spatialResolutionInMeters'},
                        'status': {'description': 'The status of the distribution in '
                                                  'the context of maturity lifecycle.',
                                   'inlined_as_list': True,
                                   'multivalued': False,
                                   'name': 'status',
                                   'range': 'Concept',
                                   'required': False,
                                   'slot_uri': 'adms:status'},
                        'temporal_resolution': {'description': 'The minimum time '
                                                               'period resolvable in '
                                                               'the dataset '
                                                               'distribution.',
                                                'inlined_as_list': True,
                                                'multivalued': False,
                                                'name': 'temporal_resolution',
                                                'range': 'duration',
                                                'required': False,
                                                'slot_uri': 'dcat:temporalResolution'},
                        'title': {'description': 'A name given to the Distribution.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': False,
                                  'slot_uri': 'dcterms:title'}}})

    access_URL: List[Resource] = Field(default=..., description="""A URL that gives access to a Distribution of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'access_URL',
         'domain_of': ['Distribution'],
         'slot_uri': 'dcat:accessURL'} })
    access_service: Optional[List[DataService]] = Field(default=None, description="""A data service that gives access to the distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'access_service',
         'domain_of': ['Distribution'],
         'slot_uri': 'dcat:accessService'} })
    applicable_legislation: Optional[List[LegalResource]] = Field(default=None, description="""The legislation that mandates the creation or management of the Distribution.""", json_schema_extra = { "linkml_meta": {'alias': 'applicable_legislation',
         'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    availability: Optional[Concept] = Field(default=None, description="""An indication how long it is planned to keep the Distribution of the Dataset available.""", json_schema_extra = { "linkml_meta": {'alias': 'availability',
         'domain_of': ['Distribution'],
         'recommended': True,
         'slot_uri': 'dcatap:availability'} })
    byte_size: Optional[int] = Field(default=None, description="""The size of a Distribution in bytes.""", json_schema_extra = { "linkml_meta": {'alias': 'byte_size',
         'domain_of': ['Distribution'],
         'slot_uri': 'dcat:byteSize'} })
    checksum: Optional[Checksum] = Field(default=None, description="""A mechanism that can be used to verify that the contents of a distribution have not changed.""", json_schema_extra = { "linkml_meta": {'alias': 'checksum',
         'domain_of': ['Distribution'],
         'slot_uri': 'spdx:checksum'} })
    compression_format: Optional[MediaType] = Field(default=None, description="""The format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.""", json_schema_extra = { "linkml_meta": {'alias': 'compression_format',
         'domain_of': ['Distribution'],
         'slot_uri': 'dcat:compressFormat'} })
    description: Optional[List[str]] = Field(default=None, description="""A free-text account of the Distribution.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'recommended': True,
         'slot_uri': 'dcterms:description'} })
    documentation: Optional[List[Document]] = Field(default=None, description="""A page or document about this Distribution.""", json_schema_extra = { "linkml_meta": {'alias': 'documentation',
         'domain_of': ['DataService', 'Dataset', 'Distribution'],
         'slot_uri': 'foaf:page'} })
    download_URL: Optional[List[Resource]] = Field(default=None, description="""A URL that is a direct link to a downloadable file in a given format.""", json_schema_extra = { "linkml_meta": {'alias': 'download_URL',
         'domain_of': ['Distribution'],
         'slot_uri': 'dcat:downloadURL'} })
    format: Optional[MediaTypeOrExtent] = Field(default=None, description="""The file format of the Distribution.""", json_schema_extra = { "linkml_meta": {'alias': 'format',
         'domain_of': ['DataService', 'Distribution'],
         'recommended': True,
         'slot_uri': 'dcterms:format'} })
    has_policy: Optional[Policy] = Field(default=None, description="""The policy expressing the rights associated with the distribution if using the [[ODRL]] vocabulary.""", json_schema_extra = { "linkml_meta": {'alias': 'has_policy',
         'domain_of': ['Distribution'],
         'slot_uri': 'odrl:hasPolicy'} })
    language: Optional[List[LinguisticSystem]] = Field(default=None, description="""A language used in the Distribution.""", json_schema_extra = { "linkml_meta": {'alias': 'language',
         'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dcterms:language'} })
    licence: Optional[LicenseDocument] = Field(default=None, description="""A licence under which the Distribution is made available.""", json_schema_extra = { "linkml_meta": {'alias': 'licence',
         'domain_of': ['Catalogue', 'DataService', 'Distribution'],
         'slot_uri': 'dcterms:license'} })
    linked_schemas: Optional[List[Standard]] = Field(default=None, description="""An established schema to which the described Distribution conforms.""", json_schema_extra = { "linkml_meta": {'alias': 'linked_schemas',
         'domain_of': ['Distribution'],
         'slot_uri': 'dcterms:conformsTo'} })
    media_type: Optional[MediaType] = Field(default=None, description="""The media type of the Distribution as defined in the official register of media types managed by IANA.""", json_schema_extra = { "linkml_meta": {'alias': 'media_type',
         'domain_of': ['Distribution'],
         'slot_uri': 'dcat:mediaType'} })
    modification_date: Optional[str] = Field(default=None, description="""The most recent date on which the Distribution was changed or modified.""", json_schema_extra = { "linkml_meta": {'alias': 'modification_date',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcterms:modified'} })
    packaging_format: Optional[MediaType] = Field(default=None, description="""The format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.""", json_schema_extra = { "linkml_meta": {'alias': 'packaging_format',
         'domain_of': ['Distribution'],
         'slot_uri': 'dcat:packageFormat'} })
    release_date: Optional[str] = Field(default=None, description="""The date of formal issuance (e.g., publication) of the Distribution.""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dcterms:issued'} })
    rights: Optional[RightsStatement] = Field(default=None, description="""A statement that specifies rights associated with the Distribution.""", json_schema_extra = { "linkml_meta": {'alias': 'rights',
         'domain_of': ['Catalogue', 'Distribution'],
         'slot_uri': 'dcterms:rights'} })
    spatial_resolution: Optional[Decimal] = Field(default=None, description="""The minimum spatial separation resolvable in a dataset distribution, measured in meters.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:spatialResolutionInMeters'} })
    status: Optional[Concept] = Field(default=None, description="""The status of the distribution in the context of maturity lifecycle.""", json_schema_extra = { "linkml_meta": {'alias': 'status', 'domain_of': ['Distribution'], 'slot_uri': 'adms:status'} })
    temporal_resolution: Optional[str] = Field(default=None, description="""The minimum time period resolvable in the dataset distribution.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:temporalResolution'} })
    title: Optional[List[str]] = Field(default=None, description="""A name given to the Distribution.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })


class SupportiveEntity(ConfiguredBaseModel):
    """
    The supportive entities are supporting the main entities in the Application Profile. They are included in the Application Profile because they form the range of properties.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Agent(SupportiveEntity):
    """
    See [DCAT-AP specs:Agent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Agent)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'foaf:Agent',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'name': {'description': 'A name of the agent.',
                                 'inlined_as_list': True,
                                 'multivalued': True,
                                 'name': 'name',
                                 'range': 'string',
                                 'required': True,
                                 'slot_uri': 'foaf:name'},
                        'type': {'description': 'The nature of the agent.',
                                 'inlined_as_list': True,
                                 'multivalued': False,
                                 'name': 'type',
                                 'range': 'Concept',
                                 'recommended': True,
                                 'required': False,
                                 'slot_uri': 'dcterms:type'}}})

    name: List[str] = Field(default=..., description="""A name of the agent.""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Agent'], 'slot_uri': 'foaf:name'} })
    type: Optional[Concept] = Field(default=None, description="""The nature of the agent.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'recommended': True,
         'slot_uri': 'dcterms:type'} })


class Attribution(SupportiveEntity):
    """
    See [DCAT-AP specs:Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'prov:Attribution',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Checksum(SupportiveEntity):
    """
    See [DCAT-AP specs:Checksum](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Checksum)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'spdx:Checksum',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'algorithm': {'description': 'The algorithm used to produce '
                                                     'the subject Checksum.',
                                      'inlined_as_list': True,
                                      'multivalued': False,
                                      'name': 'algorithm',
                                      'range': 'ChecksumAlgorithm',
                                      'required': True,
                                      'slot_uri': 'spdx:algorithm'},
                        'checksum_value': {'description': 'A lower case hexadecimal '
                                                          'encoded digest value '
                                                          'produced using a specific '
                                                          'algorithm.',
                                           'inlined_as_list': True,
                                           'multivalued': False,
                                           'name': 'checksum_value',
                                           'range': 'hexBinary',
                                           'required': True,
                                           'slot_uri': 'spdx:checksumValue'}}})

    algorithm: ChecksumAlgorithm = Field(default=..., description="""The algorithm used to produce the subject Checksum.""", json_schema_extra = { "linkml_meta": {'alias': 'algorithm', 'domain_of': ['Checksum'], 'slot_uri': 'spdx:algorithm'} })
    checksum_value: str = Field(default=..., description="""A lower case hexadecimal encoded digest value produced using a specific algorithm.""", json_schema_extra = { "linkml_meta": {'alias': 'checksum_value',
         'domain_of': ['Checksum'],
         'slot_uri': 'spdx:checksumValue'} })


class ChecksumAlgorithm(SupportiveEntity):
    """
    See [DCAT-AP specs:ChecksumAlgorithm](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ChecksumAlgorithm)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'spdx:ChecksumAlgorithm',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Concept(SupportiveEntity):
    """
    See [DCAT-AP specs:Concept](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Concept)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'skos:Concept',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'preferred_label': {'description': 'A preferred label of the '
                                                           'concept.',
                                            'inlined_as_list': True,
                                            'multivalued': True,
                                            'name': 'preferred_label',
                                            'range': 'string',
                                            'required': True,
                                            'slot_uri': 'skos:prefLabel'}}})

    preferred_label: List[str] = Field(default=..., description="""A preferred label of the concept.""", json_schema_extra = { "linkml_meta": {'alias': 'preferred_label',
         'domain_of': ['Concept'],
         'slot_uri': 'skos:prefLabel'} })


class ConceptScheme(SupportiveEntity):
    """
    See [DCAT-AP specs:ConceptScheme](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ConceptScheme)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'skos:ConceptScheme',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'title': {'description': 'A name of the concept scheme.',
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'title',
                                  'range': 'string',
                                  'required': True,
                                  'slot_uri': 'dcterms:title'}}})

    title: List[str] = Field(default=..., description="""A name of the concept scheme.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })


class Document(SupportiveEntity):
    """
    See [DCAT-AP specs:Document](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Document)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'foaf:Document',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Frequency(SupportiveEntity):
    """
    See [DCAT-AP specs:Frequency](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Frequency)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:Frequency',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Geometry(SupportiveEntity):
    """
    See [DCAT-AP specs:Geometry](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Geometry)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'locn:Geometry',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Identifier(SupportiveEntity):
    """
    See [DCAT-AP specs:Identifier](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Identifier)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'adms:Identifier',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'notation': {'description': 'A string that is an identifier in '
                                                    'the context of the identifier '
                                                    'scheme referenced by its '
                                                    'datatype.',
                                     'inlined_as_list': False,
                                     'multivalued': False,
                                     'name': 'notation',
                                     'range': 'uri',
                                     'required': True,
                                     'slot_uri': 'skos:notation'}}})

    notation: str = Field(default=..., description="""A string that is an identifier in the context of the identifier scheme referenced by its datatype.""", json_schema_extra = { "linkml_meta": {'alias': 'notation', 'domain_of': ['Identifier'], 'slot_uri': 'skos:notation'} })


class Kind(SupportiveEntity):
    """
    See [DCAT-AP specs:Kind](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Kind)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'vcard:Kind',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class LegalResource(SupportiveEntity):
    """
    See [DCAT-AP specs:LegalResource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LegalResource)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'eli:LegalResource',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class LicenseDocument(SupportiveEntity):
    """
    See [DCAT-AP specs:LicenseDocument](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LicenseDocument)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:LicenseDocument',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'type': {'description': 'A type of licence, e.g. indicating '
                                                "'public domain' or 'royalties "
                                                "required'.",
                                 'inlined_as_list': True,
                                 'multivalued': True,
                                 'name': 'type',
                                 'range': 'Concept',
                                 'recommended': True,
                                 'required': False,
                                 'slot_uri': 'dcterms:type'}}})

    type: Optional[List[Concept]] = Field(default=None, description="""A type of licence, e.g. indicating 'public domain' or 'royalties required'.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'recommended': True,
         'slot_uri': 'dcterms:type'} })


class LinguisticSystem(SupportiveEntity):
    """
    See [DCAT-AP specs:LinguisticSystem](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LinguisticSystem)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:LinguisticSystem',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Location(SupportiveEntity):
    """
    See [DCAT-AP specs:Location](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Location)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:Location',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'bbox': {'description': 'The geographic bounding box of a '
                                                'resource.',
                                 'inlined_as_list': False,
                                 'multivalued': False,
                                 'name': 'bbox',
                                 'range': 'string',
                                 'recommended': True,
                                 'required': False,
                                 'slot_uri': 'dcat:bbox'},
                        'centroid': {'description': 'The geographic center (centroid) '
                                                    'of a resource.',
                                     'inlined_as_list': False,
                                     'multivalued': False,
                                     'name': 'centroid',
                                     'range': 'string',
                                     'recommended': True,
                                     'required': False,
                                     'slot_uri': 'dcat:centroid'},
                        'geometry': {'description': 'The corresponding geometry for a '
                                                    'resource.',
                                     'inlined_as_list': False,
                                     'multivalued': False,
                                     'name': 'geometry',
                                     'range': 'Geometry',
                                     'required': False,
                                     'slot_uri': 'locn:geometry'}}})

    bbox: Optional[str] = Field(default=None, description="""The geographic bounding box of a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'bbox',
         'domain_of': ['Location'],
         'recommended': True,
         'slot_uri': 'dcat:bbox'} })
    centroid: Optional[str] = Field(default=None, description="""The geographic center (centroid) of a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'centroid',
         'domain_of': ['Location'],
         'recommended': True,
         'slot_uri': 'dcat:centroid'} })
    geometry: Optional[Geometry] = Field(default=None, description="""The corresponding geometry for a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'geometry', 'domain_of': ['Location'], 'slot_uri': 'locn:geometry'} })


class MediaType(SupportiveEntity):
    """
    See [DCAT-AP specs:MediaType](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaType)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:MediaType',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class MediaTypeOrExtent(SupportiveEntity):
    """
    See [DCAT-AP specs:MediaTypeOrExtent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaTypeOrExtent)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:MediaTypeOrExtent',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class PeriodOfTime(SupportiveEntity):
    """
    See [DCAT-AP specs:PeriodOfTime](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#PeriodOfTime)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:PeriodOfTime',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'beginning': {'description': 'The beginning of a period or '
                                                     'interval.',
                                      'inlined_as_list': True,
                                      'multivalued': False,
                                      'name': 'beginning',
                                      'range': 'TimeInstant',
                                      'required': False,
                                      'slot_uri': 'time:hasBeginning'},
                        'end': {'description': 'The end of a period or interval.',
                                'inlined_as_list': True,
                                'multivalued': False,
                                'name': 'end',
                                'range': 'TimeInstant',
                                'required': False,
                                'slot_uri': 'time:hasEnd'},
                        'end_date': {'description': 'The end of the period.',
                                     'inlined_as_list': True,
                                     'multivalued': False,
                                     'name': 'end_date',
                                     'range': 'string',
                                     'recommended': True,
                                     'required': False,
                                     'slot_uri': 'dcat:endDate'},
                        'start_date': {'description': 'The start of the period.',
                                       'inlined_as_list': False,
                                       'multivalued': False,
                                       'name': 'start_date',
                                       'range': 'string',
                                       'recommended': True,
                                       'required': False,
                                       'slot_uri': 'dcat:startDate'}}})

    beginning: Optional[TimeInstant] = Field(default=None, description="""The beginning of a period or interval.""", json_schema_extra = { "linkml_meta": {'alias': 'beginning',
         'domain_of': ['PeriodOfTime'],
         'slot_uri': 'time:hasBeginning'} })
    end: Optional[TimeInstant] = Field(default=None, description="""The end of a period or interval.""", json_schema_extra = { "linkml_meta": {'alias': 'end', 'domain_of': ['PeriodOfTime'], 'slot_uri': 'time:hasEnd'} })
    end_date: Optional[str] = Field(default=None, description="""The end of the period.""", json_schema_extra = { "linkml_meta": {'alias': 'end_date',
         'domain_of': ['PeriodOfTime'],
         'recommended': True,
         'slot_uri': 'dcat:endDate'} })
    start_date: Optional[str] = Field(default=None, description="""The start of the period.""", json_schema_extra = { "linkml_meta": {'alias': 'start_date',
         'domain_of': ['PeriodOfTime'],
         'recommended': True,
         'slot_uri': 'dcat:startDate'} })


class Policy(SupportiveEntity):
    """
    See [DCAT-AP specs:Policy](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Policy)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'odrl:Policy',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class ProvenanceStatement(SupportiveEntity):
    """
    See [DCAT-AP specs:ProvenanceStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ProvenanceStatement)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:ProvenanceStatement',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Relationship(SupportiveEntity):
    """
    See [DCAT-AP specs:Relationship](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Relationship)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcat:Relationship',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml',
         'slot_usage': {'had_role': {'description': 'A function of an entity or agent '
                                                    'with respect to another entity or '
                                                    'resource.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'had_role',
                                     'range': 'Role',
                                     'required': True,
                                     'slot_uri': 'dcat:hadRole'},
                        'relation': {'description': 'A resource related to the source '
                                                    'resource.',
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'relation',
                                     'range': 'Resource',
                                     'required': True,
                                     'slot_uri': 'dcterms:relation'}}})

    had_role: List[Role] = Field(default=..., description="""A function of an entity or agent with respect to another entity or resource.""", json_schema_extra = { "linkml_meta": {'alias': 'had_role', 'domain_of': ['Relationship'], 'slot_uri': 'dcat:hadRole'} })
    relation: List[Resource] = Field(default=..., description="""A resource related to the source resource.""", json_schema_extra = { "linkml_meta": {'alias': 'relation',
         'domain_of': ['Relationship'],
         'slot_uri': 'dcterms:relation'} })


class Resource(SupportiveEntity):
    """
    See [DCAT-AP specs:Resource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Resource)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'rdfs:Resource',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class RightsStatement(SupportiveEntity):
    """
    See [DCAT-AP specs:RightsStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#RightsStatement)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:RightsStatement',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Role(SupportiveEntity):
    """
    See [DCAT-AP specs:Role](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Role)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcat:Role',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class Standard(SupportiveEntity):
    """
    See [DCAT-AP specs:Standard](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Standard)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'dcterms:Standard',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class TimeInstant(SupportiveEntity):
    """
    See [DCAT-AP specs:TimeInstant](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TimeInstant)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': False,
         'class_uri': 'time:Instant',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml'})

    pass


class ClassifierMixin(ConfiguredBaseModel):
    """
    A mixin with which an entity of this schema can be classified via an additional rdf:type assertion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'mixin': True,
         'slot_usage': {'type': {'inlined': True,
                                 'name': 'type',
                                 'range': 'DefinedTerm'}}})

    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class DefinedTerm(ConfiguredBaseModel):
    """
    A word, name, acronym, phrase that is defined in a controlled vocabulary (CV) and that is used to provide an additional rdf:type or dcterms:type of a class within this schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:DefinedTerm',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'slot_usage': {'title': {'name': 'title', 'slot_uri': 'schema:name'}}})

    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'schema:name'} })
    from_CV: Optional[str] = Field(default=None, description="""The URL of the controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'alias': 'from_CV',
         'domain_of': ['DefinedTerm'],
         'slot_uri': 'schema:inDefinedTermSet'} })


class ResearchDataset(Dataset):
    """
    A collection of data, published or curated by a single agent, and available for access or download in one or more representations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Dataset',
         'comments': ['The name of this class is only deviating from its parent as '
                      'this is needed according to the sub-classing strategy chosen '
                      'here in this LinkML model to further constrain the slots of '
                      'existing (imported) classes.'],
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'slot_usage': {'was_generated_by': {'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'was_generated_by',
                                             'range': 'DataCreatingActivity',
                                             'required': True}},
         'tree_root': True})

    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    describes_entity: Optional[List[EvaluatedEntity]] = Field(default=None, description="""A slot to provide the EvaluatedEntity that is described by a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'describes_entity',
         'domain_of': ['ResearchDataset'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'dcterms:relation'} })
    describes_activity: Optional[List[EvaluatedActivity]] = Field(default=None, description="""A slot to provide the EvaluatedActivity that is described by a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'describes_activity',
         'domain_of': ['ResearchDataset'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'dcterms:relation'} })
    access_rights: Optional[RightsStatement] = Field(default=None, description="""Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public.""", json_schema_extra = { "linkml_meta": {'alias': 'access_rights',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcterms:accessRights'} })
    applicable_legislation: Optional[List[LegalResource]] = Field(default=None, description="""The legislation that mandates the creation or management of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'applicable_legislation',
         'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    conforms_to: Optional[List[Standard]] = Field(default=None, description="""An implementing rule or other specification.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcterms:conformsTo'} })
    contact_point: Optional[List[Kind]] = Field(default=None, description="""Contact information that can be used for sending comments about the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_point',
         'domain_of': ['DataService', 'Dataset', 'DatasetSeries'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    creator: Optional[List[Agent]] = Field(default=None, description="""An entity responsible for producing the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Catalogue', 'Dataset'],
         'slot_uri': 'dcterms:creator'} })
    dataset_distribution: Optional[List[Distribution]] = Field(default=None, description="""An available Distribution for the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_distribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:distribution'} })
    description: List[str] = Field(default=..., description="""A free-text account of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    documentation: Optional[List[Document]] = Field(default=None, description="""A page or document about this Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'documentation',
         'domain_of': ['DataService', 'Dataset', 'Distribution'],
         'slot_uri': 'foaf:page'} })
    frequency: Optional[Frequency] = Field(default=None, description="""The frequency at which the Dataset is updated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'domain_of': ['Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:accrualPeriodicity'} })
    geographical_coverage: Optional[List[Location]] = Field(default=None, description="""A geographic region that is covered by the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'geographical_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:spatial'} })
    has_version: Optional[List[Dataset]] = Field(default=None, description="""A related Dataset that is a version, edition, or adaptation of the described Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_version',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:hasVersion'} })
    identifier: Optional[List[str]] = Field(default=None, description="""The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:identifier'} })
    in_series: Optional[List[DatasetSeries]] = Field(default=None, description="""A dataset series of which the dataset is part.""", json_schema_extra = { "linkml_meta": {'alias': 'in_series', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:inSeries'} })
    is_referenced_by: Optional[List[Resource]] = Field(default=None, description="""A related resource, such as a publication, that references, cites, or otherwise points to the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'is_referenced_by',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:isReferencedBy'} })
    keyword: Optional[List[str]] = Field(default=None, description="""A keyword or tag describing the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'keyword',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:keyword'} })
    landing_page: Optional[List[Document]] = Field(default=None, description="""A web page that provides access to the Dataset, its Distributions and/or additional information.""", json_schema_extra = { "linkml_meta": {'alias': 'landing_page',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcat:landingPage'} })
    language: Optional[List[LinguisticSystem]] = Field(default=None, description="""A language of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'language',
         'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dcterms:language'} })
    modification_date: Optional[str] = Field(default=None, description="""The most recent date on which the Dataset was changed or modified.""", json_schema_extra = { "linkml_meta": {'alias': 'modification_date',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcterms:modified'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the Dataset""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    provenance: Optional[List[ProvenanceStatement]] = Field(default=None, description="""A statement about the lineage of a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'provenance',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:provenance'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity (organisation) responsible for making the Dataset available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:publisher'} })
    qualified_attribution: Optional[List[Attribution]] = Field(default=None, description="""An Agent having some form of responsibility for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'qualified_attribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'prov:qualifiedAttribution'} })
    qualified_relation: Optional[List[Relationship]] = Field(default=None, description="""A description of a relationship with another resource.""", json_schema_extra = { "linkml_meta": {'alias': 'qualified_relation',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:qualifiedRelation'} })
    related_resource: Optional[List[Resource]] = Field(default=None, description="""A related resource.""", json_schema_extra = { "linkml_meta": {'alias': 'related_resource',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:relation'} })
    release_date: Optional[str] = Field(default=None, description="""The date of formal issuance (e.g., publication) of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dcterms:issued'} })
    sample: Optional[List[Distribution]] = Field(default=None, description="""A sample distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'sample', 'domain_of': ['Dataset'], 'slot_uri': 'adms:sample'} })
    source: Optional[List[Dataset]] = Field(default=None, description="""A related Dataset from which the described Dataset is derived.""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['Dataset'], 'slot_uri': 'dcterms:source'} })
    spatial_resolution: Optional[Decimal] = Field(default=None, description="""The minimum spatial separation resolvable in a dataset, measured in meters.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:spatialResolutionInMeters'} })
    temporal_coverage: Optional[List[PeriodOfTime]] = Field(default=None, description="""A temporal period that the Dataset covers.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:temporal'} })
    temporal_resolution: Optional[str] = Field(default=None, description="""The minimum time period resolvable in the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:temporalResolution'} })
    theme: Optional[List[Concept]] = Field(default=None, description="""A category of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'theme',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:theme'} })
    title: List[str] = Field(default=..., description="""A name given to the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    type: Optional[List[Concept]] = Field(default=None, description="""A type of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    version: Optional[str] = Field(default=None, description="""The version indicator (name or identifier) of a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:version'} })
    version_notes: Optional[List[str]] = Field(default=None, description="""A description of the differences between this version and a previous version of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'version_notes',
         'domain_of': ['Dataset'],
         'slot_uri': 'adms:versionNotes'} })
    was_generated_by: List[DataCreatingActivity] = Field(default=..., description="""An activity that generated, or provides the business context for, the creation of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Dataset', 'EvaluatedEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })


class AnalysisDataset(ResearchDataset):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Dataset',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'slot_usage': {'was_generated_by': {'name': 'was_generated_by',
                                             'range': 'DataAnalysis'}}})

    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    describes_entity: Optional[List[EvaluatedEntity]] = Field(default=None, description="""A slot to provide the EvaluatedEntity that is described by a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'describes_entity',
         'domain_of': ['ResearchDataset'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'dcterms:relation'} })
    describes_activity: Optional[List[EvaluatedActivity]] = Field(default=None, description="""A slot to provide the EvaluatedActivity that is described by a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'describes_activity',
         'domain_of': ['ResearchDataset'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'dcterms:relation'} })
    access_rights: Optional[RightsStatement] = Field(default=None, description="""Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public.""", json_schema_extra = { "linkml_meta": {'alias': 'access_rights',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcterms:accessRights'} })
    applicable_legislation: Optional[List[LegalResource]] = Field(default=None, description="""The legislation that mandates the creation or management of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'applicable_legislation',
         'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    conforms_to: Optional[List[Standard]] = Field(default=None, description="""An implementing rule or other specification.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcterms:conformsTo'} })
    contact_point: Optional[List[Kind]] = Field(default=None, description="""Contact information that can be used for sending comments about the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_point',
         'domain_of': ['DataService', 'Dataset', 'DatasetSeries'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    creator: Optional[List[Agent]] = Field(default=None, description="""An entity responsible for producing the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Catalogue', 'Dataset'],
         'slot_uri': 'dcterms:creator'} })
    dataset_distribution: Optional[List[Distribution]] = Field(default=None, description="""An available Distribution for the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_distribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:distribution'} })
    description: List[str] = Field(default=..., description="""A free-text account of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    documentation: Optional[List[Document]] = Field(default=None, description="""A page or document about this Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'documentation',
         'domain_of': ['DataService', 'Dataset', 'Distribution'],
         'slot_uri': 'foaf:page'} })
    frequency: Optional[Frequency] = Field(default=None, description="""The frequency at which the Dataset is updated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'domain_of': ['Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:accrualPeriodicity'} })
    geographical_coverage: Optional[List[Location]] = Field(default=None, description="""A geographic region that is covered by the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'geographical_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:spatial'} })
    has_version: Optional[List[Dataset]] = Field(default=None, description="""A related Dataset that is a version, edition, or adaptation of the described Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_version',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:hasVersion'} })
    identifier: Optional[List[str]] = Field(default=None, description="""The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:identifier'} })
    in_series: Optional[List[DatasetSeries]] = Field(default=None, description="""A dataset series of which the dataset is part.""", json_schema_extra = { "linkml_meta": {'alias': 'in_series', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:inSeries'} })
    is_referenced_by: Optional[List[Resource]] = Field(default=None, description="""A related resource, such as a publication, that references, cites, or otherwise points to the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'is_referenced_by',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:isReferencedBy'} })
    keyword: Optional[List[str]] = Field(default=None, description="""A keyword or tag describing the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'keyword',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:keyword'} })
    landing_page: Optional[List[Document]] = Field(default=None, description="""A web page that provides access to the Dataset, its Distributions and/or additional information.""", json_schema_extra = { "linkml_meta": {'alias': 'landing_page',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcat:landingPage'} })
    language: Optional[List[LinguisticSystem]] = Field(default=None, description="""A language of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'language',
         'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dcterms:language'} })
    modification_date: Optional[str] = Field(default=None, description="""The most recent date on which the Dataset was changed or modified.""", json_schema_extra = { "linkml_meta": {'alias': 'modification_date',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcterms:modified'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the Dataset""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    provenance: Optional[List[ProvenanceStatement]] = Field(default=None, description="""A statement about the lineage of a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'provenance',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:provenance'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity (organisation) responsible for making the Dataset available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:publisher'} })
    qualified_attribution: Optional[List[Attribution]] = Field(default=None, description="""An Agent having some form of responsibility for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'qualified_attribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'prov:qualifiedAttribution'} })
    qualified_relation: Optional[List[Relationship]] = Field(default=None, description="""A description of a relationship with another resource.""", json_schema_extra = { "linkml_meta": {'alias': 'qualified_relation',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:qualifiedRelation'} })
    related_resource: Optional[List[Resource]] = Field(default=None, description="""A related resource.""", json_schema_extra = { "linkml_meta": {'alias': 'related_resource',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:relation'} })
    release_date: Optional[str] = Field(default=None, description="""The date of formal issuance (e.g., publication) of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dcterms:issued'} })
    sample: Optional[List[Distribution]] = Field(default=None, description="""A sample distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'sample', 'domain_of': ['Dataset'], 'slot_uri': 'adms:sample'} })
    source: Optional[List[Dataset]] = Field(default=None, description="""A related Dataset from which the described Dataset is derived.""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['Dataset'], 'slot_uri': 'dcterms:source'} })
    spatial_resolution: Optional[Decimal] = Field(default=None, description="""The minimum spatial separation resolvable in a dataset, measured in meters.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:spatialResolutionInMeters'} })
    temporal_coverage: Optional[List[PeriodOfTime]] = Field(default=None, description="""A temporal period that the Dataset covers.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:temporal'} })
    temporal_resolution: Optional[str] = Field(default=None, description="""The minimum time period resolvable in the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:temporalResolution'} })
    theme: Optional[List[Concept]] = Field(default=None, description="""A category of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'theme',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:theme'} })
    title: List[str] = Field(default=..., description="""A name given to the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    type: Optional[List[Concept]] = Field(default=None, description="""A type of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    version: Optional[str] = Field(default=None, description="""The version indicator (name or identifier) of a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:version'} })
    version_notes: Optional[List[str]] = Field(default=None, description="""A description of the differences between this version and a previous version of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'version_notes',
         'domain_of': ['Dataset'],
         'slot_uri': 'adms:versionNotes'} })
    was_generated_by: List[DataAnalysis] = Field(default=..., description="""An activity that generated, or provides the business context for, the creation of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Dataset', 'EvaluatedEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })


class ResearchCatalog(Catalogue):
    """
    A curated collection of metadata about data resources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Catalog',
         'comments': ['The name of this class is only deviating from its parent as '
                      'this is needed according to the sub-classing strategy chosen '
                      'here in this LinkML model to further constrain the slots of '
                      'existing (imported) classes.'],
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'slot_usage': {'has_dataset': {'name': 'has_dataset',
                                        'range': 'ResearchDataset'}}})

    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    applicable_legislation: Optional[List[LegalResource]] = Field(default=None, description="""The legislation that mandates the creation or management of the Catalog.""", json_schema_extra = { "linkml_meta": {'alias': 'applicable_legislation',
         'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    catalogue: Optional[List[Catalogue]] = Field(default=None, description="""A catalogue whose contents are of interest in the context of this catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'catalogue', 'domain_of': ['Catalogue'], 'slot_uri': 'dcat:catalog'} })
    creator: Optional[Agent] = Field(default=None, description="""An entity responsible for the creation of the catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Catalogue', 'Dataset'],
         'slot_uri': 'dcterms:creator'} })
    description: List[str] = Field(default=..., description="""A free-text account of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    geographical_coverage: Optional[List[Location]] = Field(default=None, description="""A geographical area covered by the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'geographical_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:spatial'} })
    has_dataset: Optional[List[ResearchDataset]] = Field(default=None, description="""A Dataset that is part of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'has_dataset', 'domain_of': ['Catalogue'], 'slot_uri': 'dcat:dataset'} })
    has_part: Optional[List[Catalogue]] = Field(default=None, description="""A related Catalogue that is part of the described Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    homepage: Optional[Document] = Field(default=None, description="""A web page that acts as the main page for the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'homepage',
         'domain_of': ['Catalogue'],
         'recommended': True,
         'slot_uri': 'foaf:homepage'} })
    language: Optional[List[LinguisticSystem]] = Field(default=None, description="""A language used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'language',
         'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'recommended': True,
         'slot_uri': 'dcterms:language'} })
    licence: Optional[LicenseDocument] = Field(default=None, description="""A licence under which the Catalogue can be used or reused.""", json_schema_extra = { "linkml_meta": {'alias': 'licence',
         'domain_of': ['Catalogue', 'DataService', 'Distribution'],
         'slot_uri': 'dcterms:license'} })
    modification_date: Optional[str] = Field(default=None, description="""The most recent date on which the Catalogue was modified.""", json_schema_extra = { "linkml_meta": {'alias': 'modification_date',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'recommended': True,
         'slot_uri': 'dcterms:modified'} })
    publisher: Agent = Field(default=..., description="""An entity (organisation) responsible for making the Catalogue available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:publisher'} })
    record: Optional[List[CatalogueRecord]] = Field(default=None, description="""A Catalogue Record that is part of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'record', 'domain_of': ['Catalogue'], 'slot_uri': 'dcat:record'} })
    release_date: Optional[str] = Field(default=None, description="""The date of formal issuance (e.g., publication) of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'recommended': True,
         'slot_uri': 'dcterms:issued'} })
    rights: Optional[RightsStatement] = Field(default=None, description="""A statement that specifies rights associated with the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'rights',
         'domain_of': ['Catalogue', 'Distribution'],
         'slot_uri': 'dcterms:rights'} })
    service: Optional[List[DataService]] = Field(default=None, description="""A site or end-point (Data Service) that is listed in the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'service', 'domain_of': ['Catalogue'], 'slot_uri': 'dcat:service'} })
    temporal_coverage: Optional[List[PeriodOfTime]] = Field(default=None, description="""A temporal period that the Catalogue covers.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:temporal'} })
    themes: Optional[List[ConceptScheme]] = Field(default=None, description="""A knowledge organization system used to classify the Resources that are in the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'themes',
         'domain_of': ['Catalogue'],
         'recommended': True,
         'slot_uri': 'dcat:themeTaxonomy'} })
    title: List[str] = Field(default=..., description="""A name given to the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })


class DataCreatingActivity(ClassifierMixin, Activity):
    """
    An activity (process) that has the objective to produce information about an entity or activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'mixins': ['ClassifierMixin'],
         'narrow_mappings': ['NCIT:C25598', 'sosa:Observation', 'OBI:0000070'],
         'slot_usage': {'has_part': {'description': 'A slot to provide an Activity '
                                                    'that is part of the '
                                                    'DataCreatingActivity.',
                                     'inlined': True,
                                     'name': 'has_part',
                                     'range': 'Activity'},
                        'other_identifier': {'description': 'A secondary identifier of '
                                                            'the DataCreatingActivity',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'other_identifier',
                                             'range': 'Identifier',
                                             'required': False,
                                             'slot_uri': 'adms:identifier'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the DataCreatingActivity""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    evaluated_entity: Optional[List[EvaluatedEntity]] = Field(default=None, description="""The slot to specify the entity of interest that was evaluated.""", json_schema_extra = { "linkml_meta": {'alias': 'evaluated_entity',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    evaluated_activity: Optional[List[EvaluatedActivity]] = Field(default=None, description="""The slot to specify the activity of interest that was evaluated.""", json_schema_extra = { "linkml_meta": {'alias': 'evaluated_activity',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:wasInformedBy'} })
    used_tool: Optional[List[Tool]] = Field(default=None, description="""The slot to specify the tool that was used.""", json_schema_extra = { "linkml_meta": {'alias': 'used_tool',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    realized_plan: Optional[Plan] = Field(default=None, description="""The slot to specify the Method (aka Procedure) that was realized by a DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'realized_plan',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    has_part: Optional[Activity] = Field(default=None, description="""A slot to provide an Activity that is part of the DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    occurred_in: Optional[Environment] = Field(default=None, description="""The slot to specify the Method (aka Procedure) that was used in the DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'occurred_in',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'BFO:0000066'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class DataAnalysis(DataCreatingActivity):
    """
    A DataCreatingActivity that evaluates the data produced by another DataCreatingActivity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity',
         'close_mappings': ['http://purl.obolibrary.org/obo/NCIT_C25391'],
         'exact_mappings': ['OBI:0200000'],
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'slot_usage': {'evaluated_entity': {'name': 'evaluated_entity',
                                             'range': 'AnalysisSourceData'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the DataCreatingActivity""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    evaluated_entity: Optional[List[AnalysisSourceData]] = Field(default=None, description="""The slot to specify the entity of interest that was evaluated.""", json_schema_extra = { "linkml_meta": {'alias': 'evaluated_entity',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    evaluated_activity: Optional[List[EvaluatedActivity]] = Field(default=None, description="""The slot to specify the activity of interest that was evaluated.""", json_schema_extra = { "linkml_meta": {'alias': 'evaluated_activity',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:wasInformedBy'} })
    used_tool: Optional[List[Tool]] = Field(default=None, description="""The slot to specify the tool that was used.""", json_schema_extra = { "linkml_meta": {'alias': 'used_tool',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    realized_plan: Optional[Plan] = Field(default=None, description="""The slot to specify the Method (aka Procedure) that was realized by a DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'realized_plan',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    has_part: Optional[Activity] = Field(default=None, description="""A slot to provide an Activity that is part of the DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    occurred_in: Optional[Environment] = Field(default=None, description="""The slot to specify the Method (aka Procedure) that was used in the DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'occurred_in',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'BFO:0000066'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class EvaluatedEntity(ClassifierMixin):
    """
    A physical, digital, conceptual, or other kind of thing with some fixed aspects that is not an activity or process and that is being evaluated in a DataCreatingActivity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'mixins': ['ClassifierMixin'],
         'slot_usage': {'has_part': {'description': 'A slot to provide a part of the '
                                                    'EvaluatedEntity.',
                                     'name': 'has_part',
                                     'range': 'EvaluatedEntity'},
                        'other_identifier': {'description': 'A slot to provide a '
                                                            'secondary identifier of '
                                                            'the EvaluatedEntity.',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'other_identifier',
                                             'range': 'Identifier',
                                             'required': False,
                                             'slot_uri': 'adms:identifier'},
                        'was_generated_by': {'description': 'A slot to provide the '
                                                            'Activity which created '
                                                            'the EvaluatedEntity.',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'was_generated_by',
                                             'range': 'Activity'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A slot to provide a secondary identifier of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[str] = Field(default=None, description="""A slot to provide a part of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    was_generated_by: Optional[List[Activity]] = Field(default=None, description="""A slot to provide the Activity which created the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Dataset', 'EvaluatedEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class AnalysisSourceData(EvaluatedEntity):
    """
    Information that was evaluated within a DataAnalysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'slot_usage': {'was_generated_by': {'name': 'was_generated_by',
                                             'range': 'DataCreatingActivity'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A slot to provide a secondary identifier of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[str] = Field(default=None, description="""A slot to provide a part of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    was_generated_by: Optional[List[DataCreatingActivity]] = Field(default=None, description="""A slot to provide the Activity which created the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Dataset', 'EvaluatedEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class EvaluatedActivity(ClassifierMixin, Activity):
    """
    An activity or process that is being evaluated in a DataCreatingActivity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'mixins': ['ClassifierMixin'],
         'slot_usage': {'has_part': {'description': 'A slot to provide a part of the '
                                                    'EvaluatedActivity.',
                                     'name': 'has_part',
                                     'range': 'EvaluatedActivity'},
                        'other_identifier': {'description': 'A secondary identifier of '
                                                            'the EvaluatedActivity',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'other_identifier',
                                             'range': 'Identifier',
                                             'required': False,
                                             'slot_uri': 'adms:identifier'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the EvaluatedActivity""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[str] = Field(default=None, description="""A slot to provide a part of the EvaluatedActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class Tool(ClassifierMixin):
    """
    A entity with a certain function used within a DataCreatingActivity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['prov:Entity'],
         'class_uri': 'prov:Entity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'mixins': ['ClassifierMixin'],
         'slot_usage': {'has_part': {'description': 'The slot to specify parts of a '
                                                    'tool.',
                                     'inlined': True,
                                     'inlined_as_list': True,
                                     'multivalued': True,
                                     'name': 'has_part',
                                     'range': 'Tool'},
                        'other_identifier': {'description': 'A secondary identifier of '
                                                            'the EvaluatedActivity',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'other_identifier',
                                             'range': 'Identifier',
                                             'required': False,
                                             'slot_uri': 'adms:identifier'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the EvaluatedActivity""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[List[Tool]] = Field(default=None, description="""The slot to specify parts of a tool.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class HardwareTool(Tool):
    """
    A hardware device with a certain function that was used within a DataCreatingActivity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Device'],
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core']})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the EvaluatedActivity""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[List[Tool]] = Field(default=None, description="""The slot to specify parts of a tool.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class SoftwareTool(Tool):
    """
    A software program with a certain function that was used within a DataCreatingActivity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core']})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the EvaluatedActivity""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[List[Tool]] = Field(default=None, description="""The slot to specify parts of a tool.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class Environment(ClassifierMixin):
    """
    The surrounding in which the dataset creating activity took place (e.g. a lab).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'mixins': ['ClassifierMixin'],
         'slot_usage': {'other_identifier': {'description': 'A secondary identifier of '
                                                            'the Environment',
                                             'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'other_identifier',
                                             'range': 'Identifier',
                                             'required': False,
                                             'slot_uri': 'adms:identifier'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the Environment""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class Plan(ClassifierMixin):
    """
    A piece of information that specifies how an activity has to be carried out by its agents including what kind of steps have to be taken and what kind of parameters have to be met/set.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Plan Specification', 'Method', 'Procedure'],
         'class_uri': 'prov:Entity',
         'examples': [{'description': 'We assigned the structure of sample CRS-37013 '
                                      'using a 13C NMR (CHMO:0000595) and the '
                                      'settings: pulse sequence: zgpg30, temperature: '
                                      '298.0 K, number of scans: 1024, Solvent : '
                                      'chloroform-D1 (CDCl3).'}],
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'mixins': ['ClassifierMixin']})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class QualitativeAttribute(ClassifierMixin):
    """
    A piece of information that is attributed to an entity of interest, tool or environment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'mixins': ['ClassifierMixin'],
         'slot_usage': {'value': {'description': 'The slot to provide the literal '
                                                 'value of the QualitativeAttribute.',
                                  'name': 'value',
                                  'required': True}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    value: str = Field(default=..., description="""The slot to provide the literal value of the QualitativeAttribute.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['QualitativeAttribute', 'QuantitativeAttribute'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'prov:value'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class QuantitativeAttribute(ClassifierMixin):
    """
    A quantifiable piece of information that is attributed to an entity of interest, tool or environment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Quantity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/',
         'in_subset': ['domain_agnostic_core'],
         'mixins': ['ClassifierMixin'],
         'slot_usage': {'value': {'description': 'The slot to provide the literal '
                                                 'value of the QuantitativeAttribute.',
                                  'name': 'value',
                                  'range': 'float',
                                  'required': True}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    value: float = Field(default=..., description="""The slot to provide the literal value of the QuantitativeAttribute.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['QualitativeAttribute', 'QuantitativeAttribute'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'prov:value'} })
    has_quantity_type: str = Field(default=..., description="""The type of quality that is quantifiable according to the QUDT ontology.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantity_type',
         'bindings': [{'binds_value_of': 'id',
                       'description': 'Binds the type of a quantifiable attribute to a '
                                      'QUDT Quantity Kind instance from the QUDT '
                                      'Quantity Kind vocabulary.',
                       'obligation_level': 'RECOMMENDED',
                       'range': 'QUDTQuantityKindEnum'}],
         'domain_of': ['QuantitativeAttribute'],
         'slot_uri': 'qudt:hasQuantityKind'} })
    unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'unit',
         'bindings': [{'binds_value_of': 'id',
                       'description': 'Restricts the allowable defined terms to the '
                                      'QUDT Unit vocabulary.',
                       'obligation_level': 'RECOMMENDED',
                       'range': 'QUDTUnitEnum'}],
         'domain_of': ['QuantitativeAttribute'],
         'recommended': True,
         'slot_uri': 'qudt:unit'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class NMRAnalysisDataset(AnalysisDataset):
    """
    A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dcat:Dataset',
         'comments': ['This class serves as an example for the way in which we want to '
                      'build domain specific schema profiles. It will be outsourced to '
                      'a more appropriate location in the future.'],
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap',
         'slot_usage': {'describes_entity': {'name': 'describes_entity',
                                             'range': 'ChemicalSample'},
                        'was_generated_by': {'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'was_generated_by',
                                             'range': 'NMRSpectralAnalysis'}}})

    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    describes_entity: Optional[List[ChemicalSample]] = Field(default=None, description="""A slot to provide the EvaluatedEntity that is described by a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'describes_entity',
         'domain_of': ['ResearchDataset'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'dcterms:relation'} })
    describes_activity: Optional[List[EvaluatedActivity]] = Field(default=None, description="""A slot to provide the EvaluatedActivity that is described by a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'describes_activity',
         'domain_of': ['ResearchDataset'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'dcterms:relation'} })
    access_rights: Optional[RightsStatement] = Field(default=None, description="""Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public.""", json_schema_extra = { "linkml_meta": {'alias': 'access_rights',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcterms:accessRights'} })
    applicable_legislation: Optional[List[LegalResource]] = Field(default=None, description="""The legislation that mandates the creation or management of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'applicable_legislation',
         'domain_of': ['Catalogue',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcatap:applicableLegislation'} })
    conforms_to: Optional[List[Standard]] = Field(default=None, description="""An implementing rule or other specification.""", json_schema_extra = { "linkml_meta": {'alias': 'conforms_to',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcterms:conformsTo'} })
    contact_point: Optional[List[Kind]] = Field(default=None, description="""Contact information that can be used for sending comments about the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'contact_point',
         'domain_of': ['DataService', 'Dataset', 'DatasetSeries'],
         'recommended': True,
         'slot_uri': 'dcat:contactPoint'} })
    creator: Optional[List[Agent]] = Field(default=None, description="""An entity responsible for producing the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'creator',
         'domain_of': ['Catalogue', 'Dataset'],
         'slot_uri': 'dcterms:creator'} })
    dataset_distribution: Optional[List[Distribution]] = Field(default=None, description="""An available Distribution for the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'dataset_distribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:distribution'} })
    description: List[str] = Field(default=..., description="""A free-text account of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    documentation: Optional[List[Document]] = Field(default=None, description="""A page or document about this Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'documentation',
         'domain_of': ['DataService', 'Dataset', 'Distribution'],
         'slot_uri': 'foaf:page'} })
    frequency: Optional[Frequency] = Field(default=None, description="""The frequency at which the Dataset is updated.""", json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'domain_of': ['Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:accrualPeriodicity'} })
    geographical_coverage: Optional[List[Location]] = Field(default=None, description="""A geographic region that is covered by the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'geographical_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:spatial'} })
    has_version: Optional[List[Dataset]] = Field(default=None, description="""A related Dataset that is a version, edition, or adaptation of the described Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'has_version',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:hasVersion'} })
    identifier: Optional[List[str]] = Field(default=None, description="""The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue.""", json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:identifier'} })
    in_series: Optional[List[DatasetSeries]] = Field(default=None, description="""A dataset series of which the dataset is part.""", json_schema_extra = { "linkml_meta": {'alias': 'in_series', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:inSeries'} })
    is_referenced_by: Optional[List[Resource]] = Field(default=None, description="""A related resource, such as a publication, that references, cites, or otherwise points to the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'is_referenced_by',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:isReferencedBy'} })
    keyword: Optional[List[str]] = Field(default=None, description="""A keyword or tag describing the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'keyword',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:keyword'} })
    landing_page: Optional[List[Document]] = Field(default=None, description="""A web page that provides access to the Dataset, its Distributions and/or additional information.""", json_schema_extra = { "linkml_meta": {'alias': 'landing_page',
         'domain_of': ['DataService', 'Dataset'],
         'slot_uri': 'dcat:landingPage'} })
    language: Optional[List[LinguisticSystem]] = Field(default=None, description="""A language of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'language',
         'domain_of': ['Catalogue', 'CatalogueRecord', 'Dataset', 'Distribution'],
         'slot_uri': 'dcterms:language'} })
    modification_date: Optional[str] = Field(default=None, description="""The most recent date on which the Dataset was changed or modified.""", json_schema_extra = { "linkml_meta": {'alias': 'modification_date',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution'],
         'slot_uri': 'dcterms:modified'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the Dataset""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    provenance: Optional[List[ProvenanceStatement]] = Field(default=None, description="""A statement about the lineage of a Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'provenance',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:provenance'} })
    publisher: Optional[Agent] = Field(default=None, description="""An entity (organisation) responsible for making the Dataset available.""", json_schema_extra = { "linkml_meta": {'alias': 'publisher',
         'domain_of': ['Catalogue', 'DataService', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:publisher'} })
    qualified_attribution: Optional[List[Attribution]] = Field(default=None, description="""An Agent having some form of responsibility for the resource.""", json_schema_extra = { "linkml_meta": {'alias': 'qualified_attribution',
         'domain_of': ['Dataset'],
         'slot_uri': 'prov:qualifiedAttribution'} })
    qualified_relation: Optional[List[Relationship]] = Field(default=None, description="""A description of a relationship with another resource.""", json_schema_extra = { "linkml_meta": {'alias': 'qualified_relation',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcat:qualifiedRelation'} })
    related_resource: Optional[List[Resource]] = Field(default=None, description="""A related resource.""", json_schema_extra = { "linkml_meta": {'alias': 'related_resource',
         'domain_of': ['Dataset'],
         'slot_uri': 'dcterms:relation'} })
    release_date: Optional[str] = Field(default=None, description="""The date of formal issuance (e.g., publication) of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'release_date',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries', 'Distribution'],
         'slot_uri': 'dcterms:issued'} })
    sample: Optional[List[Distribution]] = Field(default=None, description="""A sample distribution of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'sample', 'domain_of': ['Dataset'], 'slot_uri': 'adms:sample'} })
    source: Optional[List[Dataset]] = Field(default=None, description="""A related Dataset from which the described Dataset is derived.""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['Dataset'], 'slot_uri': 'dcterms:source'} })
    spatial_resolution: Optional[Decimal] = Field(default=None, description="""The minimum spatial separation resolvable in a dataset, measured in meters.""", json_schema_extra = { "linkml_meta": {'alias': 'spatial_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:spatialResolutionInMeters'} })
    temporal_coverage: Optional[List[PeriodOfTime]] = Field(default=None, description="""A temporal period that the Dataset covers.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_coverage',
         'domain_of': ['Catalogue', 'Dataset', 'DatasetSeries'],
         'slot_uri': 'dcterms:temporal'} })
    temporal_resolution: Optional[str] = Field(default=None, description="""The minimum time period resolvable in the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'temporal_resolution',
         'domain_of': ['Dataset', 'Distribution'],
         'slot_uri': 'dcat:temporalResolution'} })
    theme: Optional[List[Concept]] = Field(default=None, description="""A category of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'theme',
         'domain_of': ['DataService', 'Dataset'],
         'recommended': True,
         'slot_uri': 'dcat:theme'} })
    title: List[str] = Field(default=..., description="""A name given to the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    type: Optional[List[Concept]] = Field(default=None, description="""A type of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    version: Optional[str] = Field(default=None, description="""The version indicator (name or identifier) of a resource.""", json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['Dataset'], 'slot_uri': 'dcat:version'} })
    version_notes: Optional[List[str]] = Field(default=None, description="""A description of the differences between this version and a previous version of the Dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'version_notes',
         'domain_of': ['Dataset'],
         'slot_uri': 'adms:versionNotes'} })
    was_generated_by: List[NMRSpectralAnalysis] = Field(default=..., description="""An activity that generated, or provides the business context for, the creation of the dataset.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Dataset', 'EvaluatedEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })


class NMRSpectralAnalysis(DataAnalysis):
    """
    A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectrum generated by a NMRSpectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'NMR:1000259',
         'comments': ['This class serves as an example for the way in which we want to '
                      'build domain specific schema profiles. It will be outsourced to '
                      'a more appropriate location in the future.'],
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap',
         'slot_usage': {'evaluated_entity': {'name': 'evaluated_entity',
                                             'range': 'NMRSpectrum'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the DataCreatingActivity""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    evaluated_entity: Optional[List[NMRSpectrum]] = Field(default=None, description="""The slot to specify the entity of interest that was evaluated.""", json_schema_extra = { "linkml_meta": {'alias': 'evaluated_entity',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    evaluated_activity: Optional[List[EvaluatedActivity]] = Field(default=None, description="""The slot to specify the activity of interest that was evaluated.""", json_schema_extra = { "linkml_meta": {'alias': 'evaluated_activity',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:wasInformedBy'} })
    used_tool: Optional[List[Tool]] = Field(default=None, description="""The slot to specify the tool that was used.""", json_schema_extra = { "linkml_meta": {'alias': 'used_tool',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    realized_plan: Optional[Plan] = Field(default=None, description="""The slot to specify the Method (aka Procedure) that was realized by a DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'realized_plan',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    has_part: Optional[Activity] = Field(default=None, description="""A slot to provide an Activity that is part of the DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    occurred_in: Optional[Environment] = Field(default=None, description="""The slot to specify the Method (aka Procedure) that was used in the DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'occurred_in',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'BFO:0000066'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class NMRSpectroscopy(DataCreatingActivity):
    """
    Spectroscopy where the energy states of spin-active nuclei placed in a static magnetic field are interrogated by inducing transitions between the states via radio frequency irradiation. Each experiment consists of a sequence of radio frequency pulses with delay periods in between them.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['This class serves as an example for the way in which we want to '
                      'build domain specific schema profiles. It will be outsourced to '
                      'a more appropriate location in the future.'],
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap',
         'slot_usage': {'evaluated_entity': {'name': 'evaluated_entity',
                                             'range': 'ChemicalSample'},
                        'rdf_type': {'bindings': [{'binds_value_of': 'id',
                                                   'description': 'NMR types from the '
                                                                  'Chemical Methods '
                                                                  'Ontology',
                                                   'obligation_level': 'RECOMMENDED',
                                                   'range': 'NMRAssayEnum'}],
                                     'description': 'The type of NMR Spectroscopy '
                                                    'provided as CURIE of a subclass '
                                                    'of CHMO:0000613.',
                                     'name': 'rdf_type'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the DataCreatingActivity""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    evaluated_entity: Optional[List[ChemicalSample]] = Field(default=None, description="""The slot to specify the entity of interest that was evaluated.""", json_schema_extra = { "linkml_meta": {'alias': 'evaluated_entity',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    evaluated_activity: Optional[List[EvaluatedActivity]] = Field(default=None, description="""The slot to specify the activity of interest that was evaluated.""", json_schema_extra = { "linkml_meta": {'alias': 'evaluated_activity',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:wasInformedBy'} })
    used_tool: Optional[List[Tool]] = Field(default=None, description="""The slot to specify the tool that was used.""", json_schema_extra = { "linkml_meta": {'alias': 'used_tool',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    realized_plan: Optional[Plan] = Field(default=None, description="""The slot to specify the Method (aka Procedure) that was realized by a DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'realized_plan',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'prov:used'} })
    has_part: Optional[Activity] = Field(default=None, description="""A slot to provide an Activity that is part of the DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    occurred_in: Optional[Environment] = Field(default=None, description="""The slot to specify the Method (aka Procedure) that was used in the DataCreatingActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'occurred_in',
         'domain_of': ['DataCreatingActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'BFO:0000066'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The type of NMR Spectroscopy provided as CURIE of a subclass of CHMO:0000613.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'bindings': [{'binds_value_of': 'id',
                       'description': 'NMR types from the Chemical Methods Ontology',
                       'obligation_level': 'RECOMMENDED',
                       'range': 'NMRAssayEnum'}],
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class ChemicalReaction(EvaluatedActivity):
    """
    An experimental procedure with the aim of producing a portion of a given compound or mixture.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'RXNO:0000329',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap'})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the EvaluatedActivity""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[str] = Field(default=None, description="""A slot to provide a part of the EvaluatedActivity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class ChemicalSubstance(EvaluatedEntity):
    """
    A portion of matter of constant composition, composed of molecular entities of the same type or of different types that is being evaluated in a scientific process.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap'})

    has_role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_role', 'domain_of': ['ChemicalSubstance']} })
    composed_of: Optional[List[ChemicalEntity]] = Field(default=None, description="""The slot to provide the chemical entities of which the chemical substance is composed of.""", json_schema_extra = { "linkml_meta": {'alias': 'composed_of',
         'domain_of': ['ChemicalSubstance'],
         'exact_mappings': ['BFO:0000051'],
         'recommended': True} })
    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A slot to provide a secondary identifier of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[str] = Field(default=None, description="""A slot to provide a part of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    was_generated_by: Optional[List[Activity]] = Field(default=None, description="""A slot to provide the Activity which created the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Dataset', 'EvaluatedEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class ChemicalEntity(ConfiguredBaseModel):
    """
    Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHEBI:23367',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap'})

    inchi: Optional[InChi] = Field(default=None, description="""The slot to provide the InChi descriptor of a chemical substance.""", json_schema_extra = { "linkml_meta": {'alias': 'inchi', 'domain_of': ['ChemicalEntity']} })
    inchikey: Optional[InChIKey] = Field(default=None, description="""The slot to provide the InChiKey of a chemical substance.""", json_schema_extra = { "linkml_meta": {'alias': 'inchikey', 'domain_of': ['ChemicalEntity']} })
    smiles: Optional[SMILES] = Field(default=None, description="""The slot to provide the canonical SMILES descriptor of a chemical substance.""", json_schema_extra = { "linkml_meta": {'alias': 'smiles', 'domain_of': ['ChemicalEntity']} })
    iupac_formula: Optional[IUPACChemicalFormula] = Field(default=None, description="""The slot to provide the IUPAC name of a chemical substance.""", json_schema_extra = { "linkml_meta": {'alias': 'iupac_formula', 'domain_of': ['ChemicalEntity']} })


class ChemicalSample(ChemicalSubstance):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap'})

    has_role: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_role', 'domain_of': ['ChemicalSubstance']} })
    composed_of: Optional[List[ChemicalEntity]] = Field(default=None, description="""The slot to provide the chemical entities of which the chemical substance is composed of.""", json_schema_extra = { "linkml_meta": {'alias': 'composed_of',
         'domain_of': ['ChemicalSubstance'],
         'exact_mappings': ['BFO:0000051'],
         'recommended': True} })
    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A slot to provide a secondary identifier of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[str] = Field(default=None, description="""A slot to provide a part of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    was_generated_by: Optional[List[Activity]] = Field(default=None, description="""A slot to provide the Activity which created the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Dataset', 'EvaluatedEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class NMRSpectrum(AnalysisSourceData):
    """
    A set of chemical shifts obtained via NMR spectroscopy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'NMR:1002007',
         'comments': ['This class serves as an example for the way in which we want to '
                      'build domain specific schema profiles. It will be outsourced to '
                      'a more appropriate location in the future.'],
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap',
         'slot_usage': {'was_generated_by': {'inlined_as_list': True,
                                             'multivalued': True,
                                             'name': 'was_generated_by',
                                             'range': 'NMRSpectroscopy'}}})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    id: str = Field(default=..., description="""A slot to provide an URI for an entity within this schema.""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['DefinedTerm',
                       'ResearchDataset',
                       'ResearchCatalog',
                       'EvaluatedEntity',
                       'EvaluatedActivity'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:identifier'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A slot to provide a secondary identifier of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    has_qualitative_attribute: Optional[List[QualitativeAttribute]] = Field(default=None, description="""The slot to relate a qualitative attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_qualitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_quantitative_attribute: Optional[List[QuantitativeAttribute]] = Field(default=None, description="""The slot to relate a quantitative  attribute to an entity of interest, tool or environment.""", json_schema_extra = { "linkml_meta": {'alias': 'has_quantitative_attribute',
         'domain_of': ['EvaluatedEntity', 'EvaluatedActivity', 'Tool'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'dcterms:relation'} })
    has_part: Optional[str] = Field(default=None, description="""A slot to provide a part of the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_part',
         'domain_of': ['Catalogue',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool'],
         'slot_uri': 'dcterms:hasPart'} })
    was_generated_by: Optional[List[NMRSpectroscopy]] = Field(default=None, description="""A slot to provide the Activity which created the EvaluatedEntity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Dataset', 'EvaluatedEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class Laboratory(Environment):
    """
    A facility that provides controlled conditions in which scientific or technological research, experiments, and measurement may be performed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap'})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    other_identifier: Optional[List[Identifier]] = Field(default=None, description="""A secondary identifier of the Environment""", json_schema_extra = { "linkml_meta": {'alias': 'other_identifier',
         'domain_of': ['Dataset',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment'],
         'slot_uri': 'adms:identifier'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class InChIKey(QualitativeAttribute):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHEMINF:000059',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap'})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    value: str = Field(default=..., description="""The slot to provide the literal value of the QualitativeAttribute.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['QualitativeAttribute', 'QuantitativeAttribute'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'prov:value'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class InChi(QualitativeAttribute):
    """
    A structure descriptor which conforms to the InChI format specification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHEMINF:000113',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap'})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    value: str = Field(default=..., description="""The slot to provide the literal value of the QualitativeAttribute.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['QualitativeAttribute', 'QuantitativeAttribute'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'prov:value'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class IUPACChemicalFormula(QualitativeAttribute):
    """
    A systematic name which is formulated according to the rules and recommendations for chemical nomenclature set out by the International Union of Pure and Applied Chemistry (IUPAC).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHEMINF:000037',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap'})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    value: str = Field(default=..., description="""The slot to provide the literal value of the QualitativeAttribute.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['QualitativeAttribute', 'QuantitativeAttribute'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'prov:value'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


class SMILES(QualitativeAttribute):
    """
    A structure descriptor that denotes a molecular structure as a graph and conforms to the SMILES format specification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHEMINF:000018',
         'from_schema': 'https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap'})

    title: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'title',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'ConceptScheme',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DefinedTerm',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['Catalogue',
                       'CatalogueRecord',
                       'DataService',
                       'Dataset',
                       'DatasetSeries',
                       'Distribution',
                       'DataCreatingActivity',
                       'EvaluatedEntity',
                       'EvaluatedActivity',
                       'Tool',
                       'Environment',
                       'Plan',
                       'QualitativeAttribute',
                       'QuantitativeAttribute'],
         'slot_uri': 'dcterms:description'} })
    value: str = Field(default=..., description="""The slot to provide the literal value of the QualitativeAttribute.""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'domain_of': ['QualitativeAttribute', 'QuantitativeAttribute'],
         'in_subset': ['domain_agnostic_core'],
         'slot_uri': 'prov:value'} })
    type: Optional[DefinedTerm] = Field(default=None, description="""This slot is described in more detail within the class in which it is used.""", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Agent', 'Dataset', 'LicenseDocument', 'ClassifierMixin'],
         'slot_uri': 'dcterms:type'} })
    rdf_type: Optional[DefinedTerm] = Field(default=None, description="""The slot to specify the ontology class that is instantiated by an entity.""", json_schema_extra = { "linkml_meta": {'alias': 'rdf_type',
         'domain_of': ['ClassifierMixin'],
         'in_subset': ['domain_agnostic_core'],
         'recommended': True,
         'slot_uri': 'rdf:type'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Activity.model_rebuild()
Catalogue.model_rebuild()
CatalogueRecord.model_rebuild()
CataloguedResource.model_rebuild()
DataService.model_rebuild()
Dataset.model_rebuild()
DatasetSeries.model_rebuild()
Distribution.model_rebuild()
SupportiveEntity.model_rebuild()
Agent.model_rebuild()
Attribution.model_rebuild()
Checksum.model_rebuild()
ChecksumAlgorithm.model_rebuild()
Concept.model_rebuild()
ConceptScheme.model_rebuild()
Document.model_rebuild()
Frequency.model_rebuild()
Geometry.model_rebuild()
Identifier.model_rebuild()
Kind.model_rebuild()
LegalResource.model_rebuild()
LicenseDocument.model_rebuild()
LinguisticSystem.model_rebuild()
Location.model_rebuild()
MediaType.model_rebuild()
MediaTypeOrExtent.model_rebuild()
PeriodOfTime.model_rebuild()
Policy.model_rebuild()
ProvenanceStatement.model_rebuild()
Relationship.model_rebuild()
Resource.model_rebuild()
RightsStatement.model_rebuild()
Role.model_rebuild()
Standard.model_rebuild()
TimeInstant.model_rebuild()
ClassifierMixin.model_rebuild()
DefinedTerm.model_rebuild()
ResearchDataset.model_rebuild()
AnalysisDataset.model_rebuild()
ResearchCatalog.model_rebuild()
DataCreatingActivity.model_rebuild()
DataAnalysis.model_rebuild()
EvaluatedEntity.model_rebuild()
AnalysisSourceData.model_rebuild()
EvaluatedActivity.model_rebuild()
Tool.model_rebuild()
HardwareTool.model_rebuild()
SoftwareTool.model_rebuild()
Environment.model_rebuild()
Plan.model_rebuild()
QualitativeAttribute.model_rebuild()
QuantitativeAttribute.model_rebuild()
NMRAnalysisDataset.model_rebuild()
NMRSpectralAnalysis.model_rebuild()
NMRSpectroscopy.model_rebuild()
ChemicalReaction.model_rebuild()
ChemicalSubstance.model_rebuild()
ChemicalEntity.model_rebuild()
ChemicalSample.model_rebuild()
NMRSpectrum.model_rebuild()
Laboratory.model_rebuild()
InChIKey.model_rebuild()
InChi.model_rebuild()
IUPACChemicalFormula.model_rebuild()
SMILES.model_rebuild()

