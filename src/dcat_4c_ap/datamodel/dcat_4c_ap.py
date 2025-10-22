# Auto generated from dcat_4c_ap.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-10-22T10:32:23
# Schema: dcat-4C-ap
#
# id: https://nfdi-de.github.io/chem-dcat-ap/dcat_4c_ap.yaml
# description: This is an extension of the DCAT Application Profile PLUS LinkML schema. It is intended to be used by NFDI4Chem & NFDI4Cat as a core that can further be extended in profiles/schemas to provide chemistry specific specific metadata for a dataset.
# license: CC-BY 4.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Decimal, Float, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Decimal, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
AFE = CurieNamespace('AFE', 'http://purl.allotrope.org/ontologies/equipment#AFE_')
AFP = CurieNamespace('AFP', 'http://purl.allotrope.org/ontologies/process#AFP_')
AFR = CurieNamespace('AFR', 'http://purl.allotrope.org/ontologies/result#AFR_')
AFRL = CurieNamespace('AFRL', 'http://purl.allotrope.org/ontologies/role#AFRL_')
AFX = CurieNamespace('AFX', 'http://purl.allotrope.org/ontologies/property#AFX_')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMINF = CurieNamespace('CHEMINF', 'http://semanticscience.org/resource/CHEMINF_')
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/data_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
MOP = CurieNamespace('MOP', 'http://purl.obolibrary.org/obo/MOP_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
NMR = CurieNamespace('NMR', 'http://nmrML.org/nmrCV#NMR:')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PROCO = CurieNamespace('PROCO', 'http://purl.obolibrary.org/obo/PROCO_')
REX = CurieNamespace('REX', 'http://purl.obolibrary.org/obo/REX_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RXNO = CurieNamespace('RXNO', 'http://purl.obolibrary.org/obo/RXNO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
T4FS = CurieNamespace('T4FS', 'http://purl.obolibrary.org/obo/T4FS_')
VOC4CAT = CurieNamespace('VOC4CAT', 'https://w3id.org/nfdi4cat/voc4cat_')
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCAT_4C_AP = CurieNamespace('dcat_4c_ap', 'https://nfdi-de.github.io/chem-dcat-ap/dcat_4c_ap.yaml#')
DCAT_AP_PLUS = CurieNamespace('dcat_ap_plus', 'https://nfdi-de.github.io/dcat-ap-plus/dcat_ap_plus.yaml#')
DCATAP = CurieNamespace('dcatap', 'http://data.europa.eu/r5r/')
DCATAP_PLUS = CurieNamespace('dcatap_plus', 'https://nfdi-de.github.io/dcat-ap-plus/dcat_ap_plus.yaml#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
ELI = CurieNamespace('eli', 'http://data.europa.eu/eli/ontology#')
EPOS = CurieNamespace('epos', 'https://www.epos-eu.org/epos-dcat-ap#')
EX = CurieNamespace('ex', 'http://example.org/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
MATERIAL_ENTITIES_AP = CurieNamespace('material_entities_ap', 'https://nfdi-de.github.io/chem-dcat-ap/material_entities_ap.yaml#')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms#')
TIME = CurieNamespace('time', 'http://www.w3.org/2006/time#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DCAT_4C_AP


# Types
class Duration(str):
    """ The datatype that represents durations of time. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "duration"
    type_model_uri = DCAT_4C_AP.Duration


class HexBinary(str):
    """ The datatype that represents arbitrary hex-encoded binary data. """
    type_class_uri = XSD["hexBinary"]
    type_class_curie = "xsd:hexBinary"
    type_name = "hexBinary"
    type_model_uri = DCAT_4C_AP.HexBinary


class NonNegativeInteger(int):
    """ The datatype that represents non-negative integers. """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "nonNegativeInteger"
    type_model_uri = DCAT_4C_AP.NonNegativeInteger


# Class references
class ActivityId(URIorCURIE):
    pass


class AgenticEntityId(URIorCURIE):
    pass


class DataGeneratingActivityId(ActivityId):
    pass


class DataAnalysisId(DataGeneratingActivityId):
    pass


class DatasetId(URIorCURIE):
    pass


class AnalysisDatasetId(DatasetId):
    pass


class DefinedTermId(URIorCURIE):
    pass


class DeviceId(AgenticEntityId):
    pass


class EntityId(URIorCURIE):
    pass


class EvaluatedActivityId(ActivityId):
    pass


class EvaluatedEntityId(EntityId):
    pass


class AnalysisSourceDataId(EvaluatedEntityId):
    pass


class SoftwareId(AgenticEntityId):
    pass


class DocumentId(URIorCURIE):
    pass


class LegalResourceId(URIorCURIE):
    pass


class LicenseDocumentId(URIorCURIE):
    pass


class ResourceId(URIorCURIE):
    pass


class ChemicalReactionId(ActivityId):
    pass


class DissolvingSubstanceId(AgenticEntityId):
    pass


class CatalystId(AgenticEntityId):
    pass


class ReactorId(DeviceId):
    pass


class NMRAnalysisDatasetId(AnalysisDatasetId):
    pass


class NMRSpectralAnalysisId(DataAnalysisId):
    pass


class NMRSpectrumId(AnalysisSourceDataId):
    pass


class NMRSpectroscopyId(DataGeneratingActivityId):
    pass


class NMRSpectrometerId(DeviceId):
    pass


class AcquisitionNucleusId(AgenticEntityId):
    pass


class NMRSolventId(DissolvingSubstanceId):
    pass


class MaterialEntityId(EntityId):
    pass


class ChemicalEntityId(MaterialEntityId):
    pass


class AtomId(ChemicalEntityId):
    pass


class ChemicalSubstanceId(MaterialEntityId):
    pass


class PolymerId(ChemicalSubstanceId):
    pass


class StartingMaterialId(ChemicalSubstanceId):
    pass


class ReagentId(ChemicalSubstanceId):
    pass


class ChemicalProductId(ChemicalSubstanceId):
    pass


class ShiftCalibrationCompoundId(ChemicalEntityId):
    pass


class ShiftReferenceCompoundId(ShiftCalibrationCompoundId):
    pass


class CharacterizedCompoundId(ChemicalEntityId):
    pass


class MaterialSampleId(EvaluatedEntityId):
    pass


class SubstanceSampleId(MaterialSampleId):
    pass


class PolymerSampleId(SubstanceSampleId):
    pass


class NMRSampleId(SubstanceSampleId):
    pass


@dataclass(repr=False)
class Activity(YAMLRoot):
    """
    See [DCAT-AP specs:Activity](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Activity)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Activity

    id: Union[str, ActivityId] = None
    title: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]] = empty_dict()
    had_input_entity: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    had_output_entity: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    had_input_activity: Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]] = empty_dict()
    carried_out_by: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]] = empty_dict()
    has_qualitative_attribute: Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    part_of: Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]] = empty_dict()
    type: Optional[Union[dict, "DefinedTerm"]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Activity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="had_input_entity", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="had_output_entity", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="had_input_activity", slot_type=Activity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="carried_out_by", slot_type=AgenticEntity, key_name="id", keyed=True)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Activity, key_name="id", keyed=True)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Agent(YAMLRoot):
    """
    See [DCAT-AP specs:Agent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Agent)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Agent

    name: Union[str, list[str]] = None
    type: Optional[Union[dict, "Concept"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if self.type is not None and not isinstance(self.type, Concept):
            self.type = Concept(**as_dict(self.type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AgenticEntity(YAMLRoot):
    """
    An entity that is somehow responsible for an Activity to take place.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Agent"]
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "AgenticEntity"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.AgenticEntity

    id: Union[str, AgenticEntityId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    has_qualitative_attribute: Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]] = empty_dict()
    type: Optional[Union[dict, "DefinedTerm"]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgenticEntityId):
            self.id = AgenticEntityId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=AgenticEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=AgenticEntity, key_name="id", keyed=True)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class Catalogue(YAMLRoot):
    """
    See [DCAT-AP specs:Catalogue](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Catalogue)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Catalogue"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Catalogue

    description: Union[str, list[str]] = None
    publisher: Union[dict, Agent] = None
    title: Union[str, list[str]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    catalogue: Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]] = empty_list()
    creator: Optional[Union[dict, Agent]] = None
    geographical_coverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    has_dataset: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    has_part: Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]] = empty_list()
    homepage: Optional[Union[dict, "Document"]] = None
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    licence: Optional[Union[dict, "LicenseDocument"]] = None
    modification_date: Optional[Union[str, XSDDate]] = None
    record: Optional[Union[Union[dict, "CatalogueRecord"], list[Union[dict, "CatalogueRecord"]]]] = empty_list()
    release_date: Optional[Union[str, XSDDate]] = None
    rights: Optional[Union[dict, "RightsStatement"]] = None
    service: Optional[Union[Union[dict, "DataService"], list[Union[dict, "DataService"]]]] = empty_list()
    temporal_coverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()
    themes: Optional[Union[Union[dict, "ConceptScheme"], list[Union[dict, "ConceptScheme"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.publisher):
            self.MissingRequiredField("publisher")
        if not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.catalogue, list):
            self.catalogue = [self.catalogue] if self.catalogue is not None else []
        self.catalogue = [v if isinstance(v, Catalogue) else Catalogue(**as_dict(v)) for v in self.catalogue]

        if self.creator is not None and not isinstance(self.creator, Agent):
            self.creator = Agent(**as_dict(self.creator))

        if not isinstance(self.geographical_coverage, list):
            self.geographical_coverage = [self.geographical_coverage] if self.geographical_coverage is not None else []
        self.geographical_coverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographical_coverage]

        self._normalize_inlined_as_list(slot_name="has_dataset", slot_type=Dataset, key_name="id", keyed=True)

        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part] if self.has_part is not None else []
        self.has_part = [v if isinstance(v, Catalogue) else Catalogue(**as_dict(v)) for v in self.has_part]

        if self.homepage is not None and not isinstance(self.homepage, Document):
            self.homepage = Document(**as_dict(self.homepage))

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.licence is not None and not isinstance(self.licence, LicenseDocument):
            self.licence = LicenseDocument(**as_dict(self.licence))

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if not isinstance(self.record, list):
            self.record = [self.record] if self.record is not None else []
        self.record = [v if isinstance(v, CatalogueRecord) else CatalogueRecord(**as_dict(v)) for v in self.record]

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if self.rights is not None and not isinstance(self.rights, RightsStatement):
            self.rights = RightsStatement(**as_dict(self.rights))

        if not isinstance(self.service, list):
            self.service = [self.service] if self.service is not None else []
        self.service = [v if isinstance(v, DataService) else DataService(**as_dict(v)) for v in self.service]

        if not isinstance(self.temporal_coverage, list):
            self.temporal_coverage = [self.temporal_coverage] if self.temporal_coverage is not None else []
        self.temporal_coverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporal_coverage]

        if not isinstance(self.themes, list):
            self.themes = [self.themes] if self.themes is not None else []
        self.themes = [v if isinstance(v, ConceptScheme) else ConceptScheme(**as_dict(v)) for v in self.themes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalogueRecord(YAMLRoot):
    """
    See [DCAT-AP specs:CatalogueRecord](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#CatalogueRecord)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["CatalogRecord"]
    class_class_curie: ClassVar[str] = "dcat:CatalogRecord"
    class_name: ClassVar[str] = "CatalogueRecord"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.CatalogueRecord

    modification_date: Union[str, XSDDate] = None
    primary_topic: Union[dict, Any] = None
    application_profile: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    change_type: Optional[Union[dict, "Concept"]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    listing_date: Optional[Union[str, XSDDate]] = None
    source_metadata: Optional[Union[dict, "CatalogueRecord"]] = None
    title: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.modification_date):
            self.MissingRequiredField("modification_date")
        if not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if not isinstance(self.application_profile, list):
            self.application_profile = [self.application_profile] if self.application_profile is not None else []
        self.application_profile = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.application_profile]

        if self.change_type is not None and not isinstance(self.change_type, Concept):
            self.change_type = Concept(**as_dict(self.change_type))

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.listing_date is not None and not isinstance(self.listing_date, XSDDate):
            self.listing_date = XSDDate(self.listing_date)

        if self.source_metadata is not None and not isinstance(self.source_metadata, CatalogueRecord):
            self.source_metadata = CatalogueRecord(**as_dict(self.source_metadata))

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Checksum(YAMLRoot):
    """
    See [DCAT-AP specs:Checksum](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Checksum)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["Checksum"]
    class_class_curie: ClassVar[str] = "spdx:Checksum"
    class_name: ClassVar[str] = "Checksum"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Checksum

    algorithm: Union[dict, "ChecksumAlgorithm"] = None
    checksum_value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, ChecksumAlgorithm):
            self.algorithm = ChecksumAlgorithm(**as_dict(self.algorithm))

        if self._is_empty(self.checksum_value):
            self.MissingRequiredField("checksum_value")
        if not isinstance(self.checksum_value, str):
            self.checksum_value = str(self.checksum_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClassifierMixin(YAMLRoot):
    """
    A mixin with which an entity of this schema can be classified via an additional rdf:type or dcterms:type assertion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT_AP_PLUS["ClassifierMixin"]
    class_class_curie: ClassVar[str] = "dcat_ap_plus:ClassifierMixin"
    class_name: ClassVar[str] = "ClassifierMixin"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ClassifierMixin

    type: Optional[Union[dict, "DefinedTerm"]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataGeneratingActivity(Activity):
    """
    An Activity (process) that has the objective to produce information (in form of a dataset) about another Activity
    or Entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "DataGeneratingActivity"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.DataGeneratingActivity

    id: Union[str, DataGeneratingActivityId] = None
    evaluated_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()
    evaluated_activity: Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, "EvaluatedActivity"]], list[Union[dict, "EvaluatedActivity"]]]] = empty_dict()
    realized_plan: Optional[Union[dict, "Plan"]] = None
    occurred_in: Optional[Union[dict, "Surrounding"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGeneratingActivityId):
            self.id = DataGeneratingActivityId(self.id)

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="evaluated_activity", slot_type=EvaluatedActivity, key_name="id", keyed=True)

        if self.realized_plan is not None and not isinstance(self.realized_plan, Plan):
            self.realized_plan = Plan(**as_dict(self.realized_plan))

        if self.occurred_in is not None and not isinstance(self.occurred_in, Surrounding):
            self.occurred_in = Surrounding(**as_dict(self.occurred_in))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataAnalysis(DataGeneratingActivity):
    """
    An Activity that evaluates the data produced by another Activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "DataAnalysis"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.DataAnalysis

    id: Union[str, DataAnalysisId] = None
    evaluated_entity: Optional[Union[dict[Union[str, AnalysisSourceDataId], Union[dict, "AnalysisSourceData"]], list[Union[dict, "AnalysisSourceData"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAnalysisId):
            self.id = DataAnalysisId(self.id)

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=AnalysisSourceData, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataService(YAMLRoot):
    """
    See [DCAT-AP specs:DataService](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DataService)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DataService"]
    class_class_curie: ClassVar[str] = "dcat:DataService"
    class_name: ClassVar[str] = "DataService"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.DataService

    endpoint_URL: Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]] = empty_dict()
    title: Union[str, list[str]] = None
    access_rights: Optional[Union[dict, "RightsStatement"]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    conforms_to: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    contact_point: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    documentation: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    endpoint_description: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    format: Optional[Union[Union[dict, "MediaTypeOrExtent"], list[Union[dict, "MediaTypeOrExtent"]]]] = empty_list()
    keyword: Optional[Union[str, list[str]]] = empty_list()
    landing_page: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    licence: Optional[Union[dict, "LicenseDocument"]] = None
    publisher: Optional[Union[dict, Agent]] = None
    serves_dataset: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    theme: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.endpoint_URL):
            self.MissingRequiredField("endpoint_URL")
        self._normalize_inlined_as_list(slot_name="endpoint_URL", slot_type=Resource, key_name="id", keyed=True)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self.access_rights is not None and not isinstance(self.access_rights, RightsStatement):
            self.access_rights = RightsStatement(**as_dict(self.access_rights))

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.conforms_to, list):
            self.conforms_to = [self.conforms_to] if self.conforms_to is not None else []
        self.conforms_to = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.conforms_to]

        if not isinstance(self.contact_point, list):
            self.contact_point = [self.contact_point] if self.contact_point is not None else []
        self.contact_point = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contact_point]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        self._normalize_inlined_as_list(slot_name="documentation", slot_type=Document, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="endpoint_description", slot_type=Resource, key_name="id", keyed=True)

        if not isinstance(self.format, list):
            self.format = [self.format] if self.format is not None else []
        self.format = [v if isinstance(v, MediaTypeOrExtent) else MediaTypeOrExtent(**as_dict(v)) for v in self.format]

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] if self.keyword is not None else []
        self.keyword = [v if isinstance(v, str) else str(v) for v in self.keyword]

        self._normalize_inlined_as_list(slot_name="landing_page", slot_type=Document, key_name="id", keyed=True)

        if self.licence is not None and not isinstance(self.licence, LicenseDocument):
            self.licence = LicenseDocument(**as_dict(self.licence))

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        self._normalize_inlined_as_list(slot_name="serves_dataset", slot_type=Dataset, key_name="id", keyed=True)

        if not isinstance(self.theme, list):
            self.theme = [self.theme] if self.theme is not None else []
        self.theme = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.theme]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A collection of data, published or curated by a single agent, and available for access or download in one or more
    representations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Dataset

    id: Union[str, DatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]] = empty_dict()
    access_rights: Optional[Union[dict, "RightsStatement"]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    conforms_to: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    contact_point: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    creator: Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]] = empty_list()
    dataset_distribution: Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]] = empty_list()
    documentation: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    frequency: Optional[Union[dict, "Frequency"]] = None
    geographical_coverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    has_version: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    identifier: Optional[Union[str, list[str]]] = empty_list()
    in_series: Optional[Union[Union[dict, "DatasetSeries"], list[Union[dict, "DatasetSeries"]]]] = empty_list()
    is_referenced_by: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    keyword: Optional[Union[str, list[str]]] = empty_list()
    landing_page: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    modification_date: Optional[Union[str, XSDDate]] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    provenance: Optional[Union[Union[dict, "ProvenanceStatement"], list[Union[dict, "ProvenanceStatement"]]]] = empty_list()
    publisher: Optional[Union[dict, Agent]] = None
    qualified_attribution: Optional[Union[Union[dict, "Attribution"], list[Union[dict, "Attribution"]]]] = empty_list()
    qualified_relation: Optional[Union[Union[dict, "Relationship"], list[Union[dict, "Relationship"]]]] = empty_list()
    related_resource: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    release_date: Optional[Union[str, XSDDate]] = None
    sample: Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]] = empty_list()
    source: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    spatial_resolution: Optional[Decimal] = None
    temporal_coverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()
    temporal_resolution: Optional[str] = None
    theme: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()
    type: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()
    version: Optional[str] = None
    version_notes: Optional[Union[str, list[str]]] = empty_list()
    is_about_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()
    is_about_activity: Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, "EvaluatedActivity"]], list[Union[dict, "EvaluatedActivity"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self._is_empty(self.was_generated_by):
            self.MissingRequiredField("was_generated_by")
        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataGeneratingActivity, key_name="id", keyed=True)

        if self.access_rights is not None and not isinstance(self.access_rights, RightsStatement):
            self.access_rights = RightsStatement(**as_dict(self.access_rights))

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.conforms_to, list):
            self.conforms_to = [self.conforms_to] if self.conforms_to is not None else []
        self.conforms_to = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.conforms_to]

        if not isinstance(self.contact_point, list):
            self.contact_point = [self.contact_point] if self.contact_point is not None else []
        self.contact_point = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contact_point]

        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, Agent) else Agent(**as_dict(v)) for v in self.creator]

        if not isinstance(self.dataset_distribution, list):
            self.dataset_distribution = [self.dataset_distribution] if self.dataset_distribution is not None else []
        self.dataset_distribution = [v if isinstance(v, Distribution) else Distribution(**as_dict(v)) for v in self.dataset_distribution]

        self._normalize_inlined_as_list(slot_name="documentation", slot_type=Document, key_name="id", keyed=True)

        if self.frequency is not None and not isinstance(self.frequency, Frequency):
            self.frequency = Frequency(**as_dict(self.frequency))

        if not isinstance(self.geographical_coverage, list):
            self.geographical_coverage = [self.geographical_coverage] if self.geographical_coverage is not None else []
        self.geographical_coverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographical_coverage]

        self._normalize_inlined_as_list(slot_name="has_version", slot_type=Dataset, key_name="id", keyed=True)

        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier] if self.identifier is not None else []
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        if not isinstance(self.in_series, list):
            self.in_series = [self.in_series] if self.in_series is not None else []
        self.in_series = [v if isinstance(v, DatasetSeries) else DatasetSeries(**as_dict(v)) for v in self.in_series]

        self._normalize_inlined_as_list(slot_name="is_referenced_by", slot_type=Resource, key_name="id", keyed=True)

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] if self.keyword is not None else []
        self.keyword = [v if isinstance(v, str) else str(v) for v in self.keyword]

        self._normalize_inlined_as_list(slot_name="landing_page", slot_type=Document, key_name="id", keyed=True)

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        if not isinstance(self.provenance, list):
            self.provenance = [self.provenance] if self.provenance is not None else []
        self.provenance = [v if isinstance(v, ProvenanceStatement) else ProvenanceStatement(**as_dict(v)) for v in self.provenance]

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if not isinstance(self.qualified_attribution, list):
            self.qualified_attribution = [self.qualified_attribution] if self.qualified_attribution is not None else []
        self.qualified_attribution = [v if isinstance(v, Attribution) else Attribution(**as_dict(v)) for v in self.qualified_attribution]

        if not isinstance(self.qualified_relation, list):
            self.qualified_relation = [self.qualified_relation] if self.qualified_relation is not None else []
        self.qualified_relation = [v if isinstance(v, Relationship) else Relationship(**as_dict(v)) for v in self.qualified_relation]

        self._normalize_inlined_as_list(slot_name="related_resource", slot_type=Resource, key_name="id", keyed=True)

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if not isinstance(self.sample, list):
            self.sample = [self.sample] if self.sample is not None else []
        self.sample = [v if isinstance(v, Distribution) else Distribution(**as_dict(v)) for v in self.sample]

        self._normalize_inlined_as_list(slot_name="source", slot_type=Dataset, key_name="id", keyed=True)

        if self.spatial_resolution is not None and not isinstance(self.spatial_resolution, Decimal):
            self.spatial_resolution = Decimal(self.spatial_resolution)

        if not isinstance(self.temporal_coverage, list):
            self.temporal_coverage = [self.temporal_coverage] if self.temporal_coverage is not None else []
        self.temporal_coverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporal_coverage]

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, str):
            self.temporal_resolution = str(self.temporal_resolution)

        if not isinstance(self.theme, list):
            self.theme = [self.theme] if self.theme is not None else []
        self.theme = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.theme]

        if not isinstance(self.type, list):
            self.type = [self.type] if self.type is not None else []
        self.type = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.type]

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.version_notes, list):
            self.version_notes = [self.version_notes] if self.version_notes is not None else []
        self.version_notes = [v if isinstance(v, str) else str(v) for v in self.version_notes]

        self._normalize_inlined_as_list(slot_name="is_about_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="is_about_activity", slot_type=EvaluatedActivity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnalysisDataset(Dataset):
    """
    A Dataset that was generated by an analysis of some previously generated data. For example, a dataset that
    contains the data of an assignment of a chemical structure to a sample based on the spectral data obtained from
    the sample is an AnalyticalDataset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "AnalysisDataset"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.AnalysisDataset

    id: Union[str, AnalysisDatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Optional[Union[dict[Union[str, DataAnalysisId], Union[dict, DataAnalysis]], list[Union[dict, DataAnalysis]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisDatasetId):
            self.id = AnalysisDatasetId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataAnalysis, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatasetSeries(YAMLRoot):
    """
    See [DCAT-AP specs:DatasetSeries](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DatasetSeries)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DatasetSeries"]
    class_class_curie: ClassVar[str] = "dcat:DatasetSeries"
    class_name: ClassVar[str] = "DatasetSeries"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.DatasetSeries

    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    contact_point: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    frequency: Optional[Union[dict, "Frequency"]] = None
    geographical_coverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    modification_date: Optional[Union[str, XSDDate]] = None
    publisher: Optional[Union[dict, Agent]] = None
    release_date: Optional[Union[str, XSDDate]] = None
    temporal_coverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.contact_point, list):
            self.contact_point = [self.contact_point] if self.contact_point is not None else []
        self.contact_point = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contact_point]

        if self.frequency is not None and not isinstance(self.frequency, Frequency):
            self.frequency = Frequency(**as_dict(self.frequency))

        if not isinstance(self.geographical_coverage, list):
            self.geographical_coverage = [self.geographical_coverage] if self.geographical_coverage is not None else []
        self.geographical_coverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographical_coverage]

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if not isinstance(self.temporal_coverage, list):
            self.temporal_coverage = [self.temporal_coverage] if self.temporal_coverage is not None else []
        self.temporal_coverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporal_coverage]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DefinedTerm(YAMLRoot):
    """
    A word, name, acronym or phrase that is defined in a controlled vocabulary (CV) and that is used to provide an
    additional rdf:type or dcterms:type of a class within this schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DefinedTerm"]
    class_class_curie: ClassVar[str] = "schema:DefinedTerm"
    class_name: ClassVar[str] = "DefinedTerm"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.DefinedTerm

    id: Union[str, DefinedTermId] = None
    title: Optional[str] = None
    from_CV: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DefinedTermId):
            self.id = DefinedTermId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.from_CV is not None and not isinstance(self.from_CV, URIorCURIE):
            self.from_CV = URIorCURIE(self.from_CV)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Device(AgenticEntity):
    """
    A material instrument that is designed to perform a function primarily by means of its mechanical or electrical
    nature.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Agent"]
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Device

    id: Union[str, DeviceId] = None
    has_part: Optional[Union[dict[Union[str, DeviceId], Union[dict, "Device"]], list[Union[dict, "Device"]]]] = empty_dict()
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Device, key_name="id", keyed=True)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Distribution(YAMLRoot):
    """
    See [DCAT-AP specs:Distribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Distribution"]
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "Distribution"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Distribution

    access_URL: Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]] = empty_dict()
    access_service: Optional[Union[Union[dict, DataService], list[Union[dict, DataService]]]] = empty_list()
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    availability: Optional[Union[dict, "Concept"]] = None
    byte_size: Optional[int] = None
    checksum: Optional[Union[dict, Checksum]] = None
    compression_format: Optional[Union[dict, "MediaType"]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    documentation: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    download_URL: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    format: Optional[Union[dict, "MediaTypeOrExtent"]] = None
    has_policy: Optional[Union[dict, "Policy"]] = None
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    licence: Optional[Union[dict, "LicenseDocument"]] = None
    linked_schemas: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    media_type: Optional[Union[dict, "MediaType"]] = None
    modification_date: Optional[Union[str, XSDDate]] = None
    packaging_format: Optional[Union[dict, "MediaType"]] = None
    release_date: Optional[Union[str, XSDDate]] = None
    rights: Optional[Union[dict, "RightsStatement"]] = None
    spatial_resolution: Optional[Decimal] = None
    status: Optional[Union[dict, "Concept"]] = None
    temporal_resolution: Optional[str] = None
    title: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.access_URL):
            self.MissingRequiredField("access_URL")
        self._normalize_inlined_as_list(slot_name="access_URL", slot_type=Resource, key_name="id", keyed=True)

        if not isinstance(self.access_service, list):
            self.access_service = [self.access_service] if self.access_service is not None else []
        self.access_service = [v if isinstance(v, DataService) else DataService(**as_dict(v)) for v in self.access_service]

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if self.availability is not None and not isinstance(self.availability, Concept):
            self.availability = Concept(**as_dict(self.availability))

        if self.byte_size is not None and not isinstance(self.byte_size, int):
            self.byte_size = int(self.byte_size)

        if self.checksum is not None and not isinstance(self.checksum, Checksum):
            self.checksum = Checksum(**as_dict(self.checksum))

        if self.compression_format is not None and not isinstance(self.compression_format, MediaType):
            self.compression_format = MediaType(**as_dict(self.compression_format))

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        self._normalize_inlined_as_list(slot_name="documentation", slot_type=Document, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="download_URL", slot_type=Resource, key_name="id", keyed=True)

        if self.format is not None and not isinstance(self.format, MediaTypeOrExtent):
            self.format = MediaTypeOrExtent(**as_dict(self.format))

        if self.has_policy is not None and not isinstance(self.has_policy, Policy):
            self.has_policy = Policy(**as_dict(self.has_policy))

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.licence is not None and not isinstance(self.licence, LicenseDocument):
            self.licence = LicenseDocument(**as_dict(self.licence))

        if not isinstance(self.linked_schemas, list):
            self.linked_schemas = [self.linked_schemas] if self.linked_schemas is not None else []
        self.linked_schemas = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.linked_schemas]

        if self.media_type is not None and not isinstance(self.media_type, MediaType):
            self.media_type = MediaType(**as_dict(self.media_type))

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if self.packaging_format is not None and not isinstance(self.packaging_format, MediaType):
            self.packaging_format = MediaType(**as_dict(self.packaging_format))

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if self.rights is not None and not isinstance(self.rights, RightsStatement):
            self.rights = RightsStatement(**as_dict(self.rights))

        if self.spatial_resolution is not None and not isinstance(self.spatial_resolution, Decimal):
            self.spatial_resolution = Decimal(self.spatial_resolution)

        if self.status is not None and not isinstance(self.status, Concept):
            self.status = Concept(**as_dict(self.status))

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, str):
            self.temporal_resolution = str(self.temporal_resolution)

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    A physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Entity

    id: Union[str, EntityId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    has_qualitative_attribute: Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Entity, key_name="id", keyed=True)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaluatedActivity(Activity):
    """
    An activity or proces that is being evaluated in a DataGeneratingActivity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "EvaluatedActivity"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.EvaluatedActivity

    id: Union[str, EvaluatedActivityId] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaluatedActivityId):
            self.id = EvaluatedActivityId(self.id)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaluatedEntity(Entity):
    """
    An Entity that is being evaluated in a DataGeneratingActivity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "EvaluatedEntity"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.EvaluatedEntity

    id: Union[str, EvaluatedEntityId] = None
    was_generated_by: Optional[Union[dict[Union[str, ActivityId], Union[dict, Activity]], list[Union[dict, Activity]]]] = empty_dict()
    title: Optional[str] = None
    description: Optional[str] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaluatedEntityId):
            self.id = EvaluatedEntityId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=Activity, key_name="id", keyed=True)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnalysisSourceData(EvaluatedEntity):
    """
    Information that was evaluated within a DataAnalysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "AnalysisSourceData"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.AnalysisSourceData

    id: Union[str, AnalysisSourceDataId] = None
    was_generated_by: Optional[Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisSourceDataId):
            self.id = AnalysisSourceDataId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataGeneratingActivity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


class Kind(YAMLRoot):
    """
    See [DCAT-AP specs:Kind](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Kind)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VCARD["Kind"]
    class_class_curie: ClassVar[str] = "vcard:Kind"
    class_name: ClassVar[str] = "Kind"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Kind


@dataclass(repr=False)
class Location(YAMLRoot):
    """
    See [DCAT-AP specs:Location](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Location)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Location"]
    class_class_curie: ClassVar[str] = "dcterms:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Location

    bbox: Optional[str] = None
    centroid: Optional[str] = None
    geometry: Optional[Union[dict, "Geometry"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.bbox is not None and not isinstance(self.bbox, str):
            self.bbox = str(self.bbox)

        if self.centroid is not None and not isinstance(self.centroid, str):
            self.centroid = str(self.centroid)

        if self.geometry is not None and not isinstance(self.geometry, Geometry):
            self.geometry = Geometry(**as_dict(self.geometry))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Plan(YAMLRoot):
    """
    A piece of information that specifies how an activity has to be carried out by its agents including what kind of
    steps have to be taken and what kind of parameters have to be met/set.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Plan"]
    class_class_curie: ClassVar[str] = "prov:Plan"
    class_name: ClassVar[str] = "Plan"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Plan

    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QualitativeAttribute(YAMLRoot):
    """
    A piece of information that is attributed to an Entity, Activity or AgenticEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "QualitativeAttribute"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.QualitativeAttribute

    value: str = None
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantitativeAttribute(YAMLRoot):
    """
    A quantifiable piece of information that is attributed to an Entity, Activity or AgenticEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "QuantitativeAttribute"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.QuantitativeAttribute

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[Union[str, DefinedTermId]] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.has_quantity_type):
            self.MissingRequiredField("has_quantity_type")
        if not isinstance(self.has_quantity_type, DefinedTermId):
            self.has_quantity_type = DefinedTermId(self.has_quantity_type)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.unit is not None and not isinstance(self.unit, DefinedTermId):
            self.unit = DefinedTermId(self.unit)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    See [DCAT-AP specs:Relationship](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Relationship)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Relationship"]
    class_class_curie: ClassVar[str] = "dcat:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Relationship

    had_role: Union[Union[dict, "Role"], list[Union[dict, "Role"]]] = None
    relation: Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.had_role):
            self.MissingRequiredField("had_role")
        if not isinstance(self.had_role, list):
            self.had_role = [self.had_role] if self.had_role is not None else []
        self.had_role = [v if isinstance(v, Role) else Role(**as_dict(v)) for v in self.had_role]

        if self._is_empty(self.relation):
            self.MissingRequiredField("relation")
        self._normalize_inlined_as_list(slot_name="relation", slot_type=Resource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Software(AgenticEntity):
    """
    An instrument composed of a series of instructions that can be interpreted by or directly executed by a computer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["SoftwareAgent"]
    class_class_curie: ClassVar[str] = "prov:SoftwareAgent"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Software

    id: Union[str, SoftwareId] = None
    has_part: Optional[Union[dict[Union[str, SoftwareId], Union[dict, "Software"]], list[Union[dict, "Software"]]]] = empty_dict()
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Software, key_name="id", keyed=True)

        if not isinstance(self.other_identifier, list):
            self.other_identifier = [self.other_identifier] if self.other_identifier is not None else []
        self.other_identifier = [v if isinstance(v, Identifier) else Identifier(**as_dict(v)) for v in self.other_identifier]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportiveEntity(YAMLRoot):
    """
    The supportive entities are supporting the main entities in the Application Profile. They are included in the
    Application Profile because they form the range of properties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT_AP_PLUS["SupportiveEntity"]
    class_class_curie: ClassVar[str] = "dcat_ap_plus:SupportiveEntity"
    class_name: ClassVar[str] = "SupportiveEntity"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.SupportiveEntity

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Attribution(SupportiveEntity):
    """
    See [DCAT-AP specs:Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Attribution"]
    class_class_curie: ClassVar[str] = "prov:Attribution"
    class_name: ClassVar[str] = "Attribution"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Attribution

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChecksumAlgorithm(SupportiveEntity):
    """
    See [DCAT-AP specs:ChecksumAlgorithm](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ChecksumAlgorithm)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["ChecksumAlgorithm"]
    class_class_curie: ClassVar[str] = "spdx:ChecksumAlgorithm"
    class_name: ClassVar[str] = "ChecksumAlgorithm"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ChecksumAlgorithm

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(SupportiveEntity):
    """
    See [DCAT-AP specs:Concept](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Concept)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Concept

    preferred_label: Union[str, list[str]] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_label):
            self.MissingRequiredField("preferred_label")
        if not isinstance(self.preferred_label, list):
            self.preferred_label = [self.preferred_label] if self.preferred_label is not None else []
        self.preferred_label = [v if isinstance(v, str) else str(v) for v in self.preferred_label]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptScheme(SupportiveEntity):
    """
    See [DCAT-AP specs:ConceptScheme](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ConceptScheme)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["ConceptScheme"]
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "ConceptScheme"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ConceptScheme

    title: Union[str, list[str]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Document(SupportiveEntity):
    """
    See [DCAT-AP specs:Document](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Document)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Document"]
    class_class_curie: ClassVar[str] = "foaf:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Document

    id: Union[str, DocumentId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DocumentId):
            self.id = DocumentId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Frequency(SupportiveEntity):
    """
    See [DCAT-AP specs:Frequency](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Frequency)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Frequency"]
    class_class_curie: ClassVar[str] = "dcterms:Frequency"
    class_name: ClassVar[str] = "Frequency"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Frequency

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Geometry(SupportiveEntity):
    """
    See [DCAT-AP specs:Geometry](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Geometry)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCN["Geometry"]
    class_class_curie: ClassVar[str] = "locn:Geometry"
    class_name: ClassVar[str] = "Geometry"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Geometry

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identifier(SupportiveEntity):
    """
    See [DCAT-AP specs:Identifier](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Identifier)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADMS["Identifier"]
    class_class_curie: ClassVar[str] = "adms:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Identifier

    notation: str = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.notation):
            self.MissingRequiredField("notation")
        if not isinstance(self.notation, str):
            self.notation = str(self.notation)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalResource(SupportiveEntity):
    """
    See [DCAT-AP specs:LegalResource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LegalResource)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ELI["LegalResource"]
    class_class_curie: ClassVar[str] = "eli:LegalResource"
    class_name: ClassVar[str] = "LegalResource"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.LegalResource

    id: Union[str, LegalResourceId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalResourceId):
            self.id = LegalResourceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LicenseDocument(SupportiveEntity):
    """
    See [DCAT-AP specs:LicenseDocument](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LicenseDocument)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["LicenseDocument"]
    class_class_curie: ClassVar[str] = "dcterms:LicenseDocument"
    class_name: ClassVar[str] = "LicenseDocument"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.LicenseDocument

    id: Union[str, LicenseDocumentId] = None
    type: Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]] = empty_list()
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LicenseDocumentId):
            self.id = LicenseDocumentId(self.id)

        if not isinstance(self.type, list):
            self.type = [self.type] if self.type is not None else []
        self.type = [v if isinstance(v, Concept) else Concept(**as_dict(v)) for v in self.type]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LinguisticSystem(SupportiveEntity):
    """
    See [DCAT-AP specs:LinguisticSystem](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LinguisticSystem)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["LinguisticSystem"]
    class_class_curie: ClassVar[str] = "dcterms:LinguisticSystem"
    class_name: ClassVar[str] = "LinguisticSystem"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.LinguisticSystem

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediaType(SupportiveEntity):
    """
    See [DCAT-AP specs:MediaType](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaType)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["MediaType"]
    class_class_curie: ClassVar[str] = "dcterms:MediaType"
    class_name: ClassVar[str] = "MediaType"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.MediaType

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediaTypeOrExtent(SupportiveEntity):
    """
    See [DCAT-AP specs:MediaTypeOrExtent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaTypeOrExtent)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["MediaTypeOrExtent"]
    class_class_curie: ClassVar[str] = "dcterms:MediaTypeOrExtent"
    class_name: ClassVar[str] = "MediaTypeOrExtent"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.MediaTypeOrExtent

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PeriodOfTime(SupportiveEntity):
    """
    See [DCAT-AP specs:PeriodOfTime](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#PeriodOfTime)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["PeriodOfTime"]
    class_class_curie: ClassVar[str] = "dcterms:PeriodOfTime"
    class_name: ClassVar[str] = "PeriodOfTime"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.PeriodOfTime

    beginning: Optional[Union[dict, "TimeInstant"]] = None
    end: Optional[Union[dict, "TimeInstant"]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    start_date: Optional[Union[str, XSDDate]] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.beginning is not None and not isinstance(self.beginning, TimeInstant):
            self.beginning = TimeInstant(**as_dict(self.beginning))

        if self.end is not None and not isinstance(self.end, TimeInstant):
            self.end = TimeInstant(**as_dict(self.end))

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Policy(SupportiveEntity):
    """
    See [DCAT-AP specs:Policy](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Policy)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ODRL["Policy"]
    class_class_curie: ClassVar[str] = "odrl:Policy"
    class_name: ClassVar[str] = "Policy"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Policy

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvenanceStatement(SupportiveEntity):
    """
    See [DCAT-AP specs:ProvenanceStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ProvenanceStatement)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["ProvenanceStatement"]
    class_class_curie: ClassVar[str] = "dcterms:ProvenanceStatement"
    class_name: ClassVar[str] = "ProvenanceStatement"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ProvenanceStatement

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(SupportiveEntity):
    """
    See [DCAT-AP specs:Resource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Resource)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Resource"]
    class_class_curie: ClassVar[str] = "rdfs:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Resource

    id: Union[str, ResourceId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightsStatement(SupportiveEntity):
    """
    See [DCAT-AP specs:RightsStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#RightsStatement)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["RightsStatement"]
    class_class_curie: ClassVar[str] = "dcterms:RightsStatement"
    class_name: ClassVar[str] = "RightsStatement"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.RightsStatement

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Role(SupportiveEntity):
    """
    See [DCAT-AP specs:Role](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Role)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Role"]
    class_class_curie: ClassVar[str] = "dcat:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Role

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Standard(SupportiveEntity):
    """
    See [DCAT-AP specs:Standard](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Standard)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Standard"]
    class_class_curie: ClassVar[str] = "dcterms:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Standard

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Surrounding(YAMLRoot):
    """
    The surrounding in which the dataset creating activity took place (e.g. a lab).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Location"]
    class_class_curie: ClassVar[str] = "prov:Location"
    class_name: ClassVar[str] = "Surrounding"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Surrounding

    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


class Laboratory(Surrounding):
    """
    A facility that provides controlled conditions in which scientific or technological research, experiments, and
    measurement may be performed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ENVO["01001405"]
    class_class_curie: ClassVar[str] = "ENVO:01001405"
    class_name: ClassVar[str] = "Laboratory"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Laboratory


@dataclass(repr=False)
class TimeInstant(SupportiveEntity):
    """
    See [DCAT-AP specs:TimeInstant](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TimeInstant)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME["Instant"]
    class_class_curie: ClassVar[str] = "time:Instant"
    class_name: ClassVar[str] = "TimeInstant"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.TimeInstant

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InChIKey(QualitativeAttribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000059"]
    class_class_curie: ClassVar[str] = "CHEMINF:000059"
    class_name: ClassVar[str] = "InChIKey"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.InChIKey

    value: str = None

@dataclass(repr=False)
class InChi(QualitativeAttribute):
    """
    A structure descriptor which conforms to the InChI format specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000113"]
    class_class_curie: ClassVar[str] = "CHEMINF:000113"
    class_name: ClassVar[str] = "InChi"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.InChi

    value: str = None

@dataclass(repr=False)
class MolecularFormula(QualitativeAttribute):
    """
    A structure descriptor which identifies each constituent element by its chemical symbol and indicates the number
    of atoms of each element found in each discrete molecule of that compound.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000042"]
    class_class_curie: ClassVar[str] = "CHEMINF:000042"
    class_name: ClassVar[str] = "MolecularFormula"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.MolecularFormula

    value: str = None

@dataclass(repr=False)
class IUPACName(QualitativeAttribute):
    """
    A systematic name which is formulated according to the rules and recommendations for chemical nomenclature set out
    by the International Union of Pure and Applied Chemistry (IUPAC).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000107"]
    class_class_curie: ClassVar[str] = "CHEMINF:000107"
    class_name: ClassVar[str] = "IUPACName"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.IUPACName

    value: str = None

@dataclass(repr=False)
class SMILES(QualitativeAttribute):
    """
    A structure descriptor that denotes a molecular structure as a graph and conforms to the SMILES format
    specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000018"]
    class_class_curie: ClassVar[str] = "CHEMINF:000018"
    class_name: ClassVar[str] = "SMILES"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.SMILES

    value: str = None

@dataclass(repr=False)
class Concentration(QuantitativeAttribute):
    """
    A QuantitativeAttribute of a ChemicalSubstance that represents the amount of a constituent divided by the volume
    of the mixture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002820"]
    class_class_curie: ClassVar[str] = "CHMO:0002820"
    class_name: ClassVar[str] = "Concentration"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Concentration

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class AmountOfSubstance(QuantitativeAttribute):
    """
    The total amount of substance used in a ChemicalReaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "AmountOfSubstance"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.AmountOfSubstance

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class PHValue(QuantitativeAttribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001089"]
    class_class_curie: ClassVar[str] = "SIO:001089"
    class_name: ClassVar[str] = "PHValue"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.PHValue

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class ChemicalReaction(Activity):
    """
    A process that leads to the transformation of one set of chemical substances to another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010345"]
    class_class_curie: ClassVar[str] = "SIO:010345"
    class_name: ClassVar[str] = "ChemicalReaction"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ChemicalReaction

    id: Union[str, ChemicalReactionId] = None
    used_starting_material: Optional[Union[dict[Union[str, StartingMaterialId], Union[dict, "StartingMaterial"]], list[Union[dict, "StartingMaterial"]]]] = empty_dict()
    used_reactant: Optional[Union[dict[Union[str, ReagentId], Union[dict, "Reagent"]], list[Union[dict, "Reagent"]]]] = empty_dict()
    generated_product: Optional[Union[dict[Union[str, ChemicalProductId], Union[dict, "ChemicalProduct"]], list[Union[dict, "ChemicalProduct"]]]] = empty_dict()
    used_catalyst: Optional[Union[dict[Union[str, CatalystId], Union[dict, "Catalyst"]], list[Union[dict, "Catalyst"]]]] = empty_dict()
    used_solvent: Optional[Union[dict[Union[str, DissolvingSubstanceId], Union[dict, "DissolvingSubstance"]], list[Union[dict, "DissolvingSubstance"]]]] = empty_dict()
    has_duration: Optional[str] = None
    used_reactor: Optional[Union[dict[Union[str, ReactorId], Union[dict, "Reactor"]], list[Union[dict, "Reactor"]]]] = empty_dict()
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_yield: Optional[Union[Union[dict, "Yield"], list[Union[dict, "Yield"]]]] = empty_list()
    has_reaction_step: Optional[Union[str, ChemicalReactionId]] = None
    related_resource: Optional[Union[dict[Union[str, ResourceId], Union[dict, Resource]], list[Union[dict, Resource]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalReactionId):
            self.id = ChemicalReactionId(self.id)

        self._normalize_inlined_as_list(slot_name="used_starting_material", slot_type=StartingMaterial, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_reactant", slot_type=Reagent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="generated_product", slot_type=ChemicalProduct, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_catalyst", slot_type=Catalyst, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_solvent", slot_type=DissolvingSubstance, key_name="id", keyed=True)

        if self.has_duration is not None and not isinstance(self.has_duration, str):
            self.has_duration = str(self.has_duration)

        self._normalize_inlined_as_list(slot_name="used_reactor", slot_type=Reactor, key_name="id", keyed=True)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        if not isinstance(self.has_yield, list):
            self.has_yield = [self.has_yield] if self.has_yield is not None else []
        self.has_yield = [v if isinstance(v, Yield) else Yield(**as_dict(v)) for v in self.has_yield]

        if self.has_reaction_step is not None and not isinstance(self.has_reaction_step, ChemicalReactionId):
            self.has_reaction_step = ChemicalReactionId(self.has_reaction_step)

        self._normalize_inlined_as_list(slot_name="related_resource", slot_type=Resource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DissolvingSubstance(AgenticEntity):
    """
    A liquid ChemicalSubstance that dissolves or that is capable of dissolving a ChemicalSubstance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010417"]
    class_class_curie: ClassVar[str] = "SIO:010417"
    class_name: ClassVar[str] = "DissolvingSubstance"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.DissolvingSubstance

    id: Union[str, DissolvingSubstanceId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    has_qualitative_attribute: Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, "PercentageOfTotal"], list[Union[dict, "PercentageOfTotal"]]]] = empty_list()
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], list[Union[dict, "ChemicalEntity"]]]] = empty_dict()
    has_molar_equivalent: Optional[Union[Union[dict, "MolarEquivalent"], list[Union[dict, "MolarEquivalent"]]]] = empty_list()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DissolvingSubstanceId):
            self.id = DissolvingSubstanceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalyst(AgenticEntity):
    """
    A ChemicalSubstance or MaterialEntity that initiates or accelerates a ChemicalReaction without itself being
    affected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010344"]
    class_class_curie: ClassVar[str] = "SIO:010344"
    class_name: ClassVar[str] = "Catalyst"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Catalyst

    id: Union[str, CatalystId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    has_qualitative_attribute: Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()
    has_molar_equivalent: Optional[Union[Union[dict, "MolarEquivalent"], list[Union[dict, "MolarEquivalent"]]]] = empty_list()
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], list[Union[dict, "ChemicalEntity"]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, "PercentageOfTotal"], list[Union[dict, "PercentageOfTotal"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalystId):
            self.id = CatalystId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reactor(Device):
    """
    A reactor is a container for controlling a biological or chemical reaction or process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFE["0000153"]
    class_class_curie: ClassVar[str] = "AFE:0000153"
    class_name: ClassVar[str] = "Reactor"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Reactor

    id: Union[str, ReactorId] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactorId):
            self.id = ReactorId(self.id)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Yield(QuantitativeAttribute):
    """
    A dimensionless physical quantity describing the fraction of a product B that is formed from a reactant A taking
    into account the stoichiometry. If A fully reacts to B without side-reactions, the yield of product B is 1 (or 100
    %).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Yield"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Yield

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class MolarEquivalent(QuantitativeAttribute):
    """
    A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a
    reference substance in a chemical reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "MolarEquivalent"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.MolarEquivalent

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class PercentageOfTotal(QuantitativeAttribute):
    """
    A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a
    reference substance in a chemical reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "PercentageOfTotal"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.PercentageOfTotal

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class NMRAnalysisDataset(AnalysisDataset):
    """
    A dataset that is the result of a NMRSpectralAnalysis of a NMRSample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "NMRAnalysisDataset"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NMRAnalysisDataset

    id: Union[str, NMRAnalysisDatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Optional[Union[dict[Union[str, NMRSpectralAnalysisId], Union[dict, "NMRSpectralAnalysis"]], list[Union[dict, "NMRSpectralAnalysis"]]]] = empty_dict()
    is_about_entity: Optional[Union[dict[Union[str, NMRSampleId], Union[dict, "NMRSample"]], list[Union[dict, "NMRSample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NMRAnalysisDatasetId):
            self.id = NMRAnalysisDatasetId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=NMRSpectralAnalysis, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="is_about_entity", slot_type=NMRSample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NMRSpectralAnalysis(DataAnalysis):
    """
    A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectrum generated by a NMRSpectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1400042"]
    class_class_curie: ClassVar[str] = "NMR:1400042"
    class_name: ClassVar[str] = "NMRSpectralAnalysis"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NMRSpectralAnalysis

    id: Union[str, NMRSpectralAnalysisId] = None
    evaluated_entity: Optional[Union[dict[Union[str, NMRSpectrumId], Union[dict, "NMRSpectrum"]], list[Union[dict, "NMRSpectrum"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NMRSpectralAnalysisId):
            self.id = NMRSpectralAnalysisId(self.id)

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=NMRSpectrum, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NMRSpectrum(AnalysisSourceData):
    """
    Chemical shift data obtained via nuclear magnetic resonance (NMR) spectroscopy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1002007"]
    class_class_curie: ClassVar[str] = "NMR:1002007"
    class_name: ClassVar[str] = "NMRSpectrum"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NMRSpectrum

    id: Union[str, NMRSpectrumId] = None
    was_generated_by: Optional[Union[dict[Union[str, NMRSpectroscopyId], Union[dict, "NMRSpectroscopy"]], list[Union[dict, "NMRSpectroscopy"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NMRSpectrumId):
            self.id = NMRSpectrumId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=NMRSpectroscopy, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NMRSpectroscopy(DataGeneratingActivity):
    """
    Spectroscopy where the energy states of spin-active nuclei placed in a static magnetic field are interrogated by
    inducing transitions between the states via radio frequency irradiation. Each experiment consists of a sequence of
    radio frequency pulses with delay periods in between them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000613"]
    class_class_curie: ClassVar[str] = "CHMO:0000613"
    class_name: ClassVar[str] = "NMRSpectroscopy"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NMRSpectroscopy

    id: Union[str, NMRSpectroscopyId] = None
    used_spectrometer: Union[dict[Union[str, NMRSpectrometerId], Union[dict, "NMRSpectrometer"]], list[Union[dict, "NMRSpectrometer"]]] = empty_dict()
    used_solvent: Union[dict[Union[str, NMRSolventId], Union[dict, "NMRSolvent"]], list[Union[dict, "NMRSolvent"]]] = empty_dict()
    used_pulse_sequence: Union[dict, "PulseSequence"] = None
    probes_nucleus: Union[dict[Union[str, AcquisitionNucleusId], Union[dict, "AcquisitionNucleus"]], list[Union[dict, "AcquisitionNucleus"]]] = empty_dict()
    evaluated_entity: Union[dict[Union[str, NMRSampleId], Union[dict, "NMRSample"]], list[Union[dict, "NMRSample"]]] = empty_dict()
    rdf_type: Union[dict, DefinedTerm] = None
    used_number_of_scans: Optional[Union[dict, "NumberOfScans"]] = None
    used_sample_temperature: Optional[Union[dict, "NMRSampleTemperature"]] = None
    used_calibration_compound: Optional[Union[dict[Union[str, ShiftCalibrationCompoundId], Union[dict, "ShiftCalibrationCompound"]], list[Union[dict, "ShiftCalibrationCompound"]]]] = empty_dict()
    used_reference_compound: Optional[Union[dict[Union[str, ShiftReferenceCompoundId], Union[dict, "ShiftReferenceCompound"]], list[Union[dict, "ShiftReferenceCompound"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NMRSpectroscopyId):
            self.id = NMRSpectroscopyId(self.id)

        if self._is_empty(self.used_spectrometer):
            self.MissingRequiredField("used_spectrometer")
        self._normalize_inlined_as_list(slot_name="used_spectrometer", slot_type=NMRSpectrometer, key_name="id", keyed=True)

        if self._is_empty(self.used_solvent):
            self.MissingRequiredField("used_solvent")
        self._normalize_inlined_as_list(slot_name="used_solvent", slot_type=NMRSolvent, key_name="id", keyed=True)

        if self._is_empty(self.used_pulse_sequence):
            self.MissingRequiredField("used_pulse_sequence")
        if not isinstance(self.used_pulse_sequence, PulseSequence):
            self.used_pulse_sequence = PulseSequence(**as_dict(self.used_pulse_sequence))

        if self._is_empty(self.probes_nucleus):
            self.MissingRequiredField("probes_nucleus")
        self._normalize_inlined_as_list(slot_name="probes_nucleus", slot_type=AcquisitionNucleus, key_name="id", keyed=True)

        if self._is_empty(self.evaluated_entity):
            self.MissingRequiredField("evaluated_entity")
        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=NMRSample, key_name="id", keyed=True)

        if self._is_empty(self.rdf_type):
            self.MissingRequiredField("rdf_type")
        if not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        if self.used_number_of_scans is not None and not isinstance(self.used_number_of_scans, NumberOfScans):
            self.used_number_of_scans = NumberOfScans(**as_dict(self.used_number_of_scans))

        if self.used_sample_temperature is not None and not isinstance(self.used_sample_temperature, NMRSampleTemperature):
            self.used_sample_temperature = NMRSampleTemperature(**as_dict(self.used_sample_temperature))

        self._normalize_inlined_as_list(slot_name="used_calibration_compound", slot_type=ShiftCalibrationCompound, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_reference_compound", slot_type=ShiftReferenceCompound, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NMRSpectrometer(Device):
    """
    A Spectrometer used to conduct NMR experiments consisting of a magnet housing a sample space surrounded by two
    coils which act to transmit radio frequency radiation to the sample and to detect the response of the sample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0001807"]
    class_class_curie: ClassVar[str] = "CHMO:0001807"
    class_name: ClassVar[str] = "NMRSpectrometer"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NMRSpectrometer

    id: Union[str, NMRSpectrometerId] = None
    has_proton_frequency: Optional[Union[Union[dict, "NominalProtonFrequency"], list[Union[dict, "NominalProtonFrequency"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NMRSpectrometerId):
            self.id = NMRSpectrometerId(self.id)

        if not isinstance(self.has_proton_frequency, list):
            self.has_proton_frequency = [self.has_proton_frequency] if self.has_proton_frequency is not None else []
        self.has_proton_frequency = [v if isinstance(v, NominalProtonFrequency) else NominalProtonFrequency(**as_dict(v)) for v in self.has_proton_frequency]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcquisitionNucleus(AgenticEntity):
    """
    The nucleus of an Atom that is being studied during an NMR analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1400083"]
    class_class_curie: ClassVar[str] = "NMR:1400083"
    class_name: ClassVar[str] = "AcquisitionNucleus"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.AcquisitionNucleus

    id: Union[str, AcquisitionNucleusId] = None
    nucleus_of: Union[dict, "Atom"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcquisitionNucleusId):
            self.id = AcquisitionNucleusId(self.id)

        if self._is_empty(self.nucleus_of):
            self.MissingRequiredField("nucleus_of")
        if not isinstance(self.nucleus_of, Atom):
            self.nucleus_of = Atom(**as_dict(self.nucleus_of))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NMRSolvent(DissolvingSubstance):
    """
    A DissolvingSubstance that is used in nuclear magnetic resonance NMRSpectroscopy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1000330"]
    class_class_curie: ClassVar[str] = "NMR:1000330"
    class_name: ClassVar[str] = "NMRSolvent"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NMRSolvent

    id: Union[str, NMRSolventId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NMRSolventId):
            self.id = NMRSolventId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PulseSequence(QualitativeAttribute):
    """
    A string that denotes sequence of excitation pulses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1400037"]
    class_class_curie: ClassVar[str] = "NMR:1400037"
    class_name: ClassVar[str] = "PulseSequence"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.PulseSequence

    value: str = None

@dataclass(repr=False)
class NominalProtonFrequency(QuantitativeAttribute):
    """
    Resonance frequency of 1H at the field strength of the NMR magnet, rounded to 10-fold numbers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "NominalProtonFrequency"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NominalProtonFrequency

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class CalibrationPeakShift(QuantitativeAttribute):
    """
    The chemical shift of the peak used for chemical shift calibration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1000223"]
    class_class_curie: ClassVar[str] = "NMR:1000223"
    class_name: ClassVar[str] = "CalibrationPeakShift"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.CalibrationPeakShift

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class NumberOfScans(QuantitativeAttribute):
    """
    The number of repeat scans performed and summed to create the data set for an NMRSample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1400087"]
    class_class_curie: ClassVar[str] = "NMR:1400087"
    class_name: ClassVar[str] = "NumberOfScans"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NumberOfScans

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Materialistic(YAMLRoot):
    """
    A LinkML mixin used to pass down properties common to all material entities. It is needed for example to have
    MaterialSample have the same properties as MaterialEntity, although it is defined as a subclass of
    EvaluatedEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MATERIAL_ENTITIES_AP["Materialistic"]
    class_class_curie: ClassVar[str] = "material_entities_ap:Materialistic"
    class_name: ClassVar[str] = "Materialistic"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Materialistic

    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialEntity(Entity):
    """
    A material is an Entity that has some portion of matter as proper part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000040"]
    class_class_curie: ClassVar[str] = "BFO:0000040"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    has_part: Optional[Union[dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], list[Union[dict, "MaterialEntity"]]]] = empty_dict()
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=MaterialEntity, key_name="id", keyed=True)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(MaterialEntity):
    """
    Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex,
    conformer etc., identifiable as a separately distinguishable entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["23367"]
    class_class_curie: ClassVar[str] = "CHEBI:23367"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    inchi: Optional[Union[Union[dict, InChi], list[Union[dict, InChi]]]] = empty_list()
    inchikey: Optional[Union[Union[dict, InChIKey], list[Union[dict, InChIKey]]]] = empty_list()
    smiles: Optional[Union[Union[dict, SMILES], list[Union[dict, SMILES]]]] = empty_list()
    molecular_formula: Optional[Union[Union[dict, MolecularFormula], list[Union[dict, MolecularFormula]]]] = empty_list()
    iupac_name: Optional[Union[Union[dict, IUPACName], list[Union[dict, IUPACName]]]] = empty_list()
    has_molar_mass: Optional[Union[Union[dict, "MolarMass"], list[Union[dict, "MolarMass"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if not isinstance(self.inchi, list):
            self.inchi = [self.inchi] if self.inchi is not None else []
        self.inchi = [v if isinstance(v, InChi) else InChi(**as_dict(v)) for v in self.inchi]

        if not isinstance(self.inchikey, list):
            self.inchikey = [self.inchikey] if self.inchikey is not None else []
        self.inchikey = [v if isinstance(v, InChIKey) else InChIKey(**as_dict(v)) for v in self.inchikey]

        if not isinstance(self.smiles, list):
            self.smiles = [self.smiles] if self.smiles is not None else []
        self.smiles = [v if isinstance(v, SMILES) else SMILES(**as_dict(v)) for v in self.smiles]

        if not isinstance(self.molecular_formula, list):
            self.molecular_formula = [self.molecular_formula] if self.molecular_formula is not None else []
        self.molecular_formula = [v if isinstance(v, MolecularFormula) else MolecularFormula(**as_dict(v)) for v in self.molecular_formula]

        if not isinstance(self.iupac_name, list):
            self.iupac_name = [self.iupac_name] if self.iupac_name is not None else []
        self.iupac_name = [v if isinstance(v, IUPACName) else IUPACName(**as_dict(v)) for v in self.iupac_name]

        if not isinstance(self.has_molar_mass, list):
            self.has_molar_mass = [self.has_molar_mass] if self.has_molar_mass is not None else []
        self.has_molar_mass = [v if isinstance(v, MolarMass) else MolarMass(**as_dict(v)) for v in self.has_molar_mass]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Atom(ChemicalEntity):
    """
    A MaterialEntity constituting the smallest component of an element having the chemical properties of the element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["33250"]
    class_class_curie: ClassVar[str] = "CHEBI:33250"
    class_name: ClassVar[str] = "Atom"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Atom

    id: Union[str, AtomId] = None
    rdf_type: Union[dict, DefinedTerm] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AtomId):
            self.id = AtomId(self.id)

        if self._is_empty(self.rdf_type):
            self.MissingRequiredField("rdf_type")
        if not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalSubstance(MaterialEntity):
    """
    A MaterialEntity of constant composition, composed of chemical entities of the same type or of different types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["59999"]
    class_class_curie: ClassVar[str] = "CHEBI:59999"
    class_name: ClassVar[str] = "ChemicalSubstance"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ChemicalSubstance

    id: Union[str, ChemicalSubstanceId] = None
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, PercentageOfTotal], list[Union[dict, PercentageOfTotal]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Polymer(ChemicalSubstance):
    """
    A ChemicalSubstance that is composed of macromolecules of different kinds and which may be differentiated by
    composition, length, degree of branching etc..
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["60027"]
    class_class_curie: ClassVar[str] = "CHEBI:60027"
    class_name: ClassVar[str] = "Polymer"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Polymer

    id: Union[str, PolymerId] = None

@dataclass(repr=False)
class StartingMaterial(ChemicalSubstance):
    """
    A ChemicalSubstance with that has a starting material role in a synthesis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROCO["0000029"]
    class_class_curie: ClassVar[str] = "PROCO:0000029"
    class_name: ClassVar[str] = "StartingMaterial"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.StartingMaterial

    id: Union[str, StartingMaterialId] = None
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StartingMaterialId):
            self.id = StartingMaterialId(self.id)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reagent(ChemicalSubstance):
    """
    A ChemicalSubstance that is consumed or transformed in a ChemicalReaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010411"]
    class_class_curie: ClassVar[str] = "SIO:010411"
    class_name: ClassVar[str] = "Reagent"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Reagent

    id: Union[str, ReagentId] = None
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReagentId):
            self.id = ReagentId(self.id)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalProduct(ChemicalSubstance):
    """
    A chemical substance that is produced by a ChemicalReaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C48810"]
    class_class_curie: ClassVar[str] = "NCIT:C48810"
    class_name: ClassVar[str] = "ChemicalProduct"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ChemicalProduct

    id: Union[str, ChemicalProductId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalProductId):
            self.id = ChemicalProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ShiftCalibrationCompound(ChemicalEntity):
    """
    A ChemicalEntity that produces one or more peaks used for chemical shift calibration in nuclear magnetic resonance
    (NMR) spectroscopy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["0002003"]
    class_class_curie: ClassVar[str] = "NMR:0002003"
    class_name: ClassVar[str] = "ShiftCalibrationCompound"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ShiftCalibrationCompound

    id: Union[str, ShiftCalibrationCompoundId] = None
    has_calibration_shift: Optional[Union[Union[dict, CalibrationPeakShift], list[Union[dict, CalibrationPeakShift]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ShiftCalibrationCompoundId):
            self.id = ShiftCalibrationCompoundId(self.id)

        if not isinstance(self.has_calibration_shift, list):
            self.has_calibration_shift = [self.has_calibration_shift] if self.has_calibration_shift is not None else []
        self.has_calibration_shift = [v if isinstance(v, CalibrationPeakShift) else CalibrationPeakShift(**as_dict(v)) for v in self.has_calibration_shift]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ShiftReferenceCompound(ShiftCalibrationCompound):
    """
    A ShiftCalibrationCompound that produces a peak used as reference frequency in the delta chemical shift scale in
    nuclear magnetic resonance (NMR) spectroscopy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1400033"]
    class_class_curie: ClassVar[str] = "NMR:1400033"
    class_name: ClassVar[str] = "ShiftReferenceCompound"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.ShiftReferenceCompound

    id: Union[str, ShiftReferenceCompoundId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ShiftReferenceCompoundId):
            self.id = ShiftReferenceCompoundId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CharacterizedCompound(ChemicalEntity):
    """
    A ChemicalEntity that being characterized in an NMRSample using data acquired from a NMRSpectroscopy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["0002001"]
    class_class_curie: ClassVar[str] = "NMR:0002001"
    class_name: ClassVar[str] = "CharacterizedCompound"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.CharacterizedCompound

    id: Union[str, CharacterizedCompoundId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CharacterizedCompoundId):
            self.id = CharacterizedCompoundId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialSample(EvaluatedEntity):
    """
    A Sample that was derived from a previous MaterialSample or some other kind of MaterialEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000747"]
    class_class_curie: ClassVar[str] = "OBI:0000747"
    class_name: ClassVar[str] = "MaterialSample"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.MaterialSample

    id: Union[str, MaterialSampleId] = None
    derived_from: Optional[Union[dict, Entity]] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)

        if self.derived_from is not None and not isinstance(self.derived_from, Entity):
            self.derived_from = Entity(**as_dict(self.derived_from))

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        if not isinstance(self.has_temperature, list):
            self.has_temperature = [self.has_temperature] if self.has_temperature is not None else []
        self.has_temperature = [v if isinstance(v, Temperature) else Temperature(**as_dict(v)) for v in self.has_temperature]

        if not isinstance(self.has_mass, list):
            self.has_mass = [self.has_mass] if self.has_mass is not None else []
        self.has_mass = [v if isinstance(v, Mass) else Mass(**as_dict(v)) for v in self.has_mass]

        if not isinstance(self.has_volume, list):
            self.has_volume = [self.has_volume] if self.has_volume is not None else []
        self.has_volume = [v if isinstance(v, Volume) else Volume(**as_dict(v)) for v in self.has_volume]

        if not isinstance(self.has_density, list):
            self.has_density = [self.has_density] if self.has_density is not None else []
        self.has_density = [v if isinstance(v, Density) else Density(**as_dict(v)) for v in self.has_density]

        if not isinstance(self.has_pressure, list):
            self.has_pressure = [self.has_pressure] if self.has_pressure is not None else []
        self.has_pressure = [v if isinstance(v, Pressure) else Pressure(**as_dict(v)) for v in self.has_pressure]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubstanceSample(MaterialSample):
    """
    A MaterialSample derived from a ChemicalSubstance that is of interest in an analytical procedure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001378"]
    class_class_curie: ClassVar[str] = "SIO:001378"
    class_name: ClassVar[str] = "SubstanceSample"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.SubstanceSample

    id: Union[str, SubstanceSampleId] = None
    has_qualitative_attribute: Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]] = empty_dict()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, PercentageOfTotal], list[Union[dict, PercentageOfTotal]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubstanceSampleId):
            self.id = SubstanceSampleId(self.id)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Entity, key_name="id", keyed=True)

        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PolymerSample(SubstanceSample):
    """
    A SubstanceSample derived from a Polymer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001378"]
    class_class_curie: ClassVar[str] = "SIO:001378"
    class_name: ClassVar[str] = "PolymerSample"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.PolymerSample

    id: Union[str, PolymerSampleId] = None
    has_qualitative_attribute: Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]] = empty_dict()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()
    has_percentage_of_total: Optional[Union[Union[dict, PercentageOfTotal], list[Union[dict, PercentageOfTotal]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolymerSampleId):
            self.id = PolymerSampleId(self.id)

        if not isinstance(self.has_qualitative_attribute, list):
            self.has_qualitative_attribute = [self.has_qualitative_attribute] if self.has_qualitative_attribute is not None else []
        self.has_qualitative_attribute = [v if isinstance(v, QualitativeAttribute) else QualitativeAttribute(**as_dict(v)) for v in self.has_qualitative_attribute]

        if not isinstance(self.has_quantitative_attribute, list):
            self.has_quantitative_attribute = [self.has_quantitative_attribute] if self.has_quantitative_attribute is not None else []
        self.has_quantitative_attribute = [v if isinstance(v, QuantitativeAttribute) else QuantitativeAttribute(**as_dict(v)) for v in self.has_quantitative_attribute]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Entity, key_name="id", keyed=True)

        if not isinstance(self.has_concentration, list):
            self.has_concentration = [self.has_concentration] if self.has_concentration is not None else []
        self.has_concentration = [v if isinstance(v, Concentration) else Concentration(**as_dict(v)) for v in self.has_concentration]

        if not isinstance(self.has_ph_value, list):
            self.has_ph_value = [self.has_ph_value] if self.has_ph_value is not None else []
        self.has_ph_value = [v if isinstance(v, PHValue) else PHValue(**as_dict(v)) for v in self.has_ph_value]

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if not isinstance(self.has_molar_equivalent, list):
            self.has_molar_equivalent = [self.has_molar_equivalent] if self.has_molar_equivalent is not None else []
        self.has_molar_equivalent = [v if isinstance(v, MolarEquivalent) else MolarEquivalent(**as_dict(v)) for v in self.has_molar_equivalent]

        if not isinstance(self.has_amount, list):
            self.has_amount = [self.has_amount] if self.has_amount is not None else []
        self.has_amount = [v if isinstance(v, AmountOfSubstance) else AmountOfSubstance(**as_dict(v)) for v in self.has_amount]

        if not isinstance(self.has_percentage_of_total, list):
            self.has_percentage_of_total = [self.has_percentage_of_total] if self.has_percentage_of_total is not None else []
        self.has_percentage_of_total = [v if isinstance(v, PercentageOfTotal) else PercentageOfTotal(**as_dict(v)) for v in self.has_percentage_of_total]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NMRSample(SubstanceSample):
    """
    A SubstanceSample that has been prepared for chemical analysis by NMR.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1400128"]
    class_class_curie: ClassVar[str] = "NMR:1400128"
    class_name: ClassVar[str] = "NMRSample"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NMRSample

    id: Union[str, NMRSampleId] = None
    composed_of: Union[dict[Union[str, CharacterizedCompoundId], Union[dict, CharacterizedCompound]], list[Union[dict, CharacterizedCompound]]] = empty_dict()
    derived_from: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NMRSampleId):
            self.id = NMRSampleId(self.id)

        if self._is_empty(self.composed_of):
            self.MissingRequiredField("composed_of")
        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=CharacterizedCompound, key_name="id", keyed=True)

        if self.derived_from is not None and not isinstance(self.derived_from, Entity):
            self.derived_from = Entity(**as_dict(self.derived_from))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Temperature(QuantitativeAttribute):
    """
    A physical quantity that quantitatively expresses the attribute of hotness or coldness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Temperature"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Temperature

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class NMRSampleTemperature(Temperature):
    """
    The temperature of the NMR Sample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMR["1400262"]
    class_class_curie: ClassVar[str] = "NMR:1400262"
    class_name: ClassVar[str] = "NMRSampleTemperature"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.NMRSampleTemperature

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Mass(QuantitativeAttribute):
    """
    The strength of a body's gravitational attraction to other bodies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Mass"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Mass

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class MolarMass(Mass):
    """
    A Mass (physical quality) that quantifies the mass of a homogeneous ChemicalSubstance containing 6.02 x 10^23
    atoms or molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFR["0002409"]
    class_class_curie: ClassVar[str] = "AFR:0002409"
    class_name: ClassVar[str] = "MolarMass"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.MolarMass

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Volume(QuantitativeAttribute):
    """
    A measure of regions in three-dimensional space.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Volume

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Density(QuantitativeAttribute):
    """
    A measure of the mass per unit volume of a substance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001406"]
    class_class_curie: ClassVar[str] = "SIO:001406"
    class_name: ClassVar[str] = "Density"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Density

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Pressure(QuantitativeAttribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Pressure"
    class_model_uri: ClassVar[URIRef] = DCAT_4C_AP.Pressure

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

# Enumerations
class DatasetThemes(EnumDefinitionImpl):

    AGRI = PermissibleValue(
        text="AGRI",
        description="Agriculture, fisheries, forestry and food",
        meaning=None)
    ECON = PermissibleValue(
        text="ECON",
        description="Economy and finance",
        meaning=None)
    EDUC = PermissibleValue(
        text="EDUC",
        description="Education, culture and sport",
        meaning=None)
    ENER = PermissibleValue(
        text="ENER",
        description="Energy",
        meaning=None)
    ENVI = PermissibleValue(
        text="ENVI",
        description="Environment",
        meaning=None)
    GOVE = PermissibleValue(
        text="GOVE",
        description="Government and public sector",
        meaning=None)
    HEAL = PermissibleValue(
        text="HEAL",
        description="Health",
        meaning=None)
    INTR = PermissibleValue(
        text="INTR",
        description="International issues",
        meaning=None)
    JUST = PermissibleValue(
        text="JUST",
        description="Justice, legal system and public safety",
        meaning=None)
    OP_DATPRO = PermissibleValue(
        text="OP_DATPRO",
        description="Provisional data",
        meaning=None)
    REGI = PermissibleValue(
        text="REGI",
        description="Regions and cities",
        meaning=None)
    SOCI = PermissibleValue(
        text="SOCI",
        description="Population and society",
        meaning=None)
    TECH = PermissibleValue(
        text="TECH",
        description="Science and technology",
        meaning=None)
    TRAN = PermissibleValue(
        text="TRAN",
        description="Transport",
        meaning=None)

    _defn = EnumDefinition(
        name="DatasetThemes",
    )

class TopLevelMediaTypes(EnumDefinitionImpl):

    application = PermissibleValue(text="application")
    audio = PermissibleValue(text="audio")
    example = PermissibleValue(text="example")
    font = PermissibleValue(text="font")
    haptics = PermissibleValue(text="haptics")
    image = PermissibleValue(text="image")
    message = PermissibleValue(text="message")
    model = PermissibleValue(text="model")
    multipart = PermissibleValue(text="multipart")
    text = PermissibleValue(text="text")
    video = PermissibleValue(text="video")

    _defn = EnumDefinition(
        name="TopLevelMediaTypes",
    )

class QUDTQuantityKindEnum(EnumDefinitionImpl):
    """
    Possible kinds of quantifiable attribute types provided as QUDT QualityKind instances.
    """
    _defn = EnumDefinition(
        name="QUDTQuantityKindEnum",
        description="Possible kinds of quantifiable attribute types provided as QUDT QualityKind instances.",
    )

class QUDTUnitEnum(EnumDefinitionImpl):
    """
    Possible kinds of QUDT unit instances.
    """
    _defn = EnumDefinition(
        name="QUDTUnitEnum",
        description="Possible kinds of QUDT unit instances.",
    )

class NMRAssayEnum(EnumDefinitionImpl):
    """
    NMR types from the Chemical Methods Ontology
    """
    _defn = EnumDefinition(
        name="NMRAssayEnum",
        description="NMR types from the Chemical Methods Ontology",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CHMO:0000595",
            PermissibleValue(
                text="CHMO:0000595",
                title="13C nuclear magnetic resonance spectroscopy",
                description="""Spectroscopy where the energy states of 13C nuclei placed in a static magnetic field are interrogated by inducing transitions between the states via radio frequency irradiation. Each experiment consists of a sequence of radio frequency pulses with delay periods in between them.""",
                meaning=CHMO["0000595"]))

class PhysicalStateEnum(EnumDefinitionImpl):

    SOLID = PermissibleValue(
        text="SOLID",
        description="A state of matter in which molecules are closely packed and cannot move past each other.",
        meaning=PATO["0001736"])
    CRYSTAL = PermissibleValue(
        text="CRYSTAL",
        description="""A solid state of matter whose constituents (such as atoms, molecules, or ions) are arranged in a highly ordered microscopic structure, forming a crystal lattice that extends in all directions.""",
        meaning=PATO["0002066"])
    LIQUID = PermissibleValue(
        text="LIQUID",
        description="""A state of matter with a definite volume but no fixed shape. Liquids adapt to the shape of their container and are nearly incompressible, maintaining their volume even under pressure.""",
        meaning=PATO["0001735"])
    GASEOUS = PermissibleValue(
        text="GASEOUS",
        description="A state of matter with neither fixed volume nor fixed shape.",
        meaning=PATO["0001737"])

    _defn = EnumDefinition(
        name="PhysicalStateEnum",
    )

# Slots
class slots:
    pass

slots.access_URL = Slot(uri=DCAT.accessURL, name="access_URL", curie=DCAT.curie('accessURL'),
                   model_uri=DCAT_4C_AP.access_URL, domain=None, range=Optional[str])

slots.access_rights = Slot(uri=DCTERMS.accessRights, name="access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=DCAT_4C_AP.access_rights, domain=None, range=Optional[str])

slots.access_service = Slot(uri=DCAT.accessService, name="access_service", curie=DCAT.curie('accessService'),
                   model_uri=DCAT_4C_AP.access_service, domain=None, range=Optional[str])

slots.algorithm = Slot(uri=SPDX.algorithm, name="algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=DCAT_4C_AP.algorithm, domain=None, range=Optional[str])

slots.applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=DCAT_4C_AP.applicable_legislation, domain=None, range=Optional[str])

slots.application_profile = Slot(uri=DCTERMS.conformsTo, name="application_profile", curie=DCTERMS.curie('conformsTo'),
                   model_uri=DCAT_4C_AP.application_profile, domain=None, range=Optional[str])

slots.availability = Slot(uri=DCATAP.availability, name="availability", curie=DCATAP.curie('availability'),
                   model_uri=DCAT_4C_AP.availability, domain=None, range=Optional[str])

slots.bbox = Slot(uri=DCAT.bbox, name="bbox", curie=DCAT.curie('bbox'),
                   model_uri=DCAT_4C_AP.bbox, domain=None, range=Optional[str])

slots.beginning = Slot(uri=TIME.hasBeginning, name="beginning", curie=TIME.curie('hasBeginning'),
                   model_uri=DCAT_4C_AP.beginning, domain=None, range=Optional[str])

slots.byte_size = Slot(uri=DCAT.byteSize, name="byte_size", curie=DCAT.curie('byteSize'),
                   model_uri=DCAT_4C_AP.byte_size, domain=None, range=Optional[str])

slots.carried_out_by = Slot(uri=PROV.wasAssociatedWith, name="carried_out_by", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=DCAT_4C_AP.carried_out_by, domain=None, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, AgenticEntity]], list[Union[dict, AgenticEntity]]]])

slots.catalogue = Slot(uri=DCAT.catalog, name="catalogue", curie=DCAT.curie('catalog'),
                   model_uri=DCAT_4C_AP.catalogue, domain=None, range=Optional[str])

slots.centroid = Slot(uri=DCAT.centroid, name="centroid", curie=DCAT.curie('centroid'),
                   model_uri=DCAT_4C_AP.centroid, domain=None, range=Optional[str])

slots.change_type = Slot(uri=ADMS.status, name="change_type", curie=ADMS.curie('status'),
                   model_uri=DCAT_4C_AP.change_type, domain=None, range=Optional[str])

slots.checksum = Slot(uri=SPDX.checksum, name="checksum", curie=SPDX.curie('checksum'),
                   model_uri=DCAT_4C_AP.checksum, domain=None, range=Optional[str])

slots.checksum_value = Slot(uri=SPDX.checksumValue, name="checksum_value", curie=SPDX.curie('checksumValue'),
                   model_uri=DCAT_4C_AP.checksum_value, domain=None, range=Optional[str])

slots.compression_format = Slot(uri=DCAT.compressFormat, name="compression_format", curie=DCAT.curie('compressFormat'),
                   model_uri=DCAT_4C_AP.compression_format, domain=None, range=Optional[str])

slots.conforms_to = Slot(uri=DCTERMS.conformsTo, name="conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=DCAT_4C_AP.conforms_to, domain=None, range=Optional[str])

slots.contact_point = Slot(uri=DCAT.contactPoint, name="contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=DCAT_4C_AP.contact_point, domain=None, range=Optional[str])

slots.creator = Slot(uri=DCTERMS.creator, name="creator", curie=DCTERMS.curie('creator'),
                   model_uri=DCAT_4C_AP.creator, domain=None, range=Optional[str])

slots.dataset_distribution = Slot(uri=DCAT.distribution, name="dataset_distribution", curie=DCAT.curie('distribution'),
                   model_uri=DCAT_4C_AP.dataset_distribution, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.description, domain=None, range=Optional[str])

slots.documentation = Slot(uri=FOAF.page, name="documentation", curie=FOAF.curie('page'),
                   model_uri=DCAT_4C_AP.documentation, domain=None, range=Optional[str])

slots.download_URL = Slot(uri=DCAT.downloadURL, name="download_URL", curie=DCAT.curie('downloadURL'),
                   model_uri=DCAT_4C_AP.download_URL, domain=None, range=Optional[str])

slots.end = Slot(uri=TIME.hasEnd, name="end", curie=TIME.curie('hasEnd'),
                   model_uri=DCAT_4C_AP.end, domain=None, range=Optional[str])

slots.end_date = Slot(uri=DCAT.endDate, name="end_date", curie=DCAT.curie('endDate'),
                   model_uri=DCAT_4C_AP.end_date, domain=None, range=Optional[str])

slots.endpoint_URL = Slot(uri=DCAT.endpointURL, name="endpoint_URL", curie=DCAT.curie('endpointURL'),
                   model_uri=DCAT_4C_AP.endpoint_URL, domain=None, range=Optional[str])

slots.endpoint_description = Slot(uri=DCAT.endpointDescription, name="endpoint_description", curie=DCAT.curie('endpointDescription'),
                   model_uri=DCAT_4C_AP.endpoint_description, domain=None, range=Optional[str])

slots.evaluated_activity = Slot(uri=PROV.wasInformedBy, name="evaluated_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=DCAT_4C_AP.evaluated_activity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, EvaluatedActivity]], list[Union[dict, EvaluatedActivity]]]])

slots.evaluated_entity = Slot(uri=PROV.used, name="evaluated_entity", curie=PROV.curie('used'),
                   model_uri=DCAT_4C_AP.evaluated_entity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, EvaluatedEntity]], list[Union[dict, EvaluatedEntity]]]])

slots.format = Slot(uri=DCTERMS.format, name="format", curie=DCTERMS.curie('format'),
                   model_uri=DCAT_4C_AP.format, domain=None, range=Optional[str])

slots.frequency = Slot(uri=DCTERMS.accrualPeriodicity, name="frequency", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=DCAT_4C_AP.frequency, domain=None, range=Optional[str])

slots.geographical_coverage = Slot(uri=DCTERMS.spatial, name="geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=DCAT_4C_AP.geographical_coverage, domain=None, range=Optional[str])

slots.geometry = Slot(uri=LOCN.geometry, name="geometry", curie=LOCN.curie('geometry'),
                   model_uri=DCAT_4C_AP.geometry, domain=None, range=Optional[str])

slots.had_input_activity = Slot(uri=PROV.wasInformedBy, name="had_input_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=DCAT_4C_AP.had_input_activity, domain=None, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, Activity]], list[Union[dict, Activity]]]])

slots.had_input_entity = Slot(uri=PROV.used, name="had_input_entity", curie=PROV.curie('used'),
                   model_uri=DCAT_4C_AP.had_input_entity, domain=None, range=Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]])

slots.had_output_entity = Slot(uri=PROV.generated, name="had_output_entity", curie=PROV.curie('generated'),
                   model_uri=DCAT_4C_AP.had_output_entity, domain=None, range=Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]])

slots.had_role = Slot(uri=DCAT.hadRole, name="had_role", curie=DCAT.curie('hadRole'),
                   model_uri=DCAT_4C_AP.had_role, domain=None, range=Optional[str])

slots.has_dataset = Slot(uri=DCAT.dataset, name="has_dataset", curie=DCAT.curie('dataset'),
                   model_uri=DCAT_4C_AP.has_dataset, domain=None, range=Optional[str])

slots.has_part = Slot(uri=DCTERMS.hasPart, name="has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=DCAT_4C_AP.has_part, domain=None, range=Optional[Union[str, ActivityId]])

slots.has_policy = Slot(uri=ODRL.hasPolicy, name="has_policy", curie=ODRL.curie('hasPolicy'),
                   model_uri=DCAT_4C_AP.has_policy, domain=None, range=Optional[str])

slots.has_qualitative_attribute = Slot(uri=DCTERMS.relation, name="has_qualitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=DCAT_4C_AP.has_qualitative_attribute, domain=None, range=Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]])

slots.has_quantitative_attribute = Slot(uri=DCTERMS.relation, name="has_quantitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=DCAT_4C_AP.has_quantitative_attribute, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.has_version = Slot(uri=DCAT.hasVersion, name="has_version", curie=DCAT.curie('hasVersion'),
                   model_uri=DCAT_4C_AP.has_version, domain=None, range=Optional[str])

slots.homepage = Slot(uri=FOAF.homepage, name="homepage", curie=FOAF.curie('homepage'),
                   model_uri=DCAT_4C_AP.homepage, domain=None, range=Optional[str])

slots.id = Slot(uri=DCATAP_PLUS.id, name="id", curie=DCATAP_PLUS.curie('id'),
                   model_uri=DCAT_4C_AP.id, domain=None, range=URIRef)

slots.identifier = Slot(uri=DCTERMS.identifier, name="identifier", curie=DCTERMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.identifier, domain=None, range=Optional[str])

slots.in_series = Slot(uri=DCAT.inSeries, name="in_series", curie=DCAT.curie('inSeries'),
                   model_uri=DCAT_4C_AP.in_series, domain=None, range=Optional[str])

slots.is_about_activity = Slot(uri=DCTERMS.subject, name="is_about_activity", curie=DCTERMS.curie('subject'),
                   model_uri=DCAT_4C_AP.is_about_activity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, EvaluatedActivity]], list[Union[dict, EvaluatedActivity]]]])

slots.is_about_entity = Slot(uri=DCTERMS.subject, name="is_about_entity", curie=DCTERMS.curie('subject'),
                   model_uri=DCAT_4C_AP.is_about_entity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, EvaluatedEntity]], list[Union[dict, EvaluatedEntity]]]])

slots.is_referenced_by = Slot(uri=DCTERMS.isReferencedBy, name="is_referenced_by", curie=DCTERMS.curie('isReferencedBy'),
                   model_uri=DCAT_4C_AP.is_referenced_by, domain=None, range=Optional[str])

slots.keyword = Slot(uri=DCAT.keyword, name="keyword", curie=DCAT.curie('keyword'),
                   model_uri=DCAT_4C_AP.keyword, domain=None, range=Optional[str])

slots.landing_page = Slot(uri=DCAT.landingPage, name="landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=DCAT_4C_AP.landing_page, domain=None, range=Optional[str])

slots.language = Slot(uri=DCTERMS.language, name="language", curie=DCTERMS.curie('language'),
                   model_uri=DCAT_4C_AP.language, domain=None, range=Optional[str])

slots.licence = Slot(uri=DCTERMS.license, name="licence", curie=DCTERMS.curie('license'),
                   model_uri=DCAT_4C_AP.licence, domain=None, range=Optional[str])

slots.linked_schemas = Slot(uri=DCTERMS.conformsTo, name="linked_schemas", curie=DCTERMS.curie('conformsTo'),
                   model_uri=DCAT_4C_AP.linked_schemas, domain=None, range=Optional[str])

slots.listing_date = Slot(uri=DCTERMS.issued, name="listing_date", curie=DCTERMS.curie('issued'),
                   model_uri=DCAT_4C_AP.listing_date, domain=None, range=Optional[str])

slots.media_type = Slot(uri=DCAT.mediaType, name="media_type", curie=DCAT.curie('mediaType'),
                   model_uri=DCAT_4C_AP.media_type, domain=None, range=Optional[str])

slots.modification_date = Slot(uri=DCTERMS.modified, name="modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=DCAT_4C_AP.modification_date, domain=None, range=Optional[str])

slots.name = Slot(uri=FOAF.name, name="name", curie=FOAF.curie('name'),
                   model_uri=DCAT_4C_AP.name, domain=None, range=Optional[str])

slots.notation = Slot(uri=SKOS.notation, name="notation", curie=SKOS.curie('notation'),
                   model_uri=DCAT_4C_AP.notation, domain=None, range=Optional[str])

slots.occurred_in = Slot(uri=PROV.atLocation, name="occurred_in", curie=PROV.curie('atLocation'),
                   model_uri=DCAT_4C_AP.occurred_in, domain=None, range=Optional[Union[dict, Surrounding]])

slots.other_identifier = Slot(uri=ADMS.identifier, name="other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.other_identifier, domain=None, range=Optional[str])

slots.packaging_format = Slot(uri=DCAT.packageFormat, name="packaging_format", curie=DCAT.curie('packageFormat'),
                   model_uri=DCAT_4C_AP.packaging_format, domain=None, range=Optional[str])

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=DCAT_4C_AP.part_of, domain=None, range=Optional[Union[str, ActivityId]])

slots.preferred_label = Slot(uri=SKOS.prefLabel, name="preferred_label", curie=SKOS.curie('prefLabel'),
                   model_uri=DCAT_4C_AP.preferred_label, domain=None, range=Optional[str])

slots.primary_topic = Slot(uri=FOAF.primaryTopic, name="primary_topic", curie=FOAF.curie('primaryTopic'),
                   model_uri=DCAT_4C_AP.primary_topic, domain=None, range=Optional[str])

slots.provenance = Slot(uri=DCTERMS.provenance, name="provenance", curie=DCTERMS.curie('provenance'),
                   model_uri=DCAT_4C_AP.provenance, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DCTERMS.publisher, name="publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=DCAT_4C_AP.publisher, domain=None, range=Optional[str])

slots.qualified_attribution = Slot(uri=PROV.qualifiedAttribution, name="qualified_attribution", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=DCAT_4C_AP.qualified_attribution, domain=None, range=Optional[str])

slots.qualified_relation = Slot(uri=DCAT.qualifiedRelation, name="qualified_relation", curie=DCAT.curie('qualifiedRelation'),
                   model_uri=DCAT_4C_AP.qualified_relation, domain=None, range=Optional[str])

slots.rdf_type = Slot(uri=RDF.type, name="rdf_type", curie=RDF.curie('type'),
                   model_uri=DCAT_4C_AP.rdf_type, domain=None, range=Optional[Union[dict, DefinedTerm]])

slots.realized_plan = Slot(uri=PROV.used, name="realized_plan", curie=PROV.curie('used'),
                   model_uri=DCAT_4C_AP.realized_plan, domain=None, range=Optional[Union[dict, Plan]])

slots.record = Slot(uri=DCAT.record, name="record", curie=DCAT.curie('record'),
                   model_uri=DCAT_4C_AP.record, domain=None, range=Optional[str])

slots.related_resource = Slot(uri=DCTERMS.relation, name="related_resource", curie=DCTERMS.curie('relation'),
                   model_uri=DCAT_4C_AP.related_resource, domain=None, range=Optional[str])

slots.relation = Slot(uri=DCTERMS.relation, name="relation", curie=DCTERMS.curie('relation'),
                   model_uri=DCAT_4C_AP.relation, domain=None, range=Optional[str])

slots.release_date = Slot(uri=DCTERMS.issued, name="release_date", curie=DCTERMS.curie('issued'),
                   model_uri=DCAT_4C_AP.release_date, domain=None, range=Optional[str])

slots.rights = Slot(uri=DCTERMS.rights, name="rights", curie=DCTERMS.curie('rights'),
                   model_uri=DCAT_4C_AP.rights, domain=None, range=Optional[str])

slots.sample = Slot(uri=ADMS.sample, name="sample", curie=ADMS.curie('sample'),
                   model_uri=DCAT_4C_AP.sample, domain=None, range=Optional[str])

slots.serves_dataset = Slot(uri=DCAT.servesDataset, name="serves_dataset", curie=DCAT.curie('servesDataset'),
                   model_uri=DCAT_4C_AP.serves_dataset, domain=None, range=Optional[str])

slots.service = Slot(uri=DCAT.service, name="service", curie=DCAT.curie('service'),
                   model_uri=DCAT_4C_AP.service, domain=None, range=Optional[str])

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=DCAT_4C_AP.source, domain=None, range=Optional[str])

slots.source_metadata = Slot(uri=DCTERMS.source, name="source_metadata", curie=DCTERMS.curie('source'),
                   model_uri=DCAT_4C_AP.source_metadata, domain=None, range=Optional[str])

slots.spatial_resolution = Slot(uri=DCAT.spatialResolutionInMeters, name="spatial_resolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=DCAT_4C_AP.spatial_resolution, domain=None, range=Optional[str])

slots.start_date = Slot(uri=DCAT.startDate, name="start_date", curie=DCAT.curie('startDate'),
                   model_uri=DCAT_4C_AP.start_date, domain=None, range=Optional[str])

slots.status = Slot(uri=ADMS.status, name="status", curie=ADMS.curie('status'),
                   model_uri=DCAT_4C_AP.status, domain=None, range=Optional[str])

slots.temporal_coverage = Slot(uri=DCTERMS.temporal, name="temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=DCAT_4C_AP.temporal_coverage, domain=None, range=Optional[str])

slots.temporal_resolution = Slot(uri=DCAT.temporalResolution, name="temporal_resolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=DCAT_4C_AP.temporal_resolution, domain=None, range=Optional[str])

slots.theme = Slot(uri=DCAT.theme, name="theme", curie=DCAT.curie('theme'),
                   model_uri=DCAT_4C_AP.theme, domain=None, range=Optional[str])

slots.themes = Slot(uri=DCAT.themeTaxonomy, name="themes", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=DCAT_4C_AP.themes, domain=None, range=Optional[str])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.title, domain=None, range=Optional[str])

slots.type = Slot(uri=DCTERMS.type, name="type", curie=DCTERMS.curie('type'),
                   model_uri=DCAT_4C_AP.type, domain=None, range=Optional[str])

slots.value = Slot(uri=PROV.value, name="value", curie=PROV.curie('value'),
                   model_uri=DCAT_4C_AP.value, domain=None, range=Optional[str])

slots.version = Slot(uri=DCAT.version, name="version", curie=DCAT.curie('version'),
                   model_uri=DCAT_4C_AP.version, domain=None, range=Optional[str])

slots.version_notes = Slot(uri=ADMS.versionNotes, name="version_notes", curie=ADMS.curie('versionNotes'),
                   model_uri=DCAT_4C_AP.version_notes, domain=None, range=Optional[str])

slots.was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=DCAT_4C_AP.was_generated_by, domain=None, range=Optional[str])

slots.composed_of = Slot(uri=BFO['0000051'], name="composed_of", curie=BFO.curie('0000051'),
                   model_uri=DCAT_4C_AP.composed_of, domain=None, range=Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]])

slots.has_concentration = Slot(uri=SIO['000008'], name="has_concentration", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_concentration, domain=None, range=Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]])

slots.has_amount = Slot(uri=SIO['000008'], name="has_amount", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_amount, domain=None, range=Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]])

slots.has_ph_value = Slot(uri=SIO['000008'], name="has_ph_value", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_ph_value, domain=None, range=Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]])

slots.inchi = Slot(uri=SIO['000008'], name="inchi", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.inchi, domain=None, range=Optional[Union[Union[dict, InChi], list[Union[dict, InChi]]]])

slots.inchikey = Slot(uri=SIO['000008'], name="inchikey", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.inchikey, domain=None, range=Optional[Union[Union[dict, InChIKey], list[Union[dict, InChIKey]]]])

slots.smiles = Slot(uri=SIO['000008'], name="smiles", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.smiles, domain=None, range=Optional[Union[Union[dict, SMILES], list[Union[dict, SMILES]]]])

slots.molecular_formula = Slot(uri=SIO['000008'], name="molecular_formula", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.molecular_formula, domain=None, range=Optional[Union[Union[dict, MolecularFormula], list[Union[dict, MolecularFormula]]]])

slots.iupac_name = Slot(uri=SIO['000008'], name="iupac_name", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.iupac_name, domain=None, range=Optional[Union[Union[dict, IUPACName], list[Union[dict, IUPACName]]]])

slots.has_molar_mass = Slot(uri=SIO['000008'], name="has_molar_mass", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_molar_mass, domain=None, range=Optional[Union[Union[dict, MolarMass], list[Union[dict, MolarMass]]]])

slots.used_starting_material = Slot(uri=RO['0004009'], name="used_starting_material", curie=RO.curie('0004009'),
                   model_uri=DCAT_4C_AP.used_starting_material, domain=None, range=Optional[Union[dict[Union[str, StartingMaterialId], Union[dict, StartingMaterial]], list[Union[dict, StartingMaterial]]]])

slots.used_reactant = Slot(uri=RO['0004009'], name="used_reactant", curie=RO.curie('0004009'),
                   model_uri=DCAT_4C_AP.used_reactant, domain=None, range=Optional[Union[dict[Union[str, ReagentId], Union[dict, Reagent]], list[Union[dict, Reagent]]]])

slots.generated_product = Slot(uri=RO['0004008'], name="generated_product", curie=RO.curie('0004008'),
                   model_uri=DCAT_4C_AP.generated_product, domain=None, range=Optional[Union[dict[Union[str, ChemicalProductId], Union[dict, ChemicalProduct]], list[Union[dict, ChemicalProduct]]]])

slots.used_catalyst = Slot(uri=RXNO['0000425'], name="used_catalyst", curie=RXNO.curie('0000425'),
                   model_uri=DCAT_4C_AP.used_catalyst, domain=None, range=Optional[Union[dict[Union[str, CatalystId], Union[dict, Catalyst]], list[Union[dict, Catalyst]]]])

slots.used_solvent = Slot(uri=PROV.wasAssociatedWith, name="used_solvent", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=DCAT_4C_AP.used_solvent, domain=None, range=Optional[Union[dict[Union[str, DissolvingSubstanceId], Union[dict, DissolvingSubstance]], list[Union[dict, DissolvingSubstance]]]])

slots.has_duration = Slot(uri=SCHEMA.duration, name="has_duration", curie=SCHEMA.curie('duration'),
                   model_uri=DCAT_4C_AP.has_duration, domain=None, range=Optional[str])

slots.used_reactor = Slot(uri=PROV.wasAssociatedWith, name="used_reactor", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=DCAT_4C_AP.used_reactor, domain=None, range=Optional[Union[dict[Union[str, ReactorId], Union[dict, Reactor]], list[Union[dict, Reactor]]]])

slots.has_yield = Slot(uri=SIO['000008'], name="has_yield", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_yield, domain=None, range=Optional[Union[Union[dict, Yield], list[Union[dict, Yield]]]])

slots.has_molar_equivalent = Slot(uri=SIO['000008'], name="has_molar_equivalent", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_molar_equivalent, domain=None, range=Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]])

slots.has_percentage_of_total = Slot(uri=SIO['000008'], name="has_percentage_of_total", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_percentage_of_total, domain=None, range=Optional[Union[Union[dict, PercentageOfTotal], list[Union[dict, PercentageOfTotal]]]])

slots.has_reaction_step = Slot(uri=BFO['0000051'], name="has_reaction_step", curie=BFO.curie('0000051'),
                   model_uri=DCAT_4C_AP.has_reaction_step, domain=None, range=Optional[Union[str, ChemicalReactionId]])

slots.used_spectrometer = Slot(uri=OBI['0000293'], name="used_spectrometer", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.used_spectrometer, domain=None, range=Union[dict[Union[str, NMRSpectrometerId], Union[dict, NMRSpectrometer]], list[Union[dict, NMRSpectrometer]]])

slots.has_proton_frequency = Slot(uri=SIO['000008'], name="has_proton_frequency", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_proton_frequency, domain=None, range=Optional[Union[Union[dict, NominalProtonFrequency], list[Union[dict, NominalProtonFrequency]]]])

slots.alternative_label = Slot(uri=SKOS.altLabel, name="alternative_label", curie=SKOS.curie('altLabel'),
                   model_uri=DCAT_4C_AP.alternative_label, domain=None, range=Optional[str])

slots.has_physical_state = Slot(uri=SIO['000008'], name="has_physical_state", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_physical_state, domain=None, range=Optional[Union[str, "PhysicalStateEnum"]])

slots.has_temperature = Slot(uri=SIO['000008'], name="has_temperature", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_temperature, domain=None, range=Optional[Union[Union[dict, Temperature], list[Union[dict, Temperature]]]])

slots.has_mass = Slot(uri=SIO['000008'], name="has_mass", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_mass, domain=None, range=Optional[Union[Union[dict, Mass], list[Union[dict, Mass]]]])

slots.has_volume = Slot(uri=SIO['000008'], name="has_volume", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_volume, domain=None, range=Optional[Union[Union[dict, Volume], list[Union[dict, Volume]]]])

slots.has_density = Slot(uri=SIO['000008'], name="has_density", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_density, domain=None, range=Optional[Union[Union[dict, Density], list[Union[dict, Density]]]])

slots.has_pressure = Slot(uri=SIO['000008'], name="has_pressure", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.has_pressure, domain=None, range=Optional[Union[Union[dict, Pressure], list[Union[dict, Pressure]]]])

slots.derived_from = Slot(uri=PROV.wasDerivedFrom, name="derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=DCAT_4C_AP.derived_from, domain=None, range=Optional[Union[dict, Entity]])

slots.definedTerm__from_CV = Slot(uri=SCHEMA.inDefinedTermSet, name="definedTerm__from_CV", curie=SCHEMA.curie('inDefinedTermSet'),
                   model_uri=DCAT_4C_AP.definedTerm__from_CV, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.quantitativeAttribute__has_quantity_type = Slot(uri=QUDT.hasQuantityKind, name="quantitativeAttribute__has_quantity_type", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=DCAT_4C_AP.quantitativeAttribute__has_quantity_type, domain=None, range=Union[str, DefinedTermId])

slots.quantitativeAttribute__unit = Slot(uri=QUDT.unit, name="quantitativeAttribute__unit", curie=QUDT.curie('unit'),
                   model_uri=DCAT_4C_AP.quantitativeAttribute__unit, domain=None, range=Optional[Union[str, DefinedTermId]])

slots.nMRSpectroscopy__used_pulse_sequence = Slot(uri=OBI['0000293'], name="nMRSpectroscopy__used_pulse_sequence", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.nMRSpectroscopy__used_pulse_sequence, domain=None, range=Union[dict, PulseSequence])

slots.nMRSpectroscopy__used_number_of_scans = Slot(uri=OBI['0000293'], name="nMRSpectroscopy__used_number_of_scans", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.nMRSpectroscopy__used_number_of_scans, domain=None, range=Optional[Union[dict, NumberOfScans]])

slots.nMRSpectroscopy__used_sample_temperature = Slot(uri=OBI['0000293'], name="nMRSpectroscopy__used_sample_temperature", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.nMRSpectroscopy__used_sample_temperature, domain=None, range=Optional[Union[dict, NMRSampleTemperature]])

slots.nMRSpectroscopy__probes_nucleus = Slot(uri=OBI['0000293'], name="nMRSpectroscopy__probes_nucleus", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.nMRSpectroscopy__probes_nucleus, domain=None, range=Union[dict[Union[str, AcquisitionNucleusId], Union[dict, AcquisitionNucleus]], list[Union[dict, AcquisitionNucleus]]])

slots.nMRSpectroscopy__used_calibration_compound = Slot(uri=OBI['0000293'], name="nMRSpectroscopy__used_calibration_compound", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.nMRSpectroscopy__used_calibration_compound, domain=None, range=Optional[Union[dict[Union[str, ShiftCalibrationCompoundId], Union[dict, ShiftCalibrationCompound]], list[Union[dict, ShiftCalibrationCompound]]]])

slots.nMRSpectroscopy__used_reference_compound = Slot(uri=OBI['0000293'], name="nMRSpectroscopy__used_reference_compound", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.nMRSpectroscopy__used_reference_compound, domain=None, range=Optional[Union[dict[Union[str, ShiftReferenceCompoundId], Union[dict, ShiftReferenceCompound]], list[Union[dict, ShiftReferenceCompound]]]])

slots.shiftCalibrationCompound__has_calibration_shift = Slot(uri=SIO['000008'], name="shiftCalibrationCompound__has_calibration_shift", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.shiftCalibrationCompound__has_calibration_shift, domain=None, range=Optional[Union[Union[dict, CalibrationPeakShift], list[Union[dict, CalibrationPeakShift]]]])

slots.acquisitionNucleus__nucleus_of = Slot(uri=BFO['0000050'], name="acquisitionNucleus__nucleus_of", curie=BFO.curie('0000050'),
                   model_uri=DCAT_4C_AP.acquisitionNucleus__nucleus_of, domain=None, range=Union[dict, Atom])

slots.Activity_title = Slot(uri=DCTERMS.title, name="Activity_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.Activity_title, domain=Activity, range=Optional[Union[str, list[str]]])

slots.Activity_description = Slot(uri=DCTERMS.description, name="Activity_description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.Activity_description, domain=Activity, range=Optional[Union[str, list[str]]])

slots.Activity_has_part = Slot(uri=DCTERMS.hasPart, name="Activity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=DCAT_4C_AP.Activity_has_part, domain=Activity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]])

slots.Activity_part_of = Slot(uri=DCTERMS.isPartOf, name="Activity_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=DCAT_4C_AP.Activity_part_of, domain=Activity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]])

slots.Activity_other_identifier = Slot(uri=ADMS.identifier, name="Activity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.Activity_other_identifier, domain=Activity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Activity_has_qualitative_attribute = Slot(uri=DCTERMS.relation, name="Activity_has_qualitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=DCAT_4C_AP.Activity_has_qualitative_attribute, domain=Activity, range=Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]])

slots.Activity_has_quantitative_attribute = Slot(uri=DCTERMS.relation, name="Activity_has_quantitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=DCAT_4C_AP.Activity_has_quantitative_attribute, domain=Activity, range=Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]])

slots.Activity_had_input_entity = Slot(uri=PROV.used, name="Activity_had_input_entity", curie=PROV.curie('used'),
                   model_uri=DCAT_4C_AP.Activity_had_input_entity, domain=Activity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.Activity_had_output_entity = Slot(uri=PROV.generated, name="Activity_had_output_entity", curie=PROV.curie('generated'),
                   model_uri=DCAT_4C_AP.Activity_had_output_entity, domain=Activity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.Activity_had_input_activity = Slot(uri=PROV.wasInformedBy, name="Activity_had_input_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=DCAT_4C_AP.Activity_had_input_activity, domain=Activity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]])

slots.Activity_carried_out_by = Slot(uri=PROV.wasAssociatedWith, name="Activity_carried_out_by", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=DCAT_4C_AP.Activity_carried_out_by, domain=Activity, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]])

slots.Agent_name = Slot(uri=FOAF.name, name="Agent_name", curie=FOAF.curie('name'),
                   model_uri=DCAT_4C_AP.Agent_name, domain=Agent, range=Union[str, list[str]])

slots.Agent_type = Slot(uri=DCTERMS.type, name="Agent_type", curie=DCTERMS.curie('type'),
                   model_uri=DCAT_4C_AP.Agent_type, domain=Agent, range=Optional[Union[dict, "Concept"]])

slots.AgenticEntity_has_part = Slot(uri=DCTERMS.hasPart, name="AgenticEntity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=DCAT_4C_AP.AgenticEntity_has_part, domain=AgenticEntity, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]])

slots.AgenticEntity_part_of = Slot(uri=DCTERMS.isPartOf, name="AgenticEntity_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=DCAT_4C_AP.AgenticEntity_part_of, domain=AgenticEntity, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]])

slots.AgenticEntity_other_identifier = Slot(uri=ADMS.identifier, name="AgenticEntity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.AgenticEntity_other_identifier, domain=AgenticEntity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.AnalysisDataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="AnalysisDataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=DCAT_4C_AP.AnalysisDataset_was_generated_by, domain=AnalysisDataset, range=Optional[Union[dict[Union[str, DataAnalysisId], Union[dict, DataAnalysis]], list[Union[dict, DataAnalysis]]]])

slots.AnalysisSourceData_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="AnalysisSourceData_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=DCAT_4C_AP.AnalysisSourceData_was_generated_by, domain=AnalysisSourceData, range=Optional[Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]]])

slots.Catalogue_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="Catalogue_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=DCAT_4C_AP.Catalogue_applicable_legislation, domain=Catalogue, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.Catalogue_catalogue = Slot(uri=DCAT.catalog, name="Catalogue_catalogue", curie=DCAT.curie('catalog'),
                   model_uri=DCAT_4C_AP.Catalogue_catalogue, domain=Catalogue, range=Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]])

slots.Catalogue_creator = Slot(uri=DCTERMS.creator, name="Catalogue_creator", curie=DCTERMS.curie('creator'),
                   model_uri=DCAT_4C_AP.Catalogue_creator, domain=Catalogue, range=Optional[Union[dict, Agent]])

slots.Catalogue_description = Slot(uri=DCTERMS.description, name="Catalogue_description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.Catalogue_description, domain=Catalogue, range=Union[str, list[str]])

slots.Catalogue_geographical_coverage = Slot(uri=DCTERMS.spatial, name="Catalogue_geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=DCAT_4C_AP.Catalogue_geographical_coverage, domain=Catalogue, range=Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]])

slots.Catalogue_has_dataset = Slot(uri=DCAT.dataset, name="Catalogue_has_dataset", curie=DCAT.curie('dataset'),
                   model_uri=DCAT_4C_AP.Catalogue_has_dataset, domain=Catalogue, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.Catalogue_has_part = Slot(uri=DCTERMS.hasPart, name="Catalogue_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=DCAT_4C_AP.Catalogue_has_part, domain=Catalogue, range=Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]])

slots.Catalogue_homepage = Slot(uri=FOAF.homepage, name="Catalogue_homepage", curie=FOAF.curie('homepage'),
                   model_uri=DCAT_4C_AP.Catalogue_homepage, domain=Catalogue, range=Optional[Union[dict, "Document"]])

slots.Catalogue_language = Slot(uri=DCTERMS.language, name="Catalogue_language", curie=DCTERMS.curie('language'),
                   model_uri=DCAT_4C_AP.Catalogue_language, domain=Catalogue, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.Catalogue_licence = Slot(uri=DCTERMS.license, name="Catalogue_licence", curie=DCTERMS.curie('license'),
                   model_uri=DCAT_4C_AP.Catalogue_licence, domain=Catalogue, range=Optional[Union[dict, "LicenseDocument"]])

slots.Catalogue_modification_date = Slot(uri=DCTERMS.modified, name="Catalogue_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=DCAT_4C_AP.Catalogue_modification_date, domain=Catalogue, range=Optional[Union[str, XSDDate]])

slots.Catalogue_publisher = Slot(uri=DCTERMS.publisher, name="Catalogue_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=DCAT_4C_AP.Catalogue_publisher, domain=Catalogue, range=Union[dict, Agent])

slots.Catalogue_record = Slot(uri=DCAT.record, name="Catalogue_record", curie=DCAT.curie('record'),
                   model_uri=DCAT_4C_AP.Catalogue_record, domain=Catalogue, range=Optional[Union[Union[dict, "CatalogueRecord"], list[Union[dict, "CatalogueRecord"]]]])

slots.Catalogue_release_date = Slot(uri=DCTERMS.issued, name="Catalogue_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=DCAT_4C_AP.Catalogue_release_date, domain=Catalogue, range=Optional[Union[str, XSDDate]])

slots.Catalogue_rights = Slot(uri=DCTERMS.rights, name="Catalogue_rights", curie=DCTERMS.curie('rights'),
                   model_uri=DCAT_4C_AP.Catalogue_rights, domain=Catalogue, range=Optional[Union[dict, "RightsStatement"]])

slots.Catalogue_service = Slot(uri=DCAT.service, name="Catalogue_service", curie=DCAT.curie('service'),
                   model_uri=DCAT_4C_AP.Catalogue_service, domain=Catalogue, range=Optional[Union[Union[dict, "DataService"], list[Union[dict, "DataService"]]]])

slots.Catalogue_temporal_coverage = Slot(uri=DCTERMS.temporal, name="Catalogue_temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=DCAT_4C_AP.Catalogue_temporal_coverage, domain=Catalogue, range=Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]])

slots.Catalogue_themes = Slot(uri=DCAT.themeTaxonomy, name="Catalogue_themes", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=DCAT_4C_AP.Catalogue_themes, domain=Catalogue, range=Optional[Union[Union[dict, "ConceptScheme"], list[Union[dict, "ConceptScheme"]]]])

slots.Catalogue_title = Slot(uri=DCTERMS.title, name="Catalogue_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.Catalogue_title, domain=Catalogue, range=Union[str, list[str]])

slots.CatalogueRecord_application_profile = Slot(uri=DCTERMS.conformsTo, name="CatalogueRecord_application_profile", curie=DCTERMS.curie('conformsTo'),
                   model_uri=DCAT_4C_AP.CatalogueRecord_application_profile, domain=CatalogueRecord, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.CatalogueRecord_change_type = Slot(uri=ADMS.status, name="CatalogueRecord_change_type", curie=ADMS.curie('status'),
                   model_uri=DCAT_4C_AP.CatalogueRecord_change_type, domain=CatalogueRecord, range=Optional[Union[dict, "Concept"]])

slots.CatalogueRecord_description = Slot(uri=DCTERMS.description, name="CatalogueRecord_description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.CatalogueRecord_description, domain=CatalogueRecord, range=Optional[Union[str, list[str]]])

slots.CatalogueRecord_language = Slot(uri=DCTERMS.language, name="CatalogueRecord_language", curie=DCTERMS.curie('language'),
                   model_uri=DCAT_4C_AP.CatalogueRecord_language, domain=CatalogueRecord, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.CatalogueRecord_listing_date = Slot(uri=DCTERMS.issued, name="CatalogueRecord_listing_date", curie=DCTERMS.curie('issued'),
                   model_uri=DCAT_4C_AP.CatalogueRecord_listing_date, domain=CatalogueRecord, range=Optional[Union[str, XSDDate]])

slots.CatalogueRecord_modification_date = Slot(uri=DCTERMS.modified, name="CatalogueRecord_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=DCAT_4C_AP.CatalogueRecord_modification_date, domain=CatalogueRecord, range=Union[str, XSDDate])

slots.CatalogueRecord_primary_topic = Slot(uri=FOAF.primaryTopic, name="CatalogueRecord_primary_topic", curie=FOAF.curie('primaryTopic'),
                   model_uri=DCAT_4C_AP.CatalogueRecord_primary_topic, domain=CatalogueRecord, range=Union[dict, Any])

slots.CatalogueRecord_source_metadata = Slot(uri=DCTERMS.source, name="CatalogueRecord_source_metadata", curie=DCTERMS.curie('source'),
                   model_uri=DCAT_4C_AP.CatalogueRecord_source_metadata, domain=CatalogueRecord, range=Optional[Union[dict, "CatalogueRecord"]])

slots.CatalogueRecord_title = Slot(uri=DCTERMS.title, name="CatalogueRecord_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.CatalogueRecord_title, domain=CatalogueRecord, range=Optional[Union[str, list[str]]])

slots.Checksum_algorithm = Slot(uri=SPDX.algorithm, name="Checksum_algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=DCAT_4C_AP.Checksum_algorithm, domain=Checksum, range=Union[dict, "ChecksumAlgorithm"])

slots.Checksum_checksum_value = Slot(uri=SPDX.checksumValue, name="Checksum_checksum_value", curie=SPDX.curie('checksumValue'),
                   model_uri=DCAT_4C_AP.Checksum_checksum_value, domain=Checksum, range=str)

slots.ClassifierMixin_type = Slot(uri=DCTERMS.type, name="ClassifierMixin_type", curie=DCTERMS.curie('type'),
                   model_uri=DCAT_4C_AP.ClassifierMixin_type, domain=None, range=Optional[Union[dict, "DefinedTerm"]])

slots.Concept_preferred_label = Slot(uri=SKOS.prefLabel, name="Concept_preferred_label", curie=SKOS.curie('prefLabel'),
                   model_uri=DCAT_4C_AP.Concept_preferred_label, domain=Concept, range=Union[str, list[str]])

slots.ConceptScheme_title = Slot(uri=DCTERMS.title, name="ConceptScheme_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.ConceptScheme_title, domain=ConceptScheme, range=Union[str, list[str]])

slots.DataAnalysis_evaluated_entity = Slot(uri=PROV.used, name="DataAnalysis_evaluated_entity", curie=PROV.curie('used'),
                   model_uri=DCAT_4C_AP.DataAnalysis_evaluated_entity, domain=DataAnalysis, range=Optional[Union[dict[Union[str, AnalysisSourceDataId], Union[dict, "AnalysisSourceData"]], list[Union[dict, "AnalysisSourceData"]]]])

slots.DataService_access_rights = Slot(uri=DCTERMS.accessRights, name="DataService_access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=DCAT_4C_AP.DataService_access_rights, domain=DataService, range=Optional[Union[dict, "RightsStatement"]])

slots.DataService_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="DataService_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=DCAT_4C_AP.DataService_applicable_legislation, domain=DataService, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.DataService_conforms_to = Slot(uri=DCTERMS.conformsTo, name="DataService_conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=DCAT_4C_AP.DataService_conforms_to, domain=DataService, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.DataService_contact_point = Slot(uri=DCAT.contactPoint, name="DataService_contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=DCAT_4C_AP.DataService_contact_point, domain=DataService, range=Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]])

slots.DataService_description = Slot(uri=DCTERMS.description, name="DataService_description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.DataService_description, domain=DataService, range=Optional[Union[str, list[str]]])

slots.DataService_documentation = Slot(uri=FOAF.page, name="DataService_documentation", curie=FOAF.curie('page'),
                   model_uri=DCAT_4C_AP.DataService_documentation, domain=DataService, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.DataService_endpoint_URL = Slot(uri=DCAT.endpointURL, name="DataService_endpoint_URL", curie=DCAT.curie('endpointURL'),
                   model_uri=DCAT_4C_AP.DataService_endpoint_URL, domain=DataService, range=Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]])

slots.DataService_endpoint_description = Slot(uri=DCAT.endpointDescription, name="DataService_endpoint_description", curie=DCAT.curie('endpointDescription'),
                   model_uri=DCAT_4C_AP.DataService_endpoint_description, domain=DataService, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.DataService_format = Slot(uri=DCTERMS.format, name="DataService_format", curie=DCTERMS.curie('format'),
                   model_uri=DCAT_4C_AP.DataService_format, domain=DataService, range=Optional[Union[Union[dict, "MediaTypeOrExtent"], list[Union[dict, "MediaTypeOrExtent"]]]])

slots.DataService_keyword = Slot(uri=DCAT.keyword, name="DataService_keyword", curie=DCAT.curie('keyword'),
                   model_uri=DCAT_4C_AP.DataService_keyword, domain=DataService, range=Optional[Union[str, list[str]]])

slots.DataService_landing_page = Slot(uri=DCAT.landingPage, name="DataService_landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=DCAT_4C_AP.DataService_landing_page, domain=DataService, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.DataService_licence = Slot(uri=DCTERMS.license, name="DataService_licence", curie=DCTERMS.curie('license'),
                   model_uri=DCAT_4C_AP.DataService_licence, domain=DataService, range=Optional[Union[dict, "LicenseDocument"]])

slots.DataService_publisher = Slot(uri=DCTERMS.publisher, name="DataService_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=DCAT_4C_AP.DataService_publisher, domain=DataService, range=Optional[Union[dict, Agent]])

slots.DataService_serves_dataset = Slot(uri=DCAT.servesDataset, name="DataService_serves_dataset", curie=DCAT.curie('servesDataset'),
                   model_uri=DCAT_4C_AP.DataService_serves_dataset, domain=DataService, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.DataService_theme = Slot(uri=DCAT.theme, name="DataService_theme", curie=DCAT.curie('theme'),
                   model_uri=DCAT_4C_AP.DataService_theme, domain=DataService, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.DataService_title = Slot(uri=DCTERMS.title, name="DataService_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.DataService_title, domain=DataService, range=Union[str, list[str]])

slots.Dataset_access_rights = Slot(uri=DCTERMS.accessRights, name="Dataset_access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=DCAT_4C_AP.Dataset_access_rights, domain=Dataset, range=Optional[Union[dict, "RightsStatement"]])

slots.Dataset_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="Dataset_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=DCAT_4C_AP.Dataset_applicable_legislation, domain=Dataset, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.Dataset_conforms_to = Slot(uri=DCTERMS.conformsTo, name="Dataset_conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=DCAT_4C_AP.Dataset_conforms_to, domain=Dataset, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.Dataset_contact_point = Slot(uri=DCAT.contactPoint, name="Dataset_contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=DCAT_4C_AP.Dataset_contact_point, domain=Dataset, range=Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]])

slots.Dataset_creator = Slot(uri=DCTERMS.creator, name="Dataset_creator", curie=DCTERMS.curie('creator'),
                   model_uri=DCAT_4C_AP.Dataset_creator, domain=Dataset, range=Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]])

slots.Dataset_dataset_distribution = Slot(uri=DCAT.distribution, name="Dataset_dataset_distribution", curie=DCAT.curie('distribution'),
                   model_uri=DCAT_4C_AP.Dataset_dataset_distribution, domain=Dataset, range=Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]])

slots.Dataset_description = Slot(uri=DCTERMS.description, name="Dataset_description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.Dataset_description, domain=Dataset, range=Union[str, list[str]])

slots.Dataset_documentation = Slot(uri=FOAF.page, name="Dataset_documentation", curie=FOAF.curie('page'),
                   model_uri=DCAT_4C_AP.Dataset_documentation, domain=Dataset, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.Dataset_frequency = Slot(uri=DCTERMS.accrualPeriodicity, name="Dataset_frequency", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=DCAT_4C_AP.Dataset_frequency, domain=Dataset, range=Optional[Union[dict, "Frequency"]])

slots.Dataset_geographical_coverage = Slot(uri=DCTERMS.spatial, name="Dataset_geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=DCAT_4C_AP.Dataset_geographical_coverage, domain=Dataset, range=Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]])

slots.Dataset_has_version = Slot(uri=DCAT.hasVersion, name="Dataset_has_version", curie=DCAT.curie('hasVersion'),
                   model_uri=DCAT_4C_AP.Dataset_has_version, domain=Dataset, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.Dataset_identifier = Slot(uri=DCTERMS.identifier, name="Dataset_identifier", curie=DCTERMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.Dataset_identifier, domain=Dataset, range=Optional[Union[str, list[str]]])

slots.Dataset_in_series = Slot(uri=DCAT.inSeries, name="Dataset_in_series", curie=DCAT.curie('inSeries'),
                   model_uri=DCAT_4C_AP.Dataset_in_series, domain=Dataset, range=Optional[Union[Union[dict, "DatasetSeries"], list[Union[dict, "DatasetSeries"]]]])

slots.Dataset_is_referenced_by = Slot(uri=DCTERMS.isReferencedBy, name="Dataset_is_referenced_by", curie=DCTERMS.curie('isReferencedBy'),
                   model_uri=DCAT_4C_AP.Dataset_is_referenced_by, domain=Dataset, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.Dataset_keyword = Slot(uri=DCAT.keyword, name="Dataset_keyword", curie=DCAT.curie('keyword'),
                   model_uri=DCAT_4C_AP.Dataset_keyword, domain=Dataset, range=Optional[Union[str, list[str]]])

slots.Dataset_landing_page = Slot(uri=DCAT.landingPage, name="Dataset_landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=DCAT_4C_AP.Dataset_landing_page, domain=Dataset, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.Dataset_language = Slot(uri=DCTERMS.language, name="Dataset_language", curie=DCTERMS.curie('language'),
                   model_uri=DCAT_4C_AP.Dataset_language, domain=Dataset, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.Dataset_modification_date = Slot(uri=DCTERMS.modified, name="Dataset_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=DCAT_4C_AP.Dataset_modification_date, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.Dataset_other_identifier = Slot(uri=ADMS.identifier, name="Dataset_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.Dataset_other_identifier, domain=Dataset, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Dataset_provenance = Slot(uri=DCTERMS.provenance, name="Dataset_provenance", curie=DCTERMS.curie('provenance'),
                   model_uri=DCAT_4C_AP.Dataset_provenance, domain=Dataset, range=Optional[Union[Union[dict, "ProvenanceStatement"], list[Union[dict, "ProvenanceStatement"]]]])

slots.Dataset_publisher = Slot(uri=DCTERMS.publisher, name="Dataset_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=DCAT_4C_AP.Dataset_publisher, domain=Dataset, range=Optional[Union[dict, Agent]])

slots.Dataset_qualified_attribution = Slot(uri=PROV.qualifiedAttribution, name="Dataset_qualified_attribution", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=DCAT_4C_AP.Dataset_qualified_attribution, domain=Dataset, range=Optional[Union[Union[dict, "Attribution"], list[Union[dict, "Attribution"]]]])

slots.Dataset_qualified_relation = Slot(uri=DCAT.qualifiedRelation, name="Dataset_qualified_relation", curie=DCAT.curie('qualifiedRelation'),
                   model_uri=DCAT_4C_AP.Dataset_qualified_relation, domain=Dataset, range=Optional[Union[Union[dict, "Relationship"], list[Union[dict, "Relationship"]]]])

slots.Dataset_related_resource = Slot(uri=DCTERMS.relation, name="Dataset_related_resource", curie=DCTERMS.curie('relation'),
                   model_uri=DCAT_4C_AP.Dataset_related_resource, domain=Dataset, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.Dataset_release_date = Slot(uri=DCTERMS.issued, name="Dataset_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=DCAT_4C_AP.Dataset_release_date, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.Dataset_sample = Slot(uri=ADMS.sample, name="Dataset_sample", curie=ADMS.curie('sample'),
                   model_uri=DCAT_4C_AP.Dataset_sample, domain=Dataset, range=Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]])

slots.Dataset_source = Slot(uri=DCTERMS.source, name="Dataset_source", curie=DCTERMS.curie('source'),
                   model_uri=DCAT_4C_AP.Dataset_source, domain=Dataset, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.Dataset_spatial_resolution = Slot(uri=DCAT.spatialResolutionInMeters, name="Dataset_spatial_resolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=DCAT_4C_AP.Dataset_spatial_resolution, domain=Dataset, range=Optional[Decimal])

slots.Dataset_temporal_coverage = Slot(uri=DCTERMS.temporal, name="Dataset_temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=DCAT_4C_AP.Dataset_temporal_coverage, domain=Dataset, range=Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]])

slots.Dataset_temporal_resolution = Slot(uri=DCAT.temporalResolution, name="Dataset_temporal_resolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=DCAT_4C_AP.Dataset_temporal_resolution, domain=Dataset, range=Optional[str])

slots.Dataset_theme = Slot(uri=DCAT.theme, name="Dataset_theme", curie=DCAT.curie('theme'),
                   model_uri=DCAT_4C_AP.Dataset_theme, domain=Dataset, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.Dataset_title = Slot(uri=DCTERMS.title, name="Dataset_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.Dataset_title, domain=Dataset, range=Union[str, list[str]])

slots.Dataset_type = Slot(uri=DCTERMS.type, name="Dataset_type", curie=DCTERMS.curie('type'),
                   model_uri=DCAT_4C_AP.Dataset_type, domain=Dataset, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.Dataset_version = Slot(uri=DCAT.version, name="Dataset_version", curie=DCAT.curie('version'),
                   model_uri=DCAT_4C_AP.Dataset_version, domain=Dataset, range=Optional[str])

slots.Dataset_version_notes = Slot(uri=ADMS.versionNotes, name="Dataset_version_notes", curie=ADMS.curie('versionNotes'),
                   model_uri=DCAT_4C_AP.Dataset_version_notes, domain=Dataset, range=Optional[Union[str, list[str]]])

slots.Dataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="Dataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=DCAT_4C_AP.Dataset_was_generated_by, domain=Dataset, range=Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]])

slots.DatasetSeries_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="DatasetSeries_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=DCAT_4C_AP.DatasetSeries_applicable_legislation, domain=DatasetSeries, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.DatasetSeries_contact_point = Slot(uri=DCAT.contactPoint, name="DatasetSeries_contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=DCAT_4C_AP.DatasetSeries_contact_point, domain=DatasetSeries, range=Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]])

slots.DatasetSeries_description = Slot(uri=DCTERMS.description, name="DatasetSeries_description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.DatasetSeries_description, domain=DatasetSeries, range=Union[str, list[str]])

slots.DatasetSeries_frequency = Slot(uri=DCTERMS.accrualPeriodicity, name="DatasetSeries_frequency", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=DCAT_4C_AP.DatasetSeries_frequency, domain=DatasetSeries, range=Optional[Union[dict, "Frequency"]])

slots.DatasetSeries_geographical_coverage = Slot(uri=DCTERMS.spatial, name="DatasetSeries_geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=DCAT_4C_AP.DatasetSeries_geographical_coverage, domain=DatasetSeries, range=Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]])

slots.DatasetSeries_modification_date = Slot(uri=DCTERMS.modified, name="DatasetSeries_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=DCAT_4C_AP.DatasetSeries_modification_date, domain=DatasetSeries, range=Optional[Union[str, XSDDate]])

slots.DatasetSeries_publisher = Slot(uri=DCTERMS.publisher, name="DatasetSeries_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=DCAT_4C_AP.DatasetSeries_publisher, domain=DatasetSeries, range=Optional[Union[dict, Agent]])

slots.DatasetSeries_release_date = Slot(uri=DCTERMS.issued, name="DatasetSeries_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=DCAT_4C_AP.DatasetSeries_release_date, domain=DatasetSeries, range=Optional[Union[str, XSDDate]])

slots.DatasetSeries_temporal_coverage = Slot(uri=DCTERMS.temporal, name="DatasetSeries_temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=DCAT_4C_AP.DatasetSeries_temporal_coverage, domain=DatasetSeries, range=Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]])

slots.DatasetSeries_title = Slot(uri=DCTERMS.title, name="DatasetSeries_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.DatasetSeries_title, domain=DatasetSeries, range=Union[str, list[str]])

slots.DefinedTerm_title = Slot(uri=SCHEMA.name, name="DefinedTerm_title", curie=SCHEMA.curie('name'),
                   model_uri=DCAT_4C_AP.DefinedTerm_title, domain=DefinedTerm, range=Optional[str])

slots.Device_has_part = Slot(uri=DCTERMS.hasPart, name="Device_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=DCAT_4C_AP.Device_has_part, domain=Device, range=Optional[Union[dict[Union[str, DeviceId], Union[dict, "Device"]], list[Union[dict, "Device"]]]])

slots.Device_other_identifier = Slot(uri=ADMS.identifier, name="Device_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.Device_other_identifier, domain=Device, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Distribution_access_URL = Slot(uri=DCAT.accessURL, name="Distribution_access_URL", curie=DCAT.curie('accessURL'),
                   model_uri=DCAT_4C_AP.Distribution_access_URL, domain=Distribution, range=Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]])

slots.Distribution_access_service = Slot(uri=DCAT.accessService, name="Distribution_access_service", curie=DCAT.curie('accessService'),
                   model_uri=DCAT_4C_AP.Distribution_access_service, domain=Distribution, range=Optional[Union[Union[dict, DataService], list[Union[dict, DataService]]]])

slots.Distribution_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="Distribution_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=DCAT_4C_AP.Distribution_applicable_legislation, domain=Distribution, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.Distribution_availability = Slot(uri=DCATAP.availability, name="Distribution_availability", curie=DCATAP.curie('availability'),
                   model_uri=DCAT_4C_AP.Distribution_availability, domain=Distribution, range=Optional[Union[dict, "Concept"]])

slots.Distribution_byte_size = Slot(uri=DCAT.byteSize, name="Distribution_byte_size", curie=DCAT.curie('byteSize'),
                   model_uri=DCAT_4C_AP.Distribution_byte_size, domain=Distribution, range=Optional[int])

slots.Distribution_checksum = Slot(uri=SPDX.checksum, name="Distribution_checksum", curie=SPDX.curie('checksum'),
                   model_uri=DCAT_4C_AP.Distribution_checksum, domain=Distribution, range=Optional[Union[dict, Checksum]])

slots.Distribution_compression_format = Slot(uri=DCAT.compressFormat, name="Distribution_compression_format", curie=DCAT.curie('compressFormat'),
                   model_uri=DCAT_4C_AP.Distribution_compression_format, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_description = Slot(uri=DCTERMS.description, name="Distribution_description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.Distribution_description, domain=Distribution, range=Optional[Union[str, list[str]]])

slots.Distribution_documentation = Slot(uri=FOAF.page, name="Distribution_documentation", curie=FOAF.curie('page'),
                   model_uri=DCAT_4C_AP.Distribution_documentation, domain=Distribution, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.Distribution_download_URL = Slot(uri=DCAT.downloadURL, name="Distribution_download_URL", curie=DCAT.curie('downloadURL'),
                   model_uri=DCAT_4C_AP.Distribution_download_URL, domain=Distribution, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.Distribution_format = Slot(uri=DCTERMS.format, name="Distribution_format", curie=DCTERMS.curie('format'),
                   model_uri=DCAT_4C_AP.Distribution_format, domain=Distribution, range=Optional[Union[dict, "MediaTypeOrExtent"]])

slots.Distribution_has_policy = Slot(uri=ODRL.hasPolicy, name="Distribution_has_policy", curie=ODRL.curie('hasPolicy'),
                   model_uri=DCAT_4C_AP.Distribution_has_policy, domain=Distribution, range=Optional[Union[dict, "Policy"]])

slots.Distribution_language = Slot(uri=DCTERMS.language, name="Distribution_language", curie=DCTERMS.curie('language'),
                   model_uri=DCAT_4C_AP.Distribution_language, domain=Distribution, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.Distribution_licence = Slot(uri=DCTERMS.license, name="Distribution_licence", curie=DCTERMS.curie('license'),
                   model_uri=DCAT_4C_AP.Distribution_licence, domain=Distribution, range=Optional[Union[dict, "LicenseDocument"]])

slots.Distribution_linked_schemas = Slot(uri=DCTERMS.conformsTo, name="Distribution_linked_schemas", curie=DCTERMS.curie('conformsTo'),
                   model_uri=DCAT_4C_AP.Distribution_linked_schemas, domain=Distribution, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.Distribution_media_type = Slot(uri=DCAT.mediaType, name="Distribution_media_type", curie=DCAT.curie('mediaType'),
                   model_uri=DCAT_4C_AP.Distribution_media_type, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_modification_date = Slot(uri=DCTERMS.modified, name="Distribution_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=DCAT_4C_AP.Distribution_modification_date, domain=Distribution, range=Optional[Union[str, XSDDate]])

slots.Distribution_packaging_format = Slot(uri=DCAT.packageFormat, name="Distribution_packaging_format", curie=DCAT.curie('packageFormat'),
                   model_uri=DCAT_4C_AP.Distribution_packaging_format, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_release_date = Slot(uri=DCTERMS.issued, name="Distribution_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=DCAT_4C_AP.Distribution_release_date, domain=Distribution, range=Optional[Union[str, XSDDate]])

slots.Distribution_rights = Slot(uri=DCTERMS.rights, name="Distribution_rights", curie=DCTERMS.curie('rights'),
                   model_uri=DCAT_4C_AP.Distribution_rights, domain=Distribution, range=Optional[Union[dict, "RightsStatement"]])

slots.Distribution_spatial_resolution = Slot(uri=DCAT.spatialResolutionInMeters, name="Distribution_spatial_resolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=DCAT_4C_AP.Distribution_spatial_resolution, domain=Distribution, range=Optional[Decimal])

slots.Distribution_status = Slot(uri=ADMS.status, name="Distribution_status", curie=ADMS.curie('status'),
                   model_uri=DCAT_4C_AP.Distribution_status, domain=Distribution, range=Optional[Union[dict, "Concept"]])

slots.Distribution_temporal_resolution = Slot(uri=DCAT.temporalResolution, name="Distribution_temporal_resolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=DCAT_4C_AP.Distribution_temporal_resolution, domain=Distribution, range=Optional[str])

slots.Distribution_title = Slot(uri=DCTERMS.title, name="Distribution_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.Distribution_title, domain=Distribution, range=Optional[Union[str, list[str]]])

slots.Entity_title = Slot(uri=DCTERMS.title, name="Entity_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.Entity_title, domain=Entity, range=Optional[str])

slots.Entity_description = Slot(uri=DCTERMS.description, name="Entity_description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.Entity_description, domain=Entity, range=Optional[str])

slots.Entity_other_identifier = Slot(uri=ADMS.identifier, name="Entity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.Entity_other_identifier, domain=Entity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Entity_has_part = Slot(uri=DCTERMS.hasPart, name="Entity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=DCAT_4C_AP.Entity_has_part, domain=Entity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.Entity_part_of = Slot(uri=DCTERMS.isPartOf, name="Entity_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=DCAT_4C_AP.Entity_part_of, domain=Entity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.EvaluatedActivity_other_identifier = Slot(uri=ADMS.identifier, name="EvaluatedActivity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.EvaluatedActivity_other_identifier, domain=EvaluatedActivity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.EvaluatedEntity_title = Slot(uri=DCTERMS.title, name="EvaluatedEntity_title", curie=DCTERMS.curie('title'),
                   model_uri=DCAT_4C_AP.EvaluatedEntity_title, domain=EvaluatedEntity, range=Optional[str])

slots.EvaluatedEntity_description = Slot(uri=DCTERMS.description, name="EvaluatedEntity_description", curie=DCTERMS.curie('description'),
                   model_uri=DCAT_4C_AP.EvaluatedEntity_description, domain=EvaluatedEntity, range=Optional[str])

slots.EvaluatedEntity_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="EvaluatedEntity_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=DCAT_4C_AP.EvaluatedEntity_was_generated_by, domain=EvaluatedEntity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, Activity]], list[Union[dict, Activity]]]])

slots.EvaluatedEntity_other_identifier = Slot(uri=ADMS.identifier, name="EvaluatedEntity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.EvaluatedEntity_other_identifier, domain=EvaluatedEntity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Identifier_notation = Slot(uri=SKOS.notation, name="Identifier_notation", curie=SKOS.curie('notation'),
                   model_uri=DCAT_4C_AP.Identifier_notation, domain=Identifier, range=str)

slots.LicenseDocument_type = Slot(uri=DCTERMS.type, name="LicenseDocument_type", curie=DCTERMS.curie('type'),
                   model_uri=DCAT_4C_AP.LicenseDocument_type, domain=LicenseDocument, range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]])

slots.Location_bbox = Slot(uri=DCAT.bbox, name="Location_bbox", curie=DCAT.curie('bbox'),
                   model_uri=DCAT_4C_AP.Location_bbox, domain=Location, range=Optional[str])

slots.Location_centroid = Slot(uri=DCAT.centroid, name="Location_centroid", curie=DCAT.curie('centroid'),
                   model_uri=DCAT_4C_AP.Location_centroid, domain=Location, range=Optional[str])

slots.Location_geometry = Slot(uri=LOCN.geometry, name="Location_geometry", curie=LOCN.curie('geometry'),
                   model_uri=DCAT_4C_AP.Location_geometry, domain=Location, range=Optional[Union[dict, "Geometry"]])

slots.PeriodOfTime_beginning = Slot(uri=TIME.hasBeginning, name="PeriodOfTime_beginning", curie=TIME.curie('hasBeginning'),
                   model_uri=DCAT_4C_AP.PeriodOfTime_beginning, domain=PeriodOfTime, range=Optional[Union[dict, "TimeInstant"]])

slots.PeriodOfTime_end = Slot(uri=TIME.hasEnd, name="PeriodOfTime_end", curie=TIME.curie('hasEnd'),
                   model_uri=DCAT_4C_AP.PeriodOfTime_end, domain=PeriodOfTime, range=Optional[Union[dict, "TimeInstant"]])

slots.PeriodOfTime_end_date = Slot(uri=DCAT.endDate, name="PeriodOfTime_end_date", curie=DCAT.curie('endDate'),
                   model_uri=DCAT_4C_AP.PeriodOfTime_end_date, domain=PeriodOfTime, range=Optional[Union[str, XSDDate]])

slots.PeriodOfTime_start_date = Slot(uri=DCAT.startDate, name="PeriodOfTime_start_date", curie=DCAT.curie('startDate'),
                   model_uri=DCAT_4C_AP.PeriodOfTime_start_date, domain=PeriodOfTime, range=Optional[Union[str, XSDDate]])

slots.QualitativeAttribute_value = Slot(uri=PROV.value, name="QualitativeAttribute_value", curie=PROV.curie('value'),
                   model_uri=DCAT_4C_AP.QualitativeAttribute_value, domain=QualitativeAttribute, range=str)

slots.QuantitativeAttribute_value = Slot(uri=PROV.value, name="QuantitativeAttribute_value", curie=PROV.curie('value'),
                   model_uri=DCAT_4C_AP.QuantitativeAttribute_value, domain=QuantitativeAttribute, range=float)

slots.Relationship_had_role = Slot(uri=DCAT.hadRole, name="Relationship_had_role", curie=DCAT.curie('hadRole'),
                   model_uri=DCAT_4C_AP.Relationship_had_role, domain=Relationship, range=Union[Union[dict, "Role"], list[Union[dict, "Role"]]])

slots.Relationship_relation = Slot(uri=DCTERMS.relation, name="Relationship_relation", curie=DCTERMS.curie('relation'),
                   model_uri=DCAT_4C_AP.Relationship_relation, domain=Relationship, range=Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]])

slots.Software_has_part = Slot(uri=DCTERMS.hasPart, name="Software_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=DCAT_4C_AP.Software_has_part, domain=Software, range=Optional[Union[dict[Union[str, SoftwareId], Union[dict, "Software"]], list[Union[dict, "Software"]]]])

slots.Software_other_identifier = Slot(uri=ADMS.identifier, name="Software_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=DCAT_4C_AP.Software_other_identifier, domain=Software, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Atom_rdf_type = Slot(uri=RDF.type, name="Atom_rdf_type", curie=RDF.curie('type'),
                   model_uri=DCAT_4C_AP.Atom_rdf_type, domain=Atom, range=Union[dict, DefinedTerm])

slots.ChemicalReaction_has_temperature = Slot(uri=SIO['000008'], name="ChemicalReaction_has_temperature", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.ChemicalReaction_has_temperature, domain=ChemicalReaction, range=Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]])

slots.ChemicalReaction_has_pressure = Slot(uri=SIO['000008'], name="ChemicalReaction_has_pressure", curie=SIO.curie('000008'),
                   model_uri=DCAT_4C_AP.ChemicalReaction_has_pressure, domain=ChemicalReaction, range=Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]])

slots.ChemicalReaction_related_resource = Slot(uri=DCTERMS.relation, name="ChemicalReaction_related_resource", curie=DCTERMS.curie('relation'),
                   model_uri=DCAT_4C_AP.ChemicalReaction_related_resource, domain=ChemicalReaction, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, Resource]], list[Union[dict, Resource]]]])

slots.NMRSample_composed_of = Slot(uri=BFO['0000051'], name="NMRSample_composed_of", curie=BFO.curie('0000051'),
                   model_uri=DCAT_4C_AP.NMRSample_composed_of, domain=NMRSample, range=Union[dict[Union[str, CharacterizedCompoundId], Union[dict, CharacterizedCompound]], list[Union[dict, CharacterizedCompound]]])

slots.NMRSample_derived_from = Slot(uri=PROV.wasDerivedFrom, name="NMRSample_derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=DCAT_4C_AP.NMRSample_derived_from, domain=NMRSample, range=Optional[Union[dict, Entity]])

slots.NMRAnalysisDataset_was_generated_by = Slot(uri=OBI['0000312'], name="NMRAnalysisDataset_was_generated_by", curie=OBI.curie('0000312'),
                   model_uri=DCAT_4C_AP.NMRAnalysisDataset_was_generated_by, domain=NMRAnalysisDataset, range=Optional[Union[dict[Union[str, NMRSpectralAnalysisId], Union[dict, "NMRSpectralAnalysis"]], list[Union[dict, "NMRSpectralAnalysis"]]]])

slots.NMRAnalysisDataset_is_about_entity = Slot(uri=IAO['0000136'], name="NMRAnalysisDataset_is_about_entity", curie=IAO.curie('0000136'),
                   model_uri=DCAT_4C_AP.NMRAnalysisDataset_is_about_entity, domain=NMRAnalysisDataset, range=Optional[Union[dict[Union[str, NMRSampleId], Union[dict, "NMRSample"]], list[Union[dict, "NMRSample"]]]])

slots.NMRSpectralAnalysis_evaluated_entity = Slot(uri=OBI['0000293'], name="NMRSpectralAnalysis_evaluated_entity", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.NMRSpectralAnalysis_evaluated_entity, domain=NMRSpectralAnalysis, range=Optional[Union[dict[Union[str, NMRSpectrumId], Union[dict, "NMRSpectrum"]], list[Union[dict, "NMRSpectrum"]]]])

slots.NMRSpectrum_was_generated_by = Slot(uri=OBI['0000312'], name="NMRSpectrum_was_generated_by", curie=OBI.curie('0000312'),
                   model_uri=DCAT_4C_AP.NMRSpectrum_was_generated_by, domain=NMRSpectrum, range=Optional[Union[dict[Union[str, NMRSpectroscopyId], Union[dict, "NMRSpectroscopy"]], list[Union[dict, "NMRSpectroscopy"]]]])

slots.NMRSpectroscopy_evaluated_entity = Slot(uri=OBI['0000293'], name="NMRSpectroscopy_evaluated_entity", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.NMRSpectroscopy_evaluated_entity, domain=NMRSpectroscopy, range=Union[dict[Union[str, NMRSampleId], Union[dict, "NMRSample"]], list[Union[dict, "NMRSample"]]])

slots.NMRSpectroscopy_rdf_type = Slot(uri=RDF.type, name="NMRSpectroscopy_rdf_type", curie=RDF.curie('type'),
                   model_uri=DCAT_4C_AP.NMRSpectroscopy_rdf_type, domain=NMRSpectroscopy, range=Union[dict, DefinedTerm])

slots.NMRSpectroscopy_used_solvent = Slot(uri=OBI['0000293'], name="NMRSpectroscopy_used_solvent", curie=OBI.curie('0000293'),
                   model_uri=DCAT_4C_AP.NMRSpectroscopy_used_solvent, domain=NMRSpectroscopy, range=Union[dict[Union[str, NMRSolventId], Union[dict, "NMRSolvent"]], list[Union[dict, "NMRSolvent"]]])

slots.MaterialEntity_has_part = Slot(uri=BFO['0000051'], name="MaterialEntity_has_part", curie=BFO.curie('0000051'),
                   model_uri=DCAT_4C_AP.MaterialEntity_has_part, domain=MaterialEntity, range=Optional[Union[dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], list[Union[dict, "MaterialEntity"]]]])

slots.MaterialSample_derived_from = Slot(uri=PROV.wasDerivedFrom, name="MaterialSample_derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=DCAT_4C_AP.MaterialSample_derived_from, domain=MaterialSample, range=Optional[Union[dict, Entity]])
