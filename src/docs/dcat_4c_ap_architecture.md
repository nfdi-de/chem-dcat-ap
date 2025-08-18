# DCAT-4C-AP Architecture

** DRAFT **

The DCAT-4C-AP is an extension of the DCAT Application Profile in LinkML. It is intended to be used by NFDI4Chem & NFDI 4Cat as a core that can further be extended in profiles to provide domain specific metadata for a dataset.

The DCAT-4C-AP is based on the DCAT-AP and the DCAT-AP-DE. It extends the DCAT-AP-DE with additional classes and properties to describe datasets in the domain of chemistry and catalysis. 
The DCAT-4C-AP is designed to be used in combination with the DCAT-AP-DE and the DCAT-AP to provide a comprehensive description of datasets in the domain of chemistry and catalysis.


The design follows a modular and hierarchical approach 

1. Restriction / specification of the DCAT-AP classes to achieve higher fidelity in the description, like, e.g., using regular expressions to define an e-mail address, specify mandatory properties, cardinarlity, etc.

2. Extension of the DCAT-AP classes with additional properties to describe chemistry and measurement related, but still generic metadata.

3. Introduce domain specific layers for different subdomains of chemistry and catalysis, e.g., spectroscopy, crystallography, etc.