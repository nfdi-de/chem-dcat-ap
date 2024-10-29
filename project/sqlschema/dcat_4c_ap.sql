-- # Class: "ChemAnalysisDataset" Description: ""
--     * Slot: id Description: 
-- # Class: "NMRSpectroscopy" Description: "Spectroscopy where the energy states of spin-active nuclei placed in a static magnetic field are interrogated by inducing transitions between the states via radio frequency irradiation. Each experiment consists of a sequence of radio frequency pulses with delay periods in between them."
--     * Slot: id Description: 
--     * Slot: type_id Description: The type of NMR Spectroscopy according provided as CURIE of a subclass of CHMO:0000613.
--     * Slot: evaluated_entity_id Description: The slot to specify the entity of interest that was evaluated.
--     * Slot: used_plan_id Description: The slot to specify the PlanSpecification (Method) that was used in the ResearchActivity.
--     * Slot: has_part_id Description: The slot to specify one or more parts of the ResearchActivity that are themselves also research activities.
-- # Class: "ChemicalReaction" Description: "An experimental procedure with the aim of producing a portion of a given compound or mixture."
--     * Slot: id Description: The slot to specify the canonical unique identifier of an entity.
--     * Slot: has_part Description: A transitive, reflexive and antisymmetric relation between a whole and itself or a whole and its part.
--     * Slot: type_id Description: The type of the EntityOfInterest provided as a DefinedTerm.
-- # Class: "ChemicalSubstance" Description: "A chemical substance that is being evaluated in a scientific process."
--     * Slot: id Description: The slot to specify the canonical unique identifier of an entity.
--     * Slot: has_part Description: A transitive, reflexive and antisymmetric relation between a whole and itself or a whole and its part.
--     * Slot: type_id Description: The type of the EntityOfInterest provided as a DefinedTerm.
-- # Class: "HardwareTool" Description: "A hardware with a certain function."
--     * Slot: id Description: 
--     * Slot: type_id Description: The type of the Tool provided as a DefinedTerm.
-- # Class: "SoftwareTool" Description: "A software with a certain function."
--     * Slot: id Description: 
--     * Slot: type_id Description: The type of the Tool provided as a DefinedTerm.
-- # Class: "Laboratory" Description: "A facility that provides controlled conditions in which scientific or technological research, experiments, and measurement may be performed."
--     * Slot: id Description: 
--     * Slot: type_id Description: The type of Environment provided as a DefinedTerm.
-- # Class: "InChIKey" Description: ""
--     * Slot: id Description: 
--     * Slot: value Description: A slot to provide the value of an attribute.
--     * Slot: type_id Description: The slot to specify the type of Attribute provided as a DefinedTerm.
-- # Class: "InChi" Description: "A structure descriptor which conforms to the InChI format specification."
--     * Slot: id Description: 
--     * Slot: value Description: A slot to provide the value of an attribute.
--     * Slot: type_id Description: The slot to specify the type of Attribute provided as a DefinedTerm.
-- # Class: "IUPACName" Description: "An IUPAC name is a systematic name which is formulated according to the rules and recommendations for chemical nomenclature set out by the International Union of Pure and Applied Chemistry (IUPAC)."
--     * Slot: id Description: 
--     * Slot: value Description: A slot to provide the value of an attribute.
--     * Slot: type_id Description: The slot to specify the type of Attribute provided as a DefinedTerm.
-- # Class: "Any" Description: ""
--     * Slot: id Description: 
-- # Class: "DefinedTerm" Description: "A word, name, acronym, phrase that is defined in a controlled vocabulary (CV) and that is used to provide the rdf:type of an entity within this schema."
--     * Slot: id Description: The slot to specify the canonical unique identifier of an entity.
--     * Slot: from_CV Description: The name of the controlled vocabulary.
-- # Class: "Dataset" Description: "A collection of data, published or curated by a single agent, and available for access or download in one or more representations."
--     * Slot: id Description: The slot to specify the canonical unique identifier of an entity.
--     * Slot: DatasetCollection_id Description: Autocreated FK slot
--     * Slot: was_generated_by_id Description: The slot to provide the ResearchActivity that created a Dataset.
-- # Class: "DatasetCollection" Description: "A curated collection of metadata about data resources."
--     * Slot: id Description: The unique identifier of a Catalog.
--     * Slot: was_generated_by_id Description: The slot to provide the ResearchActivity that created a Dataset.
-- # Class: "ResearchActivity" Description: "An activity (process) that has the objective to produce information about an entity by evaluating it."
--     * Slot: id Description: 
--     * Slot: type_id Description: The slot to specify the type of the ResearchActivity provided as a DefinedTerm.
--     * Slot: evaluated_entity_id Description: The slot to specify the entity of interest that was evaluated.
--     * Slot: used_plan_id Description: The slot to specify the PlanSpecification (Method) that was used in the ResearchActivity.
--     * Slot: has_part_id Description: The slot to specify one or more parts of the ResearchActivity that are themselves also research activities.
-- # Class: "EntityOfInterest" Description: "Something that is being evaluated in a scientific process."
--     * Slot: id Description: The slot to specify the canonical unique identifier of an entity.
--     * Slot: has_part Description: A transitive, reflexive and antisymmetric relation between a whole and itself or a whole and its part.
--     * Slot: type_id Description: The type of the EntityOfInterest provided as a DefinedTerm.
-- # Class: "Tool" Description: "A entity with a certain function used within a scientific activity."
--     * Slot: id Description: 
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: HardwareTool_id Description: Autocreated FK slot
--     * Slot: SoftwareTool_id Description: Autocreated FK slot
--     * Slot: ResearchActivity_id Description: Autocreated FK slot
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: type_id Description: The type of the Tool provided as a DefinedTerm.
-- # Class: "Environment" Description: "The environment in which the dataset creating Observation took place (e.g. a lab)."
--     * Slot: id Description: 
--     * Slot: type_id Description: The type of Environment provided as a DefinedTerm.
-- # Class: "ActivitySpecification" Description: ""A piece of information that specifies: a) how an activity has to be carried out by its agents and b) the attributes of the passive activity participants that are used by the agents in terms of their presence and magnitude.""
--     * Slot: id Description: 
--     * Slot: type_id Description: The type of PlanSpecification provided as a DefinedTerm.
-- # Class: "Attribute" Description: "A piece of information that is attributed to an entity of interest, tool or environment."
--     * Slot: id Description: 
--     * Slot: value Description: A slot to provide the value of an attribute.
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: HardwareTool_id Description: Autocreated FK slot
--     * Slot: SoftwareTool_id Description: Autocreated FK slot
--     * Slot: Laboratory_id Description: Autocreated FK slot
--     * Slot: EntityOfInterest_id Description: Autocreated FK slot
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: Environment_id Description: Autocreated FK slot
--     * Slot: type_id Description: The slot to specify the type of Attribute provided as a DefinedTerm.
-- # Class: "QuantifiableAttribute" Description: "An attribute that is quantifiable."
--     * Slot: id Description: 
--     * Slot: unit Description: 
--     * Slot: is_delta_attribute Description: This property is used to identify a Quantity instance that is a measure of a change, or interval, of some property, rather than a measure of its absolute value. This is important for measurements such as temperature differences where the conversion among units would be calculated differently because of offsets.
--     * Slot: value Description: A data property to relate an observable thing with a value of any kind.
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: HardwareTool_id Description: Autocreated FK slot
--     * Slot: SoftwareTool_id Description: Autocreated FK slot
--     * Slot: Laboratory_id Description: Autocreated FK slot
--     * Slot: EntityOfInterest_id Description: Autocreated FK slot
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: Environment_id Description: Autocreated FK slot
--     * Slot: type_id Description: The slot to specify the type of Attribute provided as a DefinedTerm.
-- # Class: "NMRSpectroscopy_name" Description: ""
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "NMRSpectroscopy_description" Description: ""
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "NMRSpectroscopy_alternative_id" Description: ""
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "ChemicalReaction_name" Description: ""
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "ChemicalReaction_description" Description: ""
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "ChemicalReaction_alternative_id" Description: ""
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "ChemicalSubstance_name" Description: ""
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "ChemicalSubstance_description" Description: ""
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "ChemicalSubstance_alternative_id" Description: ""
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "HardwareTool_name" Description: ""
--     * Slot: HardwareTool_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "HardwareTool_description" Description: ""
--     * Slot: HardwareTool_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "HardwareTool_alternative_id" Description: ""
--     * Slot: HardwareTool_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "SoftwareTool_name" Description: ""
--     * Slot: SoftwareTool_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "SoftwareTool_description" Description: ""
--     * Slot: SoftwareTool_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "SoftwareTool_alternative_id" Description: ""
--     * Slot: SoftwareTool_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "Laboratory_name" Description: ""
--     * Slot: Laboratory_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "Laboratory_description" Description: ""
--     * Slot: Laboratory_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "Laboratory_alternative_id" Description: ""
--     * Slot: Laboratory_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "InChIKey_name" Description: ""
--     * Slot: InChIKey_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "InChIKey_description" Description: ""
--     * Slot: InChIKey_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "InChIKey_alternative_id" Description: ""
--     * Slot: InChIKey_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "InChi_name" Description: ""
--     * Slot: InChi_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "InChi_description" Description: ""
--     * Slot: InChi_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "InChi_alternative_id" Description: ""
--     * Slot: InChi_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "IUPACName_name" Description: ""
--     * Slot: IUPACName_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "IUPACName_description" Description: ""
--     * Slot: IUPACName_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "IUPACName_alternative_id" Description: ""
--     * Slot: IUPACName_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "DefinedTerm_alternative_id" Description: ""
--     * Slot: DefinedTerm_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "DefinedTerm_name" Description: ""
--     * Slot: DefinedTerm_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "Dataset_name" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: name Description: The label, name or title of a Dataset.
-- # Class: "Dataset_description" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of a Dataset.
-- # Class: "Dataset_alternative_id" Description: ""
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "DatasetCollection_name" Description: ""
--     * Slot: DatasetCollection_id Description: Autocreated FK slot
--     * Slot: name Description: The name of a DatasetCollection.
-- # Class: "DatasetCollection_description" Description: ""
--     * Slot: DatasetCollection_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of a DatasetCollection.
-- # Class: "DatasetCollection_alternative_id" Description: ""
--     * Slot: DatasetCollection_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "ResearchActivity_name" Description: ""
--     * Slot: ResearchActivity_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "ResearchActivity_description" Description: ""
--     * Slot: ResearchActivity_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "ResearchActivity_alternative_id" Description: ""
--     * Slot: ResearchActivity_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "EntityOfInterest_name" Description: ""
--     * Slot: EntityOfInterest_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "EntityOfInterest_description" Description: ""
--     * Slot: EntityOfInterest_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "EntityOfInterest_alternative_id" Description: ""
--     * Slot: EntityOfInterest_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "Tool_name" Description: ""
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "Tool_description" Description: ""
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "Tool_alternative_id" Description: ""
--     * Slot: Tool_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "Environment_name" Description: ""
--     * Slot: Environment_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "Environment_description" Description: ""
--     * Slot: Environment_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "Environment_alternative_id" Description: ""
--     * Slot: Environment_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "ActivitySpecification_name" Description: ""
--     * Slot: ActivitySpecification_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "ActivitySpecification_description" Description: ""
--     * Slot: ActivitySpecification_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "Attribute_name" Description: ""
--     * Slot: Attribute_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "Attribute_description" Description: ""
--     * Slot: Attribute_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "Attribute_alternative_id" Description: ""
--     * Slot: Attribute_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.
-- # Class: "QuantifiableAttribute_name" Description: ""
--     * Slot: QuantifiableAttribute_id Description: Autocreated FK slot
--     * Slot: name Description: The slot to specify the label, name or title of a thing.
-- # Class: "QuantifiableAttribute_description" Description: ""
--     * Slot: QuantifiableAttribute_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a free-text account of a thing.
-- # Class: "QuantifiableAttribute_alternative_id" Description: ""
--     * Slot: QuantifiableAttribute_id Description: Autocreated FK slot
--     * Slot: alternative_id Description: The slot to specify the unique identifier of an entity that is not considered the canonical identifier in the given context.

CREATE TABLE "ChemAnalysisDataset" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Any" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "DefinedTerm" (
	id TEXT NOT NULL, 
	"from_CV" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ChemicalReaction" (
	id TEXT NOT NULL, 
	has_part TEXT, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "ChemicalSubstance" (
	id TEXT NOT NULL, 
	has_part TEXT, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "HardwareTool" (
	id INTEGER NOT NULL, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "SoftwareTool" (
	id INTEGER NOT NULL, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "Laboratory" (
	id INTEGER NOT NULL, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "InChIKey" (
	id INTEGER NOT NULL, 
	value TEXT, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "InChi" (
	id INTEGER NOT NULL, 
	value TEXT, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "IUPACName" (
	id INTEGER NOT NULL, 
	value TEXT, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "EntityOfInterest" (
	id TEXT NOT NULL, 
	has_part TEXT, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "Environment" (
	id INTEGER NOT NULL, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "ActivitySpecification" (
	id INTEGER NOT NULL, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "DefinedTerm_alternative_id" (
	"DefinedTerm_id" TEXT, 
	alternative_id TEXT, 
	PRIMARY KEY ("DefinedTerm_id", alternative_id), 
	FOREIGN KEY("DefinedTerm_id") REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "DefinedTerm_name" (
	"DefinedTerm_id" TEXT, 
	name TEXT, 
	PRIMARY KEY ("DefinedTerm_id", name), 
	FOREIGN KEY("DefinedTerm_id") REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "ResearchActivity" (
	id INTEGER NOT NULL, 
	type_id TEXT, 
	evaluated_entity_id TEXT, 
	used_plan_id INTEGER, 
	has_part_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id), 
	FOREIGN KEY(evaluated_entity_id) REFERENCES "EntityOfInterest" (id), 
	FOREIGN KEY(used_plan_id) REFERENCES "ActivitySpecification" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ResearchActivity" (id)
);
CREATE TABLE "ChemicalReaction_name" (
	"ChemicalReaction_id" TEXT, 
	name TEXT, 
	PRIMARY KEY ("ChemicalReaction_id", name), 
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id)
);
CREATE TABLE "ChemicalReaction_description" (
	"ChemicalReaction_id" TEXT, 
	description TEXT, 
	PRIMARY KEY ("ChemicalReaction_id", description), 
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id)
);
CREATE TABLE "ChemicalReaction_alternative_id" (
	"ChemicalReaction_id" TEXT, 
	alternative_id TEXT, 
	PRIMARY KEY ("ChemicalReaction_id", alternative_id), 
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id)
);
CREATE TABLE "ChemicalSubstance_name" (
	"ChemicalSubstance_id" TEXT, 
	name TEXT, 
	PRIMARY KEY ("ChemicalSubstance_id", name), 
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id)
);
CREATE TABLE "ChemicalSubstance_description" (
	"ChemicalSubstance_id" TEXT, 
	description TEXT, 
	PRIMARY KEY ("ChemicalSubstance_id", description), 
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id)
);
CREATE TABLE "ChemicalSubstance_alternative_id" (
	"ChemicalSubstance_id" TEXT, 
	alternative_id TEXT, 
	PRIMARY KEY ("ChemicalSubstance_id", alternative_id), 
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id)
);
CREATE TABLE "HardwareTool_name" (
	"HardwareTool_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("HardwareTool_id", name), 
	FOREIGN KEY("HardwareTool_id") REFERENCES "HardwareTool" (id)
);
CREATE TABLE "HardwareTool_description" (
	"HardwareTool_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("HardwareTool_id", description), 
	FOREIGN KEY("HardwareTool_id") REFERENCES "HardwareTool" (id)
);
CREATE TABLE "HardwareTool_alternative_id" (
	"HardwareTool_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("HardwareTool_id", alternative_id), 
	FOREIGN KEY("HardwareTool_id") REFERENCES "HardwareTool" (id)
);
CREATE TABLE "SoftwareTool_name" (
	"SoftwareTool_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("SoftwareTool_id", name), 
	FOREIGN KEY("SoftwareTool_id") REFERENCES "SoftwareTool" (id)
);
CREATE TABLE "SoftwareTool_description" (
	"SoftwareTool_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("SoftwareTool_id", description), 
	FOREIGN KEY("SoftwareTool_id") REFERENCES "SoftwareTool" (id)
);
CREATE TABLE "SoftwareTool_alternative_id" (
	"SoftwareTool_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("SoftwareTool_id", alternative_id), 
	FOREIGN KEY("SoftwareTool_id") REFERENCES "SoftwareTool" (id)
);
CREATE TABLE "Laboratory_name" (
	"Laboratory_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("Laboratory_id", name), 
	FOREIGN KEY("Laboratory_id") REFERENCES "Laboratory" (id)
);
CREATE TABLE "Laboratory_description" (
	"Laboratory_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("Laboratory_id", description), 
	FOREIGN KEY("Laboratory_id") REFERENCES "Laboratory" (id)
);
CREATE TABLE "Laboratory_alternative_id" (
	"Laboratory_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("Laboratory_id", alternative_id), 
	FOREIGN KEY("Laboratory_id") REFERENCES "Laboratory" (id)
);
CREATE TABLE "InChIKey_name" (
	"InChIKey_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("InChIKey_id", name), 
	FOREIGN KEY("InChIKey_id") REFERENCES "InChIKey" (id)
);
CREATE TABLE "InChIKey_description" (
	"InChIKey_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("InChIKey_id", description), 
	FOREIGN KEY("InChIKey_id") REFERENCES "InChIKey" (id)
);
CREATE TABLE "InChIKey_alternative_id" (
	"InChIKey_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("InChIKey_id", alternative_id), 
	FOREIGN KEY("InChIKey_id") REFERENCES "InChIKey" (id)
);
CREATE TABLE "InChi_name" (
	"InChi_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("InChi_id", name), 
	FOREIGN KEY("InChi_id") REFERENCES "InChi" (id)
);
CREATE TABLE "InChi_description" (
	"InChi_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("InChi_id", description), 
	FOREIGN KEY("InChi_id") REFERENCES "InChi" (id)
);
CREATE TABLE "InChi_alternative_id" (
	"InChi_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("InChi_id", alternative_id), 
	FOREIGN KEY("InChi_id") REFERENCES "InChi" (id)
);
CREATE TABLE "IUPACName_name" (
	"IUPACName_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("IUPACName_id", name), 
	FOREIGN KEY("IUPACName_id") REFERENCES "IUPACName" (id)
);
CREATE TABLE "IUPACName_description" (
	"IUPACName_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("IUPACName_id", description), 
	FOREIGN KEY("IUPACName_id") REFERENCES "IUPACName" (id)
);
CREATE TABLE "IUPACName_alternative_id" (
	"IUPACName_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("IUPACName_id", alternative_id), 
	FOREIGN KEY("IUPACName_id") REFERENCES "IUPACName" (id)
);
CREATE TABLE "EntityOfInterest_name" (
	"EntityOfInterest_id" TEXT, 
	name TEXT, 
	PRIMARY KEY ("EntityOfInterest_id", name), 
	FOREIGN KEY("EntityOfInterest_id") REFERENCES "EntityOfInterest" (id)
);
CREATE TABLE "EntityOfInterest_description" (
	"EntityOfInterest_id" TEXT, 
	description TEXT, 
	PRIMARY KEY ("EntityOfInterest_id", description), 
	FOREIGN KEY("EntityOfInterest_id") REFERENCES "EntityOfInterest" (id)
);
CREATE TABLE "EntityOfInterest_alternative_id" (
	"EntityOfInterest_id" TEXT, 
	alternative_id TEXT, 
	PRIMARY KEY ("EntityOfInterest_id", alternative_id), 
	FOREIGN KEY("EntityOfInterest_id") REFERENCES "EntityOfInterest" (id)
);
CREATE TABLE "Environment_name" (
	"Environment_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("Environment_id", name), 
	FOREIGN KEY("Environment_id") REFERENCES "Environment" (id)
);
CREATE TABLE "Environment_description" (
	"Environment_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("Environment_id", description), 
	FOREIGN KEY("Environment_id") REFERENCES "Environment" (id)
);
CREATE TABLE "Environment_alternative_id" (
	"Environment_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("Environment_id", alternative_id), 
	FOREIGN KEY("Environment_id") REFERENCES "Environment" (id)
);
CREATE TABLE "ActivitySpecification_name" (
	"ActivitySpecification_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("ActivitySpecification_id", name), 
	FOREIGN KEY("ActivitySpecification_id") REFERENCES "ActivitySpecification" (id)
);
CREATE TABLE "ActivitySpecification_description" (
	"ActivitySpecification_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("ActivitySpecification_id", description), 
	FOREIGN KEY("ActivitySpecification_id") REFERENCES "ActivitySpecification" (id)
);
CREATE TABLE "NMRSpectroscopy" (
	id INTEGER NOT NULL, 
	type_id TEXT, 
	evaluated_entity_id TEXT, 
	used_plan_id INTEGER, 
	has_part_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id), 
	FOREIGN KEY(evaluated_entity_id) REFERENCES "ChemicalSubstance" (id), 
	FOREIGN KEY(used_plan_id) REFERENCES "ActivitySpecification" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "ResearchActivity" (id)
);
CREATE TABLE "DatasetCollection" (
	id TEXT NOT NULL, 
	was_generated_by_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by_id) REFERENCES "ResearchActivity" (id)
);
CREATE TABLE "ResearchActivity_name" (
	"ResearchActivity_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("ResearchActivity_id", name), 
	FOREIGN KEY("ResearchActivity_id") REFERENCES "ResearchActivity" (id)
);
CREATE TABLE "ResearchActivity_description" (
	"ResearchActivity_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("ResearchActivity_id", description), 
	FOREIGN KEY("ResearchActivity_id") REFERENCES "ResearchActivity" (id)
);
CREATE TABLE "ResearchActivity_alternative_id" (
	"ResearchActivity_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("ResearchActivity_id", alternative_id), 
	FOREIGN KEY("ResearchActivity_id") REFERENCES "ResearchActivity" (id)
);
CREATE TABLE "Dataset" (
	id TEXT NOT NULL, 
	"DatasetCollection_id" TEXT, 
	was_generated_by_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DatasetCollection_id") REFERENCES "DatasetCollection" (id), 
	FOREIGN KEY(was_generated_by_id) REFERENCES "ResearchActivity" (id)
);
CREATE TABLE "Tool" (
	id INTEGER NOT NULL, 
	"NMRSpectroscopy_id" INTEGER, 
	"HardwareTool_id" INTEGER, 
	"SoftwareTool_id" INTEGER, 
	"ResearchActivity_id" INTEGER, 
	"Tool_id" INTEGER, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id), 
	FOREIGN KEY("HardwareTool_id") REFERENCES "HardwareTool" (id), 
	FOREIGN KEY("SoftwareTool_id") REFERENCES "SoftwareTool" (id), 
	FOREIGN KEY("ResearchActivity_id") REFERENCES "ResearchActivity" (id), 
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "NMRSpectroscopy_name" (
	"NMRSpectroscopy_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("NMRSpectroscopy_id", name), 
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id)
);
CREATE TABLE "NMRSpectroscopy_description" (
	"NMRSpectroscopy_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("NMRSpectroscopy_id", description), 
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id)
);
CREATE TABLE "NMRSpectroscopy_alternative_id" (
	"NMRSpectroscopy_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("NMRSpectroscopy_id", alternative_id), 
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id)
);
CREATE TABLE "DatasetCollection_name" (
	"DatasetCollection_id" TEXT, 
	name TEXT NOT NULL, 
	PRIMARY KEY ("DatasetCollection_id", name), 
	FOREIGN KEY("DatasetCollection_id") REFERENCES "DatasetCollection" (id)
);
CREATE TABLE "DatasetCollection_description" (
	"DatasetCollection_id" TEXT, 
	description TEXT NOT NULL, 
	PRIMARY KEY ("DatasetCollection_id", description), 
	FOREIGN KEY("DatasetCollection_id") REFERENCES "DatasetCollection" (id)
);
CREATE TABLE "DatasetCollection_alternative_id" (
	"DatasetCollection_id" TEXT, 
	alternative_id TEXT, 
	PRIMARY KEY ("DatasetCollection_id", alternative_id), 
	FOREIGN KEY("DatasetCollection_id") REFERENCES "DatasetCollection" (id)
);
CREATE TABLE "Attribute" (
	id INTEGER NOT NULL, 
	value TEXT, 
	"ChemicalReaction_id" TEXT, 
	"ChemicalSubstance_id" TEXT, 
	"HardwareTool_id" INTEGER, 
	"SoftwareTool_id" INTEGER, 
	"Laboratory_id" INTEGER, 
	"EntityOfInterest_id" TEXT, 
	"Tool_id" INTEGER, 
	"Environment_id" INTEGER, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id), 
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id), 
	FOREIGN KEY("HardwareTool_id") REFERENCES "HardwareTool" (id), 
	FOREIGN KEY("SoftwareTool_id") REFERENCES "SoftwareTool" (id), 
	FOREIGN KEY("Laboratory_id") REFERENCES "Laboratory" (id), 
	FOREIGN KEY("EntityOfInterest_id") REFERENCES "EntityOfInterest" (id), 
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id), 
	FOREIGN KEY("Environment_id") REFERENCES "Environment" (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "QuantifiableAttribute" (
	id INTEGER NOT NULL, 
	unit TEXT, 
	is_delta_attribute BOOLEAN, 
	value TEXT, 
	"ChemicalReaction_id" TEXT, 
	"ChemicalSubstance_id" TEXT, 
	"HardwareTool_id" INTEGER, 
	"SoftwareTool_id" INTEGER, 
	"Laboratory_id" INTEGER, 
	"EntityOfInterest_id" TEXT, 
	"Tool_id" INTEGER, 
	"Environment_id" INTEGER, 
	type_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id), 
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id), 
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id), 
	FOREIGN KEY("HardwareTool_id") REFERENCES "HardwareTool" (id), 
	FOREIGN KEY("SoftwareTool_id") REFERENCES "SoftwareTool" (id), 
	FOREIGN KEY("Laboratory_id") REFERENCES "Laboratory" (id), 
	FOREIGN KEY("EntityOfInterest_id") REFERENCES "EntityOfInterest" (id), 
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id), 
	FOREIGN KEY("Environment_id") REFERENCES "Environment" (id), 
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id)
);
CREATE TABLE "Dataset_name" (
	"Dataset_id" TEXT, 
	name TEXT NOT NULL, 
	PRIMARY KEY ("Dataset_id", name), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "Dataset_description" (
	"Dataset_id" TEXT, 
	description TEXT NOT NULL, 
	PRIMARY KEY ("Dataset_id", description), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "Dataset_alternative_id" (
	"Dataset_id" TEXT, 
	alternative_id TEXT, 
	PRIMARY KEY ("Dataset_id", alternative_id), 
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE TABLE "Tool_name" (
	"Tool_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("Tool_id", name), 
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id)
);
CREATE TABLE "Tool_description" (
	"Tool_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("Tool_id", description), 
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id)
);
CREATE TABLE "Tool_alternative_id" (
	"Tool_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("Tool_id", alternative_id), 
	FOREIGN KEY("Tool_id") REFERENCES "Tool" (id)
);
CREATE TABLE "Attribute_name" (
	"Attribute_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("Attribute_id", name), 
	FOREIGN KEY("Attribute_id") REFERENCES "Attribute" (id)
);
CREATE TABLE "Attribute_description" (
	"Attribute_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("Attribute_id", description), 
	FOREIGN KEY("Attribute_id") REFERENCES "Attribute" (id)
);
CREATE TABLE "Attribute_alternative_id" (
	"Attribute_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("Attribute_id", alternative_id), 
	FOREIGN KEY("Attribute_id") REFERENCES "Attribute" (id)
);
CREATE TABLE "QuantifiableAttribute_name" (
	"QuantifiableAttribute_id" INTEGER, 
	name TEXT, 
	PRIMARY KEY ("QuantifiableAttribute_id", name), 
	FOREIGN KEY("QuantifiableAttribute_id") REFERENCES "QuantifiableAttribute" (id)
);
CREATE TABLE "QuantifiableAttribute_description" (
	"QuantifiableAttribute_id" INTEGER, 
	description TEXT, 
	PRIMARY KEY ("QuantifiableAttribute_id", description), 
	FOREIGN KEY("QuantifiableAttribute_id") REFERENCES "QuantifiableAttribute" (id)
);
CREATE TABLE "QuantifiableAttribute_alternative_id" (
	"QuantifiableAttribute_id" INTEGER, 
	alternative_id TEXT, 
	PRIMARY KEY ("QuantifiableAttribute_id", alternative_id), 
	FOREIGN KEY("QuantifiableAttribute_id") REFERENCES "QuantifiableAttribute" (id)
);