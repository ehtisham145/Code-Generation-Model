#Import Important Libraries
import streamlit as st
import google.generativeai as genai
import os
from components import header, sidebar, footer, page
# Load API key

# Get API key from Streamlit secrets
api_key = st.secrets["GOOGLE_API_KEY"]

# Configure API
genai.configure(api_key=api_key)

# DEBUG: Verify it's loaded
st.sidebar.success(f"✅ API Key loaded: {api_key[:10]}...")

# Initialize model
model = genai.GenerativeModel('gemini-2.0-flash-exp')


settings=page.show_page()
# Custom CSS for better UI
st.markdown("""
<style>
    /* Remove default padding */
    .main > div {
        padding-top: 0rem;
    }
    
    /* Info cards styling */
    .info-card {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
    }
    
    /* Main title styling */
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 2rem 0 1rem 0;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Button styling */
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    /* Code container */
    .code-container {
        background: #1e1e1e;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ========== HEADER ==========
current_page = header.create_header()

# ========== SIDEBAR ==========
settings = sidebar.create_sidebar()

# ========== MAIN CONTENT AREA ==========

# Handle different pages
if current_page == 'Chatbot' or current_page == 'Home':
    
    col1, col3, col4 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="info-card">
            <h4 style="margin:0; color:#667eea;">🔤 Language</h4>
            <p style="margin:5px 0; font-size:1.1rem;"><b>{settings['language']}</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        framework_display = settings['framework'] if settings['framework'] != "None" else "Standard"
        st.markdown(f"""
        <div class="info-card">
            <h4 style="margin:0; color:#667eea;">🛠️ Framework</h4>
            <p style="margin:5px 0; font-size:1.1rem;"><b>{framework_display}</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        creativity = int(settings['temperature'] * 100)
        st.markdown(f"""
        <div class="info-card">
            <h4 style="margin:0; color:#667eea;">🎨 Creativity</h4>
            <p style="margin:5px 0; font-size:1.1rem;"><b>{creativity}%</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
import streamlit as st
import google.generativeai as genai

# ========== DEFAULT SETTINGS ==========
settings = {
    "language": "Python",
    "code_type": "Function",
    "framework": "None",
    "libraries": [],
    "include_comments": True,
    "include_docstrings": False,
    "include_examples": False,
    "include_tests": False,
    "error_handling": True,
    "type_hints": False,
    "optimize_code": True,
    "logging": False,
    "code_style": "PEP8"
}

# ========== UI SECTION ==========

st.markdown("<p style='font-size:20px;'>.</p>", unsafe_allow_html=True)
# INPUT AREA
# Text area input
st.markdown("### 📝 Describe Your Code Requirement")

prompt = st.text_area(label="")

# GENERATE BUTTON
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    generate_btn = st.button(
        "🚀 Generate Code",
        type="primary",
        use_container_width=True,
        help="Click to generate code using AI"
    )

st.markdown("---")

# ========== CODE GENERATION LOGIC ==========
if generate_btn:
    if prompt.strip() == "":
        st.warning("⚠️ Please describe what code you want to generate!")
    else:
        with st.spinner("✨ Generating your code... This may take a few seconds"):
            try:
                # Initialize model
                model = genai.GenerativeModel("gemini-2.0-flash-exp")

                # Build full prompt
                full_prompt = f"""Generate {settings['language']} code for the following requirement:

{prompt}

Code Type: {settings['code_type']}"""

                if settings["framework"] != "None":
                    full_prompt += f"\nFramework: {settings['framework']}"

                if settings["libraries"]:
                    full_prompt += f"\nRequired Libraries: {', '.join(settings['libraries'])}"

                # Build options dynamically
                options = []
                if settings["include_comments"]: options.append("detailed inline comments")
                if settings["include_docstrings"]: options.append("comprehensive docstrings")
                if settings["include_examples"]: options.append("usage examples")
                if settings["include_tests"]: options.append("unit tests")
                if settings["error_handling"]: options.append("proper error handling")
                if settings["type_hints"]: options.append("type hints/annotations")
                if settings["optimize_code"]: options.append("performance optimizations")
                if settings["logging"]: options.append("logging statements")

                if options:
                    full_prompt += "\n\nInclude:\n- " + "\n- ".join(options)

                # Style Guide
                if settings["code_style"] not in ["None", "Auto-detect"]:
                    full_prompt += f"\n\nFollow {settings['code_style']} style guidelines."

                full_prompt += "\n\nProvide clean, production-ready, well-documented code."

                # Generate code
                response = model.generate_content(full_prompt)

                # Handle Gemini output safely
                generated_code = getattr(response, 'text', None)
                if not generated_code:
                    try:
                        generated_code = response.candidates[0].content.parts[0].text
                    except Exception:
                        generated_code = "⚠️ No code was returned. Please try again."

                # Display code
                st.success("✅ Code generated successfully!")
                st.code(generated_code, language=settings["language"].lower())

            except Exception as e:
                st.error(f"❌ An error occurred while generating code: {str(e)}")

                    
                    # Save to history
                sidebar.save_to_history(
                        prompt=prompt[:100],
                        code=generated_code,
                        language=settings['language'],
                        code_type=settings['code_type']
                    )
                    
                    # Store in session
                st.session_state.current_code = generated_code
                    
                    # Success
                st.success("🎉 Code generated successfully!")
                    
                    # Display code
                st.markdown("### 📄 Generated Code")
                st.code(generated_code, language=settings['language'].lower(), line_numbers=True)
                    
                    # Action Buttons
                st.markdown("#### 🔧 Actions")
                col1, col2, col3, col4, col5 = st.columns(5)
                    
                with col1:
                        file_ext = sidebar.get_file_extension(settings['language'])
                        st.download_button(
                            label="⬇️ Download",
                            data=generated_code,
                            file_name=f"code.{file_ext}",
                            mime="text/plain",
                            use_container_width=True
                        )
                    
                with col2:
                        if st.button("📋 Copy", use_container_width=True):
                            st.toast("✅ Code copied!", icon="📋")
                    
                with col3:
                        if st.button("🧠 Explain", use_container_width=True):
                            with st.spinner("Generating explanation..."):
                                explain = model.generate_content(f"Explain this code simply:\n\n{generated_code}")
                                st.info(f"**📖 Explanation:**\n\n{explain.text}")
                    
                with col4:
                        if st.button("🔍 Review", use_container_width=True):
                            with st.spinner("Reviewing..."):
                                review = model.generate_content(f"Review this code for quality, bugs, and improvements:\n\n{generated_code}")
                                st.warning(f"**🔍 Review:**\n\n{review.text}")
                    
                with col5:
                        if st.button("⚡ Improve", use_container_width=True):
                            with st.spinner("Improving..."):
                                improved = model.generate_content(f"Improve this code:\n\n{generated_code}")
                                st.markdown("**⚡ Improved:**")
                                st.code(improved.text, language=settings['language'].lower())
                    
            except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info("💡 **Tips:**\n- Check your internet connection\n- Verify API key is valid\n- Try simplifying your prompt")

elif current_page != 'Home' and current_page != 'Chatbot':
    # Show other pages
    header.render_page_content(current_page)

# ========== FOOTER ==========
footer.show_footer()