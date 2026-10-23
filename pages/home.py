import streamlit as st

with st.container(border=True, key="welcome_hero"):
    col1, col2 = st.columns([3, 2], gap="large")
    
    with col1:
        st.caption("WELCOME TO MY PORTFOLIO")
        st.title("Halo, Saya Said Haykal! 👋")
        st.subheader("Mahasiswa Sistem Informasi")

        st.write(
            "Selamat datang di portofolio pribadi saya. "
            "Perkenalkan, saya Said Haykal, mahasiswa "
            "Program Studi Sistem Informasi di Universitas "
            "Nurdin Hamzah, Kota Jambi. Portofolio ini saya buat "
            "untuk memperkenalkan diri, membagikan akun media sosial, "
            "menjelaskan minat keilmuan, serta menunjukkan kemampuan "
            "yang sedang saya kembangkan. Silakan jelajahi setiap "
            "halaman untuk mengenal saya lebih dekat."
        )

    with col2:
        st.video("pages/videohaykal.mp4")

st.subheader("⟪Jelajahi Portofolio Saya⟫")
st.write("Pilih menu di bawah ini untuk melihat informasi lebih lanjut.")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="portfolio-card">
        <h3>👤 Profil</h3>
        <p>Kenali identitas, hobi, moto hidup,
        dan minat keilmuan saya.</p>
    </div>
    """, unsafe_allow_html=True)
            
    if st.button("Lihat Profil →", key="btn_profil", use_container_width=True):
        st.switch_page("pages/profil.py")

    st.markdown("""
    <div class="portfolio-card">
        <h3>🌐 Akun</h3>
        <p>Lihat Gmail dan Instagram saya.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Lihat Akun →", key="btn_akun", use_container_width=True):
        st.switch_page("pages/akun.py")   

with col2:
    st.markdown("""
    <div class="portfolio-card">
        <h3>✨ Kemampuan</h3>
        <p>Kenali bidang yang saya pelajari
        dan kembangkan.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Lihat Kemampuan →", key="btn_kemampuan", use_container_width=True):
        st.switch_page("pages/kemampuan.py")

st.divider()