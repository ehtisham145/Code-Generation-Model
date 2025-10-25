"""
Professional Sidebar Module for AI Code Generator
Save this as: sidebar.py
Import in your main file: import sidebar
Use: settings = sidebar.create_sidebar()
"""

import streamlit as st
from datetime import datetime

def get_file_extension(language):
    """Returns file extension for given programming language"""
    extensions = {
        "Python": "py",
        "JavaScript": "js",
        "Java": "java",
        "C++": "cpp",
        "C#": "cs",
        "Go": "go",
        "Ruby": "rb",
        "PHP": "php",
        "Swift": "swift",
        "Kotlin": "kt",
        "TypeScript": "ts",
        "Rust": "rs",
        "SQL": "sql",
        "HTML": "html",
        "CSS": "css"
    }
    return extensions.get(language, "txt")

def initialize_session_state():
    """Initialize all session state variables"""
    if 'code_history' not in st.session_state:
        st.session_state.code_history = []
    if 'current_code' not in st.session_state:
        st.session_state.current_code = ""
    if 'favorite_prompts' not in st.session_state:
        st.session_state.favorite_prompts = []

def create_sidebar():
    """
    Creates a professional sidebar with all settings and options.
    Returns a dictionary with all selected settings.
    """
    
    # Initialize session state
    initialize_session_state()
    
    # Dictionary to store all settings
    settings = {}
    
    with st.sidebar:
        # Header with branding
        st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h2 style='margin: 0; color: #667eea;'>🤖 Code Generator</h2>
            <p style='margin: 0; font-size: 0.9rem; color: #666;'>AI-Powered Development(Ehtisham)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # ========== LANGUAGE SETTINGS ==========
        st.markdown("### 🔤 Language Settings")
        
        settings['language'] = st.selectbox(
            "Programming Language",
            ["Python", "JavaScript", "TypeScript", "Java", "C++", "C#", 
             "Go", "Ruby", "PHP", "Swift", "Kotlin", "Rust", "SQL", 
             "HTML", "CSS"],
            index=0,
            help="Select the programming language for code generation"
        )
        
        settings['framework'] = st.selectbox(
            "Framework (Optional)",
            ["None", "React", "Vue.js", "Angular", "Django", "Flask", 
             "FastAPI", "Express.js", "Spring Boot", "Next.js", "Laravel",
             "Ruby on Rails", "ASP.NET"],
            help="Choose a framework if applicable"
        )
        
        st.markdown("---")
        
        # ========== CODE TYPE ==========
        st.markdown("### 📦 Code Type")
        
        settings['code_type'] = st.radio(
            "Select what to generate:",
            ["Function", "Class", "Full Program", "Script", 
             "Algorithm", "API Endpoint", "Database Query", "Component"],
            index=0,
            help="Type of code to generate"
        )
        
        st.markdown("---")
        
        # ========== AI MODEL SETTINGS ==========
        st.markdown("### 🤖 AI Model Settings")
        
        settings['temperature'] = st.slider(
            "Creativity Level",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Higher = More creative & diverse | Lower = More focused & deterministic"
        )
        
        settings['max_tokens'] = st.slider(
            "Max Output Length",
            min_value=512,
            max_value=8192,
            value=2048,
            step=512,
            help="Maximum length of generated code"
        )
        
        st.markdown("---")
        
        # ========== CODE OPTIONS ==========
        st.markdown("### 📝 Code Quality Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            settings['include_comments'] = st.checkbox(
                "💬 Comments", 
                value=True,
                help="Add inline comments"
            )
            settings['include_docstrings'] = st.checkbox(
                "📄 Docstrings", 
                value=True,
                help="Add documentation strings"
            )
            settings['include_examples'] = st.checkbox(
                "📋 Examples", 
                value=True,
                help="Include usage examples"
            )
            settings['include_tests'] = st.checkbox(
                "🧪 Unit Tests", 
                value=False,
                help="Generate unit tests"
            )
        
        with col2:
            settings['error_handling'] = st.checkbox(
                "⚠️ Error Handling", 
                value=True,
                help="Add error handling"
            )
            settings['type_hints'] = st.checkbox(
                "🏷️ Type Hints", 
                value=True,
                help="Add type annotations"
            )
            settings['optimize_code'] = st.checkbox(
                "⚡ Optimize", 
                value=False,
                help="Optimize for performance"
            )
            settings['logging'] = st.checkbox(
                "📊 Logging", 
                value=False,
                help="Add logging statements"
            )
        
        st.markdown("---")
        
        # ========== CODE STYLE ==========
        st.markdown("### 🎨 Code Style Guide")
        
        settings['code_style'] = st.selectbox(
            "Style Standard",
            ["Auto-detect", "PEP 8 (Python)", "Airbnb", "Google", 
             "Standard JS", "PSR (PHP)", "None"],
            help="Follow specific style guidelines"
        )
        
        settings['indent_style'] = st.radio(
            "Indentation",
            ["Spaces (4)", "Spaces (2)", "Tabs"],
            horizontal=True
        )
        
        st.markdown("---")
        
        # ========== QUICK ACTIONS ==========
        st.markdown("### ⚡ Quick Actions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 New Session", use_container_width=True, help="Start fresh"):
                st.session_state.current_code = ""
                st.toast("✅ New session started!", icon="🔄")
        
        with col2:
            if st.button("🗑️ Clear History", use_container_width=True, help="Clear all history"):
                st.session_state.code_history = []
                st.session_state.favorite_prompts = []
                st.toast("✅ History cleared!", icon="🗑️")
        
        st.markdown("---")
        
        # ========== GENERATION HISTORY ==========
        st.markdown("### 📚 Generation History")
        
        if st.session_state.code_history:
            st.caption(f"📊 Total: **{len(st.session_state.code_history)}** generations")
            
            # Show last 5 generations
            for idx, item in enumerate(reversed(st.session_state.code_history[-5:])):
                actual_idx = len(st.session_state.code_history) - idx
                with st.expander(f"#{actual_idx}: {item['prompt'][:35]}...", expanded=False):
                    st.caption(f"🔤 **Language:** {item['language']}")
                    st.caption(f"📦 **Type:** {item['type']}")
                    st.caption(f"🕒 **Time:** {item['timestamp']}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button(f"📂 Load", key=f"load_{actual_idx}", use_container_width=True):
                            st.session_state.current_code = item['code']
                            st.toast(f"✅ Loaded generation #{actual_idx}", icon="📂")
                            st.rerun()
                    with col2:
                        if st.button(f"⭐ Save", key=f"save_{actual_idx}", use_container_width=True):
                            if item not in st.session_state.favorite_prompts:
                                st.session_state.favorite_prompts.append(item)
                                st.toast("⭐ Added to favorites!", icon="⭐")
        else:
            st.info("🔍 No history yet\n\nGenerate some code to see it here!")
        
        st.markdown("---")
        
        # ========== EXPORT OPTIONS ==========
        st.markdown("### 💾 Export Settings")
        
        settings['export_format'] = st.selectbox(
            "Export Format",
            ["Single File", "Markdown Document", "ZIP with Tests", 
             "Jupyter Notebook", "GitHub Gist Format"],
            help="How to export the generated code"
        )
        
        settings['include_readme'] = st.checkbox(
            "📖 Include README", 
            value=False,
            help="Generate README.md with the code"
        )
        
        st.markdown("---")
        
        # ========== STATISTICS ==========
        st.markdown("### 📊 Session Statistics")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Generations", 
                len(st.session_state.code_history),
                help="Total code generated this session"
            )
        with col2:
            if st.session_state.code_history:
                last_lang = st.session_state.code_history[-1]['language']
                st.metric(
                    "Last Language", 
                    last_lang[:8],
                    help=f"Last used: {last_lang}"
                )
            else:
                st.metric("Last Language", "N/A")
        
        # Most used language
        if st.session_state.code_history:
            languages = [item['language'] for item in st.session_state.code_history]
            most_used = max(set(languages), key=languages.count)
            count = languages.count(most_used)
            st.caption(f"🏆 Most used: **{most_used}** ({count}x)")
        
        st.markdown("---")
        
        # ========== ADVANCED SETTINGS ==========
        with st.expander("⚙️ Advanced Settings"):
            settings['model_version'] = st.selectbox(
                "AI Model",
                ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash-exp"],
                help="Select AI model version"
            )
            
            settings['streaming'] = st.checkbox(
                "Stream Output", 
                value=False,
                help="Show code as it generates"
            )
            
            settings['safe_mode'] = st.checkbox(
                "Safe Mode", 
                value=True,
                help="Filter potentially harmful code"
            )
            
            settings['auto_save'] = st.checkbox(
                "Auto-save History", 
                value=True,
                help="Automatically save all generations"
            )
        
        st.markdown("---")
        
        # ========== TEMPLATES ==========
        with st.expander("📋 Quick Templates"):
            st.markdown("""
            **Click to use:**
            - 🔐 User Authentication
            - 📊 Data Analysis Script
            - 🌐 REST API Endpoint
            - 📁 File I/O Handler
            - 🧮 Algorithm Implementation
            - 🗄️ Database CRUD Operations
            """)
            
            if st.button("Load Template", use_container_width=True):
                st.toast("Template feature coming soon!", icon="📋")
        
        st.markdown("---")
        
        # ========== HELP & TIPS ==========
        with st.expander("💡 Tips & Shortcuts"):
            st.markdown("""
            **Writing Good Prompts:**
            - ✅ Be specific about inputs/outputs
            - ✅ Mention libraries to use
            - ✅ Specify edge cases to handle
            - ✅ Include performance requirements
            
            **Pro Tips:**
            - 🎯 Use templates for common tasks
            - 📚 Review history for reuse
            - ⭐ Save favorite generations
            - 🔄 Iterate on existing code
            """)
        
        st.markdown("---")
        
        # ========== FOOTER ==========
        st.markdown("""
        <div style='text-align: center; padding: 1rem 0; color: #666; font-size: 0.85rem;'>
            <p style='margin: 5px 0;'>💡 <b>Powered by Google Gemini AI</b></p>
            <p style='margin: 5px 0;'>🔒 Your data is secure</p>
            <p style='margin: 5px 0;'>📱 v1.2.0 | Built with Streamlit</p>
            <p style='margin: 5px 0;'>Made with ❤️ by Ehtisham for developers</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Return all settings as dictionary
    return settings


def save_to_history(prompt, code, language, code_type):
    """
    Save generated code to history
    
    Args:
        prompt: The user's prompt
        code: Generated code
        language: Programming language
        code_type: Type of code generated
    """
    history_item = {
        'prompt': prompt,
        'code': code,
        'language': language,
        'type': code_type,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    st.session_state.code_history.append(history_item)
    
    # Keep only last 50 items to save memory
    if len(st.session_state.code_history) > 50:
        st.session_state.code_history = st.session_state.code_history[-50:]


def get_template_prompt(template_name):
    """
    Returns pre-written prompts for common tasks
    
    Args:
        template_name: Name of the template
        
    Returns:
        String with the template prompt
    """
    templates = {
        "User Authentication": "Create a user authentication system with password hashing, login, and session management",
        "Data Analysis": "Create a script to read CSV data, perform statistical analysis, and create visualizations",
        "REST API": "Build a REST API endpoint with GET, POST, PUT, DELETE methods and error handling",
        "File Handler": "Create a file I/O handler class that can read, write, and process different file formats",
        "Algorithm": "Implement an efficient sorting algorithm with time complexity analysis",
        "Database CRUD": "Create a database handler class with Create, Read, Update, Delete operations"
    }
    return templates.get(template_name, "")