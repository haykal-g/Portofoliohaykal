
import streamlit as st

st.title("👤 Profil Saya")
st.write("Kenali saya lebih dekat.")
st.divider()

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image(
        "pages/imagehaykal.jpeg",
        caption="Foto Haykal",
        use_container_width=True
    )

with col2:
    st.markdown("""
    <div class="portfolio-card">
        <div class="eyebrow">PERKENALKAN, SAYA 🙌</div>
        <h2>Said Haykal</h2>
        <p>🎓 <b>Universitas</b><br>
        Universitas Nurdin Hamzah</p>
        <p>🖥️ <b>Fakultas</b><br>
        Ilmu Komputer</p>
        <p>📓 <b>Program Studi</b><br>
        Sistem Informasi</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.subheader("Tentang Saya")

col3, col4 = st.columns([3, 4], gap="medium")

with col3:
    st.markdown("""
    <div class="portfolio-card">
        <h3>🎧 Hobi</h3>
        <p><b>Mendengarkan podcast</b></p>
        <p>
            Saya senang mendengarkan podcast karena dapat
            menambah wawasan, memperoleh sudut pandang baru,
            serta mempelajari berbagai hal yang bahkan
            belum saya ketahui.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="portfolio-card">
        <h3>💡 Minat Keilmuan</h3>
        <p><b>💻 Perkembangan Teknologi</b></p>
        <p>
            Saya tertarik mempelajari perkembangan teknologi
            dan inovasi terbaru serta pemanfaatannya
            dalam kehidupan sehari-hari.
        </p>
        <p><b>📊 Keilmuan Bisnis</b></p>
        <p>
            Saya tertarik mempelajari manajemen, proses bisnis,
            dan cara mengembangkan usaha dengan baik.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.subheader("Moto Hidup")

st.markdown("""
<div class="quote-card">
    <h3>“Tidak harus hebat untuk memulai, tetapi harus
    memulai untuk menjadi hebat.”</h3>
</div>
""", unsafe_allow_html=True)

st.divider()
st.page_link(
    "pages/home.py",
    label="← Kembali ke Home",
    icon="🏠"
)