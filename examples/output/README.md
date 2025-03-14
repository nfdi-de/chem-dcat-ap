## AnalysisDataset-001
### Input
```yaml
describes_entity:
- has_qualitative_attribute:
  - rdf_type:
      id: CHEMINF:000059
      title: InChiKey
    title: assigned InChiKey
    value: KVOIVNBYNQXCNY-BOCHJOTCSA-N
  id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
  other_identifier:
  - notation: https://www.chemotion-repository.net/pid/50440
  rdf_type:
    id: CHEBI:59999
    title: Chemical Substance
  title: CRS-50440
description:
- Dataset for 13C nuclear magnetic resonance spectroscopy (13C NMR)
id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1
other_identifier:
- notation: https://www.chemotion-repository.net/pid/50434
theme:
- preferred_label:
  - Science and technology
title:
- 13C nuclear magnetic resonance spectroscopy (13C NMR)
was_generated_by:
- evaluated_entity:
  - id: CDCl3_13C_NMR_Spectrum
    was_generated_by:
    - evaluated_entity:
      - id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
        title: CRS-50440
      rdf_type:
        id: CHMO:0000595
        title: 13C nuclear magnetic resonance spectroscopy
      used_tool:
      - has_qualitative_attribute:
        - rdf_type:
            id: NMR:1400037
            title: NMR pulse sequence
          title: Puls programme
          value: zgpg30
        has_quantitative_attribute:
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
          rdf_type:
            id: IAO:0000140
            title: setting datum
          title: Temperature
          unit: https://qudt.org/vocab/unit/K
          value: 300.0
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Count
          rdf_type:
            id: NMR:1400087
            title: number of scans
          title: Number of scans
          unit: http://qudt.org/vocab/unit/NUM
          value: 1024
        rdf_type:
          id: OBI:0000566
          title: NMR instrument
        title: Bruker 400 MHz
      - has_qualitative_attribute:
        - rdf_type:
            id: OBI:0302732
            title: solvent role
          value: solvent role
        rdf_type:
          id: CHEBI:85365
          title: deuterated chloroform
        title: chloroform-D1 (CDCl3)
  - id: DMSO_13C_NMR_Spectrum
    was_generated_by:
    - evaluated_entity:
      - id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
        title: CRS-50440
      rdf_type:
        id: CHMO:0000595
        title: 13C nuclear magnetic resonance spectroscopy
      used_tool:
      - has_qualitative_attribute:
        - rdf_type:
            id: NMR:1400037
            title: NMR pulse sequence
          title: Puls programme
          value: zgpg30
        has_quantitative_attribute:
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
          rdf_type:
            id: IAO:0000140
            title: setting datum
          title: Temperature
          unit: https://qudt.org/vocab/unit/K
          value: 300.0
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Count
          rdf_type:
            id: NMR:1400087
            title: number of scans
          title: Number of scans
          unit: http://qudt.org/vocab/unit/NUM
          value: 1024
        rdf_type:
          id: OBI:0000566
          title: NMR instrument
        title: Bruker 400 MHz
      - has_qualitative_attribute:
        - rdf_type:
            id: OBI:0302732
            title: solvent role
          value: solvent role
        rdf_type:
          id: CHEBI:85365
          title: deuterated chloroform
        title: DMSO
  rdf_type:
    id: NMR:1000259
    title: peak assignment

```
## Dataset-001
### Input
```yaml
description:
- Dataset for 13C nuclear magnetic resonance spectroscopy (13C NMR)
other_identifier:
- notation: https://doi.org/10.14272/KVOIVNBYNQXCNY-BOCHJOTCSA-N/CHMO0000595
- notation: https://www.chemotion-repository.net/pid/37012
theme:
- preferred_label:
  - Science and technology
title:
- 13C nuclear magnetic resonance spectroscopy (13C NMR)

```
## NMRAnalysisDataset-001
### Input
```yaml
describes_entity:
- composed_of:
  - inchi:
      title: assigned InChi
      value: InChI=1S/C11H12N2S/c1-12-7-10-8-14-11(13-10)9-5-3-2-4-6-9/h2-6,8,12H,7H2,1H3
    inchikey:
      title: assigned InChiKey
      value: UGRXAOUDHZOHPF-UHFFFAOYSA-N
    iupac_formula:
      title: assigned IUPAC formula
      value: CNCc1csc(n1)c1ccccc1
    smiles:
      title: assigned SMILES
      value: c1ccc(cc1)P(c1ccccc1)c1ccccc1.c1ccc(cc1)P(c1ccccc1)c1ccccc1.[Cu]n1cccc1/C=N/c1nc2c(s1)cccc2
  id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
  other_identifier:
  - notation: https://www.chemotion-repository.net/pid/50440
  title: CRS-50440
description:
- Dataset for 13C nuclear magnetic resonance spectroscopy (13C NMR)
id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000595.1
other_identifier:
- notation: https://www.chemotion-repository.net/pid/50434
theme:
- preferred_label:
  - Science and technology
title:
- 13C nuclear magnetic resonance spectroscopy (13C NMR)
was_generated_by:
- evaluated_entity:
  - id: CDCl3_13C_NMR_Spectrum
    was_generated_by:
    - evaluated_entity:
      - id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
        title: CRS-50440
      rdf_type:
        id: CHMO:0000595
        title: 13C nuclear magnetic resonance spectroscopy
      used_tool:
      - has_qualitative_attribute:
        - rdf_type:
            id: NMR:1400037
            title: NMR pulse sequence
          title: Puls programme
          value: zgpg30
        has_quantitative_attribute:
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
          rdf_type:
            id: IAO:0000140
            title: setting datum
          title: Temperature
          unit: https://qudt.org/vocab/unit/K
          value: 300.0
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Count
          rdf_type:
            id: NMR:1400087
            title: number of scans
          title: Number of scans
          unit: http://qudt.org/vocab/unit/NUM
          value: 1024
        rdf_type:
          id: OBI:0000566
          title: NMR instrument
        title: Bruker 400 MHz
      - has_qualitative_attribute:
        - rdf_type:
            id: OBI:0302732
            title: solvent role
          value: solvent role
        rdf_type:
          id: CHEBI:85365
          title: deuterated chloroform
        title: chloroform-D1 (CDCl3)
  - id: DMSO_13C_NMR_Spectrum
    was_generated_by:
    - evaluated_entity:
      - id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
        title: CRS-50440
      rdf_type:
        id: CHMO:0000595
        title: 13C nuclear magnetic resonance spectroscopy
      used_tool:
      - has_qualitative_attribute:
        - rdf_type:
            id: NMR:1400037
            title: NMR pulse sequence
          title: Puls programme
          value: zgpg30
        has_quantitative_attribute:
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
          rdf_type:
            id: IAO:0000140
            title: setting datum
          title: Temperature
          unit: https://qudt.org/vocab/unit/K
          value: 300.0
        - has_quantity_type: http://qudt.org/vocab/quantitykind/Count
          rdf_type:
            id: NMR:1400087
            title: number of scans
          title: Number of scans
          unit: http://qudt.org/vocab/unit/NUM
          value: 1024
        rdf_type:
          id: OBI:0000566
          title: NMR instrument
        title: Bruker 400 MHz
      - has_qualitative_attribute:
        - rdf_type:
            id: OBI:0302732
            title: solvent role
          value: solvent role
        rdf_type:
          id: CHEBI:85365
          title: deuterated chloroform
        title: DMSO

```
