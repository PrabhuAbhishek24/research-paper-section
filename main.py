import streamlit as st
import requests
from fpdf import FPDF
from docx import Document
import openai
import PyPDF2
from docx.shared import Inches
import io
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import zipfile
import os
from pathlib import Path
import csv


google_api_key = st.secrets["api"]["GOOGLE_API_KEY"]
custom_search_engine_id = st.secrets["api"]["CUSTOM_SEARCH_ENGINE_ID"]



# Research-related keywords
RESEARCH_KEYWORDS = [
"research", "article", "study", "paper", "journal", "report", "document", "thesis", "dissertation",
    "review", "literature", "source", "abstract", "manuscript", "publication", "findings", "results",
    "investigation", "survey", "exploration", "clinical trial", "experiment", "data analysis",
    "methodology", "results", "hypothesis", "sample study", "case study", "data set", "research method",
    "peer-reviewed", "academic paper", "research paper", "study report", "research proposal", "field study",
    "systematic review", "experimental study", "observational study", "control group", "clinical research",
    "medical research", "pharmaceutical research", "biotech research", "drug development", "drug discovery",
    "experimental design", "epidemiological study", "randomized control trial", "meta-analysis", "biostatistics",
    "computational study", "therapeutic research", "molecular research", "genetic research", "biomedical research",
    "cancer research", "immunology study", "pathophysiology", "translational research", "treatment protocol",
    "medical innovation", "medical device study", "medical trial", "disease research", "pharmacology",
    "pharmacovigilance", "clinical development", "clinical study protocol", "patient safety", "pharmaceutical study",
    "pharmacokinetics", "therapeutic efficacy", "pharmacodynamics", "evidence-based medicine", "drug toxicology",
    "preclinical study", "clinical outcomes", "regulatory affairs", "patent study", "artificial intelligence research",
    "machine learning algorithms", "predictive modeling", "computational biology", "quantum computing research",
    "robotics in medicine", "data mining", "neural networks in pharma", "digital health", "telemedicine research",
    "precision medicine", "genomic research", "biotechnology innovation", "CRISPR technology",
    "wearable health technology",
    "peer-reviewed articles", "research journal", "scientific journal", "academic journal", "medical journal",
    "pharmaceutical journal", "research article", "review article", "open access", "editorial", "article abstract",
    "case report", "journal impact factor", "citation analysis", "scopus indexed", "elsevier", "springer",
    "wiley online library", "doi", "pubmed indexed", "neuroscience research", "cardiology research",
    "oncology research",
    "infectious disease study", "pediatrics research", "geriatrics study", "regenerative medicine",
    "stem cell research",
    "mental health studies", "HIV/AIDS research", "diabetes research", "rare diseases study",
    "autoimmune diseases research",
    "cardiovascular diseases study", "hepatology research", "dermatology study", "orthopedics research",
    "rheumatology research",
    "patent research", "patent application", "patent literature", "patent filing", "intellectual property",
    "patent search",
    "patent documentation", "pharmaceutical patent", "drug patent", "biotechnology patent", "data-driven research",
    "systematic review", "research data", "open science", "data visualization", "collaborative research",
    "research collaboration",
    "research network", "research findings", "literature review", "trial report", "cohort study",
    "cross-sectional study",
    "research grants", "clinical evaluation", "research ethics", "scientific method", "study design",
    "research funding",
    "research institutions", "research organizations", "health policy research", "epidemiology research"

]

# Function to check if a query contains research-related keywords
def is_query_research_related(query):
    for keyword in RESEARCH_KEYWORDS:
        if keyword.lower() in query.lower():
            return True
    return False

# Function to search using Google Custom Search API
def google_custom_search(query):
    url = (
        f"https://www.googleapis.com/customsearch/v1"
        f"?q={query}&key={google_api_key}&cx={custom_search_engine_id}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Error fetching data from Google Custom Search"}
    

# Set up the page configuration (must be the first command)
st.set_page_config(page_title="Research Content Generation", layout="wide", page_icon="📚")

# Title Section with enhanced visuals
st.markdown(
    """
    <h1 style="text-align: center; font-size: 2.5rem; color: #4A90E2;">📚 Medical And Pharmaceutical Research Content Generation</h1>
    <p style="text-align: center; font-size: 1.1rem; color: #555;">Streamline your content generation process with Google API technology. Designed for the <strong>pharmaceutical</strong> and <strong>medical</strong> domains.</p>
    """,
    unsafe_allow_html=True,
)
# Horizontal line
st.markdown("---")


# Research Search Instructions
with st.expander("4️⃣ **Research Search**",expanded=True):
    st.markdown("""
    - Search for research articles, papers, or journals in the medical and pharmaceutical domains.
    - **Steps**:
       1. Enter your research query in the text area.
       2. View a list of relevant results with titles, snippets, and links.
       3. Click on a title to navigate to the full content.
        """)
    
# Horizontal line
st.markdown("---")

st.header("🔬 Research Search")
query = st.text_area("Enter a research query:", height=200)
if query:
    search_results = google_custom_search(query)
    relevant_content = []
    for item in search_results.get("items", []):
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        if any(keyword in title.lower() or keyword in snippet.lower() for keyword in RESEARCH_KEYWORDS):
            relevant_content.append({"title": title, "link": item.get("link", ""), "snippet": snippet})
    if relevant_content:
        st.write("**Research Results:**")
        for content in relevant_content:
            st.write(f"- **[{content['title']}]({content['link']})**")
            st.write(content["snippet"])
    else:
       st.write("No relevant research-related content found.")



# Horizontal line
st.markdown("---")

# Footer
st.caption("Developed by **Corbin Technology Solutions**")
