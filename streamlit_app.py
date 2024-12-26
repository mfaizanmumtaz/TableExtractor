import streamlit as st
import pandas as pd
import json
from app import model, chain, Product, ProductTable

# Page configuration
st.set_page_config(
    page_title="Table Extractor Pro",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .success-message {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        color: #155724;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("📊 Table Extractor Pro")
st.markdown("""
    Transform your tabular data into structured JSON format instantly! 
    This tool uses advanced AI to extract and format your data according to predefined schemas.
""")

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
        This application demonstrates:
        - 🎯 Precise table data extraction
        - 🔄 Consistent JSON formatting
        - 📋 Support for various table formats
        - ⚡ Real-time processing
    """)
    
    st.header("📝 Sample Input")
    st.code("""ProductID,Name,Category,Price
1,Laptop,Electronics,800
2,Chair,Furniture,150
3,Notebook,Stationery,5""")

# Text input area
st.header("📥 Input")
text_data = st.text_area(
    "Paste your table data here:",
    height=200,
    help="Paste your tabular data here. It can be CSV format or any structured table data."
)

if st.button("🔄 Extract Data", type="primary"):
    if text_data:
        with st.spinner("Processing your data..."):
            try:
                # Process the data using the imported chain
                response = chain.invoke({"text_data": text_data})
                
                # Display results
                st.header("📤 Output")
                
                # Display as formatted JSON
                st.subheader("JSON Format")
                st.json(json.loads(response.json()))
                
                # Display as table
                st.subheader("Table Format")
                df = pd.DataFrame([vars(product) for product in response.products])
                st.dataframe(df, use_container_width=True)
                
                # Success message
                st.markdown("""
                    <div class="success-message">
                        ✅ Data extracted and formatted successfully!
                    </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error processing the data: {str(e)}")
    else:
        st.warning("Please enter some data to process.") 