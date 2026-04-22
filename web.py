import streamlit as st
from deepface import DeepFace
import os
import base64

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="RK Studio | Face Analis Pro", page_icon="🕵️‍♂️", layout="centered")

# --- FUNGSI UNTUK MEMBACA & MEMASANG BACKGROUND GAMBAR ---
def set_background(image_file):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, image_file)
        
        with open(file_path, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{bin_str}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            [data-testid="stAppViewContainer"] {{
                background-image: url("data:image/jpeg;base64,{bin_str}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            [data-testid="stHeader"] {{
                background-color: transparent !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        pass

set_background("background.jpg")

# --- INJEKSI CSS TINGKAT TINGGI (KOTAK RAMPING) ---
st.markdown("""
    <style>
    /* Menyembunyikan sidebar sepenuhnya jika masih ada sisa-sisa */
    [data-testid="stSidebar"] {
        display: none;
    }

    .judul-siber {
        font-size: 40px !important;
        font-weight: bold !important;
        text-align: center !important;
        color: white !important;
        filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.8));
    }

    .subjudul-siber {
        font-size: 16px !important;
        text-align: center;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 30px;
    }

    .label-upload {
        font-size: 18px;
        font-weight: bold;
        color: white;
        display: flex;
        align-items: center;
        filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
    }

    .icon-profil {
        color: rgba(255, 75, 120, 1);
        margin-right: 10px;
    }

    div[data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.05) !important; 
        border: 2px solid rgba(255, 75, 120, 0.5) !important; 
        border-radius: 12px !important;
        box-shadow: 0 0 20px rgba(255, 75, 120, 0.3) !important;
    }

    /* --- CSS KOTAK FOOTER RAMPING (KUNCI PERUBAHAN) --- */
    .footer-container {
        text-align: center; /* Memastikan kotak yang inline berada di tengah */
        margin-top: 40px;
        width: 100%;
    }

    .footer-tengah-box {
        display: inline-block; /* KOTAK MENGIKUTI LEBAR TEKS */
        background: rgba(255, 255, 255, 0.03);
        border: 2px solid rgba(255, 75, 120, 0.7);
        border-radius: 12px;
        padding: 10px 25px; /* Padding samping agar tulisan tidak nempel ke garis */
        color: white;
        box-shadow: 0 0 20px rgba(255, 75, 120, 0.4);
    }
    
    .creator-glow {
        color: rgba(255, 75, 120, 1);
        filter: drop-shadow(0 0 7px rgba(255, 75, 120, 0.8));
    }
    </style>
""", unsafe_allow_html=True)

# --- HALAMAN UTAMA ---
st.markdown('<div class="judul-siber">AI Face Matcher Pro 🕵️‍♂️</div>', unsafe_allow_html=True)
st.markdown('<div class="subjudul-siber">Sistem verifikasi identitas cerdas dengan AI Retina Face dan Deep Learning.</div>', unsafe_allow_html=True)

kolom1, kolom2 = st.columns(2)

with kolom1:
    st.markdown('<p class="label-upload"><span class="icon-profil">👤</span> Subjek Pertama</p>', unsafe_allow_html=True)
    foto1 = st.file_uploader("Pilih foto (Resolusi baik)", type=['jpg', 'jpeg', 'png'], key="f1")

with kolom2:
    st.markdown('<p class="label-upload"><span class="icon-profil">👤</span> Subjek Kedua</p>', unsafe_allow_html=True)
    foto2 = st.file_uploader("Pilih foto pembanding", type=['jpg', 'jpeg', 'png'], key="f2")

if foto1 and foto2:
    st.image([foto1, foto2], caption=["Foto 1", "Foto 2"], use_container_width=True)
    
    if st.button("Mulai Bandingkan Wajah!", use_container_width=True):
        with st.spinner('Memindai struktur wajah...'):
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
                
                if hasil["verified"] == True:
                    st.success("✅ KESIMPULAN: WAJAH COCOK!")
                else:
                    st.error("❌ KESIMPULAN: WAJAH BERBEDA!")
            except Exception as e:
                st.error(f"⚠️ Kendala sistem: {e}")

# --- FOOTER TENGAH (HASIL DESAIN RAMPING) ---
st.markdown("""
    <div class="footer-container">
        <div class="footer-tengah-box">
            <p style="margin:0; font-size: 14px;">Developed by <b class="creator-glow">RK STUDIO (MASAK AER)</b></p>
        </div>
    </div>
""", unsafe_allow_html=True)
