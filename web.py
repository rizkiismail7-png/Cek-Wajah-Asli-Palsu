import streamlit as st
from deepface import DeepFace
import os

# 1. Konfigurasi Halaman Dasar
st.set_page_config(page_title="AI Face Match | RK Studio", page_icon="🧿", layout="centered")

# --- INJEKSI CSS KUSTOM UNTUK ESTETIKA ---
# Bagian ini akan mengubah tampilan standar Streamlit menjadi lebih premium
st.markdown("""
    <style>
    /* Desain Gradient untuk Judul Utama */
    .judul-glowing {
        font-size: 42px;
        font-weight: bold;
        background: -webkit-linear-gradient(45deg, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
    }
    /* Desain Sub-judul */
    .sub-judul {
        text-align: center;
        color: #888888;
        font-size: 18px;
        margin-bottom: 30px;
    }
    /* Mengubah desain tombol utama */
    div.stButton > button:first-child {
        background-color: #FF416C;
        color: white;
        border-radius: 12px;
        height: 50px;
        font-weight: bold;
        font-size: 18px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4);
        transition: all 0.3s ease 0s;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(255, 65, 108, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ESTETIK ---
with st.sidebar:
    # Anda bisa mengganti link gambar ini dengan logo asli RK Studio jika ada
    st.image("https://cdn-icons-png.flaticon.com/512/1157/1157077.png", width=80) 
    st.markdown("## 🚀 Tentang Creator")
    st.markdown("**RK STUDIO (MASAK AER)**")
    
    # Kotak info agar lebih mencolok
    st.info("Aplikasi web ini dirancang khusus untuk memverifikasi keaslian foto wajah secara instan & akurat menggunakan teknologi *Deep Learning*.")
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 12px; color: gray;'>© 2026 Hak Cipta Dilindungi<br>Powered by RK Studio</p>", unsafe_allow_html=True)

# --- HEADER UTAMA ---
st.markdown("<div class='judul-glowing'>AI Face Matcher Pro 🧿</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-judul'>Sistem verifikasi identitas cerdas. Unggah dua foto untuk memulai pemindaian.</div>", unsafe_allow_html=True)

# 2. AREA UPLOAD FOTO (Desain Kartu)
kolom1, kolom2 = st.columns(2)

with kolom1:
    st.markdown("#### 👤 Subjek Pertama")
    foto1 = st.file_uploader("Pilih foto (Resolusi baik)", type=['jpg', 'jpeg', 'png'], key="f1")

with kolom2:
    st.markdown("#### 👤 Subjek Kedua")
    foto2 = st.file_uploader("Pilih foto pembanding", type=['jpg', 'jpeg', 'png'], key="f2")

# 3. AREA PREVIEW & EKSEKUSI
if foto1 and foto2:
    st.markdown("---")
    
    # Menampilkan preview dengan rapi
    col_prev1, col_prev2 = st.columns(2)
    with col_prev1:
        st.image(foto1, caption="Preview Wajah 1", use_container_width=True)
    with col_prev2:
        st.image(foto2, caption="Preview Wajah 2", use_container_width=True)
    
    st.write("<br>", unsafe_allow_html=True) # Jarak estetik
    
    # 4. TOMBOL EKSEKUSI
    if st.button("Mulai Pemindaian Biometrik ⚡", use_container_width=True):
        
        with st.spinner('⏳ AI sedang mengekstraksi titik wajah (Facial Landmarks)...'):
            try:
                nama_file1 = "temp_" + foto1.name
                nama_file2 = "temp_" + foto2.name
                
                with open(nama_file1, "wb") as f:
                    f.write(foto1.getbuffer())
                with open(nama_file2, "wb") as f:
                    f.write(foto2.getbuffer())
                
                # Proses AI mencocokkan wajah
                hasil = DeepFace.verify(img1_path=nama_file1, img2_path=nama_file2)
                
                os.remove(nama_file1)
                os.remove(nama_file2)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # 5. KESIMPULAN & DETAIL ANALISIS
                if hasil["verified"] == True:
                    st.success("### ✅ IDENTITAS COCOK!")
                    st.write("Sistem AI mengonfirmasi bahwa kedua foto ini kemungkinan besar adalah **orang yang sama**.")
                else:
                    st.error("### ❌ IDENTITAS BERBEDA!")
                    st.write("Sistem AI mendeteksi perbedaan struktur tulang wajah. Ini adalah **dua orang yang berbeda**.")
                    
                # Menambahkan menu dropdown bergaya profesional untuk melihat "Dapur AI"
                with st.expander("📊 Lihat Detail Analisis AI (Log Sistem)"):
                    st.json({
                        "Model Analisis": hasil["model"],
                        "Metrik Kalkulasi": hasil["distance_metric"],
                        "Skor Perbedaan (Distance)": round(hasil["distance"], 4),
                        "Batas Maksimal Toleransi": hasil["threshold"],
                        "Kecepatan Proses": f"{round(hasil['time'], 2)} detik"
                    })
                    st.caption("*Catatan Teknis: Jika nilai 'Skor Perbedaan' lebih kecil dari 'Batas Maksimal Toleransi', maka AI menganggap kedua wajah adalah identik.*")
                    
            except Exception as e:
                st.error(f"⚠️ **Sistem mendeteksi anomali:** {e}")
                st.info("💡 Pastikan kedua foto menampilkan wajah menghadap ke depan dengan jelas (tidak terpotong, terlalu blur, atau tertutup masker penuh).")

# --- FOOTER BAWAH ---
st.markdown("---")
st.markdown("<br><p style='text-align: center; color: #888888; font-size: 15px;'>Developed by <b style='color: #FF416C;'>RK STUDIO (MASAK AER)</b></p>", unsafe_allow_html=True)
