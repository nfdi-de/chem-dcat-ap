# About ChemDCAT-AP
Funded by the German Research Foundantion (DFG) as part of the German National Research Data Infrastucture (NFDI) 
initiative under the grant numbers [441926934](https://gepris.dfg.de/gepris/projekt/441926934) and 
[441958208](https://gepris.dfg.de/gepris/projekt/441958208), 
ChemDCAT-AP is being developed in close collaboration between the German research 
infrastructure projects [NFDI4Chem](https://nfdi4chem.de) and [NFDI4Cat](https://nfdi4cat.org/).

To allow more fine-grained and semantic searches within their data repositories, 
both projects had to address the need to also provide detailed chemistry-specific metadata for the research data output
of their communities. Due to the disciplinary overlap of NFDI4Chem and NFDI4Cat, their previous collaboration was thus 
intensified to produce this common metadata schema as an extension of the 
[DCAT Application Profile](https://semiceu.github.io/DCAT-AP/releases/3.0.0/). With ChemDCAT-AP, the chemical 
substances and reactions covered by a `dcat:Dataset` as well as the processes, 
tools and devices that were involved its creation can be described in a semantically uniform way that allows further 
use-case specific extension.

This work was presented at the 19th International Conference on Metadata and Semantics Research 
([MTSR](https://www.mtsr-conf.org/home)) Thessaloniki, Greece, 15 - 19 December 2025 and will be published in the 
forthcoming proceedings.

Since the underlying basic design patterns of ChemDCAT-AP are domain-agnostic and thus applicable to a much wider 
range of use cases, the core layer of ChemDCAT-AP, called [DCAT-AP+](https://github.com/NFDI-de/dcat-ap-plus), was decided to be outsourced into its own 
repository.
