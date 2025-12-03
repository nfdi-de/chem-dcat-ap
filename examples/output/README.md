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
- "The reaction has been conducted in dry glass ware under argon atmosphere. A solution\
  \ of 1-bromo-2-fluorobenzene (1.76 g, 1.10 mL, 9.86 mmol, 1.08 equiv) in anhydrous\
  \ THF (24.0 mL) was cooled to -78 \xC2\xB0C, and n-BuLi (689 mg, 4.30 mL, 10.8 mmol,\
  \ 2.50M in hexane, 1.18 equiv) was added drop-wise over 10 min. After stirring for\
  \ further 50 min, a solution of chloro(diphenyl)phosphine (2.09 g, 1.70 mL, 9.09\
  \ mmol, 1.00 equiv) in anhydrous THF (3.00 mL) was added drop-wise over 10 min,\
  \ and the reaction mixture was stirred for 8 h at -78 \xC2\xB0C. The reaction mixture\
  \ was allowed to warm up to 25 \xC2\xB0C over 8 h, and was then quenched by the\
  \ addition of 1 M HCl (10.0 mL). The phases were separated, and the aqueous phase\
  \ was extracted with diethyl ether (3 \xC3\u2014 50.0 mL). Then, the combined organic\
  \ layers were washed with sat. aq. NaHCO3-solution (50.0 mL), water (50.0 mL), and\
  \ with brine (50.0 mL). The organic phase was dried over Na2SO4, filtered, and the\
  \ solvent was evaporated under reduced pressure to afford the phosphine intermediate\
  \ as a pale yellow oil.\n- The crude phosphine intermediate was dissolved in ethanol\
  \ (150 mL), and cooled to 0 \xC2\xB0C. Under vigorous stirring, a solution of hydrogen\
  \ peroxide (3.95 g, 3.50 mL, 40.7 mmol, 35%, 4.48 equiv), and glacial acetic acid\
  \ (1.91 g, 1.80 mL, 30.5 mmol, 3.36 equiv) in ethanol (15.0 mL) was added drop-wise\
  \ over 15 min. The mixture was stirred for 2 h at 0 \xC2\xB0C, and was then refluxed\
  \ for 2 h. After evaporating the solvent under reduced pressure, the crude was dissolved\
  \ in dichloromethane (50.0 mL), washed with sat. aq. NaHCO3-solution (2 \xC3\u2014\
  \ 25.0 mL), water (25.0 mL), and brine (25.0 mL). The organic layer was dried over\
  \ Na2SO4, before evaporating the solvent under reduced pressure.\n- Additional information\
  \ for publication and purification details: - The crude product was purified via\
  \ flash-chromatography (Interchim\xC2\xAE\xC2\_puriFLASH XS520) on silica gel (PF-30SIHP-F0040)\
  \ using cyclohexane/ethyl acetate 35:65 to 30:70 in 10 CV (1 CV = 52.7 mL; flowrate\
  \ = 26.0 mL/min). The product 1-diphenylphosphoryl-2-fluorobenzene (2.33 g, 7.78\
  \ mmol, 86% yield) was obtained as a colorless solid."
generated_product:
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_Product-1.comp
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
  id: https://www.chemotion-repository.net/pid/56408_Product-1
has_duration: PT22H
has_temperature:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
  title: Temperature of reaction step 1
  unit: http://qudt.org/vocab/unit/DEG_C
  value: -78
- has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
  title: Temperature of reaction step 2
  unit: http://qudt.org/vocab/unit/DEG_C
  value: 0
- has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
  title: Temperature of reaction step 3
  unit: http://qudt.org/vocab/unit/DEG_C
  value: 80
has_yield:
- has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
  title: Yield [%]
  type:
    id: VOC4CAT:0005005
    title: yield
  unit: http://qudt.org/vocab/unit/PERCENT
  value: 86
id: doi:10.14272/reaction/SA-FUHFF-UHFFFADPSC-MTSVGCFANK-UHFFFADPSC-NUHFF-NUHFF-NUHFF-ZZZ
other_identifier:
- notation: https://www.chemotion-repository.net/pid/56408
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
- CRR-56408
used_reactant:
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_Reactant-1.comp
    iupac_name:
    - value: n-BuLi
    molecular_formula:
    - value: C4H9Li
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
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_Reactant-2.comp
    iupac_name:
    - value: Hydrogen Peroxide
    molecular_formula:
    - value: H2O2
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
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_Reactant-3.comp
    iupac_name:
    - value: glacial acetic acid
    molecular_formula:
    - value: C2H4O2
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
  has_volume:
  - has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    title: Volume [mL]
    unit: https://qudt.org/vocab/unit/MilliL
    value: 1.8
  id: https://www.chemotion-repository.net/pid/56408_Reactant-3
used_solvent:
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_Solvent-1.comp
    iupac_name:
    - value: Tetrahydrofuran
    molecular_formula:
    - value: C4H8O
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
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_Solvent-2.comp
    iupac_name:
    - value: Tetrahydrofuran
    molecular_formula:
    - value: C4H8O
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
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_Solvent-3.comp
    iupac_name:
    - value: Ethanol
    molecular_formula:
    - value: C2H6O
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
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_Solvent-4.comp
    iupac_name:
    - value: Ethanol
    molecular_formula:
    - value: C2H6O
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
used_starting_material:
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_StartMat-1.comp
    iupac_name:
    - value: 1-bromo-2-fluorobenzene
    molecular_formula:
    - value: C6H4BrF
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
- composed_of:
  - id: https://www.chemotion-repository.net/pid/56408_StartMat-2.comp
    iupac_name:
    - value: chloro(diphenyl)phosphine
    molecular_formula:
    - value: C12H10ClP
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
