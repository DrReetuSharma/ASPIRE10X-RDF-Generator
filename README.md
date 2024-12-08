# ASPIRE10X-RDF-Generator
Overview
The ASPIRE10X-RDF-Generator is an innovative tool designed to create RDF (Resource Description Framework) triples and Knowledge Graphs by integrating data from multiple sources, such as DrugBank, Disease Ontology, and UniProt. This application allows researchers, data scientists, and knowledge engineers to query and generate downloadable RDF data for drugs, diseases, and associated targets. It plays a vital role in building semantic relationships for use in biomedical research, drug discovery, and knowledge graph development.

With this generator, users can:
1) Query a disease and retrieve associated drugs and targets.
Generate RDF data to create and extend Knowledge Graphs.
Enable semantic linking between biomedical datasets.
2) Query a drug from DRUGBANK and retrieve RDF data to create knowledge graph including disease and targets.
3) 
## Requirements
## use this tool, you need:

Three API Endpoints:

1) DrugBank API: For fetching drug-related data.

2) Disease Ontology API: For disease information.

3) UniProt API: For target protein data.

Ensure that these APIs are accessible (some may require API keys).

Python 3.8+: Ensure Python is installed in your system.

#### Dependencies:

Streamlit for the web app interface.
rdflib for generating RDF triples.
requests for fetching data from APIs.

##### Features
Feed API URLs: Users can input API endpoints for drug, disease, and target data.
Query Input: Query diseases or targets to extract associated drugs, diseases, or proteins.
Generate RDF: Automatically generates RDF triples in Turtle format.
Downloadable Output: Users can download the RDF data for use in other systems or applications.
Streamlit Interface: Simple and interactive web app for real-time querying and RDF generation.
##### How It Works
Input APIs: Users provide URLs for APIs from DrugBank, Disease Ontology, and UniProt.
RDF Generation: The tool fetches data from APIs, processes relationships, and generates RDF triples.
Knowledge Graph: Use the generated RDF for creating semantic knowledge graphs to explore biomedical relationships.
Impact
This tool bridges the gap between structured biomedical datasets and semantic technologies by:

Enabling Semantic Search: Researchers can identify drug-disease-target relationships more effectively.
Facilitating Knowledge Graph Creation: Simplifies integration and visualization of complex biomedical relationships.
Enhancing Drug Discovery: Accelerates hypothesis generation by linking drugs, diseases, and targets meaningfully.

##### Use Cases
Biomedical Research: Link diseases and potential treatments for research studies.
Drug Discovery: Identify drug-target interactions for pharmaceutical development.
Ontology Development: Build and enhance ontologies with RDF triples.

Enter the API URLs for DrugBank, Disease Ontology, and UniProt in the app interface.
Query and Generate RDF:

Query diseases or targets to generate relationships.
Download RDF files in Turtle format for further use.

###### Technical Requirements
System: Linux, macOS, or Windows
Python Version: 3.8 or higher
Dependencies:
streamlit
rdflib
requests
Install dependencies using:

bash
Copy code
pip install streamlit rdflib requests
Contributing
Contributions are welcome! Feel free to fork the repository, create feature branches, and submit pull requests.

###### Contact
For questions or support, contact: Dr. Reetu Sharma
Email: sharmar@aspire10x.com
Website
