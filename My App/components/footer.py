import streamlit as st
from datetime import datetime
def show_footer():
    """Creates a professional footer"""
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🤖 Ehtisham AI")
        st.write("AI-Powered Code Generator")
        st.write("**Developer:** Ehtisham")
        st.write("**Education:** Virtual University")
    
    with col2:
        st.markdown("### 🔗 Quick Links")
        st.write("• [Documentation](#)")
        st.write("• [GitHub](#)")
        st.write("• [Contact](#)")
    
    with col3:
        st.markdown("### 📧 Connect")
        st.link_button("💼 [LinkedIn](#)", "https://www.linkedin.com/in/ehtisham-iftikhar-4b6b86309?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BpyAUj2H%2BR3eHN2VCfXVvwA%3D%3D")
        st.link_button("🐙 [GitHub](#)", "https://github.com/ehtisham145")
        st.link_button("📧 Email", "mailto:ehtisham@example.com")

    st.markdown("---")
    
    current_year = datetime.now().year
    st.markdown(f"""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>© {current_year} Ehtisham AI - All Rights Reserved</p>
        <p>Powered by Google Gemini AI | Built with Streamlit ❤️</p>
    </div>
    """, unsafe_allow_html=True)