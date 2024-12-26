# Table Extractor Pro

A professional-grade table extraction tool that converts tabular data into structured JSON format using OpenAI's GPT-4 model.

## Features

- 🎯 Precise table data extraction
- 🔄 Consistent JSON formatting
- 📋 Support for various table formats
- ⚡ Real-time processing
- 📊 Beautiful visualization of results

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.streamlit/secrets.toml` file and add your OpenAI API key:
   ```toml
   OPENAI_API_KEY = "your-api-key-here"
   ```
   Alternatively, you can input your API key directly in the application.

## Running the Application

Run the Streamlit app with:
```bash
streamlit run streamlit_app.py
```

## Usage

1. Launch the application
2. If not configured in secrets.toml, enter your OpenAI API key
3. Paste your tabular data into the input text area
4. Click "Extract Data" to process
5. View results in both JSON and table formats

## Sample Input

```
ProductID,Name,Category,Price
1,Laptop,Electronics,800
2,Chair,Furniture,150
3,Notebook,Stationery,5
```

## Output Format

The application outputs the extracted data in two formats:
1. JSON format with a predefined schema
2. Interactive table view

## Security Note

- Never commit your API keys to version control
- Use environment variables or secrets management for API keys
- The application includes secure handling of API keys through Streamlit's secrets management 