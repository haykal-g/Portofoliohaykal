
import streamlit as st

st.title("🌐 Akun Saya")
st.write("Temukan dan hubungi saya melalui akun berikut.")
st.divider()

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="portfolio-card">
        <h3>✉️ Gmail</h3>
        <p>
            Untuk keperluan komunikasi, silakan
            menghubungi saya melalui email.
        </p>
        <p><b>hurufabjadh09@gmail.com</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "✉️ Kirim Email",
        "mailto:hurufabjadh09@gmail.com",
        use_container_width=True
    )

with col2:
    st.markdown("""
    <div class="portfolio-card">
        <h3>📸 Instagram</h3>
        <p>
            Kunjungi akun Instagram saya untuk melihat
            aktivitas dan konten yang saya bagikan.
        </p>
        <p><b>@said.haykal</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "📸 Kunjungi Instagram",
        "https://www.instagram.com/said.haykal",
        use_container_width=True
    )

st.divider()

st.markdown("""
<div class="portfolio-card">
    <h3>🤝 Mari Terhubung</h3>
    <p>
        Terbuka untuk menjalin komunikasi,
        berbagi informasi, dan menambah relasi.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()
st.page_link(
    "pages/home.py",
    label="← Kembali ke Home",
    icon="🏠"
)