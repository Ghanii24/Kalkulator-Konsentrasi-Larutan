import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Konsentrasi Larutan",
    page_icon="⚗️",
    layout="centered"
)

# Sidebar navigasi
halaman = st.sidebar.selectbox("Select Here", [
    "🏠 Beranda", 
    "🔬 Kalkulator Konsentrasi", 
    "👥 Identitas Kelompok"
])

# =========================
# Halaman Beranda
# =========================
if halaman == "🏠 Beranda":
    st.title("🏠 Selamat Datang di Aplikasi Kalkulator Konsentrasi Larutan ⚗️")
    st.markdown("""
    ### 🎯 Tujuan Aplikasi
    Aplikasi ini dibuat untuk membantu siswa, mahasiswa, dan tenaga pendidik dalam menghitung berbagai jenis konsentrasi larutan secara cepat dan akurat.

    ### 🧪 Rumus yang Digunakan
    - **PPM (Part per Million)**: `PPM = massa zat terlarut (mg) / volume larutan (L)`
    - **Molaritas (M)**: `M = mol zat / volume larutan (L)`
    - **Molalitas (m)**: `m = mol zat / massa pelarut (kg)`
    - **Normalitas (N)**: `N = ekivalen zat / volume larutan (L)`
    - **Molaritas dari Massa dan Mr**: `M = (massa zat / Mr) / volume larutan (L)`

    ### 🧭 Petunjuk Penggunaan
    Silakan gunakan **navigasi di kiri atas** (sidebar) untuk mengakses:
    - Kalkulator konsentrasi
    - Identitas kelompok

    Terima kasih telah menggunakan aplikasi kami! 🙌
    """)

# =========================
# Halaman Kalkulator
# =========================
elif halaman == "🔬 Kalkulator Konsentrasi":
    st.title("⚗️ Kalkulator Konsentrasi Larutan 🧪")
    st.markdown("""
    Aplikasi ini membantu Anda menghitung berbagai jenis konsentrasi larutan:

    - 🔹 *PPM (Part per Million)*
    - 🧪 *Molaritas (mol/L)*
    - ⚖️ *Molalitas (mol/kg)*
    - 📏 *Normalitas (N)*
    - 📘 *Molaritas dari Massa & Mr*

    Silakan pilih jenis perhitungan dan masukkan data yang diperlukan. 📥
    """)

    choice = st.selectbox("🔍 Pilih jenis konsentrasi yang ingin dihitung:", 
                          ["🟦 PPM (part per million)", 
                           "🧪 Molaritas (mol/L)", 
                           "⚖️ Molalitas (mol/kg)", 
                           "📏 Normalitas (N)",
                           "📘 Molaritas (dari massa & Mr)"])

    st.divider()

    def hitung_ppm(massa_zat, volume_larutan):
        return massa_zat / volume_larutan

    def hitung_molaritas(mol_zat, volume_larutan):
        return mol_zat / volume_larutan

    def hitung_molalitas(mol_zat, massa_pelarut):
        return mol_zat / massa_pelarut

    def hitung_normalitas(ekivalen, volume_larutan):
        return ekivalen / volume_larutan

    def hitung_molaritas_dari_massa(massa_zat, mr, volume_larutan):
        mol = massa_zat / mr
        return mol / volume_larutan

    if "PPM" in choice:
        st.subheader("🟦 Perhitungan PPM")
        massa_zat = st.number_input("📦 Massa zat terlarut (mg)", min_value=0.0, step=0.01)
        volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)
        if st.button("🧮 Hitung PPM"):
            ppm = hitung_ppm(massa_zat, volume_larutan)
            st.success(f"✅ Konsentrasi PPM: {ppm:.10g} mg/L")

    elif "Molaritas (mol/L)" in choice:
        st.subheader("🧪 Perhitungan Molaritas")
        mol_zat = st.number_input("🧬 Jumlah mol zat (mol)", min_value=0.0, step=0.01)
        volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)
        if st.button("🧮 Hitung Molaritas"):
            molaritas = hitung_molaritas(mol_zat, volume_larutan)
            st.success(f"✅ Konsentrasi Molaritas: {molaritas:.10g} mol/L")

    elif "Molalitas" in choice:
        st.subheader("⚖️ Perhitungan Molalitas")
        mol_zat = st.number_input("🧬 Jumlah mol zat (mol)", min_value=0.0, step=0.01)
        massa_pelarut = st.number_input("💧 Massa pelarut (kg)", min_value=0.0001, step=0.01)
        if st.button("🧮 Hitung Molalitas"):
            molalitas = hitung_molalitas(mol_zat, massa_pelarut)
            st.success(f"✅ Konsentrasi Molalitas: {molalitas:.10g} mol/kg")

    elif "Normalitas" in choice:
        st.subheader("📏 Perhitungan Normalitas")
        ekivalen = st.number_input("🧪 Jumlah ekivalen zat (mol ekivalen)", min_value=0.0, step=0.01)
        volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)
        if st.button("🧮 Hitung Normalitas"):
            normalitas = hitung_normalitas(ekivalen, volume_larutan)
            st.success(f"✅ Konsentrasi Normalitas: {normalitas:.10g} N")

    elif "Molaritas (dari massa & Mr)" in choice:
        st.subheader("📘 Perhitungan Molaritas dari Massa & Mr")
        massa_zat = st.number_input("⚖️ Massa zat (gram)", min_value=0.0, step=0.01)
        mr = st.number_input("🔬 Massa molar (Mr) zat (g/mol)", min_value=0.01, step=0.01)
        volume_larutan = st.number_input("🧴 Volume larutan (liter)", min_value=0.0001, step=0.01)
        if st.button("🧮 Hitung Molaritas dari Massa"):
            molaritas_massa = hitung_molaritas_dari_massa(massa_zat, mr, volume_larutan)
            st.success(f"✅ Konsentrasi Molaritas: {molaritas_massa:.10g} mol/L")

    # Watermark
    st.markdown(
        """
        <div style="
            position: relative;
            left: 0;
            width: 100%;
            background-color: white;
            border-radius: 12px;
            padding: 15px 25px;
            color: #333333;
            font-size: 16px;
            margin-top: 30px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.08);
            text-align: left;
        ">
            <p>🧪✨ <b>Dibuat oleh kelompok:</b></p>
            <p>👨‍🔬 <b>Andika</b> • 👩‍🔬 <b>Audrey</b> • 👩‍🔬 <b>Maqdalene</b> • 👨‍🔬 <b>Raihan</b> • 👩‍🔬 <b>Rifa</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# Halaman Identitas Kelompok
# =========================
elif halaman == "👥 Identitas Kelompok":
    st.title("👥 Identitas Kelompok")
    st.markdown("---")
    st.markdown(
        """
        <div style="
            background-color: rgba(255, 255, 255, 0.0);
            border-radius: 12px;
            padding: 20px;
            color: white;
            font-size: 18px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        ">
            <p><b>📚 Nama Kelompok:</b> Kelompok 5</p>
            <p><b>👩‍🔬 Anggota:</b></p>
            <ul>
                <li>👨‍🔬 Andika</li>
                <li>👩‍🔬 Audrey</li>
                <li>👩‍🔬 Maqdalene</li>
                <li>👨‍🔬 Raihan</li>
                <li>👩‍🔬 Rifa</li>
            </ul>
            <p>✨ Terima kasih telah menggunakan aplikasi kami! ✨</p>
        </div>
        """,
        unsafe_allow_html=True
    )
