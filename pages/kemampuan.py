import streamlit as st

st.title("✨ Kemampuan Saya")
st.write(
    "Bidang yang saya pelajari untuk menambah pengetahuan "
    "dan mengembangkan diri."
)
st.divider()

st.subheader("Bidang yang Saya Kembangkan")

with st.container(border=True):
    st.markdown("### 💻 Perkembangan Teknologi")
    st.write(
        "Mempelajari teknologi dan pemrograman "
        "serta mengikuti perkembangan inovasi digital."
    )
    st.progress(75, text="Proses Pembelajaran — 75%")

with st.container(border=True):
    st.markdown("### 📊 Keilmuan Bisnis")
    st.write(
        "Mempelajari dasar bisnis, manajemen, "
        "dan proses bisnis."
    )
    st.progress(69, text="Proses Pembelajaran — 69%")

with st.container(border=True):
    st.caption("03 / PERSONAL DEVELOPMENT")
    st.markdown("### 🌱 Pengembangan Diri")
    st.write(
        "Mengembangkan wawasan, pola pikir, "
        "dan kemampuan melalui proses belajar."
    )
    st.progress(87, text="Proses Pembelajaran — 87%")

st.divider()

st.markdown("""
<div class="portfolio-card">
    <h3>🎯 Komitmen Saya</h3>
    <p>
        Saya akan terus belajar, memperbaiki kekurangan,
        dan mengembangkan kemampuan agar dapat menghadapi
        tantangan di bidang teknologi maupun bisnis.
    </p>
</div>
""", unsafe_allow_html=True)

st.caption(
    "Persentase merupakan perkiraan perkembangan belajar "
    "dan dapat meningkat dengan kondisi diri sendiri."
)

st.divider()
st.page_link(
    "pages/home.py",
    label="← Kembali ke Home",
    icon="🏠"
)