"""
A Script to parse the JSON-LD DCAT-AP 3.0.0 SHACL shapes and derive a LinkML schema from them.
Author: https://orcid.org/0000-0002-1595-3213
Date: 2024-11-01
"""

from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime.dumpers import YAMLDumper
from linkml_runtime.linkml_model import SlotDefinition, TypeDefinition, ClassDefinition
import json
import re


description = """|- 
This LinkML schema representation of DCAT-AP 3.0.0 was automatically created from these 
[JSON-LD SHACL shapes](https://github.com/SEMICeu/DCAT-AP/blob/master/releases/3.0.0/shacl/dcat-ap-SHACL.jsonld) 
using this Python script: https://github.com/StroemPhi/dcat-4C-ap/tree/main/src/dcat-ap_shacl_2_linkml.py.
"""
note = """ 
The referenced JSON-LD SHACL release file within the main branch is different from the one in the GitHub 
release with the same version tag. It was used, as the former is missing the property dcatap:applicableLegislation and 
its range class eli:LegalResource, which are an important update introduced in DCAT-AP 3.0.0 according to the HTML 
specification.
"""

# Manually created prefix map based on the prefixed found in the downloaded DCAT-AP JSON-LD
prefix_map = {'linkml': 'https://w3id.org/linkml/',
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
              'vl': 'https://purl.eu/ns/shacl#'}

# Helper function to use term CURIEs instead of URIs based on prefix_map.
def get_curie(term_uri, prefixes=None):
    """ Convert a term URI into a CURIE.
            Args:
                term_uri (str): The URI of a term.
                prefixes (dict): The prefixes defined in prefix_map.
            Returns:
                term_curie (str): The CURIE (compact URI) of a term.
        TODO: Improve with error handling, it currently breaks if a prefix is not defined in the prefix_map.
    """
    term_curie = None
    if prefixes is None:
        prefixes = prefix_map
    for prefix, prefix_uri in prefixes.items():
        if prefix_uri in term_uri:
            term_curie = f"{prefix}:{term_uri.replace(prefix_uri, '')}"
    return term_curie

# Initialize the LinkML schema using SchemaBuilder.
builder = SchemaBuilder(name="dcat-ap")
builder.schema.id = 'https://stroemphi.github.io/dcat-4C-ap/dcat-4nfdi-ap/dcat-ap.yaml'
builder.schema.description = description.replace('\n', '') + '\nNOTE:' + note.replace('\n', '')
builder.schema.default_prefix = 'linkmldcatap'
builder.schema.prefixes = prefix_map
builder.schema.title = 'LinkML schema representation of DCAT-AP 3.0.0'
builder.schema.license = 'CC-BY 4.0'
builder.schema.default_range = 'string'
builder.schema.imports = ['linkml:types']
builder.schema.source = 'https://semiceu.github.io/DCAT-AP/releases/3.0.0'

# Load JSON-LD of the previously and manually downloaded DCAT-AP 3.0.0 SHACL shapes.
with open('dcat-ap-SHACL.jsonld', 'r') as file:
    dcat_ap_shapes = json.load(file)

# Variable to track added slots and thus avoid duplicate errors.
added_slots = set()

# Manually defined list of used datatypes, for some of which the LinkML builtin ones can be used.
xsd_datatypes = ['dateTime', 'decimal', 'duration', 'hexBinary','nonNegativeInteger']
linkml_builtin_xsd_datatypes = {'decimal': 'xsd:decimal','datetime': 'xsd:dateTime'}

# The node shapes for rdfs:Literal and dcterms:mediaType are ignored, since we use LinkML's 'string' as default datatype
#  for unspecified literal slot ranges and dcterms:MediaType was used twice with typo, see L251-L258 in 
#  'dcat-ap-SHACL.jsonld'.
ignored_nodes =['Literal','mediaType']

# Iterate through each SHACL node shape within the loaded JSON-LD to derive the LinkML classes or types from them.
for node_shape in dcat_ap_shapes['shapes']:
    node_curie = get_curie(node_shape['sh:targetClass'])
    if node_curie == 'dcat:Resource':
        node_name = 'CataloguedResource'
    else:
        node_name = node_shape['@id'].split('#')[-1].split(':')[-1].replace('Shape', '')

    # Parse node shapes that are considered LinkML classes.
    if node_name not in xsd_datatypes + ignored_nodes:
        # Add LinkML classes
        builder.add_class(ClassDefinition(name=node_name,
                                          class_uri=node_curie))
        # Iterate through each property shape within a node shape to derive the LinkML slots from them.
        if 'sh:property' in node_shape:
            class_slots = {}
            for slot_shape in node_shape['sh:property']:
                slot_curie = get_curie(slot_shape['sh:path'])
                # Use LinkML snake_case naming convention default for slots
                slot_name = slot_shape['sh:name']['en'].replace(' ', '_')  
                # Check cardinality constraints of a slot
                required = True if 'sh:minCount' in slot_shape and int(slot_shape['sh:minCount']) == 1 else False
                multivalued = False if 'sh:maxCount' in slot_shape and int(slot_shape['sh:maxCount']) == 1 else True
                inlined_as_list = False if multivalued == False else True
                # Use the default LinkML slot range as substitute for 'rdfs:Literal'
                slot_range = 'string'  
                if 'sh:class' in slot_shape:
                    if get_curie(slot_shape['sh:class']) == 'rdfs:Resource':
                        slot_range = 'CataloguedResource'
                    elif get_curie(slot_shape['sh:class']) == 'time:Instant':
                        slot_range = 'TimeInstant'
                    else:
                        slot_range = get_curie(slot_shape['sh:class']).split(':')[-1]
                elif 'sh:datatype' in slot_shape:
                    datatype = get_curie(slot_shape['sh:datatype'])
                    for linkml_type, type_curie in linkml_builtin_xsd_datatypes.items():
                        if datatype == type_curie:
                            slot_range = linkml_type
                        else:
                            slot_range = datatype.split(':')[-1]

                # Add a generalized version of the slot to the LinkML schema, needed for later slot reuse.
                if slot_name not in added_slots:
                    general_description = 'This slot is described in more detail within the class in which it is used.'
                    builder.add_slot(SlotDefinition(name=slot_name, 
                                                    slot_uri=slot_curie, 
                                                    description=general_description))
                    added_slots.add(slot_name)
                    
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
                    description = slot_shape.get('sh:description', {}).get('en','')
                    class_slots[slot_name] = SlotDefinition(name=slot_name,
                                                            slot_uri=slot_curie,
                                                            description=description,
                                                            required=required,
                                                            range=slot_range,
                                                            multivalued=multivalued,
                                                            inlined_as_list=inlined_as_list)
                    

            builder.schema.classes[node_name].slots = sorted(list(class_slots.keys()))
            builder.schema.classes[node_name].slot_usage = {key: class_slots[key] for key in sorted(class_slots)}
                
    # Add XSD datatypes not build into LinkML as custom LinkML types.
    elif node_name in xsd_datatypes and node_curie not in linkml_builtin_xsd_datatypes.values():
        pattern, base, description = '', '', ''
        if 'nonNegativeInteger' in node_name:
            base='int'
            description='The datatype that represents non-negative integers.'
            pattern = r'([\-+]?[0-9]+)'
        elif 'duration' in node_name:
            base='str'
            description='The datatype that represents durations of time.'
            pattern =   r"""
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
                              )
                        """.replace('\n','').replace(' ','')
        elif 'hexBinary' in node_name:
            base='str'
            description='The datatype that represents arbitrary hex-encoded binary data'
            pattern = r'([0-9a-fA-F]{2})*'

        builder.add_type(TypeDefinition(name=node_name,
                                        uri=node_curie,
                                        conforms_to=f'https://www.w3.org/TR/xmlschema11-2/#{node_name}',
                                        base=base,
                                        description=description,
                                        pattern=pattern))

# sort classes, slots and types alphabetically
builder.schema.classes =  {key: builder.schema.classes[key] for key in sorted(builder.schema.classes)}
builder.schema.slots =  {key: builder.schema.slots[key] for key in sorted(builder.schema.slots)}
builder.schema.types =  {key: builder.schema.types[key] for key in sorted(builder.schema.types)}

# Dump schema to file
YAMLDumper().dump(builder.schema, 'dcat_4c_ap/schema/dcat-ap.yaml')

