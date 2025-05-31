import json
with open("secrets.json", "r") as f:
    secrets = json.load(f)

APP_ID = secrets["app_id"]
DEV_ID = secrets["dev_id"]
CERT_ID = secrets["cert_id"]
EMAIL = secrets["email"]
PASSWORD = secrets["password"]

import streamlit as st
from utils import generate_description, mock_ebay_price_comparison

st.set_page_config(page_title="AliExpress Arbitrage Finder Pro")

st.title("🛍️ AliExpress Arbitrage Finder Pro")
product_title = st.text_input("Enter product title")
product_features = st.text_area("Enter product features (comma-separated)")

if st.button("Generate Description"):
    if product_title and product_features:
        desc = generate_description(product_title, product_features)
        st.subheader("📄 AI-Generated Description:")
        st.write(desc)
        st.subheader("🔍 eBay Comparison:")
        st.write(mock_ebay_price_comparison(product_title))
    else:
        st.error("Please enter both title and features.")
