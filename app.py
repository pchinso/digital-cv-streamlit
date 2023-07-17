from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Pablo Climent"
PAGE_ICON = ":wave:"
NAME = "Pablo Climent"
DESCRIPTION = """
Senior Multi-disciplinary Technician.
"""
EMAIL = "pcs.tech.rd@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/pablo-climent-sanchez/",
    "GitHub": "https://github.com/pchinso",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#Pending projects
PROJECTS = {
'Under construction 🚧👷‍♂️': 'https://github.com/pchinso',
}

# '''PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }'''


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
# st.write('\n')
# st.subheader("Experience & Qualifications")
# st.write('Under construction 🚧👷‍♂️')

# st.write(
   
# - ✔️ 7 Years expereince extracting actionable insights from data
# - ✔️ Strong hands on experience and knowledge in Python and Excel
# - ✔️ Good understanding of statistical principles and their respective applications
# - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
# )


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
"""
- 👩‍💻 Programming: Python (Pandas, ), Matlab, C++
- 📊 Data Visualization 
- 🧠 AI & Data analytics
- 📚 Electronics: Arduino, Automation, SCADA
- 🗄️ Databases: SQL, MongoDB
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🌞", "**R&D Technician | Abengoa**")
st.write("10/2008 - Present")
st.write(
    """
- ► Analytical software Development
- ► Data science and performance simulation.
- ► Quality control and calibration.
- ► Metrology.

Skills: 
- ☀ Renewable energies 
- 🚁 Drone photogrammetry
- 📏 Metrology 
- 💻 Software development 
- 📅 SQL 
- 📊 Data visualisation 
- 🐍 Python 
- 👨‍🔧 Troubleshooting 
- 🧠 AI & Data analytics
"""
)

# --- JOB 2
st.write('\n')
st.write("🌊", "**Scada & PLC Technician | AYESA**")
st.write("05/2007 - 09/2008")
st.write(
    """
- ► Commissioning of the SCADA system and automation of the irrigation community of the BXII sector of the Lower Guadalquivir (Lebrija).
- ► Planning of station automation installations for the Malaga Metro infrastructure. 
- ► Installation of SAITEL and SAICOM remote control systems, testing and verification of ENDESA's electricity distribution installations.

Skills: 
- 🖥 SCADA 
- 🔌 PLC Programming 
- 🧪 Field Test & implementation
"""
)

# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")


