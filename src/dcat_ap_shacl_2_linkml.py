#!/usr/bin/env python3
# Author: https://orcid.org/0000-0002-1595-3213 | Date: 2025-04-09

import json
import os
from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime.dumpers import YAMLDumper
from linkml_runtime.linkml_model import SlotDefinition, TypeDefinition, ClassDefinition, EnumDefinition

# Constants
DESCRIPTION1 = """
This LinkML schema representation of DCAT-AP 3.0.0 was automatically created from these [JSON-LD SHACL shapes](https://github.com/SEMICeu/DCAT-AP/blob/master/releases/3.0.0/shacl/dcat-ap-SHACL.jsonld) using this Python script: https://github.com/StroemPhi/dcat-4C-ap/tree/main/src/dcat-ap_shacl_2_linkml.py.
""".replace('\n', '')

NOTE = """
The JSON-LD SHACL constraints published with the [July 3.0.0 GitHub release](https://github.com/SEMICeu/DCAT-AP/releases/tag/3.0.0) and in the [3.0.0. release branch](https://github.com/SEMICeu/DCAT-AP/tree/3.0.0) are different from the ones in https://github.com/SEMICeu/DCAT-AP/tree/master/releases/3.0.0. Also the TTL shapes provided in the latter in the HTML folder differ from the ones in the SHACL folder, in that they declare "dcat:ResourceShape/DcatResource_Shape" and "TemporalLiteralShape/DateOrDateTimeDataType_Shape"(shacl/html folder) as unions of the dcat:Dataset, dcat:Catalog, dcat:DataService and dcat:DatasetSeries respectively the datatypes xsd:date, xsd:dateTime, xsd:gYear & xsd:gYearMonth. We currently address this in the conversion script by only allowing xsd:date as a [Temporal Literal](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TemporalLiteral), which means that this LinkML representation of DCAT-AP is stricter and values in xsd:dateTime format will automatically be typecast to xsd:date. Regarding the 'dcat:ResourceShape/DcatResource_Shape' we use the LinkML [union as ranges](https://linkml.io/linkml/schemas/advanced.html#unions-as-ranges) approach to provide the expected union of dcat:Resource subclasses. However, this is not fully implemented in LinkML yet, so that any kind of object/class could be used, until https://github.com/linkml/linkml/issues/1813 is fixed.
""".replace('\n', '')

DESCRIPTION2 = """
This metadata schema is an Extension of the DCAT Application Profile for Providing Links to Use-case Specific Context. It allows to provide additional metadata regarding: which kind(s) of entity(s) or activity(s) were evaluated (the dcat:Dataset is about), which kind of activity generated the dcat:Dataset, which kind of instruments were used in the dataset generating activity, in which surrounding (e.g. a laboratory) and according to which plan the dataset generating activity took place, as well as regarding which kind(s) of qualitative and quantitative characteristic were attributed to the evaluated entity or evaluated activity and to the used instruments.""".replace('\n', '')

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
    'qb': 'http://purl.org/linked-data/cube#',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'sh': 'http://www.w3.org/ns/shacl#',
    'skos': 'http://www.w3.org/2004/02/skos/core#',
    'vl': 'https://purl.eu/ns/shacl#',
    'iana': 'https://www.iana.org/assignments/',
    'epos': 'https://www.epos-eu.org/epos-dcat-ap#',
    'schema': 'https://schema.org/'}

# The shape for rdfs:Literal is ignored, since we use LinkML's 'string' as default datatype for unspecified literal
# slot ranges.
# There shape 'mediaType' is ignored, as it is a duplication/spelling error, seeAlso: L251-L258 in
# 'dcat_ap_SHACL.jsonld' and https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Mediatype.
# The shapes for 'TemporalLiteral' and 'CataloguedResource' are ignored, because the union of XSD date and time related
# datatypes respectively dcat:Resource subclasses that these shapes represent is implemented differently in LinkML,
# using the linkml:Any class as range and the "any_of" metamodel slot to build such range union.
# TODO: This "any_of" approach is not fully implemented in LinkML yet, see also:
#  https://github.com/linkml/linkml/issues/1813
# The shape for 'CataloguedResource' is
IGNORED_NODES = ['Literal', 'mediaType', 'TemporalLiteral', 'CataloguedResource']

# Manually curated dict with recommended slots for each class, as this info cannot be parsed from the used shapes.
RECOMMENDED_SLOTS = [{'Agent': ['type']},
                     {'LicenseDocument': ['type']},
                     {'Location': ['bbox', 'centroid']},
                     {'PeriodOfTime': ['end_date', 'start_date']},
                     {'Dataset': ['contact_point','keyword', 'theme']},
                     {'Distribution': ['availability','format', 'description']},
                     {'DataSeries': ['contact_point']},
                     {'CatalogueRecord': ['application_profile', 'change_type', 'listing_date']},
                     {'Catalogue': ['homepage', 'themes', 'release_date', 'language', 'modification_date']},
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


def load_dcat_ap_shacl_shapes(jsonld_file='dcat_ap_shacl.jsonld'):
    """
    Load the JSON-LD file containing the DCAT-AP SHACL shapes.
    Args:
        - jsonld_file: The filename of the previously, manually downloaded DCAT-AP SHACL shapes
    Returns:
        - A Python object containing the loaded SHACL shapes
    TODO: Use Requests to download directly from the script, maybe with cache option.
    """
    filepath = os.path.join('src', jsonld_file)
    with open(filepath, 'r') as file:
        print(f'INFO: Loaded the DCAT-AP SHACL shapes from {filepath}.')
        return json.load(file)


def parse_dcat_ap_shacl_shapes(builder):
    """
    Parse DCAT-AP SHACL shapes to create Link ML classes or datatypes from node shapes and slots from property shapes.
    Args:
        - builder (SchemaBuilder): A LinkML model builder to which DCAT-AP elements are added from SHACL shapes
    Returns:
        - builder (SchemaBuilder): A LinkML model builder with added DCAT-AP elements
    """
    dcat_ap_shapes = load_dcat_ap_shacl_shapes()

    # Add LinkML Any class to allow range unions,
    # see also https://linkml.io/linkml/schemas/advanced.html#unions-as-ranges
    builder.add_class(ClassDefinition(name='Any',
                                      class_uri='linkml:Any',
                                      description='This abstract class is needed to create the union of Dataset, '
                                                  'DatasetSeries, Catalogue and DataService for the range of the slot [primary_topic](https://stroemphi.github.io/dcat-4C-ap/elements/primary_topic/).'))
    # Iterate through each SHACL node shape within the loaded JSON-LD to derive the LinkML classes or types from them.
    for node_shape in dcat_ap_shapes['shapes']:
        node_curie = get_curie(node_shape['sh:targetClass'])

        # Account for the renaming of DCAT classes in DCAT-AP
        if node_curie == 'dcat:Resource':
            node_name = 'CataloguedResource'
        elif node_curie == 'dcat:Catalog':
            node_name = 'Catalogue'
        elif node_curie == 'dcat:CatalogRecord':
            node_name = 'CatalogueRecord'
        else:
            node_name = node_shape['@id'].split('#')[-1].split(':')[-1].replace('Shape', '')

        # Link to the DCAT-AP specs for the description of the classes.
        description = f'See [DCAT-AP specs:{node_name}](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#{node_name})'

        # Parse node shapes that are considered LinkML classes.
        if node_name not in ['dateTime', 'decimal', 'duration', 'hexBinary', 'nonNegativeInteger'] + IGNORED_NODES:
            # Add DCAT-AP Supportive Entity classes, this is done only to have an easier to read documentation.
            # 'Activity' is considered a main entity here, since we use it to extend DCAT-AP.
            if node_name not in ['Agent',
                                 'Catalogue',
                                 'CatalogueRecord',
                                 'CataloguedResource',
                                 'Checksum',
                                 'DataService',
                                 'Dataset',
                                 'DatasetSeries',
                                 'Distribution',
                                 'Kind',
                                 'Licence Document',
                                 'Location',
                                 'Relationship',
                                 'Activity' ]:
                builder.add_class(ClassDefinition(name='SupportiveEntity',
                                                  description='The supportive entities are supporting the main entities in the Application Profile. They are included in the Application Profile because they form the range of properties.'))
                builder.add_class(ClassDefinition(name=node_name,
                                                  class_uri=node_curie,
                                                  is_a='SupportiveEntity',
                                                  description=description))
            # Add DCAT-AP main classes
            else:
                builder.add_class(ClassDefinition(name=node_name,
                                                  class_uri=node_curie,
                                                  description=description))

            # Dict to store parsed slots of a class
            class_slots = {}

            # Iterate through each property shape within a node shape to derive the LinkML slots from them.
            if node_shape['sh:property']:
                for slot_shape in node_shape['sh:property']:
                    slot_curie = get_curie(slot_shape['sh:path'])
                    # Use LinkML snake_case naming convention default for slots
                    slot_name = slot_shape['sh:name']['en'].replace(' ', '_')
                    # Rename 'dataset' slot to 'has_dataset' to avoid clashes with Dataset class
                    slot_name = 'has_dataset' if slot_name == 'dataset' else slot_name
                    # Check cardinality constraints of a slot
                    required = True if 'sh:minCount' in slot_shape and int(slot_shape['sh:minCount']) == 1 else False
                    multivalued = False if 'sh:maxCount' in slot_shape and int(slot_shape['sh:maxCount']) == 1 else True
                    inlined_as_list = False if multivalued == False else True
                    # Use default slot range 'string' as substitute for 'rdfs:Literal' and 'xsd:date' for
                    # https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TemporalLiteral, except for
                    # https://semiceu.github.io/DCAT-AP/releases/3.0.0/#CataloguedResource, which uses linkml:Any.
                    any_of = None
                    if slot_name == 'primary_topic':
                        slot_range = 'Any'
                        any_of = [{'range':'Catalogue'},
                                  {'range':'Dataset'},
                                  {'range':'DatasetSeries'},
                                  {'range':'DataService'}]
                    elif slot_name in ['modification_date', 'listing_date', 'release_date', 'start_date', 'end_date']:
                        slot_range = 'date'
                    else:
                        slot_range = 'string'
                    # Assign slot range classes
                    if 'sh:class' in slot_shape:
                        # Account for the renaming of DCAT classes in DCAT-AP
                        if get_curie(slot_shape['sh:class']) == 'dcat:Resource':
                            slot_range = 'Any'
                        elif get_curie(slot_shape['sh:class']) == 'dcat:CatalogRecord':
                            slot_range = 'CatalogueRecord'
                        elif get_curie(slot_shape['sh:class']) == 'dcat:Catalog':
                            slot_range = 'Catalogue'
                        elif get_curie(slot_shape['sh:class']) == 'time:Instant':
                            slot_range = 'TimeInstant'
                        else:
                            slot_range = get_curie(slot_shape['sh:class']).split(':')[-1]
                    # Assign slot range datatypes
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

                    # Update the class slot attributes if multiple shapes exist for it.
                    if slot_name in class_slots.keys():
                        if slot_range != 'string':
                            class_slots[slot_name].range = slot_range
                        if not class_slots[slot_name].required:
                            class_slots[slot_name].required = required
                        if class_slots[slot_name].multivalued:
                            class_slots[slot_name].multivalued = multivalued
                        class_slots[slot_name].inlined_as_list = inlined_as_list

                    # Add the class slot
                    else:
                        description = slot_shape.get('sh:description', {}).get('en', '')
                        class_slots[slot_name] = SlotDefinition(name=slot_name,
                                                                slot_uri=slot_curie,
                                                                description=description,
                                                                required=required,
                                                                range=slot_range,
                                                                any_of=any_of,
                                                                multivalued=multivalued,
                                                                inlined_as_list=inlined_as_list)


                    # Add recommended flag to class slots which is not parsable from the DCAT-AP SHACL shapes.
                    for entry in RECOMMENDED_SLOTS:
                        for class_name, recommended_slots in entry.items():
                            if class_name == node_name:
                                for recommended_slot in recommended_slots:
                                    if recommended_slot in class_slots:
                                        class_slots[recommended_slot].recommended = True


                    # Add alphabetically sorted slots and their slot_usage properties to each class
                    builder.schema.classes[node_name].slots = sorted(list(class_slots.keys()))
                    builder.schema.classes[node_name].slot_usage = {key: class_slots[key] for key in
                                                                    sorted(class_slots)}
        # Parse and add datatypes
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

    # Add Enums to the schema based on https://semiceu.github.io/DCAT-AP/releases/3.0.0/#controlled-vocs
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
                                        ['application',
                                         'audio',
                                         'example',
                                         'font',
                                         'haptics',
                                         'image',
                                         'message',
                                         'model',
                                         'multipart',
                                         'text',
                                         'video'],
                                    'enum_uri': 'iana:top-level-media-types'}}
    for enum, attributes in enums.items():
        builder.add_enum(EnumDefinition(name=enum,
                                        enum_uri=attributes.get('enum_uri'),
                                        see_also=attributes.get('see_also'),
                                        code_set_tag=attributes.get('code_set_tag'),
                                        code_set_version=attributes.get('code_set_version'),
                                        permissible_values=attributes.get('permissible_values')))

    return builder


def build_dcatap_linkml():
    """
    Create a LinkML schema representation of DCAT-AP
    """
    print('\n   --- Building the DCAT-AP LinkML representation ---')

    builder = SchemaBuilder(name="dcat-ap")
    builder.schema.id = 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml.yaml'
    builder.schema.description = DESCRIPTION1 + '\nNOTE:' + NOTE
    builder.schema.default_prefix = 'dcatap_linkml'
    builder.schema.prefixes = PREFIX_MAP
    builder.schema.prefixes['dcatap_linkml']='https://stroemphi.github.io/dcat-4C-ap/dcat_ap_linkml.yaml#'
    builder.schema.title = 'LinkML schema representation of DCAT-AP 3.0.0'
    builder.schema.license = 'CC-BY 4.0'
    builder.schema.default_range = 'string'
    builder.schema.imports = ['linkml:types']
    builder.schema.source = 'https://semiceu.github.io/DCAT-AP/releases/3.0.0'

    builder = parse_dcat_ap_shacl_shapes(builder)

    # sort classes, slots and types alphabetically
    builder.schema.classes = {key: builder.schema.classes[key] for key in sorted(builder.schema.classes)}
    builder.schema.slots = {key: builder.schema.slots[key] for key in sorted(builder.schema.slots)}
    builder.schema.types = {key: builder.schema.types[key] for key in sorted(builder.schema.types)}

    # TODO list
    builder.schema.todos = ['Think about how to add all the other enums and their permissible values to constrain the allowed instances of classes such as "Concept", "MediaType", etc. as defined in https://semiceu.github.io/DCAT-AP/releases/3.0.0/#controlled-vocs. Using EnumBindings (https://linkml.io/linkml-model/latest/docs/bindings/) seems best, but does not yet work.', 'Check if https://github.com/linkml/linkml/issues/1813 is closed and range unions are validatable']

    return builder.schema


def build_dcatap_plus():
    """
    Create a LinkML schema representation of DCAT-AP with additional classes, slots and contraints.
    """
    print('\n  --- Building the extended DCAT-AP LinkML representation ---')

    def extend_dataset():
        builder.add_slot(SlotDefinition(name='id',
                                        identifier= True,
                                        range= 'uriorcurie',
                                        description= 'A slot to provide an URI for an entity within this schema.',
                                        in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='is_about_entity',
                                        slot_uri= 'dcterms:subject',
                                        range= 'EvaluatedEntity',
                                        description= 'A slot to provide the EvaluatedEntity a Dataset is about.',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core',
                                        exact_mappings=['IAO:0000136']))
        builder.add_slot(SlotDefinition(name='is_about_activity',
                                        slot_uri= 'dcterms:subject',
                                        range= 'EvaluatedActivity',
                                        description= 'A slot to provide the EvaluatedActivity a Dataset is about.',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core',
                                        exact_mappings=['IAO:0000136']))
        slots = ['id',
                 'is_about_entity',
                 'is_about_activity']
        dataset = builder.schema.classes['Dataset']
        dataset.slots = dataset.slots + slots
        dataset.slot_usage.was_generated_by.required = True
        dataset.slot_usage.was_generated_by.range = 'DataGeneratingActivity'
        dataset.slot_usage.was_generated_by.notes.append('stricter than DCAT-AP')
        dataset.in_subset=['domain_agnostic_core']
        dataset.description = 'A collection of data, published or curated by a single agent, and available for access or download in one or more representations.'


    def extend_activity():
        builder.add_slot(SlotDefinition(name='had_input_entity',
                                        slot_uri= 'prov:used',
                                        range= 'Entity',
                                        description= 'The slot to specify the Entity that was used as an input of an '
                                                     'Activity that is to be changed, consumed or transformed.',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='had_output_entity',
                                        slot_uri= 'prov:generated',
                                        range= 'Entity',
                                        description= 'The slot to specify the Entity that was generated as an output '
                                                     'of an Activity.',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='had_input_activity',
                                        slot_uri= 'prov:wasInformedBy',
                                        range= 'Activity',
                                        description= 'The slot to provide a previous Activity that informed the '
                                                     'Activity by being causally via a shared participant.',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='carried_out_by',
                                        slot_uri= 'prov:wasAssociatedWith',
                                        range= 'AgenticEntity',
                                        description= 'The slot to specify the AgenticEntity that played a certain '
                                                     'part in carrying out the Activity, either via having a specific '
                                                     'role, function or disposition that was realized in the Activity.',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='realized_plan',
                                        slot_uri= 'prov:used',
                                        range= 'Plan',
                                        description= 'The slot to specify the Plan (i.e. directive information or '
                                                     'procedure) that was realized by an Activity.',
                                        in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='occurred_in',
                                        slot_uri= 'prov:atLocation',
                                        range= 'Surrounding',
                                        description= 'The slot to specify the Surrounding in which an Activity '
                                                     'took place.',
                                        in_subset='domain_agnostic_core'))

        activity = builder.schema.classes['Activity']
        activity.slots = ['id',
                          'title',
                          'description',
                          'other_identifier',
                          'has_part',
                          'had_input_entity',
                          'had_output_entity',
                          'had_input_activity',
                          'carried_out_by',
                          'has_qualitative_attribute',
                          'has_quantitative_attribute',]
        activity.slot_usage = {
            'title': {
                'description': 'The slot to provide a title for the Activity.',
                'multivalued': True,
                'inlined_as_list': True,
                'notes':['not in DCAT-AP']},
            'description': {
                'description': 'The slot to provide a description for the Activity.',
                'multivalued': True,
                'inlined_as_list': True,
                'notes':['not in DCAT-AP']},
            'has_part': {
                'range': 'Activity',
                'description': 'The slot to provide an Activity that is part of the Activity.',
                'inlined': True,
                'notes':['not in DCAT-AP']},
            'other_identifier':{
                'range': 'Identifier',
                'description': 'The slot to provide a secondary identifier of the Activity.',
                'multivalued': True,
                'inlined_as_list': True,
                'notes':['not in DCAT-AP']},
            'has_qualitative_attribute':{
                'notes':['not in DCAT-AP']},
            'has_quantitative_attribute':{
                'notes':['not in DCAT-AP']},
            'had_input_entity':{
                'notes':['not in DCAT-AP']},
            'had_output_entity':{
                'notes':['not in DCAT-AP']},
            'had_input_activity':{
                'notes':['not in DCAT-AP']},
            'carried_out_by':{
                'notes':['not in DCAT-AP']}}
        activity.mixins = ['ClassifierMixin']
        activity.in_subset=['domain_agnostic_core']
        activity.notes = ['The specified properties (slots) of this class are part of our extension of the DCAT-AP.']

        builder.add_slot(SlotDefinition(name='evaluated_entity',
                                        slot_uri= 'prov:used',
                                        range= 'EvaluatedEntity',
                                        description= 'The slot to specify the Entity about which the '
                                                     'DataGeneratingActivity produced information.',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='evaluated_activity',
                                        slot_uri= 'prov:wasInformedBy',
                                        range= 'EvaluatedActivity',
                                        description= 'The slot to specify the Activity about which the '
                                                     'DataGeneratingActivity produced information.',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core'))
        builder.add_class(ClassDefinition(name='DataGeneratingActivity',
                                          class_uri='prov:Activity',
                                          is_a='Activity',
                                          description='An Activity (process) that has the objective to produce '
                                                      'information (in form of a dataset) about another Activity or '
                                                      'Entity.',
                                          slots=['evaluated_entity',
                                                 'evaluated_activity',
                                                 'realized_plan',
                                                 'occurred_in'],
                                          in_subset='domain_agnostic_core'))

    def add_classification_context():
        builder.add_class(ClassDefinition(name='ClassifierMixin',
                                          mixin=True,
                                          description='A mixin with which an entity of this schema can be classified via an additional rdf:type or dcterms:type assertion.',
                                          abstract=True,
                                          slots=['type',
                                                 'rdf_type'],
                                          slot_usage={
                                              'type':{
                                                  'inlined':True,
                                                  'range':'DefinedTerm'}},
                                          in_subset='domain_agnostic_core'))
        builder.add_class(ClassDefinition(name='DefinedTerm',
                                          class_uri='schema:DefinedTerm',
                                          description='A word, name, acronym or phrase that is defined in a controlled '
                                                      'vocabulary (CV) and that is used to provide an additional '
                                                      'rdf:type or dcterms:type of a class within this schema.',
                                          slots=['id',
                                                 'title'],
                                          slot_usage={
                                              'title':{
                                                  'slot_uri':'schema:name'}},
                                          attributes={
                                              'from_CV':{
                                                  'slot_uri':'schema:inDefinedTermSet',
                                                  'range':'uriorcurie',
                                                  'description': 'The URL of the controlled vocabulary.'}},
                                          in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='rdf_type',
                                        slot_uri= 'rdf:type',
                                        range= 'DefinedTerm',
                                        description= 'The slot to specify the ontology class that is instantiated by an entity.',
                                        recommended= True,
                                        inlined= True,
                                        in_subset='domain_agnostic_core'))


    def add_subject_of_interest_context():
        builder.add_class(ClassDefinition(name='Entity',
                                          class_uri='prov:Entity',
                                          mixins=['ClassifierMixin'],
                                          description='A physical, digital, conceptual, or other kind of thing with '
                                                      'some fixed aspects; entities may be real or imaginary.',
                                          slots=['title',
                                                 'description',
                                                 'id',
                                                 'other_identifier',
                                                 'has_qualitative_attribute',
                                                 'has_quantitative_attribute',
                                                 'has_part',],
                                          slot_usage={
                                              'title': {
                                                  'description': 'The slot to provide a title for the Entity.'},
                                              'description': {
                                                  'description': 'The slot to provide a description for the Entity.'},
                                              'other_identifier':{
                                                  'description': 'A slot to provide a secondary identifier of the Entity.',
                                                  'range': 'Identifier',
                                                  'required': 'false',
                                                  'multivalued': 'true',
                                                  'inlined_as_list': 'true'},
                                              'has_part':{
                                                  'description': 'A slot to provide a part of the EvaluatedEntity.',
                                                  'range':'Entity',
                                                  'multivalued': 'true',
                                                  'inlined_as_list': 'true'}},
                                          in_subset='domain_agnostic_core'))
        builder.add_class(ClassDefinition(name='EvaluatedEntity',
                                          is_a= 'Entity',
                                          class_uri='prov:Entity',
                                          description='An Entity that is being evaluated in a DataGeneratingActivity.',
                                          slots = ['was_generated_by'],
                                          slot_usage={
                                              'title': {
                                                  'description': 'The slot to provide a title for the EvaluatedEntity.'},
                                              'description': {
                                                  'description': 'The slot to provide a description for the '
                                                                 'EvaluatedEntity.'},
                                              'was_generated_by':{
                                                  'description': 'A slot to provide the Activity which created the EvaluatedEntity.',
                                                  'range':'Activity',
                                                  'multivalued': 'true',
                                                  'inlined_as_list': 'true'},
                                              'has_part':{
                                                  'description': 'A slot to provide a part of the EvaluatedEntity.',
                                                  'range':'EvaluatedEntity',
                                                  'multivalued': 'true',
                                                  'inlined_as_list': 'true'},
                                              'other_identifier':{
                                                  'description': 'A slot to provide a secondary identifier of the EvaluatedEntity.',
                                                  'range': 'Identifier',
                                                  'required': 'false',
                                                  'multivalued': 'true',
                                                  'inlined_as_list': 'true'}},
                                          in_subset='domain_agnostic_core'))
        builder.add_class(ClassDefinition(name='EvaluatedActivity',
                                          is_a='Activity',
                                          class_uri='prov:Activity',
                                          description='An activity or proces that is being evaluated in a '
                                                      'DataGeneratingActivity.',
                                          slots = ['has_qualitative_attribute',
                                                   'has_quantitative_attribute',
                                                   'has_part'],
                                          slot_usage={
                                              'has_part':{
                                                  'description': 'A slot to provide a part of the EvaluatedActivity.',
                                                  'range':'EvaluatedActivity',
                                                  'multivalued': 'true',
                                                  'inlined_as_list': 'true'},
                                              'other_identifier':{
                                                  'description': 'A slot to provide a secondary identifier of the EvaluatedActivity.',
                                                  'range': 'Identifier',
                                                  'required': False,
                                                  'multivalued': True,
                                                  'inlined_as_list': True}},
                                          in_subset='domain_agnostic_core'))


    def add_agent_context():
        builder.add_class(ClassDefinition(name='AgenticEntity',
                                          mixins= 'ClassifierMixin',
                                          class_uri='prov:Agent',
                                          description='An entity that is somehow responsible for an Activity to take '
                                                      'place.',
                                          slots = ['id',
                                                   'title',
                                                   'description',
                                                   'other_identifier',
                                                   'has_qualitative_attribute',
                                                   'has_quantitative_attribute',
                                                   'has_part'],
                                          slot_usage={
                                              'has_part':{
                                                  'description': 'The slot to specify parts of an Instrument that are '
                                                                 'themselves Instruments.',
                                                  'range':'AgenticEntity',
                                                  'inlined': True,
                                                  'multivalued': True,
                                                  'inlined_as_list': True},
                                              'other_identifier':{
                                                  'description': 'A slot to provide a secondary identifier for an Instrument.',
                                                  'range': 'Identifier',
                                                  'required': False,
                                                  'multivalued': True,
                                                  'inlined_as_list': True}},
                                          in_subset='domain_agnostic_core'))
        builder.add_class(ClassDefinition(name='Device',
                                          aliases=['hardware instrument'],
                                          is_a='AgenticEntity',
                                          class_uri='prov:Agent',
                                          description='A material instrument that is designed to perform a function '
                                                      'primarily by means of its mechanical or electrical nature.',
                                          in_subset='domain_agnostic_core',
                                          exact_mappings=['epos:Equipment',
                                                          'OBI:0000968',
                                                          'http://purl.obolibrary.org/obo/NCIT_C62103',
                                                          'http://semanticscience.org/resource/SIO_000956',
                                                          'http://purl.allotrope.org/ontologies/equipment#AFE_0000354'],
                                          slot_usage={
                                              'has_part':{
                                                  'description': 'The slot to specify parts of a Device that are '
                                                                 'themselves Devices.',
                                                  'range':'Device',
                                                  'inlined': True,
                                                  'multivalued': True,
                                                  'inlined_as_list': True},
                                              'other_identifier':{
                                                  'description': 'A slot to provide a secondary identifier for a Device.',
                                                  'range': 'Identifier',
                                                  'required': False,
                                                  'multivalued': True,
                                                  'inlined_as_list': True}}))
        builder.add_class(ClassDefinition(name='Software',
                                          is_a='AgenticEntity',
                                          class_uri='prov:SoftwareAgent',
                                          description='An instrument composed of a series of instructions that can be '
                                                      'interpreted by or directly executed by a computer.',
                                          in_subset='domain_agnostic_core',
                                          exact_mappings=['schema:SoftwareApplication'],
                                          slot_usage={
                                              'has_part':{
                                                  'description': 'The slot to specify parts of a Software that are '
                                                                 'themselves Software.',
                                                  'range':'Software',
                                                  'inlined': True,
                                                  'multivalued': True,
                                                  'inlined_as_list': True},
                                              'other_identifier':{
                                                  'description': 'A slot to provide a secondary identifier for a Software.',
                                                  'range': 'Identifier',
                                                  'required': False,
                                                  'multivalued': True,
                                              'inlined_as_list': True}}))


    def add_planning_and_surrounding_context():
        builder.add_class(ClassDefinition(name='Surrounding',
                                          mixins= 'ClassifierMixin',
                                          description='The surrounding in which the dataset creating activity took place (e.g. a lab).',
                                          class_uri='prov:Location',
                                          slots = ['title',
                                                   'description'],
                                          in_subset='domain_agnostic_core'))
        builder.add_class(ClassDefinition(name='Plan',
                                          mixins= 'ClassifierMixin',
                                          class_uri='prov:Plan',
                                          aliases=['Plan Specification',
                                                   'Method',
                                                   'Procedure'],
                                          description='A piece of information that specifies how an activity has to be carried out by its agents including what kind of steps have to be taken and what kind of parameters have to be met/set.',
                                          slots = ['title',
                                                   'description'],
                                          examples=[{'description': 'We assigned the structure of sample CRS-37013 using a 13C NMR (CHMO:0000595) and the settings: pulse sequence: zgpg30, temperature: 298.0 K, number of scans: 1024, Solvent : chloroform-D1 (CDCl3).'}],
                                          in_subset='domain_agnostic_core'))


    def add_attribute_context():
        builder.add_class(ClassDefinition(name='QualitativeAttribute',
                                          mixins= 'ClassifierMixin',
                                          class_uri='prov:Entity',
                                          description='A piece of information that is attributed to an '
                                                      'Entity, Activity or AgenticEntity.',
                                          slots = ['title',
                                                   'description',
                                                   'value'],
                                          slot_usage={
                                              'value':{
                                                  'description': 'The slot to provide the literal value of the QualitativeAttribute.',
                                                  'required': True,}},
                                          in_subset='domain_agnostic_core'))
        builder.add_class(ClassDefinition(name='QuantitativeAttribute',
                                          mixins= 'ClassifierMixin',
                                          class_uri='qudt:Quantity',
                                          description='A quantifiable piece of information that is attributed to an '
                                                      'Entity, Activity or AgenticEntity.',
                                          slots = ['title',
                                                   'description',
                                                   'value'],
                                          attributes={
                                              'has_quantity_type':{
                                                  'range': 'DefinedTerm',
                                                  'description': 'The type of quality that is quantifiable according to the QUDT ontology.',
                                                  'slot_uri': 'qudt:hasQuantityKind',
                                                  'required': True,
                                                  'bindings': [{
                                                      'binds_value_of': 'id',
                                                      'range': 'QUDTQuantityKindEnum',
                                                      'obligation_level': 'RECOMMENDED',
                                                      'description': 'Binds the type of a quantifiable attribute to a QUDT Quantity Kind instance from the QUDT Quantity Kind vocabulary.'}]},
                                              'unit':{
                                                  'slot_uri': 'qudt:unit',
                                                  'range': 'DefinedTerm',
                                                  'recommended': True,
                                                  'bindings':  [{
                                                      'binds_value_of': 'id',
                                                      'range': 'QUDTUnitEnum',
                                                      'obligation_level': 'RECOMMENDED',
                                                      'description': 'Restricts the allowable defined terms to the QUDT Unit vocabulary.'}]},},
                                          slot_usage={
                                              'value':{
                                                  'description': 'The slot to provide the literal value of the QuantitativeAttribute.',
                                                  'required': True,
                                                  'range': 'float'}},
                                          in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='has_qualitative_attribute',
                                        slot_uri= 'dcterms:relation',
                                        range= 'QualitativeAttribute',
                                        description= 'The slot to relate a qualitative attribute to an '
                                                     'EvaluatedEntity, EvaluatedActivity or AgenticEntity',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='has_quantitative_attribute',
                                        slot_uri= 'dcterms:relation',
                                        range= 'QuantitativeAttribute',
                                        description= 'The slot to relate a quantitative attribute to an '
                                                     'EvaluatedEntity, EvaluatedActivity or AgenticEntity',
                                        recommended= True,
                                        multivalued= True,
                                        inlined_as_list= True,
                                        in_subset='domain_agnostic_core'))
        builder.add_slot(SlotDefinition(name='value',
                                        slot_uri= 'prov:value',
                                        description= 'A slot to provide the literal value of an attribute.',
                                        in_subset='domain_agnostic_core'))
        todos =['Dynamic enums (https://linkml.io/linkml/schemas/enums.html#dynamic-enums) should be used to '
                'constrain the range of the type slot instead of using the default DefinedTerm as range. This will be done in profiles of this schema where we define Activity subclasses, e.g. NMRSpectroscopy. seeAlso: https://github.com/linkml/linkml-model/blob/main/tests/input/examples/schema_definition-enum_bindings-1.yaml']
        builder.add_enum(EnumDefinition(name='QUDTQuantityKindEnum',
                                        description= 'Possible kinds of quantifiable attribute types provided as QUDT QualityKind instances.',
                                        implements= ['owl:NamedIndividual'],
                                        reachable_from={
                                            'source_ontology': 'http://qudt.org/2.1/vocab/quantitykind',
                                            'source_nodes': ['qudt:QuantityKind'],
                                            'is_direct': True,
                                            'relationship_types': ['rdf:type']},
                                        in_subset='domain_agnostic_core',
                                        todos=todos))
        builder.add_enum(EnumDefinition(name='QUDTUnitEnum',
                                        description= 'Possible kinds of QUDT unit instances.',
                                        implements= ['owl:NamedIndividual'],
                                        reachable_from={
                                            'source_ontology': 'https://qudt.org/vocab/unit/',
                                            'source_nodes': ['qudt:QuantityKind'],
                                            'is_direct': True,
                                            'relationship_types': ['rdf:type']},
                                        in_subset='domain_agnostic_core',
                                        todos=todos))


    def add_analysis_context():
            builder.add_class(ClassDefinition(name='AnalysisDataset',
                                              is_a= 'Dataset',
                                              class_uri='dcat:Dataset',
                                              description='A Dataset that was generated by an analysis of some previously generated data. For example, a dataset that contains the data of an assignment of a chemical structure to a sample based on the spectral data obtained from the sample is an AnalyticalDataset.',
                                              slot_usage={
                                                  'was_generated_by':{
                                                      'range':'DataAnalysis',
                                                      'multivalued': True,
                                                      'inlined_as_list': True}},
                                              in_subset='domain_agnostic_core'))
            builder.add_class(ClassDefinition(name='DataAnalysis',
                                              is_a= 'DataGeneratingActivity',
                                              class_uri='prov:Activity',
                                              description='An Activity that evaluates the data produced by another Activity.',
                                              slot_usage={
                                                  'evaluated_entity':{
                                                      'description': 'A slot to provide the data that was analysed by the DataAnalysis.',
                                                      'range':'AnalysisSourceData',
                                                      'multivalued': True,
                                                      'inlined_as_list': True}},
                                              close_mappings=['NCIT:C25391'],
                                              exact_mappings='OBI:0200000',
                                              in_subset='domain_agnostic_core'))
            builder.add_class(ClassDefinition(name='AnalysisSourceData',
                                              is_a='EvaluatedEntity',
                                              class_uri='prov:Entity',
                                              description='Information that was evaluated within a DataAnalysis.',
                                              slot_usage={
                                                  'was_generated_by':{
                                                      'description': 'A slot to provide the Activity which created the AnalysisSourceData.',
                                                      'range':'DataGeneratingActivity',
                                                      'multivalued': True,
                                                      'inlined_as_list': True}},
                                              in_subset='domain_agnostic_core'))


    # Initialize the extended DCAT-AP LinkML schema

    builder = SchemaBuilder(name="dcat-ap-plus")
    builder.schema.id = 'https://stroemphi.github.io/dcat-4C-ap/dcat_ap_plus.yaml'
    builder.schema.description = DESCRIPTION2
    builder.schema.default_prefix = 'dcatap_plus'
    builder.schema.prefixes = PREFIX_MAP
    builder.schema.prefixes['dcatap_plus']='https://stroemphi.github.io/dcat-4C-ap/dcat_ap_plus.yaml#'
    builder.schema.prefixes['BFO']='http://purl.obolibrary.org/obo/BFO_'
    builder.schema.prefixes['OBI']='http://purl.obolibrary.org/obo/OBI_'
    builder.schema.prefixes['NCIT']='http://purl.obolibrary.org/obo/NCIT_'
    builder.schema.prefixes['SOSA']='http://www.w3.org/ns/sosa/'
    builder.schema.prefixes['qudt']= 'http://qudt.org/schema/qudt/'
    builder.schema.prefixes['schema']= 'http://schema.org/'
    builder.schema.prefixes['ex']= 'http://example.org/'
    builder.schema.title = 'DCAT-AP-PLUS'
    builder.schema.license = 'CC-BY 4.0'
    builder.schema.default_range = 'string'
    builder.schema.imports = ['linkml:types']
    builder.schema.see_also = [
        'https://github.com/StroemPhi/dcat-4C-ap',
        'https://github.com/HendrikBorgelt/DCAT-ap_as_LinkML_template/blob/main/src/dcatlinkml/schema/dcatlinkml.yaml',
        'https://gitlab.com/opensourcelab/scientificdata/scidats/-/blob/feature/linkml-schemata/schemata/metadata_model_scidats_dcat_ap.yaml?ref_type=heads']
    builder.schema.subsets = {
        'domain_agnostic_core': {
            'description':
                'The elements of this subset are considered the core layer of our DCAT-AP extension.'}}

    # Add LinkML representation of DCAT-AP v3.0.0
    builder = parse_dcat_ap_shacl_shapes(builder)

    # Add slots & constraints to DCAT-AP's Dataset class
    extend_dataset()
    extend_activity()

    # Add classes and properties needed to extend DCAT-AP
    add_classification_context()
    add_subject_of_interest_context()
    add_agent_context()
    add_planning_and_surrounding_context()
    add_attribute_context()
    add_analysis_context()

    # sort classes, slots and types alphabetically
    builder.schema.classes = {key: builder.schema.classes[key] for key in sorted(builder.schema.classes)}
    builder.schema.slots = {key: builder.schema.slots[key] for key in sorted(builder.schema.slots)}
    builder.schema.types = {key: builder.schema.types[key] for key in sorted(builder.schema.types)}

    # TODO list
    builder.schema.todos = ['Think about how to add all the other enums and their permissible values to constrain the allowed instances of classes such as "Concept", "MediaType", etc. as defined in https://semiceu.github.io/DCAT-AP/releases/3.0.0/#controlled-vocs. Using EnumBindings (https://linkml.io/linkml-model/latest/docs/bindings/) seems best, but does not yet work.', 'Check if https://github.com/linkml/linkml/issues/1813 is closed and range unions are validatable']

    return builder.schema


def dump_schema(schema, filename=None):
    if filename:
        filepath = os.path.join('src', 'dcat_4c_ap', 'schema', filename)
        YAMLDumper().dump(schema, filepath)
        print(f'INFO: {filename} was saved to {filepath}')


def main():
    # build and dump LinkML representation of DCAT-AP
    dump_schema(build_dcatap_linkml(),filename='dcat_ap_linkml.yaml')
    # build and dump DCAT-AP-PLUS
    dump_schema(build_dcatap_plus(),filename='dcat_ap_plus.yaml')

if __name__ == '__main__':
    main()
