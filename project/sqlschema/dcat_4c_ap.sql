-- # Class: SubstanceSample Description: A MaterialSample derived from a ChemicalSubstance that is of interest in an analytical procedure.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the EvaluatedEntity.
--     * Slot: description Description: The slot to provide a description for the EvaluatedEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: derived_from_id Description: The slot to specify the MaterialEntity or MaterialSample from which the MaterialSample was created.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: PolymerSample Description: A SubstanceSample derived from a Polymer.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the EvaluatedEntity.
--     * Slot: description Description: The slot to provide a description for the EvaluatedEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: derived_from_id Description: The slot to specify the MaterialEntity or MaterialSample from which the MaterialSample was created.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Laboratory Description: A facility that provides controlled conditions in which scientific or technological research, experiments, and measurement may be performed.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Activity Description: See [DCAT-AP specs:Activity](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Activity)
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: EvaluatedActivity_id Description: Autocreated FK slot
--     * Slot: EvaluatedEntity_id Description: Autocreated FK slot
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Agent Description: See [DCAT-AP specs:Agent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Agent)
--     * Slot: id
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: type_id Description: The nature of the agent.
-- # Class: AgenticEntity Description: An entity that is somehow responsible for an Activity to take place.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: AgenticEntity_id Description: Autocreated FK slot
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: Device_id Description: Autocreated FK slot
--     * Slot: EvaluatedActivity_id Description: Autocreated FK slot
--     * Slot: Software_id Description: Autocreated FK slot
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: NMRSpectrometer_id Description: Autocreated FK slot
--     * Slot: AcquisitionNucleus_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: AnalysisDataset Description: A Dataset that was generated by an analysis of some previously generated data. For example, a dataset that contains the data of an assignment of a chemical structure to a sample based on the spectral data obtained from the sample is an AnalyticalDataset.
--     * Slot: modification_date Description: The most recent date on which the Dataset was changed or modified.
--     * Slot: release_date Description: The date of formal issuance (e.g., publication) of the Dataset.
--     * Slot: spatial_resolution Description: The minimum spatial separation resolvable in a dataset, measured in meters.
--     * Slot: temporal_resolution Description: The minimum time period resolvable in the dataset.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: access_rights_id Description: Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public.
--     * Slot: frequency_id Description: The frequency at which the Dataset is updated.
--     * Slot: publisher_id Description: An entity (organisation) responsible for making the Dataset available.
-- # Class: AnalysisSourceData Description: Information that was evaluated within a DataAnalysis.
--     * Slot: title Description: The slot to provide a title for the EvaluatedEntity.
--     * Slot: description Description: The slot to provide a description for the EvaluatedEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Any Description: This abstract class is needed to create the union of Dataset, DatasetSeries, Catalogue and DataService for the range of the slot [primary_topic](https://nfdi-de.github.io/chem-dcat-ap/elements/primary_topic/).
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Class: Attribution Description: See [DCAT-AP specs:Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: Catalogue Description: See [DCAT-AP specs:Catalogue](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Catalogue)
--     * Slot: id
--     * Slot: homepage Description: A web page that acts as the main page for the Catalogue.
--     * Slot: licence Description: A licence under which the Catalogue can be used or reused.
--     * Slot: modification_date Description: The most recent date on which the Catalogue was modified.
--     * Slot: release_date Description: The date of formal issuance (e.g., publication) of the Catalogue.
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: creator_id Description: An entity responsible for the creation of the catalogue.
--     * Slot: publisher_id Description: An entity (organisation) responsible for making the Catalogue available.
--     * Slot: rights_id Description: A statement that specifies rights associated with the Catalogue.
-- # Class: CatalogueRecord Description: See [DCAT-AP specs:CatalogueRecord](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#CatalogueRecord)
--     * Slot: id
--     * Slot: listing_date Description: The date on which the description of the Resource was included in the Catalogue.
--     * Slot: modification_date Description: The most recent date on which the Catalogue entry was changed or modified.
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: change_type_id Description: The status of the catalogue record in the context of editorial flow of the dataset and data service descriptions.
--     * Slot: primary_topic_id Description: A link to the Dataset, Data service or Catalog described in the record.
--     * Slot: source_metadata_id Description: The original metadata that was used in creating metadata for the Dataset, Data Service or Dataset Series.
-- # Class: Checksum Description: See [DCAT-AP specs:Checksum](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Checksum)
--     * Slot: id
--     * Slot: checksum_value Description: A lower case hexadecimal encoded digest value produced using a specific algorithm.
--     * Slot: algorithm_id Description: The algorithm used to produce the subject Checksum.
-- # Class: ChecksumAlgorithm Description: See [DCAT-AP specs:ChecksumAlgorithm](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ChecksumAlgorithm)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Abstract Class: ClassifierMixin Description: A mixin with which an entity of this schema can be classified via an additional rdf:type or dcterms:type assertion.
--     * Slot: id
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Concept Description: See [DCAT-AP specs:Concept](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Concept)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: LicenseDocument_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: ConceptScheme Description: See [DCAT-AP specs:ConceptScheme](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ConceptScheme)
--     * Slot: id
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: Catalogue_id Description: Autocreated FK slot
-- # Class: DataAnalysis Description: An Activity that evaluates the data produced by another Activity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: realized_plan_id Description: The slot to specify the Plan (i.e. directive information or procedure) that was realized by an Activity.
--     * Slot: occurred_in_id Description: The slot to specify the Surrounding in which an Activity took place.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: DataGeneratingActivity Description: An Activity (process) that has the objective to produce information (in form of a dataset) about another Activity or Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: AnalysisSourceData_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: realized_plan_id Description: The slot to specify the Plan (i.e. directive information or procedure) that was realized by an Activity.
--     * Slot: occurred_in_id Description: The slot to specify the Surrounding in which an Activity took place.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: DataService Description: See [DCAT-AP specs:DataService](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DataService)
--     * Slot: id
--     * Slot: licence Description: A licence under which the Data service is made available.
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: access_rights_id Description: Information regarding access or restrictions based on privacy, security, or other policies.
--     * Slot: publisher_id Description: An entity (organisation) responsible for making the Data Service available.
-- # Class: Dataset Description: A collection of data, published or curated by a single agent, and available for access or download in one or more representations.
--     * Slot: modification_date Description: The most recent date on which the Dataset was changed or modified.
--     * Slot: release_date Description: The date of formal issuance (e.g., publication) of the Dataset.
--     * Slot: spatial_resolution Description: The minimum spatial separation resolvable in a dataset, measured in meters.
--     * Slot: temporal_resolution Description: The minimum time period resolvable in the dataset.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: access_rights_id Description: Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public.
--     * Slot: frequency_id Description: The frequency at which the Dataset is updated.
--     * Slot: publisher_id Description: An entity (organisation) responsible for making the Dataset available.
-- # Class: DatasetSeries Description: See [DCAT-AP specs:DatasetSeries](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DatasetSeries)
--     * Slot: id
--     * Slot: modification_date Description: The most recent date on which the Dataset Series was changed or modified.
--     * Slot: release_date Description: The date of formal issuance (e.g., publication) of the Dataset Series.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: frequency_id Description: The frequency at which the Dataset Series is updated.
--     * Slot: publisher_id Description: An entity (organisation) responsible for ensuring the coherency of the Dataset Series
-- # Class: DefinedTerm Description: A word, name, acronym or phrase that is defined in a controlled vocabulary (CV) and that is used to provide an additional rdf:type or dcterms:type of a class within this schema.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: from_CV Description: The URL of the controlled vocabulary.
-- # Class: Device Description: A material instrument that is designed to perform a function primarily by means of its mechanical or electrical nature.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: Device_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: NMRSpectrometer_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Distribution Description: See [DCAT-AP specs:Distribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution)
--     * Slot: id
--     * Slot: byte_size Description: The size of a Distribution in bytes.
--     * Slot: licence Description: A licence under which the Distribution is made available.
--     * Slot: modification_date Description: The most recent date on which the Distribution was changed or modified.
--     * Slot: release_date Description: The date of formal issuance (e.g., publication) of the Distribution.
--     * Slot: spatial_resolution Description: The minimum spatial separation resolvable in a dataset distribution, measured in meters.
--     * Slot: temporal_resolution Description: The minimum time period resolvable in the dataset distribution.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: availability_id Description: An indication how long it is planned to keep the Distribution of the Dataset available.
--     * Slot: checksum_id Description: A mechanism that can be used to verify that the contents of a distribution have not changed.
--     * Slot: compression_format_id Description: The format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.
--     * Slot: format_id Description: The file format of the Distribution.
--     * Slot: has_policy_id Description: The policy expressing the rights associated with the distribution if using the [[ODRL]] vocabulary.
--     * Slot: media_type_id Description: The media type of the Distribution as defined in the official register of media types managed by IANA.
--     * Slot: packaging_format_id Description: The format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.
--     * Slot: rights_id Description: A statement that specifies rights associated with the Distribution.
--     * Slot: status_id Description: The status of the distribution in the context of maturity lifecycle.
-- # Class: Document Description: See [DCAT-AP specs:Document](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Document)
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: Entity Description: A physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: AnalysisSourceData_id Description: Autocreated FK slot
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: Entity_id Description: Autocreated FK slot
--     * Slot: EvaluatedActivity_id Description: Autocreated FK slot
--     * Slot: EvaluatedEntity_id Description: Autocreated FK slot
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: NMRSpectrum_id Description: Autocreated FK slot
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: EvaluatedActivity Description: An activity or proces that is being evaluated in a DataGeneratingActivity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: EvaluatedEntity Description: An Entity that is being evaluated in a DataGeneratingActivity.
--     * Slot: title Description: The slot to provide a title for the EvaluatedEntity.
--     * Slot: description Description: The slot to provide a description for the EvaluatedEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Frequency Description: See [DCAT-AP specs:Frequency](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Frequency)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Class: Geometry Description: See [DCAT-AP specs:Geometry](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Geometry)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Class: Identifier Description: See [DCAT-AP specs:Identifier](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Identifier)
--     * Slot: id
--     * Slot: notation Description: A string that is an identifier in the context of the identifier scheme referenced by its datatype.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: AgenticEntity_id Description: Autocreated FK slot
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: AnalysisSourceData_id Description: Autocreated FK slot
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: Device_id Description: Autocreated FK slot
--     * Slot: Entity_id Description: Autocreated FK slot
--     * Slot: EvaluatedActivity_id Description: Autocreated FK slot
--     * Slot: EvaluatedEntity_id Description: Autocreated FK slot
--     * Slot: Software_id Description: Autocreated FK slot
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: NMRSpectrum_id Description: Autocreated FK slot
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: NMRSpectrometer_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: AcquisitionNucleus_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
-- # Class: Kind Description: See [DCAT-AP specs:Kind](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Kind)
--     * Slot: id
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: LegalResource Description: See [DCAT-AP specs:LegalResource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LegalResource)
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: LicenseDocument Description: See [DCAT-AP specs:LicenseDocument](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LicenseDocument)
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Class: LinguisticSystem Description: See [DCAT-AP specs:LinguisticSystem](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LinguisticSystem)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: CatalogueRecord_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: Location Description: See [DCAT-AP specs:Location](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Location)
--     * Slot: id
--     * Slot: bbox Description: The geographic bounding box of a resource.
--     * Slot: centroid Description: The geographic center (centroid) of a resource.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: geometry_id Description: The corresponding geometry for a resource.
-- # Class: MediaType Description: See [DCAT-AP specs:MediaType](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaType)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Class: MediaTypeOrExtent Description: See [DCAT-AP specs:MediaTypeOrExtent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaTypeOrExtent)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: DataService_id Description: Autocreated FK slot
-- # Class: PeriodOfTime Description: See [DCAT-AP specs:PeriodOfTime](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#PeriodOfTime)
--     * Slot: id
--     * Slot: end_date Description: The end of the period.
--     * Slot: start_date Description: The start of the period.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: beginning_id Description: The beginning of a period or interval.
--     * Slot: end_id Description: The end of a period or interval.
-- # Class: Plan Description: A piece of information that specifies how an activity has to be carried out by its agents including what kind of steps have to be taken and what kind of parameters have to be met/set.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Policy Description: See [DCAT-AP specs:Policy](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Policy)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Class: ProvenanceStatement Description: See [DCAT-AP specs:ProvenanceStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ProvenanceStatement)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: QualitativeAttribute Description: A piece of information that is attributed to an Entity, Activity or AgenticEntity.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QualitativeAttribute.
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: AgenticEntity_id Description: Autocreated FK slot
--     * Slot: AnalysisSourceData_id Description: Autocreated FK slot
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: Device_id Description: Autocreated FK slot
--     * Slot: Entity_id Description: Autocreated FK slot
--     * Slot: EvaluatedActivity_id Description: Autocreated FK slot
--     * Slot: EvaluatedEntity_id Description: Autocreated FK slot
--     * Slot: Software_id Description: Autocreated FK slot
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: NMRSpectrum_id Description: Autocreated FK slot
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: NMRSpectrometer_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: AcquisitionNucleus_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: QuantitativeAttribute Description: A quantifiable piece of information that is attributed to an Entity, Activity or AgenticEntity.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: AgenticEntity_id Description: Autocreated FK slot
--     * Slot: AnalysisSourceData_id Description: Autocreated FK slot
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: Device_id Description: Autocreated FK slot
--     * Slot: Entity_id Description: Autocreated FK slot
--     * Slot: EvaluatedActivity_id Description: Autocreated FK slot
--     * Slot: EvaluatedEntity_id Description: Autocreated FK slot
--     * Slot: Software_id Description: Autocreated FK slot
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: NMRSpectrum_id Description: Autocreated FK slot
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: NMRSpectrometer_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: AcquisitionNucleus_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Relationship Description: See [DCAT-AP specs:Relationship](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Relationship)
--     * Slot: id
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: Resource Description: See [DCAT-AP specs:Resource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Resource)
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: Relationship_id Description: Autocreated FK slot
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: RightsStatement Description: See [DCAT-AP specs:RightsStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#RightsStatement)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Class: Role Description: See [DCAT-AP specs:Role](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Role)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: Relationship_id Description: Autocreated FK slot
-- # Class: Software Description: An instrument composed of a series of instructions that can be interpreted by or directly executed by a computer.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: Software_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Standard Description: See [DCAT-AP specs:Standard](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Standard)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: CatalogueRecord_id Description: Autocreated FK slot
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
-- # Class: SupportiveEntity Description: The supportive entities are supporting the main entities in the Application Profile. They are included in the Application Profile because they form the range of properties.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Class: Surrounding Description: The surrounding in which the dataset creating activity took place (e.g. a lab).
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: TimeInstant Description: See [DCAT-AP specs:TimeInstant](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TimeInstant)
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
-- # Class: ChemicalEntity Description: Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Atom Description: A MaterialEntity constituting the smallest component of an element having the chemical properties of the element.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to provide the Atom as a ChEBI ID from the atom (CHEBI:33250) branch.
-- # Class: MolarMass Description: A Mass (physical quality) that quantifies the mass of a homogeneous ChemicalSubstance containing 6.02 x 10^23 atoms or molecules.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: InChIKey
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QualitativeAttribute.
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: InChi Description: A structure descriptor which conforms to the InChI format specification.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QualitativeAttribute.
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: MolecularFormula Description: A structure descriptor which identifies each constituent element by its chemical symbol and indicates the number of atoms of each element found in each discrete molecule of that compound.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QualitativeAttribute.
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: IUPACName Description: A systematic name which is formulated according to the rules and recommendations for chemical nomenclature set out by the International Union of Pure and Applied Chemistry (IUPAC).
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QualitativeAttribute.
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: SMILES Description: A structure descriptor that denotes a molecular structure as a graph and conforms to the SMILES format specification.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QualitativeAttribute.
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: ChemicalSubstance Description: A MaterialEntity of constant composition, composed of chemical entities of the same type or of different types.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Polymer Description: A ChemicalSubstance that is composed of macromolecules of different kinds and which may be differentiated by composition, length, degree of branching etc..
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Concentration Description: A QuantitativeAttribute of a ChemicalSubstance that represents the amount of a constituent divided by the volume of the mixture.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: AmountOfSubstance Description: The total amount of substance used in a ChemicalReaction.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: PHValue
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: ChemicalReaction Description: A process that leads to the transformation of one set of chemical substances to another.
--     * Slot: has_duration Description: A slot to provide the duration of a ChemicalReaction.
--     * Slot: has_reaction_step Description: A slot to specify a step (part) of a ChemicalReaction that is itself a ChemicalReaction.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: StartingMaterial Description: A ChemicalSubstance with that has a starting material role in a synthesis.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: DissolvingSubstance Description: A liquid ChemicalSubstance that dissolves or that is capable of dissolving a ChemicalSubstance.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Reagent Description: A ChemicalSubstance that is consumed or transformed in a ChemicalReaction.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: ChemicalProduct Description: A chemical substance that is produced by a ChemicalReaction.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Catalyst Description: A ChemicalSubstance or MaterialEntity that initiates or accelerates a ChemicalReaction without itself being affected.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Reactor Description: A reactor is a container for controlling a biological or chemical reaction or process.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Yield Description: A dimensionless physical quantity describing the fraction of a product B that is formed from a reactant A taking into account the stoichiometry. If A fully reacts to B without side-reactions, the yield of product B is 1 (or 100 %).
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: MolarEquivalent Description: A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a reference substance in a chemical reaction.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: PercentageOfTotal Description: A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a reference substance in a chemical reaction.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Materialistic Description: A LinkML mixin used to pass down properties common to all material entities. It is needed for example to have MaterialSample have the same properties as MaterialEntity, although it is defined as a subclass of EvaluatedEntity.
--     * Slot: id
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
-- # Class: MaterialEntity Description: A material is an Entity that has some portion of matter as proper part.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: MaterialSample Description: A Sample that was derived from a previous MaterialSample or some other kind of MaterialEntity.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the EvaluatedEntity.
--     * Slot: description Description: The slot to provide a description for the EvaluatedEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: derived_from_id Description: The slot to specify the MaterialEntity or MaterialSample from which the MaterialSample was created.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Temperature Description: A physical quantity that quantitatively expresses the attribute of hotness or coldness.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: Materialistic_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Mass Description: The strength of a body's gravitational attraction to other bodies.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: Materialistic_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Volume Description: A measure of regions in three-dimensional space.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: Materialistic_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Density Description: A measure of the mass per unit volume of a substance.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: Materialistic_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Pressure
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: SubstanceSample_id Description: Autocreated FK slot
--     * Slot: PolymerSample_id Description: Autocreated FK slot
--     * Slot: ChemicalEntity_id Description: Autocreated FK slot
--     * Slot: Atom_id Description: Autocreated FK slot
--     * Slot: ChemicalSubstance_id Description: Autocreated FK slot
--     * Slot: Polymer_id Description: Autocreated FK slot
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: StartingMaterial_id Description: Autocreated FK slot
--     * Slot: DissolvingSubstance_id Description: Autocreated FK slot
--     * Slot: Reagent_id Description: Autocreated FK slot
--     * Slot: ChemicalProduct_id Description: Autocreated FK slot
--     * Slot: Catalyst_id Description: Autocreated FK slot
--     * Slot: Reactor_id Description: Autocreated FK slot
--     * Slot: Materialistic_id Description: Autocreated FK slot
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: MaterialSample_id Description: Autocreated FK slot
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: CharacterizedCompound_id Description: Autocreated FK slot
--     * Slot: NMRSolvent_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: NMRSample Description: A SubstanceSample that has been prepared for chemical analysis by NMR.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the EvaluatedEntity.
--     * Slot: description Description: The slot to provide a description for the EvaluatedEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: derived_from_id Description: The slot to specify the MaterialEntity or MaterialSample from which the NMRSample was created.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: NMRSampleTemperature Description: The temperature of the NMR Sample.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: NMRAnalysisDataset Description: A dataset that is the result of a NMRSpectralAnalysis of a NMRSample.
--     * Slot: modification_date Description: The most recent date on which the Dataset was changed or modified.
--     * Slot: release_date Description: The date of formal issuance (e.g., publication) of the Dataset.
--     * Slot: spatial_resolution Description: The minimum spatial separation resolvable in a dataset, measured in meters.
--     * Slot: temporal_resolution Description: The minimum time period resolvable in the dataset.
--     * Slot: version Description: The version indicator (name or identifier) of a resource.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: access_rights_id Description: Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public.
--     * Slot: frequency_id Description: The frequency at which the Dataset is updated.
--     * Slot: publisher_id Description: An entity (organisation) responsible for making the Dataset available.
-- # Class: NMRSpectralAnalysis Description: A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectrum generated by a NMRSpectroscopy
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: realized_plan_id Description: The slot to specify the Plan (i.e. directive information or procedure) that was realized by an Activity.
--     * Slot: occurred_in_id Description: The slot to specify the Surrounding in which an Activity took place.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: NMRSpectrum Description: Chemical shift data obtained via nuclear magnetic resonance (NMR) spectroscopy.
--     * Slot: title Description: The slot to provide a title for the EvaluatedEntity.
--     * Slot: description Description: The slot to provide a description for the EvaluatedEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: NMRSpectroscopy Description: Spectroscopy where the energy states of spin-active nuclei placed in a static magnetic field are interrogated by inducing transitions between the states via radio frequency irradiation. Each experiment consists of a sequence of radio frequency pulses with delay periods in between them.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: NMRSpectrum_id Description: Autocreated FK slot
--     * Slot: used_pulse_sequence_id Description: The slot to specify the PulseSequence used as a setting in the NMRSpectroscopy.
--     * Slot: used_number_of_scans_id Description: The slot to specify the NumberOfScans used as a setting in the NMRSpectroscopy.
--     * Slot: used_sample_temperature_id Description: The slot to specify the NMRSampleTemperature used as a setting in the NMRSpectroscopy.
--     * Slot: realized_plan_id Description: The slot to specify the Plan (i.e. directive information or procedure) that was realized by an Activity.
--     * Slot: occurred_in_id Description: The slot to specify the Surrounding in which an Activity took place.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The type of NMRSpectroscopy provided as CURIE of a subclass of CHMO:0000613.
-- # Class: NMRSpectrometer Description: A Spectrometer used to conduct NMR experiments consisting of a magnet housing a sample space surrounded by two coils which act to transmit radio frequency radiation to the sample and to detect the response of the sample.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: ShiftCalibrationCompound Description: A ChemicalEntity that produces one or more peaks used for chemical shift calibration in nuclear magnetic resonance (NMR) spectroscopy.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: ShiftReferenceCompound Description: A ShiftCalibrationCompound that produces a peak used as reference frequency in the delta chemical shift scale in nuclear magnetic resonance (NMR) spectroscopy.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: CharacterizedCompound Description: A ChemicalEntity that being characterized in an NMRSample using data acquired from a NMRSpectroscopy.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: NMRSample_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: AcquisitionNucleus Description: The nucleus of an Atom that is being studied during an NMR analysis.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: nucleus_of_id Description: The slot to specify the Atom that is being studied during an NMR analysis
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: NMRSolvent Description: A DissolvingSubstance that is used in nuclear magnetic resonance NMRSpectroscopy.
--     * Slot: alternative_label Description: The slot to specify an alternative label, name or title for a MaterialEntity.
--     * Slot: has_physical_state Description: The slot to specify the physical state of a MaterialEntity.
--     * Slot: id Description: A slot to provide an URI for an entity within this schema.
--     * Slot: title Description: The slot to provide a title for the Entity.
--     * Slot: description Description: The slot to provide a description for the Entity.
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: PulseSequence Description: A string that denotes sequence of excitation pulses.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QualitativeAttribute.
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: NominalProtonFrequency Description: Resonance frequency of 1H at the field strength of the NMR magnet, rounded to 10-fold numbers.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: NMRSpectrometer_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: CalibrationPeakShift Description: The chemical shift of the peak used for chemical shift calibration.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: ShiftCalibrationCompound_id Description: Autocreated FK slot
--     * Slot: ShiftReferenceCompound_id Description: Autocreated FK slot
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: NumberOfScans Description: The number of repeat scans performed and summed to create the data set for an NMRSample.
--     * Slot: id
--     * Slot: title Description: This slot is described in more detail within the class in which it is used.
--     * Slot: description Description: This slot is described in more detail within the class in which it is used.
--     * Slot: value Description: The slot to provide the literal value of the QuantitativeAttribute.
--     * Slot: has_quantity_type Description: The type of quality that is quantifiable according to the QUDT ontology.
--     * Slot: unit
--     * Slot: type_id Description: This slot is described in more detail within the class in which it is used.
--     * Slot: rdf_type_id Description: The slot to specify the ontology class that is instantiated by an entity.
-- # Class: Activity_title
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: title Description: The slot to provide a title for the Activity.
-- # Class: Activity_description
--     * Slot: Activity_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a description for the Activity.
-- # Class: Agent_name
--     * Slot: Agent_id Description: Autocreated FK slot
--     * Slot: name Description: A name of the agent.
-- # Class: AnalysisDataset_description
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the Dataset.
-- # Class: AnalysisDataset_identifier
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: identifier Description: The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue.
-- # Class: AnalysisDataset_keyword
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the Dataset.
-- # Class: AnalysisDataset_title
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the Dataset.
-- # Class: AnalysisDataset_version_notes
--     * Slot: AnalysisDataset_id Description: Autocreated FK slot
--     * Slot: version_notes Description: A description of the differences between this version and a previous version of the Dataset.
-- # Class: Catalogue_description
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the Catalogue.
-- # Class: Catalogue_title
--     * Slot: Catalogue_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the Catalogue.
-- # Class: CatalogueRecord_description
--     * Slot: CatalogueRecord_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the record. This property can be repeated for parallel language versions of the description.
-- # Class: CatalogueRecord_title
--     * Slot: CatalogueRecord_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the Catalogue Record.
-- # Class: Concept_preferred_label
--     * Slot: Concept_id Description: Autocreated FK slot
--     * Slot: preferred_label Description: A preferred label of the concept.
-- # Class: ConceptScheme_title
--     * Slot: ConceptScheme_id Description: Autocreated FK slot
--     * Slot: title Description: A name of the concept scheme.
-- # Class: DataAnalysis_title
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: title Description: The slot to provide a title for the Activity.
-- # Class: DataAnalysis_description
--     * Slot: DataAnalysis_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a description for the Activity.
-- # Class: DataGeneratingActivity_title
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: title Description: The slot to provide a title for the Activity.
-- # Class: DataGeneratingActivity_description
--     * Slot: DataGeneratingActivity_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a description for the Activity.
-- # Class: DataService_description
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the Data Service.
-- # Class: DataService_keyword
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the Data Service.
-- # Class: DataService_title
--     * Slot: DataService_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the Data Service.
-- # Class: Dataset_description
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the Dataset.
-- # Class: Dataset_identifier
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: identifier Description: The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue.
-- # Class: Dataset_keyword
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the Dataset.
-- # Class: Dataset_title
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the Dataset.
-- # Class: Dataset_version_notes
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: version_notes Description: A description of the differences between this version and a previous version of the Dataset.
-- # Class: DatasetSeries_description
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the Dataset Series.
-- # Class: DatasetSeries_title
--     * Slot: DatasetSeries_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the Dataset Series.
-- # Class: Distribution_description
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the Distribution.
-- # Class: Distribution_title
--     * Slot: Distribution_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the Distribution.
-- # Class: EvaluatedActivity_title
--     * Slot: EvaluatedActivity_id Description: Autocreated FK slot
--     * Slot: title Description: The slot to provide a title for the Activity.
-- # Class: EvaluatedActivity_description
--     * Slot: EvaluatedActivity_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a description for the Activity.
-- # Class: ChemicalReaction_title
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: title Description: The slot to provide a title for the Activity.
-- # Class: ChemicalReaction_description
--     * Slot: ChemicalReaction_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a description for the Activity.
-- # Class: NMRAnalysisDataset_description
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: description Description: A free-text account of the Dataset.
-- # Class: NMRAnalysisDataset_identifier
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: identifier Description: The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue.
-- # Class: NMRAnalysisDataset_keyword
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: keyword Description: A keyword or tag describing the Dataset.
-- # Class: NMRAnalysisDataset_title
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: title Description: A name given to the Dataset.
-- # Class: NMRAnalysisDataset_version_notes
--     * Slot: NMRAnalysisDataset_id Description: Autocreated FK slot
--     * Slot: version_notes Description: A description of the differences between this version and a previous version of the Dataset.
-- # Class: NMRSpectralAnalysis_title
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: title Description: The slot to provide a title for the Activity.
-- # Class: NMRSpectralAnalysis_description
--     * Slot: NMRSpectralAnalysis_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a description for the Activity.
-- # Class: NMRSpectroscopy_title
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: title Description: The slot to provide a title for the Activity.
-- # Class: NMRSpectroscopy_description
--     * Slot: NMRSpectroscopy_id Description: Autocreated FK slot
--     * Slot: description Description: The slot to provide a description for the Activity.

CREATE TABLE "SubstanceSample" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	derived_from_id TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(derived_from_id) REFERENCES "Entity" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_SubstanceSample_id" ON "SubstanceSample" (id);
CREATE TABLE "PolymerSample" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	derived_from_id TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(derived_from_id) REFERENCES "Entity" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_PolymerSample_id" ON "PolymerSample" (id);
CREATE TABLE "Activity" (
	id TEXT NOT NULL,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"Activity_id" TEXT,
	"DataAnalysis_id" TEXT,
	"DataGeneratingActivity_id" TEXT,
	"EvaluatedActivity_id" TEXT,
	"EvaluatedEntity_id" TEXT,
	"ChemicalReaction_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRSpectralAnalysis_id" TEXT,
	"NMRSpectroscopy_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id),
	FOREIGN KEY("EvaluatedActivity_id") REFERENCES "EvaluatedActivity" (id),
	FOREIGN KEY("EvaluatedEntity_id") REFERENCES "EvaluatedEntity" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Activity_id" ON "Activity" (id);
CREATE TABLE "Agent" (
	id INTEGER NOT NULL,
	"AnalysisDataset_id" TEXT,
	"Dataset_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	type_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY(type_id) REFERENCES "Concept" (id)
);CREATE INDEX "ix_Agent_id" ON "Agent" (id);
CREATE TABLE "AnalysisDataset" (
	modification_date DATE,
	release_date DATE,
	spatial_resolution INTEGER,
	temporal_resolution TEXT,
	version TEXT,
	id TEXT NOT NULL,
	access_rights_id INTEGER,
	frequency_id INTEGER,
	publisher_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(access_rights_id) REFERENCES "RightsStatement" (id),
	FOREIGN KEY(frequency_id) REFERENCES "Frequency" (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id)
);CREATE INDEX "ix_AnalysisDataset_id" ON "AnalysisDataset" (id);
CREATE TABLE "Any" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Any_id" ON "Any" (id);
CREATE TABLE "Catalogue" (
	id INTEGER NOT NULL,
	homepage TEXT,
	licence TEXT,
	modification_date DATE,
	release_date DATE,
	"Catalogue_id" INTEGER,
	creator_id INTEGER,
	publisher_id INTEGER NOT NULL,
	rights_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(homepage) REFERENCES "Document" (id),
	FOREIGN KEY(licence) REFERENCES "LicenseDocument" (id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY(creator_id) REFERENCES "Agent" (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id),
	FOREIGN KEY(rights_id) REFERENCES "RightsStatement" (id)
);CREATE INDEX "ix_Catalogue_id" ON "Catalogue" (id);
CREATE TABLE "ChecksumAlgorithm" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ChecksumAlgorithm_id" ON "ChecksumAlgorithm" (id);
CREATE TABLE "Concept" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	"AnalysisDataset_id" TEXT,
	"DataService_id" INTEGER,
	"Dataset_id" TEXT,
	"LicenseDocument_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("LicenseDocument_id") REFERENCES "LicenseDocument" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_Concept_id" ON "Concept" (id);
CREATE TABLE "DataService" (
	id INTEGER NOT NULL,
	licence TEXT,
	"Catalogue_id" INTEGER,
	"Distribution_id" INTEGER,
	access_rights_id INTEGER,
	publisher_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(licence) REFERENCES "LicenseDocument" (id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY(access_rights_id) REFERENCES "RightsStatement" (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id)
);CREATE INDEX "ix_DataService_id" ON "DataService" (id);
CREATE TABLE "Dataset" (
	modification_date DATE,
	release_date DATE,
	spatial_resolution INTEGER,
	temporal_resolution TEXT,
	version TEXT,
	id TEXT NOT NULL,
	"AnalysisDataset_id" TEXT,
	"Catalogue_id" INTEGER,
	"DataService_id" INTEGER,
	"Dataset_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	access_rights_id INTEGER,
	frequency_id INTEGER,
	publisher_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY(access_rights_id) REFERENCES "RightsStatement" (id),
	FOREIGN KEY(frequency_id) REFERENCES "Frequency" (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id)
);CREATE INDEX "ix_Dataset_id" ON "Dataset" (id);
CREATE TABLE "DefinedTerm" (
	id TEXT NOT NULL,
	title TEXT,
	"from_CV" TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_DefinedTerm_id" ON "DefinedTerm" (id);
CREATE TABLE "Distribution" (
	id INTEGER NOT NULL,
	byte_size INTEGER,
	licence TEXT,
	modification_date DATE,
	release_date DATE,
	spatial_resolution INTEGER,
	temporal_resolution TEXT,
	"AnalysisDataset_id" TEXT,
	"Dataset_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	availability_id INTEGER,
	checksum_id INTEGER,
	compression_format_id INTEGER,
	format_id INTEGER,
	has_policy_id INTEGER,
	media_type_id INTEGER,
	packaging_format_id INTEGER,
	rights_id INTEGER,
	status_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(licence) REFERENCES "LicenseDocument" (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY(availability_id) REFERENCES "Concept" (id),
	FOREIGN KEY(checksum_id) REFERENCES "Checksum" (id),
	FOREIGN KEY(compression_format_id) REFERENCES "MediaType" (id),
	FOREIGN KEY(format_id) REFERENCES "MediaTypeOrExtent" (id),
	FOREIGN KEY(has_policy_id) REFERENCES "Policy" (id),
	FOREIGN KEY(media_type_id) REFERENCES "MediaType" (id),
	FOREIGN KEY(packaging_format_id) REFERENCES "MediaType" (id),
	FOREIGN KEY(rights_id) REFERENCES "RightsStatement" (id),
	FOREIGN KEY(status_id) REFERENCES "Concept" (id)
);CREATE INDEX "ix_Distribution_id" ON "Distribution" (id);
CREATE TABLE "Document" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AnalysisDataset_id" TEXT,
	"DataService_id" INTEGER,
	"Dataset_id" TEXT,
	"Distribution_id" INTEGER,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_Document_id" ON "Document" (id);
CREATE TABLE "Entity" (
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"Activity_id" TEXT,
	"AnalysisSourceData_id" TEXT,
	"DataAnalysis_id" TEXT,
	"DataGeneratingActivity_id" TEXT,
	"Entity_id" TEXT,
	"EvaluatedActivity_id" TEXT,
	"EvaluatedEntity_id" TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"ChemicalReaction_id" TEXT,
	"StartingMaterial_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"MaterialEntity_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRSpectralAnalysis_id" TEXT,
	"NMRSpectrum_id" TEXT,
	"NMRSpectroscopy_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY("AnalysisSourceData_id") REFERENCES "AnalysisSourceData" (id),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id),
	FOREIGN KEY("Entity_id") REFERENCES "Entity" (id),
	FOREIGN KEY("EvaluatedActivity_id") REFERENCES "EvaluatedActivity" (id),
	FOREIGN KEY("EvaluatedEntity_id") REFERENCES "EvaluatedEntity" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id),
	FOREIGN KEY("NMRSpectrum_id") REFERENCES "NMRSpectrum" (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Entity_id" ON "Entity" (id);
CREATE TABLE "Frequency" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Frequency_id" ON "Frequency" (id);
CREATE TABLE "Geometry" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Geometry_id" ON "Geometry" (id);
CREATE TABLE "LicenseDocument" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_LicenseDocument_id" ON "LicenseDocument" (id);
CREATE TABLE "MediaType" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_MediaType_id" ON "MediaType" (id);
CREATE TABLE "MediaTypeOrExtent" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	"DataService_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);CREATE INDEX "ix_MediaTypeOrExtent_id" ON "MediaTypeOrExtent" (id);
CREATE TABLE "Policy" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Policy_id" ON "Policy" (id);
CREATE TABLE "RightsStatement" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_RightsStatement_id" ON "RightsStatement" (id);
CREATE TABLE "SupportiveEntity" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_SupportiveEntity_id" ON "SupportiveEntity" (id);
CREATE TABLE "TimeInstant" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TimeInstant_id" ON "TimeInstant" (id);
CREATE TABLE "ChemicalEntity" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_ChemicalEntity_id" ON "ChemicalEntity" (id);
CREATE TABLE "Materialistic" (
	id INTEGER NOT NULL,
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	PRIMARY KEY (id)
);CREATE INDEX "ix_Materialistic_id" ON "Materialistic" (id);
CREATE TABLE "MaterialEntity" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"MaterialEntity_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_MaterialEntity_id" ON "MaterialEntity" (id);
CREATE TABLE "MaterialSample" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	derived_from_id TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(derived_from_id) REFERENCES "Entity" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_MaterialSample_id" ON "MaterialSample" (id);
CREATE TABLE "NMRSample" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"NMRAnalysisDataset_id" TEXT,
	"NMRSpectroscopy_id" TEXT,
	derived_from_id TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY(derived_from_id) REFERENCES "Entity" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_NMRSample_id" ON "NMRSample" (id);
CREATE TABLE "NMRAnalysisDataset" (
	modification_date DATE,
	release_date DATE,
	spatial_resolution INTEGER,
	temporal_resolution TEXT,
	version TEXT,
	id TEXT NOT NULL,
	access_rights_id INTEGER,
	frequency_id INTEGER,
	publisher_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(access_rights_id) REFERENCES "RightsStatement" (id),
	FOREIGN KEY(frequency_id) REFERENCES "Frequency" (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id)
);CREATE INDEX "ix_NMRAnalysisDataset_id" ON "NMRAnalysisDataset" (id);
CREATE TABLE "CharacterizedCompound" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"NMRSample_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_CharacterizedCompound_id" ON "CharacterizedCompound" (id);
CREATE TABLE "Laboratory" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Laboratory_id" ON "Laboratory" (id);
CREATE TABLE "Attribution" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	"AnalysisDataset_id" TEXT,
	"Dataset_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_Attribution_id" ON "Attribution" (id);
CREATE TABLE "CatalogueRecord" (
	id INTEGER NOT NULL,
	listing_date DATE,
	modification_date DATE NOT NULL,
	"Catalogue_id" INTEGER,
	change_type_id INTEGER,
	primary_topic_id INTEGER NOT NULL,
	source_metadata_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY(change_type_id) REFERENCES "Concept" (id),
	FOREIGN KEY(primary_topic_id) REFERENCES "Any" (id),
	FOREIGN KEY(source_metadata_id) REFERENCES "CatalogueRecord" (id)
);CREATE INDEX "ix_CatalogueRecord_id" ON "CatalogueRecord" (id);
CREATE TABLE "Checksum" (
	id INTEGER NOT NULL,
	checksum_value TEXT NOT NULL,
	algorithm_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(algorithm_id) REFERENCES "ChecksumAlgorithm" (id)
);CREATE INDEX "ix_Checksum_id" ON "Checksum" (id);
CREATE TABLE "ClassifierMixin" (
	id INTEGER NOT NULL,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_ClassifierMixin_id" ON "ClassifierMixin" (id);
CREATE TABLE "ConceptScheme" (
	id INTEGER NOT NULL,
	description TEXT,
	"Catalogue_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id)
);CREATE INDEX "ix_ConceptScheme_id" ON "ConceptScheme" (id);
CREATE TABLE "DatasetSeries" (
	id INTEGER NOT NULL,
	modification_date DATE,
	release_date DATE,
	"AnalysisDataset_id" TEXT,
	"Dataset_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	frequency_id INTEGER,
	publisher_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY(frequency_id) REFERENCES "Frequency" (id),
	FOREIGN KEY(publisher_id) REFERENCES "Agent" (id)
);CREATE INDEX "ix_DatasetSeries_id" ON "DatasetSeries" (id);
CREATE TABLE "Plan" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Plan_id" ON "Plan" (id);
CREATE TABLE "ProvenanceStatement" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	"AnalysisDataset_id" TEXT,
	"Dataset_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_ProvenanceStatement_id" ON "ProvenanceStatement" (id);
CREATE TABLE "Relationship" (
	id INTEGER NOT NULL,
	"AnalysisDataset_id" TEXT,
	"Dataset_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_Relationship_id" ON "Relationship" (id);
CREATE TABLE "Software" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Software_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Software_id") REFERENCES "Software" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Software_id" ON "Software" (id);
CREATE TABLE "Surrounding" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Surrounding_id" ON "Surrounding" (id);
CREATE TABLE "Atom" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	type_id TEXT,
	rdf_type_id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Atom_id" ON "Atom" (id);
CREATE TABLE "ChemicalSubstance" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_ChemicalSubstance_id" ON "ChemicalSubstance" (id);
CREATE TABLE "Polymer" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Polymer_id" ON "Polymer" (id);
CREATE TABLE "ChemicalReaction" (
	has_duration TEXT,
	has_reaction_step TEXT,
	id TEXT NOT NULL,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_reaction_step) REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_ChemicalReaction_id" ON "ChemicalReaction" (id);
CREATE TABLE "NMRSampleTemperature" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_NMRSampleTemperature_id" ON "NMRSampleTemperature" (id);
CREATE TABLE "PulseSequence" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value TEXT NOT NULL,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_PulseSequence_id" ON "PulseSequence" (id);
CREATE TABLE "NumberOfScans" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_NumberOfScans_id" ON "NumberOfScans" (id);
CREATE TABLE "Activity_title" (
	"Activity_id" TEXT,
	title TEXT,
	PRIMARY KEY ("Activity_id", title),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id)
);CREATE INDEX "ix_Activity_title_title" ON "Activity_title" (title);CREATE INDEX "ix_Activity_title_Activity_id" ON "Activity_title" ("Activity_id");
CREATE TABLE "Activity_description" (
	"Activity_id" TEXT,
	description TEXT,
	PRIMARY KEY ("Activity_id", description),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id)
);CREATE INDEX "ix_Activity_description_description" ON "Activity_description" (description);CREATE INDEX "ix_Activity_description_Activity_id" ON "Activity_description" ("Activity_id");
CREATE TABLE "Agent_name" (
	"Agent_id" INTEGER,
	name TEXT NOT NULL,
	PRIMARY KEY ("Agent_id", name),
	FOREIGN KEY("Agent_id") REFERENCES "Agent" (id)
);CREATE INDEX "ix_Agent_name_name" ON "Agent_name" (name);CREATE INDEX "ix_Agent_name_Agent_id" ON "Agent_name" ("Agent_id");
CREATE TABLE "AnalysisDataset_description" (
	"AnalysisDataset_id" TEXT,
	description TEXT NOT NULL,
	PRIMARY KEY ("AnalysisDataset_id", description),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id)
);CREATE INDEX "ix_AnalysisDataset_description_AnalysisDataset_id" ON "AnalysisDataset_description" ("AnalysisDataset_id");CREATE INDEX "ix_AnalysisDataset_description_description" ON "AnalysisDataset_description" (description);
CREATE TABLE "AnalysisDataset_identifier" (
	"AnalysisDataset_id" TEXT,
	identifier TEXT,
	PRIMARY KEY ("AnalysisDataset_id", identifier),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id)
);CREATE INDEX "ix_AnalysisDataset_identifier_AnalysisDataset_id" ON "AnalysisDataset_identifier" ("AnalysisDataset_id");CREATE INDEX "ix_AnalysisDataset_identifier_identifier" ON "AnalysisDataset_identifier" (identifier);
CREATE TABLE "AnalysisDataset_keyword" (
	"AnalysisDataset_id" TEXT,
	keyword TEXT,
	PRIMARY KEY ("AnalysisDataset_id", keyword),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id)
);CREATE INDEX "ix_AnalysisDataset_keyword_AnalysisDataset_id" ON "AnalysisDataset_keyword" ("AnalysisDataset_id");CREATE INDEX "ix_AnalysisDataset_keyword_keyword" ON "AnalysisDataset_keyword" (keyword);
CREATE TABLE "AnalysisDataset_title" (
	"AnalysisDataset_id" TEXT,
	title TEXT NOT NULL,
	PRIMARY KEY ("AnalysisDataset_id", title),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id)
);CREATE INDEX "ix_AnalysisDataset_title_AnalysisDataset_id" ON "AnalysisDataset_title" ("AnalysisDataset_id");CREATE INDEX "ix_AnalysisDataset_title_title" ON "AnalysisDataset_title" (title);
CREATE TABLE "AnalysisDataset_version_notes" (
	"AnalysisDataset_id" TEXT,
	version_notes TEXT,
	PRIMARY KEY ("AnalysisDataset_id", version_notes),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id)
);CREATE INDEX "ix_AnalysisDataset_version_notes_AnalysisDataset_id" ON "AnalysisDataset_version_notes" ("AnalysisDataset_id");CREATE INDEX "ix_AnalysisDataset_version_notes_version_notes" ON "AnalysisDataset_version_notes" (version_notes);
CREATE TABLE "Catalogue_description" (
	"Catalogue_id" INTEGER,
	description TEXT NOT NULL,
	PRIMARY KEY ("Catalogue_id", description),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id)
);CREATE INDEX "ix_Catalogue_description_Catalogue_id" ON "Catalogue_description" ("Catalogue_id");CREATE INDEX "ix_Catalogue_description_description" ON "Catalogue_description" (description);
CREATE TABLE "Catalogue_title" (
	"Catalogue_id" INTEGER,
	title TEXT NOT NULL,
	PRIMARY KEY ("Catalogue_id", title),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id)
);CREATE INDEX "ix_Catalogue_title_Catalogue_id" ON "Catalogue_title" ("Catalogue_id");CREATE INDEX "ix_Catalogue_title_title" ON "Catalogue_title" (title);
CREATE TABLE "Concept_preferred_label" (
	"Concept_id" INTEGER,
	preferred_label TEXT NOT NULL,
	PRIMARY KEY ("Concept_id", preferred_label),
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id)
);CREATE INDEX "ix_Concept_preferred_label_Concept_id" ON "Concept_preferred_label" ("Concept_id");CREATE INDEX "ix_Concept_preferred_label_preferred_label" ON "Concept_preferred_label" (preferred_label);
CREATE TABLE "DataService_description" (
	"DataService_id" INTEGER,
	description TEXT,
	PRIMARY KEY ("DataService_id", description),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);CREATE INDEX "ix_DataService_description_description" ON "DataService_description" (description);CREATE INDEX "ix_DataService_description_DataService_id" ON "DataService_description" ("DataService_id");
CREATE TABLE "DataService_keyword" (
	"DataService_id" INTEGER,
	keyword TEXT,
	PRIMARY KEY ("DataService_id", keyword),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);CREATE INDEX "ix_DataService_keyword_DataService_id" ON "DataService_keyword" ("DataService_id");CREATE INDEX "ix_DataService_keyword_keyword" ON "DataService_keyword" (keyword);
CREATE TABLE "DataService_title" (
	"DataService_id" INTEGER,
	title TEXT NOT NULL,
	PRIMARY KEY ("DataService_id", title),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id)
);CREATE INDEX "ix_DataService_title_title" ON "DataService_title" (title);CREATE INDEX "ix_DataService_title_DataService_id" ON "DataService_title" ("DataService_id");
CREATE TABLE "Dataset_description" (
	"Dataset_id" TEXT,
	description TEXT NOT NULL,
	PRIMARY KEY ("Dataset_id", description),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Dataset_description_Dataset_id" ON "Dataset_description" ("Dataset_id");CREATE INDEX "ix_Dataset_description_description" ON "Dataset_description" (description);
CREATE TABLE "Dataset_identifier" (
	"Dataset_id" TEXT,
	identifier TEXT,
	PRIMARY KEY ("Dataset_id", identifier),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Dataset_identifier_Dataset_id" ON "Dataset_identifier" ("Dataset_id");CREATE INDEX "ix_Dataset_identifier_identifier" ON "Dataset_identifier" (identifier);
CREATE TABLE "Dataset_keyword" (
	"Dataset_id" TEXT,
	keyword TEXT,
	PRIMARY KEY ("Dataset_id", keyword),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Dataset_keyword_keyword" ON "Dataset_keyword" (keyword);CREATE INDEX "ix_Dataset_keyword_Dataset_id" ON "Dataset_keyword" ("Dataset_id");
CREATE TABLE "Dataset_title" (
	"Dataset_id" TEXT,
	title TEXT NOT NULL,
	PRIMARY KEY ("Dataset_id", title),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Dataset_title_title" ON "Dataset_title" (title);CREATE INDEX "ix_Dataset_title_Dataset_id" ON "Dataset_title" ("Dataset_id");
CREATE TABLE "Dataset_version_notes" (
	"Dataset_id" TEXT,
	version_notes TEXT,
	PRIMARY KEY ("Dataset_id", version_notes),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Dataset_version_notes_version_notes" ON "Dataset_version_notes" (version_notes);CREATE INDEX "ix_Dataset_version_notes_Dataset_id" ON "Dataset_version_notes" ("Dataset_id");
CREATE TABLE "Distribution_description" (
	"Distribution_id" INTEGER,
	description TEXT,
	PRIMARY KEY ("Distribution_id", description),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id)
);CREATE INDEX "ix_Distribution_description_Distribution_id" ON "Distribution_description" ("Distribution_id");CREATE INDEX "ix_Distribution_description_description" ON "Distribution_description" (description);
CREATE TABLE "Distribution_title" (
	"Distribution_id" INTEGER,
	title TEXT,
	PRIMARY KEY ("Distribution_id", title),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id)
);CREATE INDEX "ix_Distribution_title_title" ON "Distribution_title" (title);CREATE INDEX "ix_Distribution_title_Distribution_id" ON "Distribution_title" ("Distribution_id");
CREATE TABLE "NMRAnalysisDataset_description" (
	"NMRAnalysisDataset_id" TEXT,
	description TEXT NOT NULL,
	PRIMARY KEY ("NMRAnalysisDataset_id", description),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_NMRAnalysisDataset_description_NMRAnalysisDataset_id" ON "NMRAnalysisDataset_description" ("NMRAnalysisDataset_id");CREATE INDEX "ix_NMRAnalysisDataset_description_description" ON "NMRAnalysisDataset_description" (description);
CREATE TABLE "NMRAnalysisDataset_identifier" (
	"NMRAnalysisDataset_id" TEXT,
	identifier TEXT,
	PRIMARY KEY ("NMRAnalysisDataset_id", identifier),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_NMRAnalysisDataset_identifier_NMRAnalysisDataset_id" ON "NMRAnalysisDataset_identifier" ("NMRAnalysisDataset_id");CREATE INDEX "ix_NMRAnalysisDataset_identifier_identifier" ON "NMRAnalysisDataset_identifier" (identifier);
CREATE TABLE "NMRAnalysisDataset_keyword" (
	"NMRAnalysisDataset_id" TEXT,
	keyword TEXT,
	PRIMARY KEY ("NMRAnalysisDataset_id", keyword),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_NMRAnalysisDataset_keyword_NMRAnalysisDataset_id" ON "NMRAnalysisDataset_keyword" ("NMRAnalysisDataset_id");CREATE INDEX "ix_NMRAnalysisDataset_keyword_keyword" ON "NMRAnalysisDataset_keyword" (keyword);
CREATE TABLE "NMRAnalysisDataset_title" (
	"NMRAnalysisDataset_id" TEXT,
	title TEXT NOT NULL,
	PRIMARY KEY ("NMRAnalysisDataset_id", title),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_NMRAnalysisDataset_title_title" ON "NMRAnalysisDataset_title" (title);CREATE INDEX "ix_NMRAnalysisDataset_title_NMRAnalysisDataset_id" ON "NMRAnalysisDataset_title" ("NMRAnalysisDataset_id");
CREATE TABLE "NMRAnalysisDataset_version_notes" (
	"NMRAnalysisDataset_id" TEXT,
	version_notes TEXT,
	PRIMARY KEY ("NMRAnalysisDataset_id", version_notes),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_NMRAnalysisDataset_version_notes_version_notes" ON "NMRAnalysisDataset_version_notes" (version_notes);CREATE INDEX "ix_NMRAnalysisDataset_version_notes_NMRAnalysisDataset_id" ON "NMRAnalysisDataset_version_notes" ("NMRAnalysisDataset_id");
CREATE TABLE "DataAnalysis" (
	id TEXT NOT NULL,
	"AnalysisDataset_id" TEXT,
	realized_plan_id INTEGER,
	occurred_in_id INTEGER,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY(realized_plan_id) REFERENCES "Plan" (id),
	FOREIGN KEY(occurred_in_id) REFERENCES "Surrounding" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_DataAnalysis_id" ON "DataAnalysis" (id);
CREATE TABLE "Kind" (
	id INTEGER NOT NULL,
	"AnalysisDataset_id" TEXT,
	"DataService_id" INTEGER,
	"Dataset_id" TEXT,
	"DatasetSeries_id" INTEGER,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_Kind_id" ON "Kind" (id);
CREATE TABLE "LegalResource" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AnalysisDataset_id" TEXT,
	"Catalogue_id" INTEGER,
	"DataService_id" INTEGER,
	"Dataset_id" TEXT,
	"DatasetSeries_id" INTEGER,
	"Distribution_id" INTEGER,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_LegalResource_id" ON "LegalResource" (id);
CREATE TABLE "LinguisticSystem" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	"AnalysisDataset_id" TEXT,
	"Catalogue_id" INTEGER,
	"CatalogueRecord_id" INTEGER,
	"Dataset_id" TEXT,
	"Distribution_id" INTEGER,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("CatalogueRecord_id") REFERENCES "CatalogueRecord" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_LinguisticSystem_id" ON "LinguisticSystem" (id);
CREATE TABLE "Location" (
	id INTEGER NOT NULL,
	bbox TEXT,
	centroid TEXT,
	"AnalysisDataset_id" TEXT,
	"Catalogue_id" INTEGER,
	"Dataset_id" TEXT,
	"DatasetSeries_id" INTEGER,
	"NMRAnalysisDataset_id" TEXT,
	geometry_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY(geometry_id) REFERENCES "Geometry" (id)
);CREATE INDEX "ix_Location_id" ON "Location" (id);
CREATE TABLE "PeriodOfTime" (
	id INTEGER NOT NULL,
	end_date DATE,
	start_date DATE,
	title TEXT,
	description TEXT,
	"AnalysisDataset_id" TEXT,
	"Catalogue_id" INTEGER,
	"Dataset_id" TEXT,
	"DatasetSeries_id" INTEGER,
	"NMRAnalysisDataset_id" TEXT,
	beginning_id INTEGER,
	end_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("Catalogue_id") REFERENCES "Catalogue" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY(beginning_id) REFERENCES "TimeInstant" (id),
	FOREIGN KEY(end_id) REFERENCES "TimeInstant" (id)
);CREATE INDEX "ix_PeriodOfTime_id" ON "PeriodOfTime" (id);
CREATE TABLE "Resource" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AnalysisDataset_id" TEXT,
	"DataService_id" INTEGER,
	"Dataset_id" TEXT,
	"Distribution_id" INTEGER,
	"Relationship_id" INTEGER,
	"ChemicalReaction_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_Resource_id" ON "Resource" (id);
CREATE TABLE "Role" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	"Relationship_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Relationship_id") REFERENCES "Relationship" (id)
);CREATE INDEX "ix_Role_id" ON "Role" (id);
CREATE TABLE "Standard" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	"AnalysisDataset_id" TEXT,
	"CatalogueRecord_id" INTEGER,
	"DataService_id" INTEGER,
	"Dataset_id" TEXT,
	"Distribution_id" INTEGER,
	"NMRAnalysisDataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("CatalogueRecord_id") REFERENCES "CatalogueRecord" (id),
	FOREIGN KEY("DataService_id") REFERENCES "DataService" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("Distribution_id") REFERENCES "Distribution" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id)
);CREATE INDEX "ix_Standard_id" ON "Standard" (id);
CREATE TABLE "StartingMaterial" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"ChemicalReaction_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_StartingMaterial_id" ON "StartingMaterial" (id);
CREATE TABLE "DissolvingSubstance" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"ChemicalReaction_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_DissolvingSubstance_id" ON "DissolvingSubstance" (id);
CREATE TABLE "Reagent" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"ChemicalReaction_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Reagent_id" ON "Reagent" (id);
CREATE TABLE "ChemicalProduct" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"ChemicalReaction_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_ChemicalProduct_id" ON "ChemicalProduct" (id);
CREATE TABLE "Catalyst" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"ChemicalReaction_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Catalyst_id" ON "Catalyst" (id);
CREATE TABLE "Reactor" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"ChemicalReaction_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Reactor_id" ON "Reactor" (id);
CREATE TABLE "Yield" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"ChemicalReaction_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Yield_id" ON "Yield" (id);
CREATE TABLE "NMRSpectralAnalysis" (
	id TEXT NOT NULL,
	"NMRAnalysisDataset_id" TEXT,
	realized_plan_id INTEGER,
	occurred_in_id INTEGER,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY(realized_plan_id) REFERENCES "Plan" (id),
	FOREIGN KEY(occurred_in_id) REFERENCES "Surrounding" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_NMRSpectralAnalysis_id" ON "NMRSpectralAnalysis" (id);
CREATE TABLE "CatalogueRecord_description" (
	"CatalogueRecord_id" INTEGER,
	description TEXT,
	PRIMARY KEY ("CatalogueRecord_id", description),
	FOREIGN KEY("CatalogueRecord_id") REFERENCES "CatalogueRecord" (id)
);CREATE INDEX "ix_CatalogueRecord_description_description" ON "CatalogueRecord_description" (description);CREATE INDEX "ix_CatalogueRecord_description_CatalogueRecord_id" ON "CatalogueRecord_description" ("CatalogueRecord_id");
CREATE TABLE "CatalogueRecord_title" (
	"CatalogueRecord_id" INTEGER,
	title TEXT,
	PRIMARY KEY ("CatalogueRecord_id", title),
	FOREIGN KEY("CatalogueRecord_id") REFERENCES "CatalogueRecord" (id)
);CREATE INDEX "ix_CatalogueRecord_title_title" ON "CatalogueRecord_title" (title);CREATE INDEX "ix_CatalogueRecord_title_CatalogueRecord_id" ON "CatalogueRecord_title" ("CatalogueRecord_id");
CREATE TABLE "ConceptScheme_title" (
	"ConceptScheme_id" INTEGER,
	title TEXT NOT NULL,
	PRIMARY KEY ("ConceptScheme_id", title),
	FOREIGN KEY("ConceptScheme_id") REFERENCES "ConceptScheme" (id)
);CREATE INDEX "ix_ConceptScheme_title_title" ON "ConceptScheme_title" (title);CREATE INDEX "ix_ConceptScheme_title_ConceptScheme_id" ON "ConceptScheme_title" ("ConceptScheme_id");
CREATE TABLE "DatasetSeries_description" (
	"DatasetSeries_id" INTEGER,
	description TEXT NOT NULL,
	PRIMARY KEY ("DatasetSeries_id", description),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id)
);CREATE INDEX "ix_DatasetSeries_description_description" ON "DatasetSeries_description" (description);CREATE INDEX "ix_DatasetSeries_description_DatasetSeries_id" ON "DatasetSeries_description" ("DatasetSeries_id");
CREATE TABLE "DatasetSeries_title" (
	"DatasetSeries_id" INTEGER,
	title TEXT NOT NULL,
	PRIMARY KEY ("DatasetSeries_id", title),
	FOREIGN KEY("DatasetSeries_id") REFERENCES "DatasetSeries" (id)
);CREATE INDEX "ix_DatasetSeries_title_title" ON "DatasetSeries_title" (title);CREATE INDEX "ix_DatasetSeries_title_DatasetSeries_id" ON "DatasetSeries_title" ("DatasetSeries_id");
CREATE TABLE "ChemicalReaction_title" (
	"ChemicalReaction_id" TEXT,
	title TEXT,
	PRIMARY KEY ("ChemicalReaction_id", title),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id)
);CREATE INDEX "ix_ChemicalReaction_title_title" ON "ChemicalReaction_title" (title);CREATE INDEX "ix_ChemicalReaction_title_ChemicalReaction_id" ON "ChemicalReaction_title" ("ChemicalReaction_id");
CREATE TABLE "ChemicalReaction_description" (
	"ChemicalReaction_id" TEXT,
	description TEXT,
	PRIMARY KEY ("ChemicalReaction_id", description),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id)
);CREATE INDEX "ix_ChemicalReaction_description_description" ON "ChemicalReaction_description" (description);CREATE INDEX "ix_ChemicalReaction_description_ChemicalReaction_id" ON "ChemicalReaction_description" ("ChemicalReaction_id");
CREATE TABLE "AnalysisSourceData" (
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"DataAnalysis_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_AnalysisSourceData_id" ON "AnalysisSourceData" (id);
CREATE TABLE "NMRSpectrum" (
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"NMRSpectralAnalysis_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_NMRSpectrum_id" ON "NMRSpectrum" (id);
CREATE TABLE "DataAnalysis_title" (
	"DataAnalysis_id" TEXT,
	title TEXT,
	PRIMARY KEY ("DataAnalysis_id", title),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id)
);CREATE INDEX "ix_DataAnalysis_title_title" ON "DataAnalysis_title" (title);CREATE INDEX "ix_DataAnalysis_title_DataAnalysis_id" ON "DataAnalysis_title" ("DataAnalysis_id");
CREATE TABLE "DataAnalysis_description" (
	"DataAnalysis_id" TEXT,
	description TEXT,
	PRIMARY KEY ("DataAnalysis_id", description),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id)
);CREATE INDEX "ix_DataAnalysis_description_description" ON "DataAnalysis_description" (description);CREATE INDEX "ix_DataAnalysis_description_DataAnalysis_id" ON "DataAnalysis_description" ("DataAnalysis_id");
CREATE TABLE "NMRSpectralAnalysis_title" (
	"NMRSpectralAnalysis_id" TEXT,
	title TEXT,
	PRIMARY KEY ("NMRSpectralAnalysis_id", title),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id)
);CREATE INDEX "ix_NMRSpectralAnalysis_title_title" ON "NMRSpectralAnalysis_title" (title);CREATE INDEX "ix_NMRSpectralAnalysis_title_NMRSpectralAnalysis_id" ON "NMRSpectralAnalysis_title" ("NMRSpectralAnalysis_id");
CREATE TABLE "NMRSpectralAnalysis_description" (
	"NMRSpectralAnalysis_id" TEXT,
	description TEXT,
	PRIMARY KEY ("NMRSpectralAnalysis_id", description),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id)
);CREATE INDEX "ix_NMRSpectralAnalysis_description_NMRSpectralAnalysis_id" ON "NMRSpectralAnalysis_description" ("NMRSpectralAnalysis_id");CREATE INDEX "ix_NMRSpectralAnalysis_description_description" ON "NMRSpectralAnalysis_description" (description);
CREATE TABLE "DataGeneratingActivity" (
	id TEXT NOT NULL,
	"AnalysisSourceData_id" TEXT,
	"Dataset_id" TEXT,
	realized_plan_id INTEGER,
	occurred_in_id INTEGER,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisSourceData_id") REFERENCES "AnalysisSourceData" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(realized_plan_id) REFERENCES "Plan" (id),
	FOREIGN KEY(occurred_in_id) REFERENCES "Surrounding" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_DataGeneratingActivity_id" ON "DataGeneratingActivity" (id);
CREATE TABLE "NMRSpectroscopy" (
	id TEXT NOT NULL,
	"NMRSpectrum_id" TEXT,
	used_pulse_sequence_id INTEGER NOT NULL,
	used_number_of_scans_id INTEGER,
	used_sample_temperature_id INTEGER,
	realized_plan_id INTEGER,
	occurred_in_id INTEGER,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRSpectrum_id") REFERENCES "NMRSpectrum" (id),
	FOREIGN KEY(used_pulse_sequence_id) REFERENCES "PulseSequence" (id),
	FOREIGN KEY(used_number_of_scans_id) REFERENCES "NumberOfScans" (id),
	FOREIGN KEY(used_sample_temperature_id) REFERENCES "NMRSampleTemperature" (id),
	FOREIGN KEY(realized_plan_id) REFERENCES "Plan" (id),
	FOREIGN KEY(occurred_in_id) REFERENCES "Surrounding" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_NMRSpectroscopy_id" ON "NMRSpectroscopy" (id);
CREATE TABLE "EvaluatedActivity" (
	id TEXT NOT NULL,
	"AnalysisDataset_id" TEXT,
	"DataAnalysis_id" TEXT,
	"DataGeneratingActivity_id" TEXT,
	"Dataset_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	"NMRSpectralAnalysis_id" TEXT,
	"NMRSpectroscopy_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_EvaluatedActivity_id" ON "EvaluatedActivity" (id);
CREATE TABLE "EvaluatedEntity" (
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"AnalysisDataset_id" TEXT,
	"DataGeneratingActivity_id" TEXT,
	"Dataset_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_EvaluatedEntity_id" ON "EvaluatedEntity" (id);
CREATE TABLE "NMRSpectrometer" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"NMRSpectroscopy_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_NMRSpectrometer_id" ON "NMRSpectrometer" (id);
CREATE TABLE "ShiftCalibrationCompound" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"NMRSpectroscopy_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_ShiftCalibrationCompound_id" ON "ShiftCalibrationCompound" (id);
CREATE TABLE "ShiftReferenceCompound" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	title TEXT,
	description TEXT,
	id TEXT NOT NULL,
	"NMRSpectroscopy_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_ShiftReferenceCompound_id" ON "ShiftReferenceCompound" (id);
CREATE TABLE "AcquisitionNucleus" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"NMRSpectroscopy_id" TEXT,
	nucleus_of_id TEXT NOT NULL,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY(nucleus_of_id) REFERENCES "Atom" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_AcquisitionNucleus_id" ON "AcquisitionNucleus" (id);
CREATE TABLE "NMRSolvent" (
	alternative_label TEXT,
	has_physical_state VARCHAR(7),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"NMRSpectroscopy_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_NMRSolvent_id" ON "NMRSolvent" (id);
CREATE TABLE "DataGeneratingActivity_title" (
	"DataGeneratingActivity_id" TEXT,
	title TEXT,
	PRIMARY KEY ("DataGeneratingActivity_id", title),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id)
);CREATE INDEX "ix_DataGeneratingActivity_title_title" ON "DataGeneratingActivity_title" (title);CREATE INDEX "ix_DataGeneratingActivity_title_DataGeneratingActivity_id" ON "DataGeneratingActivity_title" ("DataGeneratingActivity_id");
CREATE TABLE "DataGeneratingActivity_description" (
	"DataGeneratingActivity_id" TEXT,
	description TEXT,
	PRIMARY KEY ("DataGeneratingActivity_id", description),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id)
);CREATE INDEX "ix_DataGeneratingActivity_description_DataGeneratingActivity_id" ON "DataGeneratingActivity_description" ("DataGeneratingActivity_id");CREATE INDEX "ix_DataGeneratingActivity_description_description" ON "DataGeneratingActivity_description" (description);
CREATE TABLE "NMRSpectroscopy_title" (
	"NMRSpectroscopy_id" TEXT,
	title TEXT,
	PRIMARY KEY ("NMRSpectroscopy_id", title),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id)
);CREATE INDEX "ix_NMRSpectroscopy_title_title" ON "NMRSpectroscopy_title" (title);CREATE INDEX "ix_NMRSpectroscopy_title_NMRSpectroscopy_id" ON "NMRSpectroscopy_title" ("NMRSpectroscopy_id");
CREATE TABLE "NMRSpectroscopy_description" (
	"NMRSpectroscopy_id" TEXT,
	description TEXT,
	PRIMARY KEY ("NMRSpectroscopy_id", description),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id)
);CREATE INDEX "ix_NMRSpectroscopy_description_NMRSpectroscopy_id" ON "NMRSpectroscopy_description" ("NMRSpectroscopy_id");CREATE INDEX "ix_NMRSpectroscopy_description_description" ON "NMRSpectroscopy_description" (description);
CREATE TABLE "Device" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Device_id" TEXT,
	"Reactor_id" TEXT,
	"NMRSpectrometer_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Device_id") REFERENCES "Device" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("NMRSpectrometer_id") REFERENCES "NMRSpectrometer" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Device_id" ON "Device" (id);
CREATE TABLE "MolarMass" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_MolarMass_id" ON "MolarMass" (id);
CREATE TABLE "InChIKey" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value TEXT NOT NULL,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_InChIKey_id" ON "InChIKey" (id);
CREATE TABLE "InChi" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value TEXT NOT NULL,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_InChi_id" ON "InChi" (id);
CREATE TABLE "MolecularFormula" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value TEXT NOT NULL,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_MolecularFormula_id" ON "MolecularFormula" (id);
CREATE TABLE "IUPACName" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value TEXT NOT NULL,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_IUPACName_id" ON "IUPACName" (id);
CREATE TABLE "SMILES" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value TEXT NOT NULL,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_SMILES_id" ON "SMILES" (id);
CREATE TABLE "Concentration" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Concentration_id" ON "Concentration" (id);
CREATE TABLE "AmountOfSubstance" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_AmountOfSubstance_id" ON "AmountOfSubstance" (id);
CREATE TABLE "PHValue" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_PHValue_id" ON "PHValue" (id);
CREATE TABLE "MolarEquivalent" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_MolarEquivalent_id" ON "MolarEquivalent" (id);
CREATE TABLE "PercentageOfTotal" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_PercentageOfTotal_id" ON "PercentageOfTotal" (id);
CREATE TABLE "Temperature" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"ChemicalReaction_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"Reactor_id" TEXT,
	"Materialistic_id" INTEGER,
	"MaterialEntity_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("Materialistic_id") REFERENCES "Materialistic" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Temperature_id" ON "Temperature" (id);
CREATE TABLE "Mass" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"Reactor_id" TEXT,
	"Materialistic_id" INTEGER,
	"MaterialEntity_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("Materialistic_id") REFERENCES "Materialistic" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Mass_id" ON "Mass" (id);
CREATE TABLE "Volume" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"Reactor_id" TEXT,
	"Materialistic_id" INTEGER,
	"MaterialEntity_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("Materialistic_id") REFERENCES "Materialistic" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Volume_id" ON "Volume" (id);
CREATE TABLE "Density" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"Reactor_id" TEXT,
	"Materialistic_id" INTEGER,
	"MaterialEntity_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("Materialistic_id") REFERENCES "Materialistic" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Density_id" ON "Density" (id);
CREATE TABLE "Pressure" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"ChemicalReaction_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"Reactor_id" TEXT,
	"Materialistic_id" INTEGER,
	"MaterialEntity_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("Materialistic_id") REFERENCES "Materialistic" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_Pressure_id" ON "Pressure" (id);
CREATE TABLE "NominalProtonFrequency" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"NMRSpectrometer_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("NMRSpectrometer_id") REFERENCES "NMRSpectrometer" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_NominalProtonFrequency_id" ON "NominalProtonFrequency" (id);
CREATE TABLE "CalibrationPeakShift" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_CalibrationPeakShift_id" ON "CalibrationPeakShift" (id);
CREATE TABLE "EvaluatedActivity_title" (
	"EvaluatedActivity_id" TEXT,
	title TEXT,
	PRIMARY KEY ("EvaluatedActivity_id", title),
	FOREIGN KEY("EvaluatedActivity_id") REFERENCES "EvaluatedActivity" (id)
);CREATE INDEX "ix_EvaluatedActivity_title_title" ON "EvaluatedActivity_title" (title);CREATE INDEX "ix_EvaluatedActivity_title_EvaluatedActivity_id" ON "EvaluatedActivity_title" ("EvaluatedActivity_id");
CREATE TABLE "EvaluatedActivity_description" (
	"EvaluatedActivity_id" TEXT,
	description TEXT,
	PRIMARY KEY ("EvaluatedActivity_id", description),
	FOREIGN KEY("EvaluatedActivity_id") REFERENCES "EvaluatedActivity" (id)
);CREATE INDEX "ix_EvaluatedActivity_description_description" ON "EvaluatedActivity_description" (description);CREATE INDEX "ix_EvaluatedActivity_description_EvaluatedActivity_id" ON "EvaluatedActivity_description" ("EvaluatedActivity_id");
CREATE TABLE "AgenticEntity" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Activity_id" TEXT,
	"AgenticEntity_id" TEXT,
	"DataAnalysis_id" TEXT,
	"DataGeneratingActivity_id" TEXT,
	"Device_id" TEXT,
	"EvaluatedActivity_id" TEXT,
	"Software_id" TEXT,
	"ChemicalReaction_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Catalyst_id" TEXT,
	"Reactor_id" TEXT,
	"NMRSpectralAnalysis_id" TEXT,
	"NMRSpectroscopy_id" TEXT,
	"NMRSpectrometer_id" TEXT,
	"AcquisitionNucleus_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY("AgenticEntity_id") REFERENCES "AgenticEntity" (id),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id),
	FOREIGN KEY("Device_id") REFERENCES "Device" (id),
	FOREIGN KEY("EvaluatedActivity_id") REFERENCES "EvaluatedActivity" (id),
	FOREIGN KEY("Software_id") REFERENCES "Software" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY("NMRSpectrometer_id") REFERENCES "NMRSpectrometer" (id),
	FOREIGN KEY("AcquisitionNucleus_id") REFERENCES "AcquisitionNucleus" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_AgenticEntity_id" ON "AgenticEntity" (id);
CREATE TABLE "Identifier" (
	id INTEGER NOT NULL,
	notation TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"Activity_id" TEXT,
	"AgenticEntity_id" TEXT,
	"AnalysisDataset_id" TEXT,
	"AnalysisSourceData_id" TEXT,
	"DataAnalysis_id" TEXT,
	"DataGeneratingActivity_id" TEXT,
	"Dataset_id" TEXT,
	"Device_id" TEXT,
	"Entity_id" TEXT,
	"EvaluatedActivity_id" TEXT,
	"EvaluatedEntity_id" TEXT,
	"Software_id" TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"ChemicalReaction_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"Reactor_id" TEXT,
	"MaterialEntity_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRAnalysisDataset_id" TEXT,
	"NMRSpectralAnalysis_id" TEXT,
	"NMRSpectrum_id" TEXT,
	"NMRSpectroscopy_id" TEXT,
	"NMRSpectrometer_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	"AcquisitionNucleus_id" TEXT,
	"NMRSolvent_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY("AgenticEntity_id") REFERENCES "AgenticEntity" (id),
	FOREIGN KEY("AnalysisDataset_id") REFERENCES "AnalysisDataset" (id),
	FOREIGN KEY("AnalysisSourceData_id") REFERENCES "AnalysisSourceData" (id),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY("Device_id") REFERENCES "Device" (id),
	FOREIGN KEY("Entity_id") REFERENCES "Entity" (id),
	FOREIGN KEY("EvaluatedActivity_id") REFERENCES "EvaluatedActivity" (id),
	FOREIGN KEY("EvaluatedEntity_id") REFERENCES "EvaluatedEntity" (id),
	FOREIGN KEY("Software_id") REFERENCES "Software" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRAnalysisDataset_id") REFERENCES "NMRAnalysisDataset" (id),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id),
	FOREIGN KEY("NMRSpectrum_id") REFERENCES "NMRSpectrum" (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY("NMRSpectrometer_id") REFERENCES "NMRSpectrometer" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY("AcquisitionNucleus_id") REFERENCES "AcquisitionNucleus" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id)
);CREATE INDEX "ix_Identifier_id" ON "Identifier" (id);
CREATE TABLE "QualitativeAttribute" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value TEXT NOT NULL,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"Activity_id" TEXT,
	"AgenticEntity_id" TEXT,
	"AnalysisSourceData_id" TEXT,
	"DataAnalysis_id" TEXT,
	"DataGeneratingActivity_id" TEXT,
	"Device_id" TEXT,
	"Entity_id" TEXT,
	"EvaluatedActivity_id" TEXT,
	"EvaluatedEntity_id" TEXT,
	"Software_id" TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"ChemicalReaction_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"Reactor_id" TEXT,
	"MaterialEntity_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRSpectralAnalysis_id" TEXT,
	"NMRSpectrum_id" TEXT,
	"NMRSpectroscopy_id" TEXT,
	"NMRSpectrometer_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	"AcquisitionNucleus_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY("AgenticEntity_id") REFERENCES "AgenticEntity" (id),
	FOREIGN KEY("AnalysisSourceData_id") REFERENCES "AnalysisSourceData" (id),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id),
	FOREIGN KEY("Device_id") REFERENCES "Device" (id),
	FOREIGN KEY("Entity_id") REFERENCES "Entity" (id),
	FOREIGN KEY("EvaluatedActivity_id") REFERENCES "EvaluatedActivity" (id),
	FOREIGN KEY("EvaluatedEntity_id") REFERENCES "EvaluatedEntity" (id),
	FOREIGN KEY("Software_id") REFERENCES "Software" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id),
	FOREIGN KEY("NMRSpectrum_id") REFERENCES "NMRSpectrum" (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY("NMRSpectrometer_id") REFERENCES "NMRSpectrometer" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY("AcquisitionNucleus_id") REFERENCES "AcquisitionNucleus" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_QualitativeAttribute_id" ON "QualitativeAttribute" (id);
CREATE TABLE "QuantitativeAttribute" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	value FLOAT NOT NULL,
	has_quantity_type TEXT NOT NULL,
	unit TEXT,
	"SubstanceSample_id" TEXT,
	"PolymerSample_id" TEXT,
	"Activity_id" TEXT,
	"AgenticEntity_id" TEXT,
	"AnalysisSourceData_id" TEXT,
	"DataAnalysis_id" TEXT,
	"DataGeneratingActivity_id" TEXT,
	"Device_id" TEXT,
	"Entity_id" TEXT,
	"EvaluatedActivity_id" TEXT,
	"EvaluatedEntity_id" TEXT,
	"Software_id" TEXT,
	"ChemicalEntity_id" TEXT,
	"Atom_id" TEXT,
	"ChemicalSubstance_id" TEXT,
	"Polymer_id" TEXT,
	"ChemicalReaction_id" TEXT,
	"StartingMaterial_id" TEXT,
	"DissolvingSubstance_id" TEXT,
	"Reagent_id" TEXT,
	"ChemicalProduct_id" TEXT,
	"Catalyst_id" TEXT,
	"Reactor_id" TEXT,
	"MaterialEntity_id" TEXT,
	"MaterialSample_id" TEXT,
	"NMRSample_id" TEXT,
	"NMRSpectralAnalysis_id" TEXT,
	"NMRSpectrum_id" TEXT,
	"NMRSpectroscopy_id" TEXT,
	"NMRSpectrometer_id" TEXT,
	"ShiftCalibrationCompound_id" TEXT,
	"ShiftReferenceCompound_id" TEXT,
	"CharacterizedCompound_id" TEXT,
	"AcquisitionNucleus_id" TEXT,
	"NMRSolvent_id" TEXT,
	type_id TEXT,
	rdf_type_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(has_quantity_type) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(unit) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY("SubstanceSample_id") REFERENCES "SubstanceSample" (id),
	FOREIGN KEY("PolymerSample_id") REFERENCES "PolymerSample" (id),
	FOREIGN KEY("Activity_id") REFERENCES "Activity" (id),
	FOREIGN KEY("AgenticEntity_id") REFERENCES "AgenticEntity" (id),
	FOREIGN KEY("AnalysisSourceData_id") REFERENCES "AnalysisSourceData" (id),
	FOREIGN KEY("DataAnalysis_id") REFERENCES "DataAnalysis" (id),
	FOREIGN KEY("DataGeneratingActivity_id") REFERENCES "DataGeneratingActivity" (id),
	FOREIGN KEY("Device_id") REFERENCES "Device" (id),
	FOREIGN KEY("Entity_id") REFERENCES "Entity" (id),
	FOREIGN KEY("EvaluatedActivity_id") REFERENCES "EvaluatedActivity" (id),
	FOREIGN KEY("EvaluatedEntity_id") REFERENCES "EvaluatedEntity" (id),
	FOREIGN KEY("Software_id") REFERENCES "Software" (id),
	FOREIGN KEY("ChemicalEntity_id") REFERENCES "ChemicalEntity" (id),
	FOREIGN KEY("Atom_id") REFERENCES "Atom" (id),
	FOREIGN KEY("ChemicalSubstance_id") REFERENCES "ChemicalSubstance" (id),
	FOREIGN KEY("Polymer_id") REFERENCES "Polymer" (id),
	FOREIGN KEY("ChemicalReaction_id") REFERENCES "ChemicalReaction" (id),
	FOREIGN KEY("StartingMaterial_id") REFERENCES "StartingMaterial" (id),
	FOREIGN KEY("DissolvingSubstance_id") REFERENCES "DissolvingSubstance" (id),
	FOREIGN KEY("Reagent_id") REFERENCES "Reagent" (id),
	FOREIGN KEY("ChemicalProduct_id") REFERENCES "ChemicalProduct" (id),
	FOREIGN KEY("Catalyst_id") REFERENCES "Catalyst" (id),
	FOREIGN KEY("Reactor_id") REFERENCES "Reactor" (id),
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id),
	FOREIGN KEY("MaterialSample_id") REFERENCES "MaterialSample" (id),
	FOREIGN KEY("NMRSample_id") REFERENCES "NMRSample" (id),
	FOREIGN KEY("NMRSpectralAnalysis_id") REFERENCES "NMRSpectralAnalysis" (id),
	FOREIGN KEY("NMRSpectrum_id") REFERENCES "NMRSpectrum" (id),
	FOREIGN KEY("NMRSpectroscopy_id") REFERENCES "NMRSpectroscopy" (id),
	FOREIGN KEY("NMRSpectrometer_id") REFERENCES "NMRSpectrometer" (id),
	FOREIGN KEY("ShiftCalibrationCompound_id") REFERENCES "ShiftCalibrationCompound" (id),
	FOREIGN KEY("ShiftReferenceCompound_id") REFERENCES "ShiftReferenceCompound" (id),
	FOREIGN KEY("CharacterizedCompound_id") REFERENCES "CharacterizedCompound" (id),
	FOREIGN KEY("AcquisitionNucleus_id") REFERENCES "AcquisitionNucleus" (id),
	FOREIGN KEY("NMRSolvent_id") REFERENCES "NMRSolvent" (id),
	FOREIGN KEY(type_id) REFERENCES "DefinedTerm" (id),
	FOREIGN KEY(rdf_type_id) REFERENCES "DefinedTerm" (id)
);CREATE INDEX "ix_QuantitativeAttribute_id" ON "QuantitativeAttribute" (id);
