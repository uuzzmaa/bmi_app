import streamlit as st
 
# Optional: custom CSS
st.markdown("""
<style>
    .stApp { background-color: #f0f8ff; }
    h1 { color: #2E75B6; }
</style>
""", unsafe_allow_html=True)
 
st.title("My App Name")
 
# Add your inputs here
# value = st.number_input("Label")
 
if st.button("Calculate"):
    # Your logic here
    st.success(f"Result: {result}")

