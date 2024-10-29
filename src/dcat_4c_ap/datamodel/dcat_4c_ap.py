# Auto generated from dcat_4c_ap.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-10-29T09:00:30
# Schema: dcat-4C-ap
#
# id: https://w3id.org/StroemPhi/dcat-4C-ap
# description: This is an extension of the DCAT Application Profile in LinkML. It is intended to be used by NFDI4Chem & NFDI 4Cat as a core that can further be extended in profiles to provide domain specific metadata for a dataset.
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
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
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

from linkml_runtime.linkml_model.types import Boolean, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMINF = CurieNamespace('CHEMINF', 'http://semanticscience.org/resource/CHEMINF_')
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
NMR = CurieNamespace('NMR', 'http://nmrML.org/nmrCV#NMR:')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RXNO = CurieNamespace('RXNO', 'http://semanticscience.org/resource/RXNO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
T4FS = CurieNamespace('T4FS', 'http://purl.obolibrary.org/obo/T4FS_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
EX = CurieNamespace('ex', 'http://example.org/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NFDI = CurieNamespace('nfdi', 'https://w3id.org/StroemPhi/dcat-4nfdi-ap/')
NFDI4C = CurieNamespace('nfdi4c', 'https://w3id.org/StroemPhi/dcat_4C_ap/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
DEFAULT_ = NFDI4C


# Types

# Class references
class DefinedTermId(URIorCURIE):
    pass


class DatasetId(URIorCURIE):
    pass


class DatasetCollectionId(DatasetId):
    pass


class EntityOfInterestId(URIorCURIE):
    pass


class ChemicalReactionId(EntityOfInterestId):
    pass


class ChemicalSubstanceId(EntityOfInterestId):
    pass


class ChemAnalysisDataset(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NFDI4C["ChemAnalysisDataset"]
    class_class_curie: ClassVar[str] = "nfdi4c:ChemAnalysisDataset"
    class_name: ClassVar[str] = "ChemAnalysisDataset"
    class_model_uri: ClassVar[URIRef] = NFDI4C.ChemAnalysisDataset


Any = Any

@dataclass(repr=False)
class DefinedTerm(YAMLRoot):
    """
    A word, name, acronym, phrase that is defined in a controlled vocabulary (CV) and that is used to provide the
    rdf:type of an entity within this schema.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DefinedTerm"]
    class_class_curie: ClassVar[str] = "schema:DefinedTerm"
    class_name: ClassVar[str] = "DefinedTerm"
    class_model_uri: ClassVar[URIRef] = NFDI4C.DefinedTerm

    id: Union[str, DefinedTermId] = None
    alternative_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    name: Optional[Union[str, List[str]]] = empty_list()
    from_CV: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DefinedTermId):
            self.id = DefinedTermId(self.id)

        if not isinstance(self.alternative_id, list):
            self.alternative_id = [self.alternative_id] if self.alternative_id is not None else []
        self.alternative_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_id]

        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if self.from_CV is not None and not isinstance(self.from_CV, str):
            self.from_CV = str(self.from_CV)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A collection of data, published or curated by a single agent, and available for access or download in one or more
    representations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = NFDI4C.Dataset

    id: Union[str, DatasetId] = None
    name: Union[str, List[str]] = None
    description: Union[str, List[str]] = None
    alternative_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    was_generated_by: Optional[Union[dict, "ResearchActivity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.alternative_id, list):
            self.alternative_id = [self.alternative_id] if self.alternative_id is not None else []
        self.alternative_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_id]

        if self.was_generated_by is not None and not isinstance(self.was_generated_by, ResearchActivity):
            self.was_generated_by = ResearchActivity(**as_dict(self.was_generated_by))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatasetCollection(Dataset):
    """
    A curated collection of metadata about data resources.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "DatasetCollection"
    class_model_uri: ClassVar[URIRef] = NFDI4C.DatasetCollection

    id: Union[str, DatasetCollectionId] = None
    name: Union[str, List[str]] = None
    description: Union[str, List[str]] = None
    has_dataset: Optional[Union[Dict[Union[str, DatasetId], Union[dict, Dataset]], List[Union[dict, Dataset]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetCollectionId):
            self.id = DatasetCollectionId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        self._normalize_inlined_as_list(slot_name="has_dataset", slot_type=Dataset, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResearchActivity(YAMLRoot):
    """
    An activity (process) that has the objective to produce information about an entity by evaluating it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "ResearchActivity"
    class_model_uri: ClassVar[URIRef] = NFDI4C.ResearchActivity

    name: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[Union[str, List[str]]] = empty_list()
    alternative_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    type: Optional[Union[dict, DefinedTerm]] = None
    evaluated_entity: Optional[Union[dict, "EntityOfInterest"]] = None
    used_tool: Optional[Union[Union[dict, "Tool"], List[Union[dict, "Tool"]]]] = empty_list()
    used_plan: Optional[Union[dict, "ActivitySpecification"]] = None
    has_part: Optional[Union[dict, "ResearchActivity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.alternative_id, list):
            self.alternative_id = [self.alternative_id] if self.alternative_id is not None else []
        self.alternative_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_id]

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.evaluated_entity is not None and not isinstance(self.evaluated_entity, EntityOfInterest):
            self.evaluated_entity = EntityOfInterest(**as_dict(self.evaluated_entity))

        if not isinstance(self.used_tool, list):
            self.used_tool = [self.used_tool] if self.used_tool is not None else []
        self.used_tool = [v if isinstance(v, Tool) else Tool(**as_dict(v)) for v in self.used_tool]

        if self.used_plan is not None and not isinstance(self.used_plan, ActivitySpecification):
            self.used_plan = ActivitySpecification(**as_dict(self.used_plan))

        if self.has_part is not None and not isinstance(self.has_part, ResearchActivity):
            self.has_part = ResearchActivity(**as_dict(self.has_part))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NMRSpectroscopy(ResearchActivity):
    """
    Spectroscopy where the energy states of spin-active nuclei placed in a static magnetic field are interrogated by
    inducing transitions between the states via radio frequency irradiation. Each experiment consists of a sequence of
    radio frequency pulses with delay periods in between them.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000613"]
    class_class_curie: ClassVar[str] = "CHMO:0000613"
    class_name: ClassVar[str] = "NMRSpectroscopy"
    class_model_uri: ClassVar[URIRef] = NFDI4C.NMRSpectroscopy

    evaluated_entity: Optional[Union[dict, "ChemicalSubstance"]] = None
    type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.evaluated_entity is not None and not isinstance(self.evaluated_entity, ChemicalSubstance):
            self.evaluated_entity = ChemicalSubstance(**as_dict(self.evaluated_entity))

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityOfInterest(YAMLRoot):
    """
    Something that is being evaluated in a scientific process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "EntityOfInterest"
    class_model_uri: ClassVar[URIRef] = NFDI4C.EntityOfInterest

    id: Union[str, EntityOfInterestId] = None
    name: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[Union[str, List[str]]] = empty_list()
    alternative_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    type: Optional[Union[dict, DefinedTerm]] = None
    has_attribute: Optional[Union[Union[dict, "Attribute"], List[Union[dict, "Attribute"]]]] = empty_list()
    has_quantifiable_attribute: Optional[Union[Union[dict, "QuantifiableAttribute"], List[Union[dict, "QuantifiableAttribute"]]]] = empty_list()
    has_part: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityOfInterestId):
            self.id = EntityOfInterestId(self.id)

        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.alternative_id, list):
            self.alternative_id = [self.alternative_id] if self.alternative_id is not None else []
        self.alternative_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_id]

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        if not isinstance(self.has_quantifiable_attribute, list):
            self.has_quantifiable_attribute = [self.has_quantifiable_attribute] if self.has_quantifiable_attribute is not None else []
        self.has_quantifiable_attribute = [v if isinstance(v, QuantifiableAttribute) else QuantifiableAttribute(**as_dict(v)) for v in self.has_quantifiable_attribute]

        if self.has_part is not None and not isinstance(self.has_part, str):
            self.has_part = str(self.has_part)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalReaction(EntityOfInterest):
    """
    An experimental procedure with the aim of producing a portion of a given compound or mixture.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RXNO["0000329"]
    class_class_curie: ClassVar[str] = "RXNO:0000329"
    class_name: ClassVar[str] = "ChemicalReaction"
    class_model_uri: ClassVar[URIRef] = NFDI4C.ChemicalReaction

    id: Union[str, ChemicalReactionId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalReactionId):
            self.id = ChemicalReactionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalSubstance(EntityOfInterest):
    """
    A chemical substance that is being evaluated in a scientific process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["59999"]
    class_class_curie: ClassVar[str] = "CHEBI:59999"
    class_name: ClassVar[str] = "ChemicalSubstance"
    class_model_uri: ClassVar[URIRef] = NFDI4C.ChemicalSubstance

    id: Union[str, ChemicalSubstanceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalSubstanceId):
            self.id = ChemicalSubstanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tool(YAMLRoot):
    """
    A entity with a certain function used within a scientific activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = NFDI4C.Tool

    name: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[Union[str, List[str]]] = empty_list()
    alternative_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    type: Optional[Union[dict, DefinedTerm]] = None
    has_part: Optional[Union[Union[dict, "Tool"], List[Union[dict, "Tool"]]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, "Attribute"], List[Union[dict, "Attribute"]]]] = empty_list()
    has_quantifiable_attribute: Optional[Union[Union[dict, "QuantifiableAttribute"], List[Union[dict, "QuantifiableAttribute"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.alternative_id, list):
            self.alternative_id = [self.alternative_id] if self.alternative_id is not None else []
        self.alternative_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_id]

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part] if self.has_part is not None else []
        self.has_part = [v if isinstance(v, Tool) else Tool(**as_dict(v)) for v in self.has_part]

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        if not isinstance(self.has_quantifiable_attribute, list):
            self.has_quantifiable_attribute = [self.has_quantifiable_attribute] if self.has_quantifiable_attribute is not None else []
        self.has_quantifiable_attribute = [v if isinstance(v, QuantifiableAttribute) else QuantifiableAttribute(**as_dict(v)) for v in self.has_quantifiable_attribute]

        super().__post_init__(**kwargs)


class HardwareTool(Tool):
    """
    A hardware with a certain function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NFDI4C["HardwareTool"]
    class_class_curie: ClassVar[str] = "nfdi4c:HardwareTool"
    class_name: ClassVar[str] = "HardwareTool"
    class_model_uri: ClassVar[URIRef] = NFDI4C.HardwareTool


class SoftwareTool(Tool):
    """
    A software with a certain function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NFDI4C["SoftwareTool"]
    class_class_curie: ClassVar[str] = "nfdi4c:SoftwareTool"
    class_name: ClassVar[str] = "SoftwareTool"
    class_model_uri: ClassVar[URIRef] = NFDI4C.SoftwareTool


@dataclass(repr=False)
class Environment(YAMLRoot):
    """
    The environment in which the dataset creating Observation took place (e.g. a lab).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "Environment"
    class_model_uri: ClassVar[URIRef] = NFDI4C.Environment

    name: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[Union[str, List[str]]] = empty_list()
    alternative_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    type: Optional[Union[dict, DefinedTerm]] = None
    has_attribute: Optional[Union[Union[dict, "Attribute"], List[Union[dict, "Attribute"]]]] = empty_list()
    has_quantifiable_attribute: Optional[Union[Union[dict, "QuantifiableAttribute"], List[Union[dict, "QuantifiableAttribute"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.alternative_id, list):
            self.alternative_id = [self.alternative_id] if self.alternative_id is not None else []
        self.alternative_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_id]

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        if not isinstance(self.has_quantifiable_attribute, list):
            self.has_quantifiable_attribute = [self.has_quantifiable_attribute] if self.has_quantifiable_attribute is not None else []
        self.has_quantifiable_attribute = [v if isinstance(v, QuantifiableAttribute) else QuantifiableAttribute(**as_dict(v)) for v in self.has_quantifiable_attribute]

        super().__post_init__(**kwargs)


class Laboratory(Environment):
    """
    A facility that provides controlled conditions in which scientific or technological research, experiments, and
    measurement may be performed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "Laboratory"
    class_model_uri: ClassVar[URIRef] = NFDI4C.Laboratory


@dataclass(repr=False)
class ActivitySpecification(YAMLRoot):
    """
    "A piece of information that specifies: a) how an activity has to be carried out by its agents and b) the
    attributes of the passive activity participants that are used by the agents in terms of their presence and
    magnitude."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "ActivitySpecification"
    class_model_uri: ClassVar[URIRef] = NFDI4C.ActivitySpecification

    name: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[Union[str, List[str]]] = empty_list()
    type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Attribute(YAMLRoot):
    """
    A piece of information that is attributed to an entity of interest, tool or environment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IAO["0000030"]
    class_class_curie: ClassVar[str] = "IAO:0000030"
    class_name: ClassVar[str] = "Attribute"
    class_model_uri: ClassVar[URIRef] = NFDI4C.Attribute

    name: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[Union[str, List[str]]] = empty_list()
    alternative_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    type: Optional[Union[dict, DefinedTerm]] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.alternative_id, list):
            self.alternative_id = [self.alternative_id] if self.alternative_id is not None else []
        self.alternative_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.alternative_id]

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


class InChIKey(Attribute):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000059"]
    class_class_curie: ClassVar[str] = "CHEMINF:000059"
    class_name: ClassVar[str] = "InChIKey"
    class_model_uri: ClassVar[URIRef] = NFDI4C.InChIKey


class InChi(Attribute):
    """
    A structure descriptor which conforms to the InChI format specification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000113"]
    class_class_curie: ClassVar[str] = "CHEMINF:000113"
    class_name: ClassVar[str] = "InChi"
    class_model_uri: ClassVar[URIRef] = NFDI4C.InChi


class IUPACName(Attribute):
    """
    An IUPAC name is a systematic name which is formulated according to the rules and recommendations for chemical
    nomenclature set out by the International Union of Pure and Applied Chemistry (IUPAC).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000107"]
    class_class_curie: ClassVar[str] = "CHEMINF:000107"
    class_name: ClassVar[str] = "IUPACName"
    class_model_uri: ClassVar[URIRef] = NFDI4C.IUPACName


@dataclass(repr=False)
class QuantifiableAttribute(Attribute):
    """
    An attribute that is quantifiable.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "QuantifiableAttribute"
    class_model_uri: ClassVar[URIRef] = NFDI4C.QuantifiableAttribute

    unit: Optional[Union[str, DefinedTermId]] = None
    is_delta_attribute: Optional[Union[bool, Bool]] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.unit is not None and not isinstance(self.unit, DefinedTermId):
            self.unit = DefinedTermId(self.unit)

        if self.is_delta_attribute is not None and not isinstance(self.is_delta_attribute, Bool):
            self.is_delta_attribute = Bool(self.is_delta_attribute)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


# Enumerations
class NMRAssayEnum(EnumDefinitionImpl):
    """
    NMR types from the Chemical Methods Ontology
    """
    _defn = EnumDefinition(
        name="NMRAssayEnum",
        description="NMR types from the Chemical Methods Ontology",
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

# Slots
class slots:
    pass

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=NFDI4C.type, domain=None, range=Optional[str])

slots.alternative_id = Slot(uri=DCTERMS.identifier, name="alternative_id", curie=DCTERMS.curie('identifier'),
                   model_uri=NFDI4C.alternative_id, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.id = Slot(uri=NFDI.id, name="id", curie=NFDI.curie('id'),
                   model_uri=NFDI4C.id, domain=None, range=URIRef)

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=NFDI4C.description, domain=None, range=Optional[Union[str, List[str]]])

slots.name = Slot(uri=DCTERMS.title, name="name", curie=DCTERMS.curie('title'),
                   model_uri=NFDI4C.name, domain=None, range=Optional[Union[str, List[str]]])

slots.was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=NFDI4C.was_generated_by, domain=None, range=Optional[Union[dict, ResearchActivity]])

slots.has_dataset = Slot(uri=DCAT.dataset, name="has_dataset", curie=DCAT.curie('dataset'),
                   model_uri=NFDI4C.has_dataset, domain=None, range=Optional[Union[Dict[Union[str, DatasetId], Union[dict, Dataset]], List[Union[dict, Dataset]]]])

slots.evaluated_entity = Slot(uri=PROV.used, name="evaluated_entity", curie=PROV.curie('used'),
                   model_uri=NFDI4C.evaluated_entity, domain=None, range=Optional[Union[dict, EntityOfInterest]])

slots.used_tool = Slot(uri=PROV.used, name="used_tool", curie=PROV.curie('used'),
                   model_uri=NFDI4C.used_tool, domain=None, range=Optional[Union[Union[dict, Tool], List[Union[dict, Tool]]]])

slots.used_plan = Slot(uri=PROV.used, name="used_plan", curie=PROV.curie('used'),
                   model_uri=NFDI4C.used_plan, domain=None, range=Optional[Union[dict, ActivitySpecification]])

slots.has_part = Slot(uri=DCTERMS.hasPart, name="has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=NFDI4C.has_part, domain=None, range=Optional[str])

slots.has_attribute = Slot(uri=DCTERMS.relation, name="has_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=NFDI4C.has_attribute, domain=None, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.has_quantifiable_attribute = Slot(uri=DCTERMS.relation, name="has_quantifiable_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=NFDI4C.has_quantifiable_attribute, domain=None, range=Optional[Union[Union[dict, QuantifiableAttribute], List[Union[dict, QuantifiableAttribute]]]])

slots.value = Slot(uri=PROV.value, name="value", curie=PROV.curie('value'),
                   model_uri=NFDI4C.value, domain=None, range=Optional[str])

slots.definedTerm__from_CV = Slot(uri=SCHEMA.inDefinedTermSet, name="definedTerm__from_CV", curie=SCHEMA.curie('inDefinedTermSet'),
                   model_uri=NFDI4C.definedTerm__from_CV, domain=None, range=Optional[str])

slots.quantifiableAttribute__unit = Slot(uri=QUDT.applicableUnit, name="quantifiableAttribute__unit", curie=QUDT.curie('applicableUnit'),
                   model_uri=NFDI4C.quantifiableAttribute__unit, domain=None, range=Optional[Union[str, DefinedTermId]])

slots.quantifiableAttribute__is_delta_attribute = Slot(uri=QUDT['Quantity-isDeltaQuantity'], name="quantifiableAttribute__is_delta_attribute", curie=QUDT.curie('Quantity-isDeltaQuantity'),
                   model_uri=NFDI4C.quantifiableAttribute__is_delta_attribute, domain=None, range=Optional[Union[bool, Bool]])

slots.NMRSpectroscopy_evaluated_entity = Slot(uri=PROV.used, name="NMRSpectroscopy_evaluated_entity", curie=PROV.curie('used'),
                   model_uri=NFDI4C.NMRSpectroscopy_evaluated_entity, domain=NMRSpectroscopy, range=Optional[Union[dict, "ChemicalSubstance"]])

slots.NMRSpectroscopy_type = Slot(uri=RDF.type, name="NMRSpectroscopy_type", curie=RDF.curie('type'),
                   model_uri=NFDI4C.NMRSpectroscopy_type, domain=NMRSpectroscopy, range=Optional[Union[dict, DefinedTerm]])

slots.DefinedTerm_name = Slot(uri=SCHEMA.name, name="DefinedTerm_name", curie=SCHEMA.curie('name'),
                   model_uri=NFDI4C.DefinedTerm_name, domain=DefinedTerm, range=Optional[Union[str, List[str]]])

slots.DefinedTerm_alternative_id = Slot(uri=SCHEMA.identifier, name="DefinedTerm_alternative_id", curie=SCHEMA.curie('identifier'),
                   model_uri=NFDI4C.DefinedTerm_alternative_id, domain=DefinedTerm, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.Dataset_name = Slot(uri=DCTERMS.title, name="Dataset_name", curie=DCTERMS.curie('title'),
                   model_uri=NFDI4C.Dataset_name, domain=Dataset, range=Union[str, List[str]])

slots.Dataset_description = Slot(uri=DCTERMS.description, name="Dataset_description", curie=DCTERMS.curie('description'),
                   model_uri=NFDI4C.Dataset_description, domain=Dataset, range=Union[str, List[str]])

slots.Dataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="Dataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=NFDI4C.Dataset_was_generated_by, domain=Dataset, range=Optional[Union[dict, "ResearchActivity"]])

slots.DatasetCollection_id = Slot(uri=NFDI.id, name="DatasetCollection_id", curie=NFDI.curie('id'),
                   model_uri=NFDI4C.DatasetCollection_id, domain=DatasetCollection, range=Union[str, DatasetCollectionId])

slots.DatasetCollection_name = Slot(uri=DCTERMS.title, name="DatasetCollection_name", curie=DCTERMS.curie('title'),
                   model_uri=NFDI4C.DatasetCollection_name, domain=DatasetCollection, range=Union[str, List[str]])

slots.DatasetCollection_description = Slot(uri=DCTERMS.description, name="DatasetCollection_description", curie=DCTERMS.curie('description'),
                   model_uri=NFDI4C.DatasetCollection_description, domain=DatasetCollection, range=Union[str, List[str]])

slots.ResearchActivity_type = Slot(uri=RDF.type, name="ResearchActivity_type", curie=RDF.curie('type'),
                   model_uri=NFDI4C.ResearchActivity_type, domain=ResearchActivity, range=Optional[Union[dict, DefinedTerm]])

slots.ResearchActivity_has_part = Slot(uri=DCTERMS.hasPart, name="ResearchActivity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=NFDI4C.ResearchActivity_has_part, domain=ResearchActivity, range=Optional[Union[dict, "ResearchActivity"]])

slots.EntityOfInterest_type = Slot(uri=RDF.type, name="EntityOfInterest_type", curie=RDF.curie('type'),
                   model_uri=NFDI4C.EntityOfInterest_type, domain=EntityOfInterest, range=Optional[Union[dict, DefinedTerm]])

slots.Tool_type = Slot(uri=RDF.type, name="Tool_type", curie=RDF.curie('type'),
                   model_uri=NFDI4C.Tool_type, domain=Tool, range=Optional[Union[dict, DefinedTerm]])

slots.Tool_has_part = Slot(uri=DCTERMS.hasPart, name="Tool_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=NFDI4C.Tool_has_part, domain=Tool, range=Optional[Union[Union[dict, "Tool"], List[Union[dict, "Tool"]]]])

slots.Environment_type = Slot(uri=RDF.type, name="Environment_type", curie=RDF.curie('type'),
                   model_uri=NFDI4C.Environment_type, domain=Environment, range=Optional[Union[dict, DefinedTerm]])

slots.ActivitySpecification_type = Slot(uri=RDF.type, name="ActivitySpecification_type", curie=RDF.curie('type'),
                   model_uri=NFDI4C.ActivitySpecification_type, domain=ActivitySpecification, range=Optional[Union[dict, DefinedTerm]])

slots.Attribute_type = Slot(uri=RDF.type, name="Attribute_type", curie=RDF.curie('type'),
                   model_uri=NFDI4C.Attribute_type, domain=Attribute, range=Optional[Union[dict, DefinedTerm]])

slots.QuantifiableAttribute_type = Slot(uri=QUDT.hasQuantityKind, name="QuantifiableAttribute_type", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=NFDI4C.QuantifiableAttribute_type, domain=QuantifiableAttribute, range=Optional[Union[dict, DefinedTerm]])

slots.QuantifiableAttribute_value = Slot(uri=QUDT.value, name="QuantifiableAttribute_value", curie=QUDT.curie('value'),
                   model_uri=NFDI4C.QuantifiableAttribute_value, domain=QuantifiableAttribute, range=Optional[str])