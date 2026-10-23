
import streamlit as st

st.set_page_config(
    page_title="My Portofolio",
    page_icon="🪪",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(ellipse at top right, #291641 0%, transparent 42%),
        linear-gradient(135deg, #09090f 0%, #15101f 55%, #0b0b12 100%);
    color: #f5f3ff;
}

.st-key-welcome_hero {
    background: linear-gradient(115deg, #291640, #171020 75%);
    border: 1px solid #604080;
    border-radius: 24px;
    padding: 20px;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #120d20, #0b0a11);
    border-right: 1px solid #352347;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] p {
    color: #f5f3ff;
}

h1, h2, h3 {
    color: #eee5ff !important;
}

p, li, label {
    color: #d7d0e5;
}

[data-testid="stMetric"] {
    background: rgba(139, 92, 246, 0.10);
    border: 1px solid #39264f;
    padding: 18px;
    border-radius: 15px;
}

.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #7c3aed, #c4b5fd);
}

div.stButton > button,
div.stLinkButton > a {
    background: linear-gradient(100deg, #7c3aed, #9f67ed);
    color: white;
    border: 1px solid #a78bfa;
    border-radius: 10px;
}

div.stButton > button:hover,
div.stLinkButton > a:hover {
    border-color: #ddd6fe;
    color: white;
}

hr {
    border-color: #39264f;
}

.portfolio-card {
    background: linear-gradient(
        135deg,
        rgba(139, 92, 246, 0.13),
        rgba(28, 22, 40, 0.78)
    );
    border: 1px solid #443058;
    border-radius: 18px;
    padding: 23px;
    margin-bottom: 14px;
    min-height: 125px;
}

.portfolio-card h3 {
    margin-top: 0;
    color: #e9d5ff;
}

.portfolio-card p {
    color: #d7d0e5;
    line-height: 1.7;
}

.eyebrow {
    color: #c4b5fd;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 600;
}

.hero {
    background: linear-gradient(115deg, #291640, #171020 75%);
    border: 1px solid #604080;
    border-radius: 24px;
    padding: 35px;
    margin-bottom: 24px;
}

.hero h1 {
    font-size: 2.6rem;
    margin-bottom: 10px;
}

.hero p {
    line-height: 1.8;
}

.quote-card {
    background: rgba(139, 92, 246, 0.09);
    border-left: 4px solid #a78bfa;
    border-radius: 6px 14px 14px 6px;
    padding: 20px;
    margin: 12px 0;
}

div[data-testid="stImage"] img {
    border-radius: 18px;
}

#MainMenu, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

profil = st.Page(
    "pages/profil.py",
    title="Profil",
    icon="👤"
)

akun = st.Page(
    "pages/akun.py",
    title="Akun",
    icon="🌐"
)

kemampuan = st.Page(
    "pages/kemampuan.py",
    title="Kemampuan",
    icon="✨"
)

pg = st.navigation(
    [home, profil, akun, kemampuan],
    position="sidebar"
)

with st.sidebar:
    st.subheader("💜 PORTOFOLIO HAYKAL")
    st.divider()
    st.write("Universitas Nurdin Hamzah")
    st.write("Ilmu Komputer")
    st.write("Sistem Informasi")
    st.divider()

pg.run()