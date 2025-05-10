import streamlit as st
import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Demo Sidebar Responsif", layout="wide")

# CSS untuk sidebar responsif terhadap tema gelap/terang
st.markdown(
    """
    <style>
    @media (prefers-color-scheme: dark) {
        section[data-testid="stSidebar"] {
            background-color: #1e1e1e;
            color: white;
        }
    }

    @media (prefers-color-scheme: light) {
        section[data-testid="stSidebar"] {
            background-color: #f0f2f6;
            color: black;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Kalkulator Konsentrasi Larutan",
    page_icon="⚗️",
    layout="centered"
)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)),
                    url('https://img.freepik.com/free-photo/side-view-hand-pouring-substance_23-2149731486.jpg?t=st=1746860017~exp=1746863617~hmac=f818fce0db537a021c6c9c2795193a245bf11bdb8deb3535c440fc783e29e887&w=1380');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar navigasi
halaman = st.sidebar.selectbox("📂 Navigasi Halaman", ["🔬 Kalkulator Konsentrasi", "👥 Identitas Kelompok"])

# =========================
# Halaman 1: Kalkulator
# =========================
if halaman == "🔬 Kalkulator Konsentrasi":
    st.title("⚗️ Kalkulator Konsentrasi Larutan")
    st.markdown("""
    Aplikasi ini membantu Anda menghitung berbagai jenis konsentrasi larutan:

    - 🔹 *PPM (Part per Million)*
    - 🧪 *Molaritas (mol/L)*
    - ⚖️ *Molalitas (mol/kg)*
    - 📏 *Normalitas (N)*
    - 📘 *Molaritas dari Massa & Mr*
    
    Silakan pilih jenis perhitungan dan masukkan data yang diperlukan. 📥
    """)

    # ==========Pilihan jenis perhitungan==========
    choice = st.selectbox("🔍 Pilih jenis konsentrasi yang ingin dihitung:", 
                          ["🟦 PPM (part per million)", 
                           "🧪 Molaritas (mol/L)", 
                           "⚖️ Molalitas (mol/kg)", 
                           "📏 Normalitas (N)",
                           "📘 Molaritas (dari massa & Mr)"])

    st.divider()

    # ==========Fungsi perhitungan==========
    def hitung_ppm(massa_zat, volume_larutan):
        return (massa_zat / volume_larutan)

    def hitung_molaritas(mol_zat, volume_larutan):
        return mol_zat / volume_larutan

    def hitung_molalitas(mol_zat, massa_pelarut):
        return mol_zat / massa_pelarut

    def hitung_normalitas(ekivalen, volume_larutan):
        return ekivalen / volume_larutan

    def hitung_molaritas_dari_massa(massa_zat, mr, volume_larutan):
        mol = massa_zat / mr
        return mol / volume_larutan

    # ==========Input dan output berdasarkan pilihan==========
    if "PPM" in choice:
        st.subheader("🟦 Perhitungan PPM")
        massa_zat = st.number_input("📦 Massa zat terlarut (mg)", min_value=0.0, step=0.01)
        volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)
        
        if st.button("🧮 Hitung PPM"):
            ppm = hitung_ppm(massa_zat, volume_larutan)
            st.success(f"✅ Konsentrasi PPM: {ppm:.4f} mg/L")

    elif "Molaritas (mol/L)" in choice:
        st.subheader("🧪 Perhitungan Molaritas")
        mol_zat = st.number_input("🧬 Jumlah mol zat (mol)", min_value=0.0, step=0.01)
        volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)

        if st.button("🧮 Hitung Molaritas"):
            molaritas = hitung_molaritas(mol_zat, volume_larutan)
            st.success(f"✅ Konsentrasi Molaritas: {molaritas:.4f} mol/L")

    elif "Molalitas" in choice:
        st.subheader("⚖️ Perhitungan Molalitas")
        mol_zat = st.number_input("🧬 Jumlah mol zat (mol)", min_value=0.0, step=0.01)
        massa_pelarut = st.number_input("💧 Massa pelarut (kg)", min_value=0.0001, step=0.01)

        if st.button("🧮 Hitung Molalitas"):
            molalitas = hitung_molalitas(mol_zat, massa_pelarut)
            st.success(f"✅ Konsentrasi Molalitas: {molalitas:.4f} mol/kg")

    elif "Normalitas" in choice:
        st.subheader("📏 Perhitungan Normalitas")
        ekivalen = st.number_input("🧪 Jumlah ekivalen zat (mol ekivalen)", min_value=0.0, step=0.01)
        volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)

        if st.button("🧮 Hitung Normalitas"):
            normalitas = hitung_normalitas(ekivalen, volume_larutan)
            st.success(f"✅ Konsentrasi Normalitas: {normalitas:.4f} N")

    elif "Molaritas (dari massa & Mr)" in choice:
        st.subheader("📘 Perhitungan Molaritas dari Massa & Mr")
        massa_zat = st.number_input("⚖️ Massa zat (gram)", min_value=0.0, step=0.01)
        mr = st.number_input("🔬 Massa molar (Mr) zat (g/mol)", min_value=0.01, step=0.01)
        volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)

        if st.button("🧮 Hitung Molaritas dari Massa"):
            molaritas_massa = hitung_molaritas_dari_massa(massa_zat, mr, volume_larutan)
            st.success(f"✅ Konsentrasi Molaritas: {molaritas_massa:.4f} mol/L")

# =========================
# Halaman 2: Identitas Kelompok
# =========================
elif halaman == "👥 Identitas Kelompok":
    st.title("👥 Identitas Kelompok")
    st.markdown("---")
    st.markdown(
        """
        <div style="
            background-color: transparent;
            border-radius: 12px;
            padding: 20px;
            color: white;
            font-size: 18px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
            text-align: left;
        ">
            <p><b>📚 Nama Kelompok:</b> Kelompok 2 (PMIP 1E-1)</p>
            <p><b>👩‍🔬 Anggota:</b></p>
            <ul>
                <li>👨‍🔬 Andika Daffa Arya Putra</li>
                <li>👩‍🔬 Audrey Arva Callista</li>
                <li>👩‍🔬 Maqdalene Tri Okta Dinanti Banjarnahor</li>
                <li>👨‍🔬 Raihan Ghani Priyananda</li>
                <li>👩‍🔬 Rifa Novita Putri Sulaeman</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
