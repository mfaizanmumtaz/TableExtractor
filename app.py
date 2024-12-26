from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()
    

class Product(BaseModel):
    """Extracts the product details from the table"""
    ProductID: str = Field(description="Unique identifier for the product")
    Name: str = Field(description="Name of the product")
    Category: str = Field(description="Category of the product") 
    Price: str = Field(description="Price of the product")

class ProductTable(BaseModel):
    products: List[Product] = Field(description="List of products")

# Get API key from environment variable

model = ChatOpenAI(model="gpt-4").with_structured_output(ProductTable)

system_message = SystemMessage(content="Extract the product details from the table")

prompt = ChatPromptTemplate.from_messages([
    system_message,
    HumanMessage(content="> Text Data: ```{text_data}```"),
])

chain = prompt | model

if __name__ == "__main__":
    # Test the chain with sample data
    sample_data = "ProductID,Name,Category,Price\n1,Laptop,Electronics,800\n2,Chair,Furniture,150\n3,Notebook,Stationery,5"
    response = chain.invoke({"text_data": sample_data})
    print(response)