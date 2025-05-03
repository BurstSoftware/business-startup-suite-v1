import streamlit as st
import qrcode
from PIL import Image
import io
import pandas as pd
import datetime

# Streamlit page configuration
st.set_page_config(page_title="General Business Startup Suite", layout="wide")

# App title and description
st.title("General Business Startup Suite")
st.markdown("""
This all-in-one toolset helps entrepreneurs kickstart their business with planning, invoicing, marketing, and resource-finding tools. 
Select a tool from the sidebar to get started!
""")

# Sidebar for tool selection
tool = st.sidebar.selectbox(
    "Choose a Tool",
    [
        "Business Plan Writer",
        "Simple Invoice Generator",
        "AI Advertising Writer",
        "Business Marketing Checklist",
        "Tool, Business, and Service Finder",
        "Static QR Code Generator"
    ]
)

# Tool 1: Business Plan Writer
if tool == "Business Plan Writer":
    st.header("Business Plan Writer")
    st.write("Create a structured business plan by filling out the sections below.")
    
    with st.form("business_plan_form"):
        business_name = st.text_input("Business Name")
        mission = st.text_area("Mission Statement")
        goals = st.text_area("Business Goals")
        target_market = st.text_area("Target Market")
        financial_plan = st.text_area("Financial Plan (e.g., budget, funding needs)")
        strategies = st.text_area("Strategies (e.g., marketing, operations)")
        
        submitted = st.form_submit_button("Generate Business Plan")
        if submitted:
            st.subheader("Your Business Plan")
            st.write(f"**Business Name**: {business_name}")
            st.write(f"**Mission Statement**: {mission}")
            st.write(f"**Goals**: {goals}")
            st.write(f"**Target Market**: {target_market}")
            st.write(f"**Financial Plan**: {financial_plan}")
            st.write(f"**Strategies**: {strategies}")
            st.download_button(
                label="Download Business Plan",
                data=f"Business Plan for {business_name}\n\nMission Statement:\n{mission}\n\nGoals:\n{goals}\n\nTarget Market:\n{target_market}\n\nFinancial Plan:\n{financial_plan}\n\nStrategies:\n{strategies}",
                file_name=f"{business_name}_business_plan.txt",
                mime="text/plain"
            )

# Tool 2: Simple Invoice Generator
elif tool == "Simple Invoice Generator":
    st.header("Simple Invoice Generator")
    st.write("Generate a basic invoice for your clients.")
    
    with st.form("invoice_form"):
        client_name = st.text_input("Client Name")
        client_email = st.text_input("Client Email")
        service = st.text_input("Service/Product")
        amount = st.number_input("Amount ($)", min_value=0.0, step=0.01)
        due_date = st.date_input("Due Date", min_value=datetime.date.today())
        
        submitted = st.form_submit_button("Generate Invoice")
        if submitted:
            st.subheader("Invoice")
            st.write(f"**To**: {client_name} ({client_email})")
            st.write(f"**Service/Product**: {service}")
            st.write(f"**Amount**: ${amount:.2f}")
            st.write(f"**Due Date**: {due_date}")
            st.download_button(
                label="Download Invoice",
                data=f"Invoice\n\nTo: {client_name} ({client_email})\nService/Product: {service}\nAmount: ${amount:.2f}\nDue Date: {due_date}",
                file_name=f"invoice_{client_name}.txt",
                mime="text/plain"
            )

# Tool 3: AI Advertising Writer
elif tool == "AI Advertising Writer":
    st.header("AI Advertising Writer")
    st.write("Generate compelling ad copy for your business.")
    
    product_service = st.text_input("Product/Service Name")
    target_audience = st.text_input("Target Audience (e.g., young professionals, families)")
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Bold", "Humorous"])
    ad_platform = st.selectbox("Ad Platform", ["Social Media", "Google Ads", "Print"])
    
    if st.button("Generate Ad Copy"):
        # Placeholder for AI-generated ad copy (you can integrate an actual AI model here)
        ad_copy = f"Discover {product_service}! Perfect for {target_audience}. {tone} and tailored for {ad_platform}. Get started today!"
        st.subheader("Generated Ad Copy")
        st.write(ad_copy)
        st.download_button(
            label="Download Ad Copy",
            data=ad_copy,
            file_name="ad_copy.txt",
            mime="text/plain"
        )

# Tool 4: Business Marketing Checklist
elif tool == "Business Marketing Checklist":
    st.header("Business Marketing Checklist")
    st.write("Track your marketing tasks to ensure a comprehensive strategy.")
    
    checklist = [
        "Define target audience",
        "Create a brand identity",
        "Set up a website",
        "Launch social media profiles",
        "Plan advertising campaigns",
        "Engage with customers",
        "Analyze marketing performance"
    ]
    
    st.subheader("Marketing Tasks")
    completed_tasks = []
    for task in checklist:
        if st.checkbox(task):
            completed_tasks.append(task)
    
    if st.button("Save Checklist Progress"):
        st.write("**Completed Tasks**:")
        for task in completed_tasks:
            st.write(f"- {task}")
        st.download_button(
            label="Download Checklist",
            data="\n".join([f"Completed: {task}" for task in completed_tasks]),
            file_name="marketing_checklist.txt",
            mime="text/plain"
        )

# Tool 5: Tool, Business, and Service Finder
elif tool == "Tool, Business, and Service Finder":
    st.header("Tool, Business, and Service Finder")
    st.write("Search for resources, vendors, or services to support your business.")
    
    search_query = st.text_input("Search (e.g., legal support, suppliers)")
    if st.button("Search"):
        # Placeholder for search results (you can integrate a real search API here)
        st.subheader("Search Results")
        st.write(f"Found resources for '{search_query}':")
        st.write("- Sample Vendor 1: Contact at vendor1@example.com")
        st.write("- Sample Service 2: Visit www.service2.com")
        st.write("(This is a placeholder. Integrate a real search API for actual results.)")

# Tool 6: Static QR Code Generator
elif tool == "Static QR Code Generator":
    st.header("Static QR Code Generator")
    st.write("Create a QR code linking to your website, social media, or payment page.")
    
    qr_url = st.text_input("Enter URL (e.g., website, social media link)")
    if st.button("Generate QR Code"):
        if qr_url:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_url)
            qr.make(fit=True)
            img = qr.make_image(fill="black", back_color="white")
            
            # Save QR code to a bytes buffer
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.image(byte_im, caption="Your QR Code", width=200)
            st.download_button(
                label="Download QR Code",
                data=byte_im,
                file_name="qr_code.png",
                mime="image/png"
            )
        else:
            st.error("Please enter a valid URL.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Streamlit for entrepreneurs | General Business Startup Suite")
