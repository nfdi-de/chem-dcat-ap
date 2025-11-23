# Examples of use of dcat_4c_ap

This folder contains example data conforming to dcat_4c_ap

The source for these is in [tests/data/valid](../tests/data/valid)

## Generation of output files

To generate the output of each DCAT-AP profile into a TTL graph run:
    * Convert domain agnostic DCAT-AP extension conform example of an analysis
    ````commandline
    uv run linkml-convert -t ttl ../tests/data/valid/AnalysisDataset-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C AnalysisDataset
    ````
  * Convert a NMR spectroscopy-specific DCAT-AP extension conform example
    ````commandline
    uv run linkml-convert -t ttl ../tests/data/valid/NMRAnalysisDataset-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C NMRAnalysisDataset
    ````
  * Convert domain agnostic DCAT-AP extension conform example of a MaterialSample
    ````commandline
    uv run linkml-convert -t ttl ../tests/data/valid/MaterialSample-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C MaterialSample
    ````
  * Convert domain agnostic DCAT-AP extension conform example of a SubstanceSample
    ````commandline
    uv run linkml-convert -t ttl ../tests/data/valid/SubstanceSample-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C SubstanceSample
    ````
  * Convert domain agnostic DCAT-AP extension conform example of a ChemicalReaction
    ````commandline
    uv run linkml-convert -t ttl ../tests/data/valid/ChemicalReaction-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C ChemicalReaction
    ````

To generate the output of each DCAT-AP profile into a JSON file:
    * Convert domain agnostic DCAT-AP extension conform example of an analysis
    ````commandline
    uv run linkml-convert -t json ../tests/data/valid/AnalysisDataset-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C AnalysisDataset
    ````
  * Convert a NMR spectroscopy-specific DCAT-AP extension conform example
    ````commandline
    uv run linkml-convert -t json ../tests/data/valid/NMRAnalysisDataset-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C NMRAnalysisDataset
    ````
  * Convert domain agnostic DCAT-AP extension conform example of a MaterialSample
    ````commandline
    uv run linkml-convert -t json ../tests/data/valid/MaterialSample-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C MaterialSample
    ````
  * Convert domain agnostic DCAT-AP extension conform example of a SubstanceSample
    ````commandline
    uv run linkml-convert -t json ../tests/data/valid/SubstanceSample-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C SubstanceSample
    ````
  * Convert domain agnostic DCAT-AP extension conform example of a ChemicalReaction
    ````commandline
    uv run linkml-convert -t json ../tests/data/valid/ChemicalReaction-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C ChemicalReaction
    ````

Mind that with the commands above, all output is printed to standard output, to redirect it to a file use shell redirection, e.g.:

```commandline
uv run linkml-convert -t ttl ../tests/data/valid/AnalysisDataset-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C AnalysisDataset > output/AnalysisDataset-001.ttl
```

These results of such conversions can be found in the [output/](./output/) folder.
