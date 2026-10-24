
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
    background-color: #09070f;
    background-image:
        linear-gradient(
            135deg,
            rgba(9, 7, 15, 0.45),
            rgba(20, 10, 32, 0.40)
        ),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='174' viewBox='0 0 100 174'%3E%3Cg fill='none' stroke='%238b5cf6' stroke-opacity='.65' stroke-width='1'%3E%3Cpath d='M25 1 L49 15 L49 43 L25 57 L1 43 L1 15 Z M75 30 L99 44 L99 72 L75 86 L51 72 L51 44 Z M25 59 L49 73 L49 101 L25 115 L1 101 L1 73 Z M75 88 L99 102 L99 130 L75 144 L51 130 L51 102 Z M25 117 L49 131 L49 159 L25 173 L1 159 L1 131 Z'/%3E%3C/g%3E%3C/svg%3E");
    background-attachment: fixed;
    background-size: auto, 100px 174px;
}

.st-key-welcome_hero {
    background: linear-gradient(
        135deg,
        rgba(139, 92, 246, 0.12),
        rgba(28, 22, 40, 0.35)
    );
    border: 1px solid rgba(167, 139, 250, 0.55);
    border-radius: 24px;
    padding: 20px;
}


[data-testid="stSidebar"] {
    background-color: #09070F !important;
    background-image:
        radial-gradient(
            ellipse at 20% 0%,
            rgba(124, 58, 237, 0.16),
            transparent 55%
        ),
        linear-gradient(
            180deg,
            #170E21 0%,
            #0D0913 50%,
            #09070F 100%
        ) !important;

    background-size: 100% 100%;
    background-repeat: no-repeat;

    border-right: 1px solid rgba(167, 139, 250, 0.28);
    box-shadow: 4px 0 25px rgba(124, 58, 237, 0.06);
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
    position="hidden"
)


with st.sidebar:
    st.subheader("💜 PORTOFOLIO HAYKAL")
    st.divider()
    st.page_link("pages/home.py", label="Home", icon="🏠")
    st.page_link("pages/profil.py", label="Profil", icon="👤")
    st.page_link("pages/akun.py", label="Akun", icon="🌐")
    st.page_link("pages/kemampuan.py", label="Kemampuan", icon="✨")

    st.divider()

    # Informasi kampus
    st.write("Universitas Nurdin Hamzah")
    st.write("Ilmu Komputer")
    st.write("Sistem Informasi")

    st.divider()

# Jalankan halaman yang dipilih
pg.run()
