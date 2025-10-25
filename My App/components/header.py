"""
Professional Header Component for AI Code Generator
Save this as: components/header.py
Import in your main file: from components import header
Use: header.create_header()
"""

import streamlit as st

def create_header():
    """
    Creates a beautiful, professional header with navigation
    """
    
    # Custom CSS for the header
    st.markdown("""
    <style>    
         /* Header Container */
        .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 2rem;
        border-radius: 0;  /* Remove rounded corners for full-width */
        margin-bottom: 2rem;
        margin-top: -5rem;  /* Pull it to the very top */
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        position: sticky;  /* Make it stick to top when scrolling */
        top: 0;
        z-index: 999;
    }       
        /* Brand Section */
        .brand-section {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        
        .brand-logo {
            font-size: 2.5rem;
            animation: rotate 3s linear infinite;
        }
        
        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .brand-name {
            font-size: 2rem;
            font-weight: 800;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            letter-spacing: 1px;
        }
        
        .brand-tagline {
            color: rgba(255,255,255,0.9);
            font-size: 0.95rem;
            font-style: italic;
            margin-top: -0.5rem;
        }
        
        /* Navigation Bar */
        .nav-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }
        
        .nav-links {
            display: flex;
            gap: 1.5rem;
            flex-wrap: wrap;
        }
        
        .nav-link {
            color: white;
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            transition: all 0.3s ease;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
        }
        
        .nav-link:hover {
            background: rgba(255,255,255,0.25);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        .nav-link.active {
            background: rgba(255,255,255,0.3);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        
        /* User Section */
        .user-section {
            display: flex;
            gap: 1rem;
            align-items: center;
        }
        
        .user-badge {
            background: rgba(255,255,255,0.2);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            color: white;
            font-weight: 600;
            font-size: 0.9rem;
            backdrop-filter: blur(10px);
        }
        
        /* Profile Section */
        .profile-section {
            background: rgba(255,255,255,0.15);
            padding: 1rem;
            border-radius: 10px;
            margin-top: 1rem;
            backdrop-filter: blur(10px);
        }
        
        .profile-info {
            color: white;
            line-height: 1.6;
        }
        
        .profile-title {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: white;
        }
        
        .social-links {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .social-link {
            background: rgba(255,255,255,0.2);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            text-decoration: none;
            font-size: 0.9rem;
            transition: all 0.3s ease;
        }
        
        .social-link:hover {
            background: rgba(255,255,255,0.35);
            transform: scale(1.05);
        }
        
        /* Status Badge */
        .status-badge {
            display: inline-block;
            background: #10b981;
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-left: 0.5rem;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .brand-name {
                font-size: 1.5rem;
            }
            .nav-links {
                width: 100%;
                justify-content: center;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state for navigation
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Home'
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False
    if 'show_profile' not in st.session_state:
        st.session_state.show_profile = False
    
    # Navigation buttons
    # All buttons same width
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        # About Ehtisham Button
        if st.button("Ehtisham", use_container_width=True, key="about_btn"):
            st.session_state.show_profile = True
    
    with col2:
        if st.button(" Home", use_container_width=True, key="home_btn"):
            st.session_state.current_page = 'Home'
            st.session_state.show_profile = False
            st.rerun()
    
    with col3:
        if st.button("About", use_container_width=True, key="about_app_btn"):
            st.session_state.current_page = 'About'
            st.session_state.show_profile = False
            st.rerun()
    
    with col4:
        if st.button("Careers", use_container_width=True, key="careers_btn"):
            st.session_state.current_page = 'Careers'
            st.session_state.show_profile = False
            st.rerun()
    

    with col5:
        if st.button("Contact", use_container_width=False, key="contact_btn"):
            st.session_state.current_page = 'Contact'
            st.session_state.show_profile = False
            st.rerun()

    
    with col6:
        if not st.session_state.is_logged_in:
            if st.button("Login", use_container_width=True, key="login_btn"):
                st.session_state.current_page = 'Login'
                st.session_state.show_profile = False
                st.rerun()
        else:
            if st.button("🚪 Logout", use_container_width=True, key="logout_btn"):
                st.session_state.is_logged_in = False
                st.toast("✅ Logged out successfully!", icon="🚪")
                st.rerun()
    
    # Profile Section (Expandable)
    if st.session_state.show_profile:
        st.subheader("👨‍💻 About Ehtisham")
        st.caption("🟢 Available for projects and collaborations")

    # Profile Description
        st.write(
        """
        👋 **Hi! I'm Ehtisham**, a passionate *Generative AI Engineer in training!*  
        I love working on cutting-edge AI tools and building smart applications that help developers code faster and better.
        """
    )

    # Education Section
        st.write("🎓 **Education:**")
        st.info("Currently studying **BS Data Science** at Virtual University (VU), specializing in Artificial Intelligence and Machine Learning.")

    # Expertise Section
        st.write("💡 **Expertise:**")
        skills = [
        "🤖 Generative AI & Large Language Models",
        "💻 AI-Powered Code Generation",
        "🔧 Python, Streamlit, Google AI Studio",
        "🚀 Building Intelligent Applications"
    ]
        for skill in skills:
            st.markdown(f"- {skill}")

    # Mission Section
        st.write("🎯 **Mission:**")
        st.success("Creating innovative AI solutions that make development faster, smarter, and more accessible to everyone!")

    # Current Project Section
        st.write("🔥 **Current Project:**")
        st.warning(
        "Building an advanced AI Code Generator that helps developers write better code faster using cutting-edge Generative AI technology."
    )

    # Social Links (Interactive Buttons)
        st.write("🌐 **Connect with me:**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/ehtisham-iftikhar-4b6b86309?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BChJs%2F55SQVOwkXtyPUgqjg%3D%3D")
        with col2:
            st.link_button("🐙 GitHub", "https://github.com/ehtisham145")

    # Footer Section
        st.divider()
        st.caption("✨ Empowering developers with AI — by Ehtisham")

    return st.session_state.current_page


def render_page_content(page):
    """
    Renders content based on selected page
    
    Args:
        page: Current page name
    """
    
    if page == 'Home':
        st.markdown("### 🏠 Welcome to Ehtisham AI Code Generator!")
        st.info("🚀 Start generating production-ready code using the power of AI!")
        
    elif page == 'About':
        st.markdown("### ℹ️ About This Application")
        st.markdown("""
        **Ehtisham AI Code Generator** is an advanced AI-powered tool that helps developers:
        
        - ✅ Generate clean, production-ready code instantly
        - ✅ Support for 15+ programming languages
        - ✅ Include comments, tests, and documentation
        - ✅ Follow industry-standard coding practices
        - ✅ Optimize code for performance
        
        **Powered by:**
        - 🤖 Google Gemini AI (Latest Model)
        - ⚡ Streamlit Framework
        - 🎨 Modern UI/UX Design
        
        **Version:** 1.2.0 | **Developer:** Ehtisham
        """)
        
    elif page == 'Chatbot':
        st.markdown("### 💬 AI Code Generator Chatbot")
        st.success("✅ You're in the Code Generator! Use the sidebar to configure and generate your code.")
        
    elif page == 'Contact':
        st.markdown("### 📧 Contact Ehtisham")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Get in Touch:**
            
            📧 **Email:** ehtishamexp@gmail.com
            💼 **LinkedIn:** linkedin.com/in/ehtisham
            🐙 **GitHub:** github.com/ehtisham
            🌐 **Portfolio:** ehtisham-ai.dev
            
            📍 **Location:** Lahore, Pakistan
            🕒 **Availability:** Open for collaboration
            """)
        
        with col2:
            st.markdown("**Send a Message:**")
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message", height=150)
            
            if st.button("📤 Send Message", type="primary"):
                if name and email and message:
                    st.success("✅ Message sent successfully! I'll get back to you soon.")
                else:
                    st.warning("⚠️ Please fill all fields")
        
    elif page == 'Login':
        st.markdown("### 🔐 Login to Your Account")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("---")
            username = st.text_input("👤 Username", placeholder="Enter your username")
            password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
            
            col_a, col_b = st.columns(2)
            with col_a:
                remember = st.checkbox("Remember me")
            with col_b:
                st.markdown("[Forgot Password?](#)")
            
            if st.button("🚀 Login", type="primary", use_container_width=True):
                if username and password:
                    # Simple demo login (in production, use proper authentication)
                    if username == "ehtisham" and password == "demo":
                        st.session_state.is_logged_in = True
                        st.session_state.current_page = 'Home'
                        st.success("✅ Login successful! Welcome back, Ehtisham!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials. Try: username='ehtisham', password='demo'")
                else:
                    st.warning("⚠️ Please enter both username and password")
            
            st.markdown("---")
            st.caption("Don't have an account? [Sign up here](#)")
    elif page=='Careers':
        st.markdown("### 🚀 Careers at Ehtisham Solutions")
        st.markdown("""
        **Join Our Team!**
        
        We are looking for passionate individuals to join our mission of revolutionizing code generation with AI.
        
        **Open Positions:**
        - AI Researcher
        - Full-Stack Developer
        - UX/UI Designer
        - Marketing Specialist
        
        **Why Work With Us?**
        - 🌟 Innovative Projects
        - 🤖 Cutting-Edge AI Technology
        - 🌍 Remote Work Opportunities
        - 📈 Career Growth

        **Apply Now:** Send your resume and portfolio to [ehtishamexp@gmail.com](mailto:ehtishamexp@gmail.com)      
""",unsafe_allow_html=True)
def get_current_page():
    """Returns the current active page"""
    return st.session_state.get('current_page', 'Home')


def is_user_logged_in():
    """Returns login status"""
    return st.session_state.get('is_logged_in', False)