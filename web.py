import streamlit as st
from deepface import DeepFace
import os
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="RK Studio | Face Analis Pro", page_icon="🕵️‍♂️", layout="centered")

# --- FUNGSI UNTUK MEMBACA & MEMASANG BACKGROUND GAMBAR ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Mencoba membaca file background.jpg. Jika gagal, gunakan background gelap biasa.
try:
    if os.path.exists("background.jpg"):
        bin_str = get_base64_of_bin_file("background.jpg")
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{bin_str}");
                background-size: cover;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.write("<!- Background image not found, using default dark theme -->", unsafe_allow_html=True)
except Exception as e:
    st.write("<!- Background system error -->", unsafe_allow_html=True)


# --- JURUS PAMUNGKAS: INJEKSI CSS TINGKAT TINGGI (SIBER-NEON GLASSMORPHISM) ---
st.markdown("""
    <style>
    /* Mengubah font global agar lebih modern */
    * { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; }

    /* --- SIDEBAR GLASSMORPHISM & NEON --- */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.05); /* Transparan buram */
        backdrop-filter: blur(20px); /* Efek Kaca Buram */
        -webkit-backdrop-filter: blur(20px);
        border-right: 2px solid rgba(255, 75, 120, 0.4); /* Garis neon samping */
        box-shadow: 10px 0 30px rgba(0, 0, 0, 0.3);
    }
    
    /* Ikon Folder di Sidebar */
    .sidebar-icon {
        color: rgba(255, 75, 120, 1) !important;
        font-size: 70px !important;
        text-align: center !important;
        display: block !important;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 10px rgba(255, 75, 120, 0.7));
    }

    /* Judul di Sidebar */
    .sidebar-header {
        color: white !important;
        font-size: 24px !important;
        font-weight: bold !important;
        text-align: center !important;
        margin-bottom: 5px;
        filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
    }

    /* Deskripsi di Sidebar (Versi screenshot) */
    .sidebar-desc-box {
        background: rgba(255, 255, 255, 0.03);
        border: 2px solid rgba(255, 75, 120, 0.6);
        border-radius: 12px;
        padding: 15px;
        margin-top: 20px;
        font-size: 14px;
        color: rgba(255, 255, 255, 0.9);
        box-shadow: 0 0 15px rgba(255, 75, 120, 0.3);
    }

    /* Footer Sidebar */
    .sidebar-footer {
        color: rgba(255, 255, 255, 0.6) !important;
        font-size: 11px !important;
        text-align: center;
        margin-top: 40px;
    }

    /* --- HALAMAN UTAMA & ELEMEN SIBER --- */
    /* Judul Utama */
    .judul-siber {
        font-size: 40px !important;
        font-weight: bold !important;
        text-align: center !important;
        color: white !important;
        filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.8));
    }

    /* Sub-judul */
    .subjudul-siber {
        font-size: 16px !important;
        text-align: center;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 30px;
    }

    /* Label Upload (👤 Subjek...) */
    .label-upload {
        font-size: 20px;
        font-weight: bold;
        color: white;
        display: flex;
        align-items: center;
        filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
    }

    /* Ikon Profil */
    .icon-profil {
        color: rgba(255, 75, 120, 1);
        margin-right: 10px;
        font-size: 22px;
        filter: drop-shadow(0 0 5px rgba(255, 75, 120, 0.7));
    }

    /* --- KARTU UPLOAD GLASSMORPHISM & GLOW --- */
    div[data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.05) !important; /* Kaca Buram */
        border: 2px solid rgba(255, 75, 120, 0.5) !important; /* Neon glow */
        border-radius: 12px !important;
        padding: 10px !important;
        box-shadow: 0 0 20px rgba(255, 75, 120, 0.3) !important;
    }

    /* Tombol Upload Asli (Diusahakan transparansinya) */
    div[data-testid="stFileUploader"] > section > button {
        background-color: transparent !important;
        border: 1px solid rgba(255, 75, 120, 0.8) !important;
        color: white !important;
        border-radius: 6px !important;
    }

    /* --- KOTAK FOOTER TENGAH & KESIMPULAN --- */
    .footer-tengah-box {
        background: rgba(255, 255, 255, 0.03);
        border: 2px solid rgba(255, 75, 120, 0.7);
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        color: white;
        margin-top: 30px;
        box-shadow: 0 0 15px rgba(255, 75, 120, 0.4);
    }
    
    .footer-desc {
        color: white;
    }
    
    .creator-glow {
        color: rgba(255, 75, 120, 1);
        filter: drop-shadow(0 0 7px rgba(255, 75, 120, 0.8));
    }

    /* Menyesuaikan jarak pembatas */
    .stDivider {
        border-bottom: 2px solid rgba(255, 75, 120, 0.4) !important;
        filter: drop-shadow(0 0 5px rgba(255, 75, 120, 0.5));
    }

    </style>
""", unsafe_allow_html=True)


# --- KONSTRUKSI UI (GLASSMORPHISM EDITION) ---

# --- SIDEBAR (Kustomisasi Screenshot) ---
with st.sidebar:
    # Menggunakan HTML Kustom untuk ikon dan teks bergaya siber
    st.markdown('<div class="sidebar-icon">📁</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-header">Tentang Creator</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:rgba(255,255,255,0.8); text-align:center;">RK STUDIO (MASAK AER)</p>', unsafe_allow_html=True)
    
    # Kotak deskripsi transparan & glow
    st.markdown("""
        <div class="sidebar-desc-box">
            Aplikasi web ini dirancang khusus untuk memverifikasi keaslian foto wajah secara instan & akurat menggunakan teknologi <span class='creator-glow'>Deep Learning</span>.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="sidebar-footer">© 2026 Hak Cipta Dilindungi<br>Powered by RK Studio</p>', unsafe_allow_html=True)

# --- HALAMAN UTAMA (Desain Siber) ---
st.markdown('<div class="judul-siber">AI Face Matcher Pro 🕵️‍♂️</div>', unsafe_allow_html=True)
st.markdown('<div class="subjudul-siber">Sistem verifikasi identitas cerdas. Unggah dua foto untuk memulai pemindaian.</div>', unsafe_allow_html=True)

# 1. Kolom Upload dengan Label Transparan
kolom1, kolom2 = st.columns(2)

with kolom1:
    st.markdown('<p class="label-upload"><span class="icon-profil">👤</span> Subjek Pertama</p>', unsafe_allow_html=True)
    foto1 = st.file_uploader("Pilih foto (Resolusi baik)", type=['jpg', 'jpeg', 'png'])

with kolom2:
    st.markdown('<p class="label-upload"><span class="icon-profil">👤</span> Subjek Kedua</p>', unsafe_allow_html=True)
    foto2 = st.file_uploader("Pilih foto pembanding", type=['jpg', 'jpeg', 'png'])

# 2. Area Preview & Eksekusi
if foto1 and foto2:
    st.image([foto1, foto2], caption=["Foto 1", "Foto 2"], use_container_width=True)
    
    st.markdown("---")
    
    # 3. Tombol Eksekusi
    if st.button("Mulai Bandingkan Wajah!", use_container_width=True):
        
        with st.spinner('Mesin AI sedang memindai wajah...'):
            try:
                nama_file1 = "tmp1_" + foto1.name
                nama_file2 = "tmp2_" + foto2.name
                
                with open(nama_file1, "wb") as f:
                    f.write(foto1.getbuffer())
                with open(nama_file2, "wb") as f:
                    f.write(foto2.getbuffer())
                
                hasil = DeepFace.verify(img1_path=nama_file1, img2_path=nama_file2)
                
                os.remove(nama_file1)
                os.remove(nama_file2)
                
                # Kesimpulan Glassmorphism
                if hasil["verified"] == True:
                    st.success("✅ KESIMPULAN: WAJAH COCOK! AI sangat yakin ini adalah orang yang sama.")
                else:
                    st.error("❌ KESIMPULAN: WAJAH BERBEDA! AI menilai ini adalah dua orang yang berbeda.")
                    
            except Exception as e:
                st.error(f"⚠️ Terjadi kendala sistem: {e}")

# 4. Kotak Footer Tengah (Glassmorphism Screenshot)
st.markdown("""
    <div class="footer-tengah-box">
        <p class="footer-desc">Developed by <b class="creator-glow">RK STUDIO (MASAK AER)</b></p>
    </div>
""", unsafe_allow_html=True)
