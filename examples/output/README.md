## AnalysisDataset-001
### Input
```yaml
description:
- Dataset for 13C nuclear magnetic resonance spectroscopy (13C NMR)
id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1
is_about_entity:
- description: The analysed chemical substance sample CRS-50440.
  has_part:
  - description: compound assigned to doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
    has_qualitative_attribute:
    - rdf_type:
        id: CHEMINF:000059
        title: InChiKey
      title: assigned InChiKey
      value: KVOIVNBYNQXCNY-BOCHJOTCSA-N
    - rdf_type:
        id: CHEMINF:000113
        title: InChi
      title: assigned InChi
      value: InChI=1S/C11H12N2S/c1-12-7-10-8-14-11(13-10)9-5-3-2-4-6-9/h2-6,8,12H,7H2,1H3
    - rdf_type:
        id: CHEMINF:000018
        title: SMILES descriptor
      title: assigned SMILES
      value: CNCc1csc(n1)c1ccccc1
    - rdf_type:
        id: CHEMINF:000042
        title: molecular formula
      title: assigned molecular formula
      value: C11H12N2S
    - description: Chemotion IUPAC name
      rdf_type:
        id: CHEMINF:000107
        title: IUPAC name
      value: N-methyl-1-(2-phenyl-1,3-thiazol-4-yl)methanamine
    - description: PubChem IUPAC name
      rdf_type:
        id: CHEMINF:000107
        title: IUPAC name
      value: Methyl[(2-phenyl-1,3-thiazol-4-yl)methyl]amine
    has_quantitative_attribute:
    - description: Molar mass as specified in the Chemotion repository.
      has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
      unit: https://qudt.org/vocab/unit/GM-PER-MOL
      value: 204.072119
    - description: Molar mass as specified in PubChem
      has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
      unit: https://qudt.org/vocab/unit/GM-PER-MOL
      value: 204.29
    id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2#EvaluatedCompound
    other_identifier:
    - notation: https://pubchem.ncbi.nlm.nih.gov/compound/26248854
    rdf_type:
      id: CHEBI:23367
      title: molecular entity
  id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
  rdf_type:
    id: CHEBI:59999
    title: chemical substance
  title: CRS-50440
other_identifier:
- notation: https://www.chemotion-repository.net/pid/50434
theme:
- preferred_label:
  - Science and technology
title:
- 13C nuclear magnetic resonance spectroscopy (13C NMR)
was_generated_by:
- description:
  - Analysis of NMR spectra.
  evaluated_entity:
  - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#CDCl3_13C_NMR_Spectrum
    was_generated_by:
    - carried_out_by:
      - description: The NMR spectrometer used.
        id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#CDCl3_13C_NMR_Spectrometer
        rdf_type:
          id: OBI:0000566
          title: NMR instrument
        title: Bruker 400 MHz
      - description: used solvent
        has_part:
        - id: https://pubchem.ncbi.nlm.nih.gov/compound/71583
          rdf_type:
            id: CHEBI:85365
            title: deuterated chloroform
          title: chloroform-D1 (CDCl3)
        id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#CDCl3_13C_NMR_Solvent
      - id: https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#CDCl3_13C_NMR_AcquisitionNucleus
        part_of:
        - description: The atom of the probed nucleus
          id: https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#DMSO_13C_NMR_AcquisitionNucleusAtom
          rdf_type:
            id: CHEBI:36928
            title: carbon-13 atom
          title: 13C
        title: probed nucleus
      - description: The used calibration compound
        has_quantitative_attribute:
        - description: The chemical shift of the peak used for chemical shift calibration.
          has_quantity_type: http://qudt.org/vocab/quantitykind/DimensionlessRatio
          unit: https://qudt.org/vocab/unit/PPM
          value: 77.16
        id: https://pubchem.ncbi.nlm.nih.gov/compound/71583
        rdf_type:
          id: CHEBI:85365
          title: deuterated chloroform
        title: Chloroform-D
      evaluated_entity:
      - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
        title: CRS-50440
      has_qualitative_attribute:
      - rdf_type:
          id: NMR:1400037
          title: NMR pulse sequence
        title: Puls programme
        value: zgpg30
      has_quantitative_attribute:
      - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
        rdf_type:
          id: NMR:1400262
          title: sample temperature information
        title: sample temperature setting
        unit: https://qudt.org/vocab/unit/K
        value: 300.0
      - has_quantity_type: http://qudt.org/vocab/quantitykind/Count
        rdf_type:
          id: NMR:1400087
          title: number of scans
        title: Number of scans
        unit: http://qudt.org/vocab/unit/NUM
        value: 1024
      id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#CDCl3_13C_NMR
      rdf_type:
        id: CHMO:0000595
        title: 13C nuclear magnetic resonance spectroscopy
      title:
      - CDCl3_13C_NMR
  - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#DMSO_13C_NMR_Spectrum
    was_generated_by:
    - carried_out_by:
      - description: used spectrometer
        id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#DMSO_13C_NMR_Spectrometer
        rdf_type:
          id: OBI:0000566
          title: NMR instrument
        title: Bruker 400 MHz
      - description: used solvent
        has_part:
        - id: https://pubchem.ncbi.nlm.nih.gov/compound/679
          rdf_type:
            id: CHEBI:28262
            title: dimethyl sulfoxide
          title: DMSO
        id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#DMSO_13C_NMR_Solvent
      - id: https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#DMSO_13C_NMR_AcquisitionNucleus
        part_of:
        - description: The atom of the probed nucleus
          id: https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#DMSO_13C_NMR_AcquisitionNucleusAtom
          rdf_type:
            id: CHEBI:36928
            title: carbon-13 atom
          title: 13C
        title: probed nucleus
      - description: The used calibration compound
        has_quantitative_attribute:
        - description: The chemical shift of the peak used for chemical shift calibration.
          has_quantity_type: http://qudt.org/vocab/quantitykind/DimensionlessRatio
          unit: https://qudt.org/vocab/unit/PPM
          value: 39.52
        id: https://pubchem.ncbi.nlm.nih.gov/compound/679
        rdf_type:
          id: CHEBI:28262
          title: dimethyl sulfoxide
        title: DMSO
      evaluated_entity:
      - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
        title: CRS-50440
      has_qualitative_attribute:
      - rdf_type:
          id: NMR:1400037
          title: NMR pulse sequence
        title: Puls programme
        value: zgpg30
      has_quantitative_attribute:
      - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
        rdf_type:
          id: NMR:1400262
          title: sample temperature information
        title: sample temperature setting
        unit: https://qudt.org/vocab/unit/K
        value: 300.0
      - has_quantity_type: http://qudt.org/vocab/quantitykind/Count
        rdf_type:
          id: NMR:1400087
          title: number of scans
        title: Number of scans
        unit: http://qudt.org/vocab/unit/NUM
        value: 1024
      id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#DMSO_13C_NMR
      rdf_type:
        id: CHMO:0000595
        title: 13C nuclear magnetic resonance spectroscopy
      title:
      - DMSO_13C_NMR
  id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#NMRSpectralAnalysis
  rdf_type:
    id: NMR:1400042
    title: NMR data processing

```
## ChemicalReaction-001
### Input
```yaml
description:
- Synthesis of 1-diphenylphosphoryl-2-fluorobenzene via lithiation-phosphination-oxidation
generated_product:
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/13005284
    iupac_name:
    - value: 1-diphenylphosphoryl-2-fluorobenzene
    molecular_formula:
    - value: C18H14FOP
  has_amount:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
    title: Amount [mmol]
    unit: https://qudt.org/vocab/unit/MilliMOL
    value: 7.779
  has_mass:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    title: Mass [mg]
    unit: https://qudt.org/vocab/unit/MilliGM
    value: 2328.0
  has_physical_state: SOLID
  has_qualitative_attribute:
  - rdf_type:
      id: PATO:0000337
      title: colorless
    title: 'property: colorless'
    value: colorless
  id: https://dx.doi.org/10.14272/MTSVGCFANKMACF-UHFFFAOYSA-N.1
  title: Reaction mixture containing crude 1-diphenylphosphoryl-2-fluorobenzene
has_duration: PT22H
has_qualitative_attribute:
- rdf_type:
    id: IAO:0020000
    title: identifier
  title: RInChI
  value: 1.00.1S/C12H10ClP/c13-14(11-7-3-1-4-8-11) 12-9-5-2-6-10-12/h1-10H!C6H4BrF/c7-5-3-1-2-4-6(5)8/h1-4H<>C18H14FOP/c19-17-13-7-8-14-18(17)21(20,15-9-3-1-4-10-15)16-11-5-2-6-12-16/h1-14H<>C2H4O2/c1-2(3)4/h1H3,(H,3,4)!C2H6O/c1-2-3/h3H,2H2,1H3!C2H6O/c1-2-3/h3H,2H2,1H3!C4H8O/c1-2-4-5-3-1/h1-4H2!C4H8O/c1-2-4-5-3-1/h1-4H2!C4H9.Li/c1-3-4-2;/h1,3-4H2,2H3;!H2O2/c1-2/h1-2H/d+
- rdf_type:
    id: IAO:0020000
    title: identifier
  title: Long-RInChIKey
  value: SA-FUHFF-XGRJZXREYAXTGV-UHFFFAOYSA-N-IPWBFGUBXWMIPR-UHFFFAOYSA-N--MTSVGCFANKMACF-UHFFFAOYSA-N--QTBSBXVTEAMEQO-UHFFFAOYSA-N-LFQSCWFLJHTTHZ-UHFFFAOYSA-N-LFQSCWFLJHTTHZ-UHFFFAOYSA-N-WYURNTSHIVDZCO-UHFFFAOYSA-N-WYURNTSHIVDZCO-UHFFFAOYSA-N-MZRVEZGGRBJDDB-UHFFFAOYSA-N-MHAJPDPJQMAIIY-UHFFFAOYSA-N
- rdf_type:
    id: IAO:0020000
    title: identifier
  title: Short-RInChIKey
  value: SA-FUHFF-SCESBIRHVX-MTSVGCFANK-IWBUMUHRPY-NUHFF-NUHFF-NUHFF-ZZZ
- rdf_type:
    id: IAO:0020000
    title: identifier
  title: Web-RInChIKey
  value: BOMQVCJFVRPGKEKDX-NUHFFFADPSCTJSA
- description: The status of the reaction
  rdf_type:
    id: SIO:001326
    title: status descriptor
  title: Status
  value: Successful
has_yield:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
  title: Yield [%]
  type:
    id: VOC4CAT:0005005
    title: yield
  unit: http://qudt.org/vocab/unit/PERCENT
  value: 86
id: https://www.chemotion-repository.net/pid/56408
rdf_type:
  id: RXNO:0000329
  title: planned synthesis
title:
- Chemotion Repository synthesis CRR-56408
used_reactant:
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/53627823
    rdf_type:
      id: CHEBI:51469
      title: butyllithium
  has_amount:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
    title: Amount [mmol]
    unit: https://qudt.org/vocab/unit/MilliMOL
    value: 10.75
  has_concentration:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstanceConcentration
    title: Molarity [M]
    unit: https://qudt.org/vocab/unit/MOL-PER-L
    value: 2.5
  has_mass:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    title: Mass [mg]
    unit: https://qudt.org/vocab/unit/MilliGM
    value: 688.594
  has_molar_equivalent:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: Molar Equivalent
    unit: https://qudt.org/vocab/unit/PERCENT
    value: 1.183
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 4.3
  id: https://www.chemotion-repository.net/pid/56408_Reactant-1
  rdf_type:
    id: CHEBI:60004
    title: mixture
  title: 'Reactant-1: n-BuLi'
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/784
    rdf_type:
      id: CHEBI:16240
      title: Hydrogen Peroxide
  has_amount:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
    title: Amount [mmol]
    unit: https://qudt.org/vocab/unit/MilliMOL
    value: 40.696
  has_density:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Density
    title: Density [g/mL]
    unit: https://qudt.org/vocab/unit/GM-PER-MilliL
    value: 1.13
  has_mass:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    title: Mass [mg]
    unit: https://qudt.org/vocab/unit/MilliGM
    value: 3955.0
  has_molar_equivalent:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: Molar Equivalent
    unit: https://qudt.org/vocab/unit/PERCENT
    value: 4.477
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 3.5
  id: https://www.chemotion-repository.net/pid/56408_Reactant-2
  title: 'Reactant-2: Hydrogen Peroxide'
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/176
    rdf_type:
      id: CHEBI:15366
      title: acetic acid
  has_amount:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
    title: Amount [mmol]
    unit: https://qudt.org/vocab/unit/MilliMOL
    value: 30.502
  has_density:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Density
    title: Density [g/mL]
    unit: https://qudt.org/vocab/unit/GM-PER-MilliL
    value: 1.06
  has_mass:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    title: Mass [mg]
    unit: https://qudt.org/vocab/unit/MilliGM
    value: 1908.0
  has_molar_equivalent:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: Molar Equivalent
    unit: https://qudt.org/vocab/unit/PERCENT
    value: 3.355
  has_qualitative_attribute:
  - rdf_type:
      id: AFR:0002371
      title: purity
    title: Grade/Purity
    value: Glacial
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 1.8
  id: https://www.chemotion-repository.net/pid/56408_Reactant-3
  title: 'Reactant-3: glacial acetic acid'
used_reactor:
- has_qualitative_attribute:
  - title: Argon atmosphere of the glass ware
    type:
      id: VOC4CAT:0007809
      title: atmosphere
    value: Argon atmosphere
  - title: dryness of the used glass ware
    type:
      id: PATO:0001824
      title: dry
    value: dry
  id: https://www.chemotion-repository.net/pid/56408_Reactor-1
  rdf_type:
    id: OBI:0002089
    title: container with environmental control
  title: dry glass ware under argon atmosphere
used_solvent:
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/8028
    iupac_name:
    - value: oxolane
    rdf_type:
      id: CHEBI:26911
      title: oxolane
    title: THF
  has_percentage_of_total:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: PercentageOfTotal
    unit: https://qudt.org/vocab/unit/PERCENT
    value: 13
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 24.0
  id: https://www.chemotion-repository.net/pid/56408_Solvent-1
  title: 'Solvent-1: THF'
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/8028
    title: THF
  has_percentage_of_total:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: PercentageOfTotal
    unit: https://qudt.org/vocab/unit/PERCENT
    value: 2
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 3.0
  id: https://www.chemotion-repository.net/pid/56408_Solvent-2
  title: 'Solvent-2: THF'
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/702
    rdf_type:
      id: CHEBI:16236
      title: ethanol
    title: Ethanol
  has_percentage_of_total:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: PercentageOfTotal
    unit: https://qudt.org/vocab/unit/PERCENT
    value: 78
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 150.0
  id: https://www.chemotion-repository.net/pid/56408_Solvent-3
  title: 'Solvent-3: Ethanol'
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/702
    title: Ethanol
  has_percentage_of_total:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: PercentageOfTotal
    unit: https://qudt.org/vocab/unit/PERCENT
    value: 8
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 15.0
  id: https://www.chemotion-repository.net/pid/56408_Solvent-4
  title: 'Solvent-4: Ethanol'
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/3283
    rdf_type:
      id: CHEBI:35702
      title: diethyl ether
    title: Diethyl Ether
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 150.0
  id: https://www.chemotion-repository.net/pid/56408_Solvent-5
  title: 'Solvent-5: Diethyl Ether'
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/6344
    rdf_type:
      id: CHEBI:15767
      title: dichloromethane
    title: Dichloromethane
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 50.0
  id: https://www.chemotion-repository.net/pid/56408_Solvent-6
  title: 'Solvent-6: Dichloromethane'
used_starting_material:
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/61259
    rdf_type:
      id: CHEBI:35496
      title: fluorobenzenes
  has_amount:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
    title: Amount [mmol]
    unit: https://qudt.org/vocab/unit/MilliMOL
    value: 9.862
  has_density:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Density
    title: Density [g/mL]
    unit: https://qudt.org/vocab/unit/GM-PER-MilliL
    value: 1.601
  has_mass:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    title: Mass [mg]
    unit: https://qudt.org/vocab/unit/MilliGM
    value: 1761.1
  has_molar_equivalent:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: Molar Equivalent
    unit: https://qudt.org/vocab/unit/PERCENT
    value: 1.085
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 1.1
  id: https://www.chemotion-repository.net/pid/56408_StartMat-1
  title: 'StartMat-1: 1-bromo-2-fluorobenzene'
- composed_of:
  - id: https://pubchem.ncbi.nlm.nih.gov/compound/66180
    iupac_name:
    - value: chloro(diphenyl)phosphine
    molecular_formula:
    - value: C12H10ClP
    rdf_type:
      id: CHEBI:63258
      title: phosphine derivative
  has_amount:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
    title: Amount [mmol]
    unit: https://qudt.org/vocab/unit/MilliMOL
    value: 9.091
  has_density:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Density
    title: Density [g/mL]
    unit: https://qudt.org/vocab/unit/GM-PER-MilliL
    value: 1.229
  has_mass:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    title: Mass [mg]
    unit: https://qudt.org/vocab/unit/MilliGM
    value: 2089.3
  has_molar_equivalent:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: Molar Equivalent
    unit: https://qudt.org/vocab/unit/PERCENT
    value: 1.0
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 1.7
  id: https://www.chemotion-repository.net/pid/56408_StartMat-2
  title: 'StartMat-2: chloro(diphenyl)phosphine'

```
## Dataset-001
### Input
```yaml
description:
- Dataset for 13C nuclear magnetic resonance spectroscopy (13C NMR)
id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1
other_identifier:
- notation: https://www.chemotion-repository.net/pid/37012
theme:
- preferred_label:
  - Science and technology
title:
- 13C nuclear magnetic resonance spectroscopy (13C NMR)
was_generated_by:
- description:
  - The analysis of the spectrum generated by a 13C nuclear magnetic resonance spectroscopy
  id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1#DataGeneratingActivity

```
## MaterialSample-001
### Input
```yaml
derived_from:
  id: https://www.wikidata.org/wiki/Q4204
  rdf_type:
    id: ENVO:01000174
    title: forest biome
has_mass:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
  title: Mass in mg
  unit: https://qudt.org/vocab/unit/MilliGM
  value: 300.0
has_physical_state: SOLID
has_pressure:
- description: This is just a test value for this attribute, well knowing that this
    value makes no sense for a piece of wood
  has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
  title: Pressure in Bar
  unit: https://qudt.org/vocab/unit/BAR
  value: 2.0
has_temperature:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
  title: Temperature
  unit: https://qudt.org/vocab/unit/DEG_C
  value: 20.0
has_volume:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
  title: Volume in L
  unit: https://qudt.org/vocab/unit/L
  value: 0.03
id: https://www.example.com/wood3000
other_identifier:
- notation: https://www.chemotion-repository.net/pid/50440
rdf_type:
  id: ENVO:00002040
  title: wood
title: Philip's wood sample

```
## ReactionRecordingDataset-001
### Input
```yaml
description:
- This dataset contains the recorded information for the Chemotion Repository synthesis
  CRR-56408.
id: doi:10.14272/reaction/SA-FUHFF-UHFFFADPSC-MTSVGCFANK-UHFFFADPSC-NUHFF-NUHFF-NUHFF-ZZZ
is_about_activity:
- description:
  - Synthesis of 1-diphenylphosphoryl-2-fluorobenzene via lithiation-phosphination-oxidation
  generated_product:
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/13005284
      iupac_name:
      - value: 1-diphenylphosphoryl-2-fluorobenzene
      molecular_formula:
      - value: C18H14FOP
    has_amount:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
      title: Amount [mmol]
      unit: https://qudt.org/vocab/unit/MilliMOL
      value: 7.779
    has_mass:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      title: Mass [mg]
      unit: https://qudt.org/vocab/unit/MilliGM
      value: 2328.0
    has_physical_state: SOLID
    has_qualitative_attribute:
    - rdf_type:
        id: PATO:0000337
        title: colorless
      title: 'property: colorless'
      value: colorless
    id: https://dx.doi.org/10.14272/MTSVGCFANKMACF-UHFFFAOYSA-N.1
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: Reaction mixture containing crude 1-diphenylphosphoryl-2-fluorobenzene
  has_duration: PT22H
  has_qualitative_attribute:
  - rdf_type:
      id: IAO:0020000
      title: identifier
    title: RInChI
    value: 1.00.1S/C12H10ClP/c13-14(11-7-3-1-4-8-11) 12-9-5-2-6-10-12/h1-10H!C6H4BrF/c7-5-3-1-2-4-6(5)8/h1-4H<>C18H14FOP/c19-17-13-7-8-14-18(17)21(20,15-9-3-1-4-10-15)16-11-5-2-6-12-16/h1-14H<>C2H4O2/c1-2(3)4/h1H3,(H,3,4)!C2H6O/c1-2-3/h3H,2H2,1H3!C2H6O/c1-2-3/h3H,2H2,1H3!C4H8O/c1-2-4-5-3-1/h1-4H2!C4H8O/c1-2-4-5-3-1/h1-4H2!C4H9.Li/c1-3-4-2;/h1,3-4H2,2H3;!H2O2/c1-2/h1-2H/d+
  - rdf_type:
      id: IAO:0020000
      title: identifier
    title: Long-RInChIKey
    value: SA-FUHFF-XGRJZXREYAXTGV-UHFFFAOYSA-N-IPWBFGUBXWMIPR-UHFFFAOYSA-N--MTSVGCFANKMACF-UHFFFAOYSA-N--QTBSBXVTEAMEQO-UHFFFAOYSA-N-LFQSCWFLJHTTHZ-UHFFFAOYSA-N-LFQSCWFLJHTTHZ-UHFFFAOYSA-N-WYURNTSHIVDZCO-UHFFFAOYSA-N-WYURNTSHIVDZCO-UHFFFAOYSA-N-MZRVEZGGRBJDDB-UHFFFAOYSA-N-MHAJPDPJQMAIIY-UHFFFAOYSA-N
  - rdf_type:
      id: IAO:0020000
      title: identifier
    title: Short-RInChIKey
    value: SA-FUHFF-SCESBIRHVX-MTSVGCFANK-IWBUMUHRPY-NUHFF-NUHFF-NUHFF-ZZZ
  - rdf_type:
      id: IAO:0020000
      title: identifier
    title: Web-RInChIKey
    value: BOMQVCJFVRPGKEKDX-NUHFFFADPSCTJSA
  - description: The status of the reaction
    rdf_type:
      id: SIO:001326
      title: status descriptor
    title: Status
    value: Successful
  has_yield:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    title: Yield [%]
    type:
      id: VOC4CAT:0005005
      title: yield
    unit: http://qudt.org/vocab/unit/PERCENT
    value: 86
  id: https://www.chemotion-repository.net/pid/56408
  rdf_type:
    id: RXNO:0000329
    title: planned synthesis
  title:
  - Chemotion Repository synthesis CRR-56408
  used_reactant:
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/53627823
      rdf_type:
        id: CHEBI:51469
        title: butyllithium
    has_amount:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
      title: Amount [mmol]
      unit: https://qudt.org/vocab/unit/MilliMOL
      value: 10.75
    has_concentration:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstanceConcentration
      title: Molarity [M]
      unit: https://qudt.org/vocab/unit/MOL-PER-L
      value: 2.5
    has_mass:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      title: Mass [mg]
      unit: https://qudt.org/vocab/unit/MilliGM
      value: 688.594
    has_molar_equivalent:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: Molar Equivalent
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.183
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 4.3
    id: https://www.chemotion-repository.net/pid/56408_Reactant-1
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'Reactant-1: n-BuLi'
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/784
      rdf_type:
        id: CHEBI:16240
        title: Hydrogen Peroxide
    has_amount:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
      title: Amount [mmol]
      unit: https://qudt.org/vocab/unit/MilliMOL
      value: 40.696
    has_density:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Density
      title: Density [g/mL]
      unit: https://qudt.org/vocab/unit/GM-PER-MilliL
      value: 1.13
    has_mass:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      title: Mass [mg]
      unit: https://qudt.org/vocab/unit/MilliGM
      value: 3955.0
    has_molar_equivalent:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: Molar Equivalent
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 4.477
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 3.5
    id: https://www.chemotion-repository.net/pid/56408_Reactant-2
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'Reactant-2: Hydrogen Peroxide'
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/176
      rdf_type:
        id: CHEBI:15366
        title: acetic acid
    has_amount:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
      title: Amount [mmol]
      unit: https://qudt.org/vocab/unit/MilliMOL
      value: 30.502
    has_density:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Density
      title: Density [g/mL]
      unit: https://qudt.org/vocab/unit/GM-PER-MilliL
      value: 1.06
    has_mass:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      title: Mass [mg]
      unit: https://qudt.org/vocab/unit/MilliGM
      value: 1908.0
    has_molar_equivalent:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: Molar Equivalent
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 3.355
    has_qualitative_attribute:
    - rdf_type:
        id: AFR:0002371
        title: purity
      title: Grade/Purity
      value: Glacial
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 1.8
    id: https://www.chemotion-repository.net/pid/56408_Reactant-3
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'Reactant-3: glacial acetic acid'
  used_reactor:
  - has_qualitative_attribute:
    - title: Argon atmosphere of the glass ware
      type:
        id: VOC4CAT:0007809
        title: atmosphere
      value: Argon atmosphere
    - title: dryness of the used glass ware
      type:
        id: PATO:0001824
        title: dry
      value: dry
    id: https://www.chemotion-repository.net/pid/56408_Reactor-1
    rdf_type:
      id: OBI:0002089
      title: container with environmental control
    title: dry glass ware under argon atmosphere
  used_solvent:
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/8028
      iupac_name:
      - value: oxolane
      rdf_type:
        id: CHEBI:26911
        title: oxolane
      title: THF
    has_percentage_of_total:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: PercentageOfTotal
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 13
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 24.0
    id: https://www.chemotion-repository.net/pid/56408_Solvent-1
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'Solvent-1: THF'
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/8028
      title: THF
    has_percentage_of_total:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: PercentageOfTotal
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 2
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 3.0
    id: https://www.chemotion-repository.net/pid/56408_Solvent-2
    title: 'Solvent-2: THF'
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/702
      rdf_type:
        id: CHEBI:16236
        title: ethanol
      title: Ethanol
    has_percentage_of_total:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: PercentageOfTotal
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 78
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 150.0
    id: https://www.chemotion-repository.net/pid/56408_Solvent-3
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'Solvent-3: Ethanol'
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/702
      title: Ethanol
    has_percentage_of_total:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: PercentageOfTotal
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 8
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 15.0
    id: https://www.chemotion-repository.net/pid/56408_Solvent-4
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'Solvent-4: Ethanol'
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/3283
      rdf_type:
        id: CHEBI:35702
        title: diethyl ether
      title: Diethyl Ether
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 150.0
    id: https://www.chemotion-repository.net/pid/56408_Solvent-5
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'Solvent-5: Diethyl Ether'
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/6344
      rdf_type:
        id: CHEBI:15767
        title: dichloromethane
      title: Dichloromethane
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 50.0
    id: https://www.chemotion-repository.net/pid/56408_Solvent-6
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'Solvent-6: Dichloromethane'
  used_starting_material:
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/61259
      rdf_type:
        id: CHEBI:35496
        title: fluorobenzenes
    has_amount:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
      title: Amount [mmol]
      unit: https://qudt.org/vocab/unit/MilliMOL
      value: 9.862
    has_density:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Density
      title: Density [g/mL]
      unit: https://qudt.org/vocab/unit/GM-PER-MilliL
      value: 1.601
    has_mass:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      title: Mass [mg]
      unit: https://qudt.org/vocab/unit/MilliGM
      value: 1761.1
    has_molar_equivalent:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: Molar Equivalent
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.085
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 1.1
    id: https://www.chemotion-repository.net/pid/56408_StartMat-1
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'StartMat-1: 1-bromo-2-fluorobenzene'
  - composed_of:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/66180
      iupac_name:
      - value: chloro(diphenyl)phosphine
      molecular_formula:
      - value: C12H10ClP
      rdf_type:
        id: CHEBI:63258
        title: phosphine derivative
    has_amount:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
      title: Amount [mmol]
      unit: https://qudt.org/vocab/unit/MilliMOL
      value: 9.091
    has_density:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Density
      title: Density [g/mL]
      unit: https://qudt.org/vocab/unit/GM-PER-MilliL
      value: 1.229
    has_mass:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
      title: Mass [mg]
      unit: https://qudt.org/vocab/unit/MilliGM
      value: 2089.3
    has_molar_equivalent:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
      title: Molar Equivalent
      unit: https://qudt.org/vocab/unit/PERCENT
      value: 1.0
    has_volume:
    - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
      title: Volume [mL]
      unit: https://qudt.org/vocab/unit/MilliL
      value: 1.7
    id: https://www.chemotion-repository.net/pid/56408_StartMat-2
    rdf_type:
      id: CHEBI:59999
      title: chemical substance
    title: 'StartMat-2: chloro(diphenyl)phosphine'
related_resource:
- id: doi:10.1080/03086648208081193
  title: SYNTHESE UND NMR-UNTERSUCHUNGEN VON 2-FLUOR-TRIPHENYLPHOSPHINEN UND IHREN
    DERIVATEN
- id: doi:10.1016/j.jorganchem.2007.08.037
  title: Synthesis and thermal behavior of dimethyl scandium complexes featuring anilido-phosphinimine
    ancillary ligands
- id: doi:10.1021/ja00491a030
  title: Role of through space 2p-3d overlap in the alkylation of phosphines
- id: doi:10.1002/adsc.202400919
  title: Arylation of Secondary Phosphines with Diaryliodonium Salts under Metal-Free
    and Non-Photochemical Conditions
title:
- Dataset for Chemotion Repository synthesis CRR-56408
was_generated_by:
- description:
  - "The reaction has been conducted in dry glass ware under argon atmosphere. A solution\
    \ of 1-bromo-2-fluorobenzene (1.76 g, 1.10 mL, 9.86 mmol, 1.08 equiv) in anhydrous\
    \ THF (24.0 mL) was cooled to -78 \xB0C, and n-BuLi (689 mg, 4.30 mL, 10.8 mmol,\
    \ 2.50M in hexane, 1.18 equiv) was added drop-wise over 10 min. After stirring\
    \ for further 50 min, a solution of chloro(diphenyl)phosphine (2.09 g, 1.70 mL,\
    \ 9.09 mmol, 1.00 equiv) in anhydrous THF (3.00 mL) was added drop-wise over 10\
    \ min, and the reaction mixture was stirred for 8 h at -78 \xB0C. The reaction\
    \ mixture was allowed to warm up to 25 \xB0C over 8 h, and was then quenched by\
    \ the addition of 1 M HCl (10.0 mL). The phases were separated, and the aqueous\
    \ phase was extracted with diethyl ether (3 \xD7 50.0 mL). Then, the combined\
    \ organic layers were washed with sat. aq. NaHCO3-solution (50.0 mL), water (50.0\
    \ mL), and with brine (50.0 mL). The organic phase was dried over Na2SO4, filtered,\
    \ and the solvent was evaporated under reduced pressure to afford the phosphine\
    \ intermediate as a pale yellow oil. The crude phosphine intermediate was dissolved\
    \ in ethanol (150 mL), and cooled to 0 \xB0C. Under vigorous stirring, a solution\
    \ of hydrogen peroxide (3.95 g, 3.50 mL, 40.7 mmol, 35%, 4.48 equiv), and glacial\
    \ acetic acid (1.91 g, 1.80 mL, 30.5 mmol, 3.36 equiv) in ethanol (15.0 mL) was\
    \ added drop-wise over 15 min. The mixture was stirred for 2 h at 0 \xB0C, and\
    \ was then refluxed for 2 h. After evaporating the solvent under reduced pressure,\
    \ the crude was dissolved in dichloromethane (50.0 mL), washed with sat. aq. NaHCO3-solution\
    \ (2 \xD7 25.0 mL), water (25.0 mL), and brine (25.0 mL). The organic layer was\
    \ dried over Na2SO4, before evaporating the solvent under reduced pressure. Additional\
    \ information for publication and purification details: The crude product was\
    \ purified via flash-chromatography (Interchim\xAE\_puriFLASH XS520) on silica\
    \ gel (PF-30SIHP-F0040) using cyclohexane/ethyl acetate 35:65 to 30:70 in 10 CV\
    \ (1 CV = 52.7 mL; flowrate = 26.0 mL/min). The product 1-diphenylphosphoryl-2-fluorobenzene\
    \ (2.33 g, 7.78 mmol, 86% yield) was obtained as a colorless solid."
  evaluated_activity:
  - has_part:
    - id: https://www.chemotion-repository.net/pid/56408#step-1
      title:
      - 'Step 1: Lithiation and Phosphination'
    - description:
      - "The reaction mixture was allowed to warm up to 25 \xB0C over 8 h, and was\
        \ then quenched by the addition of 1 M HCl (10.0 mL). The phases were separated,\
        \ and the aqueous phase was extracted with diethyl ether (3 \xD7 50.0 mL).\
        \ Then, the combined organic layers were washed with sat. aq. NaHCO3-solution\
        \ (50.0 mL), water (50.0 mL), and with brine (50.0 mL). The organic phase\
        \ was dried over Na2SO4, filtered, and the solvent was evaporated under reduced\
        \ pressure to afford the phosphine intermediate as a pale yellow oil."
      had_input_activity:
      - id: https://www.chemotion-repository.net/pid/56408#step-1
        title:
        - 'Step 1: Lithiation and Phosphination'
      had_input_entity:
      - id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-2
        title: 'step-1_ReactionMixture-2: 1-bromo-2-fluorobenzene & chloro(diphenyl)phosphine
          in THF + n-BuLi'
      had_output_entity:
      - id: https://www.chemotion-repository.net/pid/56408#step-2_Output-1
        rdf_type:
          id: CHEBI:60004
          title: mixture
        title: 'step-2_Output-1: Crude phosphine intermediate (pale yellow oil)'
      has_part:
      - description:
        - "The reaction mixture was allowed to warm up to 25 \xB0C over 8 h"
        had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_part-6
          title:
          - 'step-1_part-6: stirring for 8 hours'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-2
          title: 'step-1_ReactionMixture-2: 1-bromo-2-fluorobenzene & chloro(diphenyl)phosphine
            in THF + n-BuLi'
        has_qualitative_attribute:
        - title: duration of step-2_part-1
          type:
            id: https://schema.org/Duration
            title: Duration
          value: PT8H
        has_quantitative_attribute:
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
          title: 'start temperature '
          unit: http://qudt.org/vocab/unit/DEG_C
          value: -78
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
          title: end temperature
          unit: http://qudt.org/vocab/unit/DEG_C
          value: 25
        id: https://www.chemotion-repository.net/pid/56408#step-2_part-1
        rdf_type:
          id: ENVO:01001739
          title: warming of a fluid
        title:
        - "step-2_part-1: Warming to 25 \xB0C over 8 h"
      - description:
        - The reaction mixture was quenched by the addition of 1 M HCl (10.0 mL)
        had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_part-1
          title:
          - "step-2_part-1: Warming to 25 \xB0C over 8 h"
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-2
          title: 'step-1_ReactionMixture-2: 1-bromo-2-fluorobenzene & chloro(diphenyl)phosphine
            in THF + n-BuLi'
        - has_part:
          - id: https://pubchem.ncbi.nlm.nih.gov/compound/313
            rdf_type:
              id: CHEBI:17883
              title: hydrogen chloride
          has_quantitative_attribute:
          - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
            title: Volume [mL]
            unit: https://qudt.org/vocab/unit/MilliL
            value: 10.0
          - has_quantity_type: http://qudt.org/vocab/quantitykind/Concentration
            rdf_type:
              id: CHMO:0002820
              title: concentration
            title: Concentration [mol/L]
            unit: https://qudt.org/vocab/unit/MOL-PER-L
            value: 1
          id: https://www.chemotion-repository.net/pid/56408#step-2_Reagent-1
          title: 'step-2_Reagent-1: HCl'
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-1
          title: step-2_ReactionMixture-1
        id: https://www.chemotion-repository.net/pid/56408#step-2_part-2
        rdf_type:
          id: OBI:0000274
          title: adding a material entity into a target
        title:
        - 'step-2_part-2: Quench with 1 M HCl'
      - description:
        - "The phases were separated, and the aqueous phase was extracted with diethyl\
          \ ether (3 \xD7 50.0 mL)."
        had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_part-2
          title:
          - 'step-2_part-2: Quench with 1 M HCl'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-1
          title: step-2_ReactionMixture-1
        - id: https://www.chemotion-repository.net/pid/56408_Solvent-5
          title: 'Solvent-5: Diethyl Ether'
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-2
          title: step-2_ReactionMixture-2
        id: https://www.chemotion-repository.net/pid/56408#step-2_part-3
        rdf_type:
          id: CHMO:0001577
          title: extraction
        title:
        - 'step-2_part-3: Extraction with Diethyl Ether'
      - description:
        - The combined organic layers were washed with sat. aq. NaHCO3-solution (50.0
          mL), water (50.0 mL), and with brine (50.0 mL).
        had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_part-3
          title:
          - 'step-2_part-3: Extraction with Diethyl Ether'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-2
          title: step-2_ReactionMixture-2
        - has_part:
          - id: https://pubchem.ncbi.nlm.nih.gov/compound/516892
            rdf_type:
              id: CHEBI:32139
              title: sodium hydrogencarbonate
            title: sodium hydrogen carbonate
          has_quantitative_attribute:
          - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
            title: Volume [mL]
            unit: https://qudt.org/vocab/unit/MilliL
            value: 50.0
          id: https://www.chemotion-repository.net/pid/56408#step-2_Reagent-2
          rdf_type:
            id: CHEBI:59999
            title: chemical substance
          title: 'step-2_Reagent-2: NaHCO3'
        - has_quantitative_attribute:
          - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
            title: Volume [mL]
            unit: https://qudt.org/vocab/unit/MilliL
            value: 50.0
          id: https://www.chemotion-repository.net/pid/56408#step-2_Reagent-3
          rdf_type:
            id: ENVO:00002006
            title: liquid water
          title: 'step-2_Reagent-3: water'
        - has_quantitative_attribute:
          - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
            title: Volume [mL]
            unit: https://qudt.org/vocab/unit/MilliL
            value: 50.0
          id: https://www.chemotion-repository.net/pid/56408#step-2_Reagent-4
          rdf_type:
            id: ENVO:00003044
            title: brine
          title: 'step-2_Reagent-4: brine'
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-3
          title: step-2_ReactionMixture-3
        id: https://www.chemotion-repository.net/pid/56408#step-2_part-4
        rdf_type:
          id: OBI:0302888
          title: washing
        title:
        - 'step-2_part-4: Washing (NaHCO3, Water, Brine)'
      - description:
        - The step-2_ReactionMixture-3 organic phase was dried over Na2SO4, filtered
        had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_part-4
          title:
          - 'step-2_part-4: Washing (NaHCO3, Water, Brine)'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-3
          title: step-2_ReactionMixture-3
        - has_part:
          - id: https://pubchem.ncbi.nlm.nih.gov/compound/24436
            rdf_type:
              id: CHEBI:32149
              title: sodium sulfate
          id: https://www.chemotion-repository.net/pid/56408#step-2_Reagent-5
          rdf_type:
            id: CHEBI:59999
            title: chemical substance
          title: 'step-2_Reagent-5: Na2SO4'
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-4
          title: step-2_ReactionMixture-4
        id: https://www.chemotion-repository.net/pid/56408#step-2_part-5
        rdf_type:
          id: CHMO:0001549
          title: sample drying
        title:
        - 'step-2_part-5: Drying over Na2SO4'
      - description:
        - The step-2_ReactionMixture-4 organic phase was filtered.
        had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_part-5
          title:
          - 'step-2_part-5: Drying over Na2SO4'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-4
          title: step-2_ReactionMixture-4
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-5
          title: step-2_ReactionMixture-5
        id: https://www.chemotion-repository.net/pid/56408#step-2_part-6
        rdf_type:
          id: CHMO:0001640
          title: filtration
        title:
        - 'step-2_part-6: Filtering'
      - description:
        - the solvent was evaporated under reduced pressure
        had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_part-6
          title:
          - 'step-2_part-6: Filtering'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_ReactionMixture-5
          title: step-2_ReactionMixture-5
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_Output-1
          title: 'step-2_Output-1: Crude phosphine intermediate (pale yellow oil)'
        id: https://www.chemotion-repository.net/pid/56408#step-2_part-7
        rdf_type:
          id: CHMO:0002208
          title: solvent evaporation
        title:
        - 'step-2_part-7: Evaporation to afford crude oil'
      id: https://www.chemotion-repository.net/pid/56408#step-2
      rdf_type:
        id: OBI:0000094
        title: material processing
      title:
      - 'Step 1: Warm-up, Quench, and Extraction'
    - id: https://www.chemotion-repository.net/pid/56408#step-3
      title:
      - 'Step 3: Oxidation to Phosphine Oxide'
    - description:
      - Evaporation of solvent, dissolution in DCM, washing (NaHCO3, water, brine),
        drying, and final evaporation.
      had_input_activity:
      - id: https://www.chemotion-repository.net/pid/56408#step-3
        title:
        - 'Step 3: Oxidation to Phosphine Oxide'
      had_input_entity:
      - id: https://www.chemotion-repository.net/pid/56408#step-3_Output-1
        title: 'step-3_Output-1: containing crude 1-diphenylphosphoryl-2-fluorobenzene'
      had_output_entity:
      - id: https://www.chemotion-repository.net/pid/56408#step-4_Output-1
        rdf_type:
          id: CHEBI:60004
          title: mixture
        title: 'step-4_Output-1: Crude 1-diphenylphosphoryl-2-fluorobenzene'
      has_part:
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_part-5
          title:
          - 'step-3_part-5: reflux for 2 hours'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_Output-1
          title: 'step-3_Output-1: containing crude 1-diphenylphosphoryl-2-fluorobenzene'
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_ReactionMixture-1
          rdf_type:
            id: CHEBI:60004
            title: mixture
          title: 'step-4_ReactionMixture-1: crude residue after evaporation'
        id: https://www.chemotion-repository.net/pid/56408#step-4_part-1
        rdf_type:
          id: CHMO:0002208
          title: solvent evaporation
        title:
        - 'step-4_part-1: Evaporation of solvent under reduced pressure'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_part-1
          title:
          - 'step-4_part-1: Evaporation of solvent under reduced pressure'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_ReactionMixture-1
          title: 'step-4_ReactionMixture-1: crude residue after evaporation'
        - id: https://www.chemotion-repository.net/pid/56408_Solvent-6
          title: 'Solvent-6: Dichloromethane'
        had_output_entity:
        - has_part:
          - id: https://www.chemotion-repository.net/pid/56408#step-4_ReactionMixture-1
            title: 'step-4_ReactionMixture-1: crude residue after evaporation'
          - id: https://www.chemotion-repository.net/pid/56408_Solvent-6
            title: 'Solvent-6: Dichloromethane'
          id: https://www.chemotion-repository.net/pid/56408#step-4_Solution-1
          rdf_type:
            id: CHEBI:75958
            title: solution
          title: Solution in Dichloromethane
        id: https://www.chemotion-repository.net/pid/56408#step-4_part-2
        rdf_type:
          id: CHMO:0002773
          title: dissolving
        title:
        - 'step-4_part-2: Dissolution in Dichloromethane'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_part-2
          title:
          - 'step-4_part-2: Dissolution in Dichloromethane'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_Solution-1
          title: Solution in Dichloromethane
        - has_part:
          - id: https://pubchem.ncbi.nlm.nih.gov/compound/516892
            title: sodium hydrogen carbonate
          has_quantitative_attribute:
          - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
            unit: https://qudt.org/vocab/unit/MilliL
            value: 50.0
          id: https://www.chemotion-repository.net/pid/56408#step-4_Reagent-1
          title: Sat. aq. NaHCO3 solution (2 x 25.0 mL)
        - has_quantitative_attribute:
          - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
            unit: https://qudt.org/vocab/unit/MilliL
            value: 25.0
          id: https://www.chemotion-repository.net/pid/56408#step-4_Reagent-2
          rdf_type:
            id: ENVO:00002006
            title: liquid water
          title: Water (25.0 mL)
        - has_quantitative_attribute:
          - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
            unit: https://qudt.org/vocab/unit/MilliL
            value: 25.0
          id: https://www.chemotion-repository.net/pid/56408#step-4_Reagent-3
          rdf_type:
            id: ENVO:00003044
            title: brine
          title: Brine (25.0 mL)
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_ReactionMixture-2
          rdf_type:
            id: CHEBI:59999
            title: chemical substance
          title: Washed organic layer
        id: https://www.chemotion-repository.net/pid/56408#step-4_part-3
        rdf_type:
          id: OBI:0302888
          title: washing
        title:
        - 'step-4_part-3: Washing (NaHCO3, Water, Brine)'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_part-3
          title:
          - 'step-4_part-3: Washing (NaHCO3, Water, Brine)'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_ReactionMixture-2
          title: 'step-4_ReactionMixture-2: Washed organic layer'
        - has_part:
          - id: https://pubchem.ncbi.nlm.nih.gov/compound/24436
            title: sodium sulfate
          id: https://www.chemotion-repository.net/pid/56408#step-4_Reagent-4
          rdf_type:
            id: CHEBI:59999
            title: chemical substance
          title: 'step-4_Reagent-4: Sodium sulfate (Na2SO4)'
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_ReactionMixture-3
          rdf_type:
            id: CHEBI:59999
            title: chemical substance
          title: 'step-4_ReactionMixture-3: dried organic solution'
        id: https://www.chemotion-repository.net/pid/56408#step-4_part-4
        rdf_type:
          id: CHMO:0001549
          title: sample drying
        title:
        - 'step-4_part-4: Drying over Na2SO4'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_part-4
          title:
          - 'step-4_part-4: Drying over Na2SO4'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_ReactionMixture-3
          title: 'step-4_ReactionMixture-3: dried organic solution'
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-4_Output-1
          rdf_type:
            id: CHEBI:59999
            title: chemical substance
          title: 'step-4_Output-1: Crude 1-diphenylphosphoryl-2-fluorobenzene'
        id: https://www.chemotion-repository.net/pid/56408#step-4_part-5
        rdf_type:
          id: CHMO:0002208
          title: solvent evaporation
        title:
        - 'step-4_part-5: Evaporation to afford crude product'
      id: https://www.chemotion-repository.net/pid/56408#step-4
      rdf_type:
        id: OBI:0000094
        title: material processing
      title:
      - 'STEP 4: Work-up of Oxidation Mixture'
    - carried_out_by:
      - description: Flash chromatography system.
        has_part:
        - description: Silica gel column used for purification.
          has_part:
          - id: https://www.chemotion-repository.net/pid/56408#step-5_device-3
            part_of:
            - id: https://www.chemotion-repository.net/pid/56408#step-5_device-2
              title: Interchim puriFLASH Column (PF-30SIHP-F0040)
            rdf_type:
              id: CHMO:0002782
              title: silica gel
            title: 'step-5_StationaryPhase: Silica gel (PF-30SIHP-F0040)'
          has_quantitative_attribute:
          - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
            title: Column Volume (1 CV)
            unit: https://qudt.org/vocab/unit/MilliL
            value: 52.7
          id: https://www.chemotion-repository.net/pid/56408#step-5_device-2
          part_of:
          - id: https://www.chemotion-repository.net/pid/56408#step-5_device-1
            title: Interchim puriFLASH XS520
          rdf_type:
            id: OBI:0000038
            title: chromatography column
          title: Interchim puriFLASH Column (PF-30SIHP-F0040)
        id: https://www.chemotion-repository.net/pid/56408#step-5_device-1
        rdf_type:
          id: OBI:0000485
          title: chromatography instrument
        title: Interchim puriFLASH XS520
      description:
      - "The crude product was purified via flash-chromatography (Interchim\xAE\_\
        puriFLASH XS520) on silica gel (PF-30SIHP-F0040) using cyclohexane/ethyl acetate\
        \ 35:65 to 30:70 in 10 CV (1 CV = 52.7 mL; flowrate = 26.0 mL/min). The product\
        \ 1-diphenylphosphoryl-2-fluorobenzene (2.33 g, 7.78 mmol, 86% yield) was\
        \ obtained as a colorless solid."
      had_input_activity:
      - id: https://www.chemotion-repository.net/pid/56408#step-4
        title:
        - 'STEP 4: Work-up of Oxidation Mixture'
      had_input_entity:
      - id: https://www.chemotion-repository.net/pid/56408#step-4_Output-1
        title: 'step-4_Output-1: Crude 1-diphenylphosphoryl-2-fluorobenzene'
      - has_part:
        - id: https://pubchem.ncbi.nlm.nih.gov/compound/8078
          rdf_type:
            id: CHEBI:29005
            title: cyclohexane
        id: https://www.chemotion-repository.net/pid/56408#step-5_Solvent-1
        title: 'step-5_Solvent-1: Cyclohexane'
      - has_part:
        - id: https://pubchem.ncbi.nlm.nih.gov/compound/8857
          rdf_type:
            id: CHEBI:27750
            title: ethyl acetate
        id: https://www.chemotion-repository.net/pid/56408#step-5_Solvent-2
        title: 'step-5_Solvent-2: Ethyl acetate'
      had_output_entity:
      - id: https://www.chemotion-repository.net/pid/56408#step-5_Product
        rdf_type:
          id: CHEBI:59999
          title: chemical substance
        title: 'step-5_Product: 1-diphenylphosphoryl-2-fluorobenzene'
      has_quantitative_attribute:
      - has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFlowRate
        title: Flow Rate
        unit: https://qudt.org/vocab/unit/MilliL-PER-MIN
        value: 26.0
      - has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
        title: Initial Ethyl Acetate Concentration
        unit: http://qudt.org/vocab/unit/PERCENT
        value: 65.0
      - has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
        title: Final Ethyl Acetate Concentration
        unit: http://qudt.org/vocab/unit/PERCENT
        value: 70.0
      - has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
        title: Initial Cyclohexane Concentration
        unit: http://qudt.org/vocab/unit/PERCENT
        value: 35.0
      - has_quantity_type: http://qudt.org/vocab/quantitykind/VolumeFraction
        title: Final Cyclohexane Concentration
        unit: http://qudt.org/vocab/unit/PERCENT
        value: 30.0
      - has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
        title: Gradient Duration in Column Volumes
        unit: http://qudt.org/vocab/unit/UNITLESS
        value: 10.0
      id: https://www.chemotion-repository.net/pid/56408#step-5
      rdf_type:
        id: CHMO:0002582
        title: flash chromatography
      title:
      - 'step-5: Purification via Flash Chromatography'
    has_reaction_step:
    - description:
      - "The reaction has been conducted in dry glass ware under argon atmosphere.\
        \ A solution of 1-bromo-2-fluorobenzene (1.76 g, 1.10 mL, 9.86 mmol, 1.08\
        \ equiv) in anhydrous THF (24.0 mL) was cooled to -78 \xB0C, and n-BuLi (689\
        \ mg, 4.30 mL, 10.8 mmol, 2.50M in hexane, 1.18 equiv) was added drop-wise\
        \ over 10 min. After stirring for further 50 min, a solution of chloro(diphenyl)phosphine\
        \ (2.09 g, 1.70 mL, 9.09 mmol, 1.00 equiv) in anhydrous THF (3.00 mL) was\
        \ added drop-wise over 10 min, and the reaction mixture was stirred for 8\
        \ h at -78 \xB0C."
      generated_product:
      - id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-2
        title: 'step-1_ReactionMixture-2: 1-bromo-2-fluorobenzene & chloro(diphenyl)phosphine
          in THF + n-BuLi'
      has_duration: PT9H10M
      has_part:
      - had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408_Solvent-1
          title: 'Solvent-1: THF'
        - id: https://www.chemotion-repository.net/pid/56408_StartMat-1
          title: 'StartMat-1: 1-bromo-2-fluorobenzene'
        had_output_entity:
        - has_part:
          - id: https://www.chemotion-repository.net/pid/56408_Solvent-1
            title: 'Solvent-1: THF'
          - id: https://www.chemotion-repository.net/pid/56408_StartMat-1
            title: 'StartMat-1: 1-bromo-2-fluorobenzene'
          id: https://www.chemotion-repository.net/pid/56408#step-1_Solution-1
          rdf_type:
            id: CHEBI:75958
            title: solution
          title: step-1_Solution-1 of 1-bromo-2-fluorobenzene in Tetrahydrofuran
        id: https://www.chemotion-repository.net/pid/56408#step-1_part-1
        rdf_type:
          id: CHMO:0002773
          title: dissolving
        title:
        - 'step-1_part-1: dissolving of 1-bromo-2-fluorobenzene in Tetrahydrofuran'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_part-1
          title:
          - 'step-1_part-1: dissolving of 1-bromo-2-fluorobenzene in Tetrahydrofuran'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_Solution-1
          title: 'step-1_Solution-1: 1-bromo-2-fluorobenzene in Tetrahydrofuran'
        - id: https://www.chemotion-repository.net/pid/56408_Reactant-1
          title: 'Reactant-1: n-BuLi'
        had_output_entity:
        - has_part:
          - id: https://www.chemotion-repository.net/pid/56408#step-1_Solution-1
            title: 'step-1_Solution-1: 1-bromo-2-fluorobenzene in Tetrahydrofuran'
          - id: https://www.chemotion-repository.net/pid/56408_Reactant-1
            title: 'Reactant-1: n-BuLi'
          id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-1
          rdf_type:
            id: CHEBI:60004
            title: mixture
          title: 'step-1_ReactionMixture-1: 1-bromo-2-fluorobenzene in Tetrahydrofuran
            and n-BuLi'
        has_qualitative_attribute:
        - type:
            id: https://schema.org/Duration
            title: Duration
          value: PT10M
        id: https://www.chemotion-repository.net/pid/56408#step-1_part-2
        rdf_type:
          id: OBI:0000274
          title: adding a material entity into a target
        title:
        - 'step-1_part-2: drop-wise addition of n-BuLi (2.5M in hexane)'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_part-2
          title:
          - 'step-1_part-2: drop-wise addition of n-BuLi (2.5M in hexane)'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-1
          title: 'step-1_ReactionMixture-1: 1-bromo-2-fluorobenzene in Tetrahydrofuran
            and n-BuLi'
        has_qualitative_attribute:
        - title: duration of step-1_part-4
          type:
            id: https://schema.org/Duration
            title: Duration
          value: PT50M
        id: https://www.chemotion-repository.net/pid/56408#step-1_part-3
        rdf_type:
          id: CHMO:0002774
          title: stirring
        title:
        - 'step-1_part-3: stirring for 50 minutes'
      - had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408_StartMat-2
          title: 'StartMat-2: chloro(diphenyl)phosphine'
        - id: https://www.chemotion-repository.net/pid/56408_Solvent-2
          title: 'Solvent-2: THF'
        had_output_entity:
        - has_part:
          - id: https://www.chemotion-repository.net/pid/56408_StartMat-2
            title: 'StartMat-2: chloro(diphenyl)phosphine'
          - id: https://www.chemotion-repository.net/pid/56408_Solvent-2
            title: 'Solvent-2: THF'
          id: https://www.chemotion-repository.net/pid/56408#step-1_Solution-2
          rdf_type:
            id: CHEBI:75958
            title: solution
          title: 'step-1_Solution-2: chloro(diphenyl)phosphine in anhydrous THF'
        id: https://www.chemotion-repository.net/pid/56408#step-1_part-4
        rdf_type:
          id: CHMO:0002773
          title: dissolving
        title:
        - 'step-1_part-4: dissolving of chloro(diphenyl)phosphine in anhydrous THF
          (3.00 mL)'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_part-4
          title:
          - 'step-1_part-4: dissolving of chloro(diphenyl)phosphine in anhydrous THF
            (3.00 mL)'
        - id: https://www.chemotion-repository.net/pid/56408#step-1_part-3
          title:
          - 'step-1_part-3: stirring for 50 minutes'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_Solution-2
          title: 'step-1_Solution-2: chloro(diphenyl)phosphine in anhydrous THF'
        - id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-1
          title: 'step-1_ReactionMixture-1: 1-bromo-2-fluorobenzene in Tetrahydrofuran
            and n-BuLi'
        had_output_entity:
        - has_part:
          - id: https://www.chemotion-repository.net/pid/56408#step-1_Solution-2
            title: 'step-1_Solution-2: chloro(diphenyl)phosphine in anhydrous THF'
          - id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-1
            title: 'step-1_ReactionMixture-1: 1-bromo-2-fluorobenzene in Tetrahydrofuran
              and n-BuLi'
          id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-2
          rdf_type:
            id: CHEBI:60004
            title: mixture
          title: 'step-1_ReactionMixture-2: 1-bromo-2-fluorobenzene & chloro(diphenyl)phosphine
            in THF + n-BuLi'
        has_qualitative_attribute:
        - title: duration of step-1_part-5
          type:
            id: https://schema.org/Duration
            title: Duration
          value: PT10M
        id: https://www.chemotion-repository.net/pid/56408#step-1_part-5
        rdf_type:
          id: OBI:0000274
          title: adding a material entity into a target
        title:
        - 'step-1_part-5: drop-wise addition of chloro(diphenyl)phosphine in THF'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_part-5
          title:
          - 'step-1_part-5: drop-wise addition of chloro(diphenyl)phosphine in THF'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-1_ReactionMixture-2
          title: 'step-1_ReactionMixture-2: 1-bromo-2-fluorobenzene & chloro(diphenyl)phosphine
            in THF + n-BuLi'
        has_qualitative_attribute:
        - title: duration of step-1_part-6
          type:
            id: https://schema.org/Duration
            title: Duration
          value: PT8H
        id: https://www.chemotion-repository.net/pid/56408#step-1_part-6
        rdf_type:
          id: CHMO:0002774
          title: stirring
        title:
        - 'step-1_part-6: stirring for 8 hours'
      has_temperature:
      - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
        title: Temperature of reaction step 1
        unit: http://qudt.org/vocab/unit/DEG_C
        value: -78
      id: https://www.chemotion-repository.net/pid/56408#step-1
      rdf_type:
        id: RXNO:0000001
        title: planned reaction step
      title:
      - 'Step 1: Lithiation and Phosphination'
      used_reactant:
      - id: https://www.chemotion-repository.net/pid/56408_Reactant-1
        title: 'Reactant-1: n-BuLi'
      used_reactor:
      - id: https://www.chemotion-repository.net/pid/56408_Reactor-1
        title: dry glass ware under argon atmosphere
      used_solvent:
      - id: https://www.chemotion-repository.net/pid/56408_Solvent-1
        title: 'Solvent-1: THF'
      - id: https://www.chemotion-repository.net/pid/56408_Solvent-2
        title: 'Solvent-2: THF'
      used_starting_material:
      - id: https://www.chemotion-repository.net/pid/56408_StartMat-1
        title: 'StartMat-1: 1-bromo-2-fluorobenzene'
      - id: https://www.chemotion-repository.net/pid/56408_StartMat-2
        title: 'StartMat-2: chloro(diphenyl)phosphine'
    - description:
      - "The crude phosphine intermediate was dissolved in ethanol (150 mL), and cooled\
        \ to 0 \xB0C. Under vigorous stirring, a solution of hydrogen peroxide (3.95\
        \ g, 3.50 mL, 40.7 mmol, 35%, 4.48 equiv), and glacial acetic acid (1.91 g,\
        \ 1.80 mL, 30.5 mmol, 3.36 equiv) in ethanol (15.0 mL) was added drop-wise\
        \ over 15 min. The mixture was stirred for 2 h at 0 \xB0C, and was then refluxed\
        \ for 2 h."
      generated_product:
      - id: https://www.chemotion-repository.net/pid/56408#step-3_Output-1
        title: 'step-3_Output-1: containing crude 1-diphenylphosphoryl-2-fluorobenzene'
      had_input_activity:
      - id: https://www.chemotion-repository.net/pid/56408#step-2
        title:
        - 'Step 2: Warm-up, Quench, and Extraction'
      has_duration: PT4H15M
      has_part:
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_part-6
          title:
          - Filtering
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-2_Output-1
          title: 'step-2_Output-1: Crude phosphine intermediate (pale yellow oil)'
        - id: https://www.chemotion-repository.net/pid/56408_Solvent-3
          title: 'Solvent-3: Ethanol'
        had_output_entity:
        - has_part:
          - id: https://www.chemotion-repository.net/pid/56408#step-2_Output-1
            title: 'step-2_Output-1: Crude phosphine intermediate (pale yellow oil)'
          - id: https://www.chemotion-repository.net/pid/56408_Solvent-3
            title: 'Solvent-3: Ethanol'
          id: https://www.chemotion-repository.net/pid/56408#step-3_Solution-1
          rdf_type:
            id: CHEBI:75958
            title: solution
          title: 'step-3_Solution-1: crude phosphine in Ethanol'
        id: https://www.chemotion-repository.net/pid/56408#step-3_part-1
        rdf_type:
          id: CHMO:0002773
          title: dissolving
        title:
        - 'step-3_part-1: dissolving of crude phosphine in Ethanol'
      - had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408_Reactant-2
          title: 'Reactant-2: Hydrogen Peroxide'
        - id: https://www.chemotion-repository.net/pid/56408_Reactant-3
          title: 'Reactant-3: glacial acetic acid'
        - id: https://www.chemotion-repository.net/pid/56408_Solvent-4
          title: 'Solvent-4: Ethanol'
        had_output_entity:
        - has_part:
          - id: https://www.chemotion-repository.net/pid/56408_Reactant-2
            title: 'Reactant-2: Hydrogen Peroxide'
          - id: https://www.chemotion-repository.net/pid/56408_Reactant-3
            title: 'Reactant-3: glacial acetic acid'
          - id: https://www.chemotion-repository.net/pid/56408_Solvent-4
            title: 'Solvent-4: Ethanol'
          id: https://www.chemotion-repository.net/pid/56408#step-3_Solution-2
          rdf_type:
            id: CHEBI:75958
            title: solution
          title: 'step-3_Solution-2: H2O2 and Acetic Acid in Ethanol'
        id: https://www.chemotion-repository.net/pid/56408#step-3_part-2
        rdf_type:
          id: CHMO:0002773
          title: dissolving
        title:
        - 'step-3_part-2: preparation of H2O2/Acetic Acid solution in Ethanol'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_part-1
          title:
          - 'step-3_part-1: dissolving of crude phosphine in Ethanol'
        - id: https://www.chemotion-repository.net/pid/56408#step-3_part-2
          title:
          - 'step-3_part-2: preparation of H2O2/Acetic Acid solution in Ethanol'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_Solution-1
          title: 'step-3_Solution-1: crude phosphine in Ethanol'
        - id: https://www.chemotion-repository.net/pid/56408#step-3_Solution-2
          title: 'step-3_Solution-2: H2O2 and Acetic Acid in Ethanol'
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_ReactionMixture-1
          rdf_type:
            id: CHEBI:60004
            title: mixture
          title: "step-3_ReactionMixture-1 mixture at 0\xB0C"
        has_qualitative_attribute:
        - title: duration of step-3_part-3
          type:
            id: https://schema.org/Duration
            title: Duration
          value: PT15M
        has_quantitative_attribute:
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
          title: temperature of step-3_part-3
          unit: http://qudt.org/vocab/unit/DEG_C
          value: 0
        id: https://www.chemotion-repository.net/pid/56408#step-3_part-3
        rdf_type:
          id: OBI:0000274
          title: adding a material entity into a target
        title:
        - 'step-3_part-3: drop-wise addition of H2O2/Acetic Acid solution'
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_part-3
          title:
          - 'step-3_part-3: drop-wise addition of H2O2/Acetic Acid solution'
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_ReactionMixture-1
          title: "step-3_ReactionMixture-1 mixture at 0\xB0C"
        has_qualitative_attribute:
        - title: duration of step-3_part-4
          type:
            id: https://schema.org/Duration
            title: Duration
          value: PT2H
        has_quantitative_attribute:
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
          title: temperature of stirring
          unit: http://qudt.org/vocab/unit/DEG_C
          value: 0
        id: https://www.chemotion-repository.net/pid/56408#step-3_part-4
        rdf_type:
          id: CHMO:0002774
          title: stirring
        title:
        - "step-3_part-4: stirring for 2 hours at 0\xB0C"
      - had_input_activity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_part-4
          title:
          - "step-3_part-4: stirring for 2 hours at 0\xB0C"
        had_input_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_ReactionMixture-1
          title: "step-3_ReactionMixture-1: mixture at 0\xB0C"
        had_output_entity:
        - id: https://www.chemotion-repository.net/pid/56408#step-3_Output-1
          rdf_type:
            id: CHEBI:60004
            title: mixture
          title: 'step-3_Output-1: containing crude 1-diphenylphosphoryl-2-fluorobenzene'
        has_qualitative_attribute:
        - title: duration of reflux
          type:
            id: https://schema.org/Duration
            title: Duration
          value: PT2H
        has_quantitative_attribute:
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
          title: Reflux Temperature (Ethanol)
          unit: http://qudt.org/vocab/unit/DEG_C
          value: 80
        id: https://www.chemotion-repository.net/pid/56408#step-3_part-5
        rdf_type:
          id: ENVO:01000623
          title: boiling
        title:
        - 'step-3_part-5: reflux for 2 hours'
      id: https://www.chemotion-repository.net/pid/56408#step-3
      rdf_type:
        id: RXNO:0000001
        title: planned reaction step
      title:
      - 'Step 3: Oxidation to Phosphine Oxide'
      used_reactant:
      - id: https://www.chemotion-repository.net/pid/56408_Reactant-2
        title: 'Reactant-2: Hydrogen Peroxide'
      - id: https://www.chemotion-repository.net/pid/56408_Reactant-3
        title: 'Reactant-3: glacial acetic acid'
      used_reactor:
      - id: https://www.chemotion-repository.net/pid/56408_Reactor-1
        title: dry glass ware under argon atmosphere
      used_solvent:
      - id: https://www.chemotion-repository.net/pid/56408_Solvent-3
        title: 'Solvent-3: Ethanol'
      - id: https://www.chemotion-repository.net/pid/56408_Solvent-4
        title: 'Solvent-4: Ethanol'
      used_starting_material:
      - id: https://www.chemotion-repository.net/pid/56408#step-2_Output-1
        title: Crude phosphine intermediate (pale yellow oil)
    id: https://www.chemotion-repository.net/pid/56408
  id: doi:10.14272/reaction/SA-FUHFF-UHFFFADPSC-MTSVGCFANK-UHFFFADPSC-NUHFF-NUHFF-NUHFF-ZZZ#Recording
  title:
  - Recording of the Chemotion Repo synthesis CRR-56408

```
## SubstanceCharacterizationDataset-001
### Input
```yaml
description:
- 'Dataset analysing Sample ID: CRS-50440 with heteronuclear single quantum coherence
  (HSQC) NMR spectroscopy'
id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604
is_about_entity:
- composed_of:
  - description: compound assigned to doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
    has_molar_mass:
    - description: Molar mass as specified in the Chemotion repository.
      has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
      unit: https://qudt.org/vocab/unit/GM-PER-MOL
      value: 204.072119
    - description: Molar mass as specified in PubChem
      has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
      unit: https://qudt.org/vocab/unit/GM-PER-MOL
      value: 204.29
    id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2#EvaluatedCompound
    inchi:
    - description: assigned InChi
      value: InChI=1S/C11H12N2S/c1-12-7-10-8-14-11(13-10)9-5-3-2-4-6-9/h2-6,8,12H,7H2,1H3
    inchikey:
    - description: assigned InChiKey
      value: KVOIVNBYNQXCNY-BOCHJOTCSA-N
    iupac_name:
    - description: Chemotion IUPAC name
      value: N-methyl-1-(2-phenyl-1,3-thiazol-4-yl)methanamine
    - description: PubChem IUPAC name
      value: Methyl[(2-phenyl-1,3-thiazol-4-yl)methyl]amine
    molecular_formula:
    - description: assigned molecular formula
      value: C11H12N2S
    other_identifier:
    - notation: https://pubchem.ncbi.nlm.nih.gov/compound/26248854
    smiles:
    - description: assigned SMILES
      value: CNCc1csc(n1)c1ccccc1
  description: The analysed chemical substance sample CRS-50440.
  id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
  rdf_type:
    id: CHEBI:59999
    title: chemical substance
  title: CRS-50440
other_identifier:
- notation: https://www.chemotion-repository.net/pid/50438
theme:
- preferred_label:
  - Science and technology
title:
- heteronuclear single quantum coherence (HSQC) dataset
was_generated_by:
- carried_out_by:
  - description: used NMR spectrometer
    id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932_NMR_Spectrometer
    rdf_type:
      id: NMR:1000371
      title: AVANCE III HD
    title: Avance III 400 NMR spectrometer
  - description: used solvent
    has_part:
    - id: https://pubchem.ncbi.nlm.nih.gov/compound/71583
      rdf_type:
        id: CHEBI:85365
        title: deuterated chloroform
      title: chloroform-D1 (CDCl3)
    id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932_NMR_Solvent
    rdf_type:
      id: NCIT:C45790
      title: Solvent
  description:
  - heteronuclear single quantum coherence (HSQC) NMR spectroscopy.
  evaluated_entity:
  - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
    title: CRS-50440
  has_qualitative_attribute:
  - description: used pulse program
    rdf_type:
      id: NMR:1400037
      title: NMR pulse sequence
    value: hsqcedetgp
  has_quantitative_attribute:
  - description: used sample temperature setting
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    rdf_type:
      id: NMR:1400025
      title: sample temperature in magnet
    unit: https://qudt.org/vocab/unit/K
    value: 300.1
  - description: used number of scans
    has_quantity_type: http://qudt.org/vocab/quantitykind/Count
    rdf_type:
      id: NMR:1400087
      title: number of scans
    unit: http://qudt.org/vocab/unit/NUM
    value: 2
  id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932
  rdf_type:
    id: CHMO:0000604
    title: heteronuclear single quantum coherence
  title:
  - X27932

```
## SubstanceSample-001
### Input
```yaml
description: The analysed chemical substance sample CRS-50440.
has_part:
- description: compound assigned to https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
  has_qualitative_attribute:
  - rdf_type:
      id: CHEMINF:000059
      title: InChiKey
    title: assigned InChiKey
    value: KVOIVNBYNQXCNY-BOCHJOTCSA-N
  - rdf_type:
      id: CHEMINF:000113
      title: InChi
    title: assigned InChi
    value: InChI=1S/C11H12N2S/c1-12-7-10-8-14-11(13-10)9-5-3-2-4-6-9/h2-6,8,12H,7H2,1H3
  - rdf_type:
      id: CHEMINF:000018
      title: SMILES descriptor
    title: assigned SMILES
    value: CNCc1csc(n1)c1ccccc1
  - rdf_type:
      id: CHEMINF:000042
      title: molecular formula
    title: assigned molecular formula
    value: C11H12N2S
  - description: Chemotion IUPAC name
    rdf_type:
      id: CHEMINF:000107
      title: IUPAC name
    value: N-methyl-1-(2-phenyl-1,3-thiazol-4-yl)methanamine
  - description: PubChem IUPAC name
    rdf_type:
      id: CHEMINF:000107
      title: IUPAC name
    value: Methyl[(2-phenyl-1,3-thiazol-4-yl)methyl]amine
  has_quantitative_attribute:
  - description: Molar mass as specified in the Chemotion repository.
    has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
    unit: https://qudt.org/vocab/unit/GM-PER-MOL
    value: 204.072119
  - description: Molar mass as specified in PubChem
    has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
    unit: https://qudt.org/vocab/unit/GM-PER-MOL
    value: 204.29
  id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2#EvaluatedCompound
  other_identifier:
  - notation: https://pubchem.ncbi.nlm.nih.gov/compound/26248854
  rdf_type:
    id: CHEBI:23367
    title: molecular entity
id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
other_identifier:
- notation: https://www.chemotion-repository.net/pid/50440
rdf_type:
  id: CHEBI:59999
  title: Chemical Substance
title: CRS-50440

```
## SubstanceSample-002
### Input
```yaml
composed_of:
- description: compound assigned to https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
  has_molar_mass:
  - description: Molar mass as specified in the Chemotion repository.
    has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
    unit: https://qudt.org/vocab/unit/GM-PER-MOL
    value: 204.072119
  - description: Molar mass as specified in PubChem.
    has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
    unit: https://qudt.org/vocab/unit/GM-PER-MOL
    value: 204.29
  id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2#EvaluatedCompound
  inchi:
  - title: assigned InChi
    value: InChI=1S/C11H12N2S/c1-12-7-10-8-14-11(13-10)9-5-3-2-4-6-9/h2-6,8,12H,7H2,1H3
  inchikey:
  - title: assigned InChiKey
    value: UGRXAOUDHZOHPF-UHFFFAOYSA-N
  iupac_name:
  - description: Chemotion IUPAC name
    value: N-methyl-1-(2-phenyl-1,3-thiazol-4-yl)methanamine
  - description: PubChem IUPAC name
    value: Methyl[(2-phenyl-1,3-thiazol-4-yl)methyl]amine
  molecular_formula:
  - title: assigned molecular formula
    value: C11H12N2S
  other_identifier:
  - notation: https://pubchem.ncbi.nlm.nih.gov/compound/26248854
  smiles:
  - title: assigned SMILES
    value: ' CNCc1csc(n1)c1ccccc1'
has_quantitative_attribute:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
  rdf_type:
    id: NMR:1400025
    title: sample temperature in magnet
  title: sample temperature in magnet
  unit: https://qudt.org/vocab/unit/K
  value: 300.0
id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
other_identifier:
- notation: https://www.chemotion-repository.net/pid/50440
title: CRS-50440

```
