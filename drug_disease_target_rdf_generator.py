import streamlit as st
import requests
from rdflib import Graph, URIRef
from rdflib.namespace import RDF

# RDF namespace
EX = "http://example.org/"

# Function to fetch data from an API
def fetch_data(api_url, query_param=None):
    params = {"query": query_param} if query_param else {}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data from {api_url}: {response.status_code}")
        return []

# Function to generate RDF graph
def generate_rdf_graph(query_type, query_value, drug_api, disease_api, target_api):
    g = Graph()

    if query_type == "Drug":
        drug_data = fetch_data(drug_api, query_value)
        for drug in drug_data:
            drug_uri = URIRef(EX + drug.get("id", "unknown"))
            g.add((drug_uri, RDF.type, URIRef(EX + "Drug")))

            for disease in drug.get("diseases", []):
                disease_uri = URIRef(EX + disease.get("id", "unknown"))
                g.add((drug_uri, URIRef(EX + "treats"), disease_uri))

            for target in drug.get("targets", []):
                target_uri = URIRef(EX + target.get("id", "unknown"))
                g.add((drug_uri, URIRef(EX + "affects"), target_uri))

    elif query_type == "Disease":
        disease_data = fetch_data(disease_api, query_value)
        for disease in disease_data:
            disease_uri = URIRef(EX + disease.get("id", "unknown"))
            g.add((disease_uri, RDF.type, URIRef(EX + "Disease")))

            for drug in disease.get("drugs", []):
                drug_uri = URIRef(EX + drug.get("id", "unknown"))
                g.add((disease_uri, URIRef(EX + "treated_by"), drug_uri))

            for target in disease.get("targets", []):
                target_uri = URIRef(EX + target.get("id", "unknown"))
                g.add((disease_uri, URIRef(EX + "associated_with"), target_uri))

    elif query_type == "Target":
        target_data = fetch_data(target_api, query_value)
        for target in target_data:
            target_uri = URIRef(EX + target.get("id", "unknown"))
            g.add((target_uri, RDF.type, URIRef(EX + "Target")))

            for disease in target.get("diseases", []):
                disease_uri = URIRef(EX + disease.get("id", "unknown"))
                g.add((target_uri, URIRef(EX + "associated_with"), disease_uri))

            for drug in target.get("drugs", []):
                drug_uri = URIRef(EX + drug.get("id", "unknown"))
                g.add((target_uri, URIRef(EX + "affected_by"), drug_uri))

    return g

# Streamlit app
st.title("ASPIRE10X Drug-Disease-Target RDF Generator for Knowledge Graphs")
st.subheader("Create and Download RDF Knowledge Graphs for Drug, Disease, and Target Relationships")

# Query type selection
query_type = st.selectbox("Select Query Type", ["Drug", "Disease", "Target"])
query_value = st.text_input(f"Enter {query_type} Name/ID")

# API endpoints
drug_api_url = st.text_input("Drug API URL (e.g., DrugBank)", "")
disease_api_url = st.text_input("Disease API URL (e.g., Disease Ontology)", "")
target_api_url = st.text_input("Target API URL (e.g., UniProt)", "")

# Submit button to trigger RDF graph generation
if st.button("Generate Knowledge Graph RDF"):
    if query_value and drug_api_url and disease_api_url and target_api_url:
        # Generate RDF graph
        rdf_graph = generate_rdf_graph(query_type, query_value, drug_api_url, disease_api_url, target_api_url)

        # Display the RDF graph as text
        st.subheader("Generated RDF Data")
        rdf_data = rdf_graph.serialize(format="turtle").decode("utf-8")
        st.text(rdf_data)

        # Provide option to download RDF data
        st.download_button(
            label="Download RDF Data",
            data=rdf_data,
            file_name=f"aspire10x_{query_type.lower()}_knowledge_graph.rdf",
            mime="text/turtle"
        )
    else:
        st.error("Please provide all required inputs (Query Type, Query Value, and API URLs).")
