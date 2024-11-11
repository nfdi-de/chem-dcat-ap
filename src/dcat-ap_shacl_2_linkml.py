#!/usr/bin/env python3
# Author: https://orcid.org/0000-0002-1595-3213 | Date: 2024-11-01

import json
from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime.dumpers import YAMLDumper
from linkml_runtime.linkml_model import SlotDefinition, TypeDefinition, ClassDefinition, EnumDefinition

# Constants
DESCRIPTION = """
This LinkML schema representation of DCAT-AP 3.0.0 was automatically created from these 
[JSON-LD SHACL shapes](https://github.com/SEMICeu/DCAT-AP/blob/master/releases/3.0.0/shacl/dcat-ap-SHACL.jsonld) 
using this Python script: https://github.com/StroemPhi/dcat-4C-ap/tree/main/src/dcat-ap_shacl_2_linkml.py.
""".replace('\n', '')

NOTE = """ 
The JSON-LD SHACL constraints published with the [Juli 3.0.0 GitHub release](
https://github.com/SEMICeu/DCAT-AP/releases/tag/3.0.0) and in the [3.0.0. release branch](
https://github.com/SEMICeu/DCAT-AP/tree/3.0.0) are different from the ones in 
https://github.com/SEMICeu/DCAT-AP/tree/master/releases/3.0.0. Also the TTL shapes provided in the latter in the 
HTML folder differ from the ones in the SHACL folder, in that they declare dcat:Resource and dcatap:TemporalLiteral 
as unions of the dcat:Resource subclasses respectively different XML Schema datatypes for date and time. 
We address this with 'helper code' in the conversion script. 
""".replace('\n', '')

PREFIX_MAP = {
    'linkml': 'https://w3id.org/linkml/',
    'foaf': 'http://xmlns.com/foaf/0.1/',
    'prov': 'http://www.w3.org/ns/prov#',
    'dcat': 'http://www.w3.org/ns/dcat#',
    'dcterms': 'http://purl.org/dc/terms/',
    'spdx': 'http://spdx.org/rdf/terms#',
    'odrl': 'http://www.w3.org/ns/odrl/2/',
    'eli': 'http://data.europa.eu/eli/ontology#',
    'locn': 'http://www.w3.org/ns/locn#',
    'time': 'http://www.w3.org/2006/time#',
    'xsd': 'http://www.w3.org/2001/XMLSchema#',
    'vcard': 'http://www.w3.org/2006/vcard/ns#',
    'adms': 'http://www.w3.org/ns/adms#',
    'dcatap': 'http://data.europa.eu/r5r/',
    'linkmldcatap': 'https://stroemphi.github.io/dcat-4C-ap/dcat-4nfdi-ap/dcat-ap/',
    'qb': 'http://purl.org/linked-data/cube#',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'sh': 'http://www.w3.org/ns/shacl#',
    'skos': 'http://www.w3.org/2004/02/skos/core#',
    'vl': 'https://purl.eu/ns/shacl#',
    'iana': 'https://www.iana.org/assignments/'}

# The shapes for rdfs:Literal and dcterms:mediaType [sic] are ignored, 
# since we use LinkML's 'string' as default datatype for unspecified literal slot ranges 
# and dcterms:MediaType was used twice, once with this typo in the SHACL and a similar one in the HTML.
# seeAlso: L251-L258 in 'dcat-ap-SHACL.jsonld' and https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Mediatype
IGNORED_NODES = ['Literal', 'mediaType', 'TemporalLiteral']

# Manually curated dict with recommended slots for each class, as this info cannot be parsed from the used shapes.
RECOMMENDED_SLOTS = [{'Agent': ['type']},
                     {'LicenseDocument': ['type']},
                     {'Location': ['bbox', 'centroid']},
                     {'PeriodOfTime': ['end_date', 'start_date']},
                     {'Dataset': ['contact_point','keyword', 'theme']},
                     {'Distribution': ['availability','format', 'description']},
                     {'DataSeries': ['contact_point']},
                     {'CatalogRecord': ['application_profile', 'change_type', 'listing_date']},
                     {'Catalog': ['homepage', 'themes', 'release_date', 'language', 'modification_date']},
                     {'DataService': ['contact_point', 'endpoint_description', 'keyword', 'theme', 'conforms_to']},
                     ]

def get_curie(term_uri, prefixes=None):
    """
    Helper function to convert a term URI into a CURIE based on the known PREFIX_MAP.
        Args:
            - term_uri (str): The URI of a term.
            - prefixes (dict): The prefixes defined in PREFIX_MAP.
        Returns: 
            - term_curie (str): The CURIE (compact URI) of a term.
    TODO: 
        - Overkill to use [CURIEs](https://curies.readthedocs.io/en/stable/index.html) library instead?
    """
    term_curie = None
    if prefixes is None:
        prefixes = PREFIX_MAP
    for prefix, prefix_uri in prefixes.items():
        if prefix_uri in term_uri:
            term_curie = f"{prefix}:{term_uri.replace(prefix_uri, '')}"
    return term_curie


def load_shacl_shapes(jsonld_file='src/dcat-ap-SHACL.jsonld'):
    """
    Load the JSON-LD file containing the DCAT-AP SHACL shapes.
    TODO: Use Requests to download directly from the script, maybe with cache option.
    """
    with open(jsonld_file, 'r') as file:
        return json.load(file)


def parse_shacl_shapes(builder):
    """ 
    Parse DACAT-AP SHACL shapes to create Link ML classes or datatypes from node shapes and slots from property shapes. 
    Args:
        - builder (SchemaBuilder): The LinkML model builder to which to add the classes
        - dcat_ap_shapes (dict):
    Returns: 
        - builder (SchemaBuilder): The builder with added classes
    """
    dcat_ap_shapes = load_shacl_shapes()
    # Iterate through each SHACL node shape within the loaded JSON-LD to derive the LinkML classes or types from them.
    for node_shape in dcat_ap_shapes['shapes']:
        node_curie = get_curie(node_shape['sh:targetClass'])
        if node_curie == 'dcat:Resource':
            node_name = 'CataloguedResource'
        else:
            node_name = node_shape['@id'].split('#')[-1].split(':')[-1].replace('Shape', '')

        # Parse node shapes that are considered LinkML classes.
        if node_name not in ['dateTime', 'decimal', 'duration', 'hexBinary', 'nonNegativeInteger'] + IGNORED_NODES:
            # Add LinkML classes
            builder.add_class(ClassDefinition(name=node_name,
                                              class_uri=node_curie))
            # Dict to store parsed slots of a class
            class_slots = {}

            # Iterate through each property shape within a node shape to derive the LinkML slots from them.
            if 'sh:property' in node_shape:
                for slot_shape in node_shape['sh:property']:
                    slot_curie = get_curie(slot_shape['sh:path'])
                    # Use LinkML snake_case naming convention default for slots
                    slot_name = slot_shape['sh:name']['en'].replace(' ', '_')
                    slot_name = 'has_dataset' if slot_name == 'dataset' else slot_name
                    # Check cardinality constraints of a slot
                    required = True if 'sh:minCount' in slot_shape and int(slot_shape['sh:minCount']) == 1 else False
                    multivalued = False if 'sh:maxCount' in slot_shape and int(slot_shape['sh:maxCount']) == 1 else True
                    inlined_as_list = False if multivalued == False else True
                    # Use the default LinkML slot range as substitute for 'rdfs:Literal'
                    slot_range = 'string'
                    # Assign slot ranges
                    if 'sh:class' in slot_shape:
                        if get_curie(slot_shape['sh:class']) == 'dcat:Resource':
                            slot_range = 'CataloguedResource'
                        elif get_curie(slot_shape['sh:class']) == 'time:Instant':
                            slot_range = 'TimeInstant'
                        else:
                            slot_range = get_curie(slot_shape['sh:class']).split(':')[-1]
                    elif 'sh:datatype' in slot_shape:
                        datatype = get_curie(slot_shape['sh:datatype'])
                        if datatype.split(':')[-1] == 'dateTime':
                            slot_range = datatype.split(':')[-1].lower()
                        else:
                            slot_range = datatype.split(':')[-1]

                    # Add a generalized version of the slot to the LinkML schema, needed for later slot reuse.
                    if slot_name not in builder.schema.slots:
                        general_description = 'This slot is described in more detail within the class in which it is used.'
                        builder.add_slot(SlotDefinition(name=slot_name,
                                                        slot_uri=slot_curie,
                                                        description=general_description))

                    # Add the class slot
                    if slot_name in class_slots.keys():
                        if slot_range != 'string':
                            class_slots[slot_name].range = slot_range
                        if not class_slots[slot_name].required:
                            class_slots[slot_name].required = required
                        if class_slots[slot_name].multivalued:
                            class_slots[slot_name].multivalued = multivalued
                        class_slots[slot_name].inlined_as_list = inlined_as_list

                    # Update the class slot attributes if multiple shapes exist for it.
                    else:
                        description = slot_shape.get('sh:description', {}).get('en', '')
                        class_slots[slot_name] = SlotDefinition(name=slot_name,
                                                                slot_uri=slot_curie,
                                                                description=description,
                                                                required=required,
                                                                range=slot_range,
                                                                multivalued=multivalued,
                                                                inlined_as_list=inlined_as_list)

                    """
                    WILL BE IMPOSED IN THE PROFILES
                    # Add 'uri' slot to all classes in identified_resources
                    if node_name in ['Resource', 'Concept', 'Dataset', 'DatasetSeries', 'CatalogRecord', 'CataloguedResource',
                                     'RightsStatement','Policy', 'MediaTypeOrExtent']:
                        class_slots['id']= SlotDefinition(name= 'id',
                                                          identifier=True,
                                                          description=f'The URI of an instance of {node_name}.')
                        if 'id' not in builder.schema.slots:
                            class_slots['id'].description = 'The URI of an instance of the class.'
                            builder.add_slot(class_slots['id'])
                    """

                    # Add recommended flag to class slots which is not parsable from the DCAT-AP SHACL shapes.
                    for entry in RECOMMENDED_SLOTS:
                        for class_name, recommended_slots in entry.items():
                            if class_name == node_name:
                                for recommended_slot in recommended_slots:
                                    if recommended_slot in class_slots:
                                        class_slots[recommended_slot].recommended = True
                    

                    builder.schema.classes[node_name].slots = sorted(list(class_slots.keys()))
                    builder.schema.classes[node_name].slot_usage = {key: class_slots[key] for key in
                                                                    sorted(class_slots)}                 
                    
                    
        elif node_name in ['duration', 'hexBinary', 'nonNegativeInteger']:
            pattern, base, description = '', '', ''
            if 'nonNegativeInteger' in node_name:
                base = 'int'
                description = 'The datatype that represents non-negative integers.'
                pattern = r'([\-+]?[0-9]+)'
            elif 'duration' in node_name:
                base = 'str'
                description = 'The datatype that represents durations of time.'
                pattern =  r"""
                                        -?P( ( ( [0-9]+Y([0-9]+M)?([0-9]+D)?
                                               | ([0-9]+M)([0-9]+D)?
                                               | ([0-9]+D)
                                               )
                                               (T ( ([0-9]+H)([0-9]+M)?([0-9]+(\.[0-9]+)?S)?
                                                  | ([0-9]+M)([0-9]+(\.[0-9]+)?S)?
                                                  | ([0-9]+(\.[0-9]+)?S)
                                                  )
                                               )?
                                            )
                                          | (T ( ([0-9]+H)([0-9]+M)?([0-9]+(\.[0-9]+)?S)?
                                               | ([0-9]+M)([0-9]+(\.[0-9]+)?S)?
                                               | ([0-9]+(\.[0-9]+)?S)
                                               )
                                            )
                                          )""".replace('\n','').replace(' ','')
            elif 'hexBinary' in node_name:
                base = 'str'
                description = 'The datatype that represents arbitrary hex-encoded binary data.'
                pattern = r'([0-9a-fA-F]{2})*'

            builder.add_type(TypeDefinition(name=node_name,
                                            uri=node_curie,
                                            conforms_to=f'https://www.w3.org/TR/xmlschema11-2/#{node_name}',
                                            base=base,
                                            description=description,
                                            pattern=pattern)) 
                                
    return builder


def add_enums(builder):
    """
    Add Enums to the schema based on https://semiceu.github.io/DCAT-AP/releases/3.0.0/#controlled-vocs
    Args:
        - builder (SchemaBuilder): The LinkML model builder to which to add the enums
    Returns:
        - builder (SchemaBuilder): The builder with added enums
    """

    enums = {'DatasetThemes': {'permissible_values':
                                   [{'text': 'Agriculture, fisheries, forestry and food', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/AGRI'},
                                    {'text': 'Economy and finance', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/ECON'},
                                    {'text': 'Education, culture and sport', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/EDUC'},
                                    {'text': 'Energy', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/ENER'},
                                    {'text': 'Environment', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/ENVI'},
                                    {'text': 'Government and public sector', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/GOVE'},
                                    {'text': 'Health', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/HEAL'},
                                    {'text': 'International issues', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/INTR'},
                                    {'text': 'Justice, legal system and public safety', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/JUST'},
                                    {'text': 'Provisional data', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/OP_DATPRO'},
                                    {'text': 'Regions and cities', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/REGI'},
                                    {'text': 'Population and society', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/SOCI'},
                                    {'text': 'Science and technology', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/TECH'},
                                    {'text': 'Transport', 'meaning': 'http://publications.europa.eu/resource/authority/data-theme/TRAN'}],
                               'enum_uri':'http://publications.europa.eu/resource/authority/data-theme',
                               'see_also': 'https://op.europa.eu/s/zXIN'},
             'TopLevelMediaTypes': {'permissible_values':
                                        ['application', 'audio', 'example', 'font', 'haptics', 'image', 'message',
                                         'model', 'multipart', 'text', 'video'],
                                    'enum_uri': 'iana:top-level-media-types'}}

    for enum, attributes in enums.items():
        builder.add_enum(EnumDefinition(name=enum,
                                        permissible_values=attributes.get('permissible_values'),
                                        enum_uri=attributes.get('enum_uri'),
                                        see_also=attributes.get('see_also'),
                                        code_set_tag=attributes.get('code_set_tag'),
                                        code_set_version=attributes.get('code_set_version')))

    return builder


def build_schema():
    """
    Create a LinkML schema representation
    """
    builder = SchemaBuilder(name="dcat-ap")
    builder.schema.id = 'https://stroemphi.github.io/dcat-4C-ap/dcat-4nfdi-ap/dcat-ap.yaml'
    builder.schema.description = DESCRIPTION + '\nNOTE:' + NOTE
    builder.schema.default_prefix = 'linkmldcatap'
    builder.schema.prefixes = PREFIX_MAP
    builder.schema.title = 'LinkML schema representation of DCAT-AP 3.0.0'
    builder.schema.license = 'CC-BY 4.0'
    builder.schema.default_range = 'string'
    builder.schema.imports = ['linkml:types']
    builder.schema.source = 'https://semiceu.github.io/DCAT-AP/releases/3.0.0'
    
    builder = parse_shacl_shapes(builder)
    builder = add_enums(builder)


    # sort classes, slots and types alphabetically
    builder.schema.classes = {key: builder.schema.classes[key] for key in sorted(builder.schema.classes)}
    builder.schema.slots = {key: builder.schema.slots[key] for key in sorted(builder.schema.slots)}
    builder.schema.types = {key: builder.schema.types[key] for key in sorted(builder.schema.types)}

    # TODO list
    builder.schema.todos = ['Think about how to add all the enums and their permissible values to constrain the '
                            'allowed instances of classes such as "Concept", "MediaType", etc. as defined in '
                            'https://semiceu.github.io/DCAT-AP/releases/3.0.0/#controlled-vocs. '
                            'Using EnumBindings (https://linkml.io/linkml-model/latest/docs/bindings/) seems best, '
                            'but does not yet work.']

    return builder.schema


def dump_schema(schema, output_file='src/dcat_4c_ap/schema/dcat-ap.yaml'):
    YAMLDumper().dump(schema, output_file)


def main():
    dump_schema(build_schema())


if __name__ == '__main__':
    main()
