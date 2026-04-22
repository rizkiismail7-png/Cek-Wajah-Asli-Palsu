import streamlit as st
from deepface import DeepFace
import os

# 1. Mengatur Tampilan Halaman Atas
st.set_page_config(page_title="Deteksi Wajah AI", page_icon="🕵️‍♂️", layout="centered")

# --- TAMBAHAN HIASAN: MENU SAMPING (SIDEBAR) ---
with st.sidebar:
    st.title("Tentang Creator 🚀")
    st.write("Aplikasi AI ini dikembangkan oleh **RK STUDIO (MASAK AER)**.")
    st.write("Alat ini dirancang khusus untuk memverifikasi keaslian foto wajah secara akurat menggunakan teknologi *Retina Face* *Deep Learning*.")
    st.markdown("---")
    st.caption("© 2026 Hak Cipta Dilindungi")

# --- JUDUL UTAMA ---
st.title("Aplikasi Pencocok Wajah AI 🕵️‍♂️")
st.write("Unggah dua foto untuk mengecek apakah mereka adalah orang yang sama.")
st.markdown("---") # Tambahan garis pembatas estetik

# 2. Membuat Dua Kolom untuk Upload Foto
kolom1, kolom2 = st.columns(2)

with kolom1:
    foto1 = st.file_uploader("Unggah Foto Orang Pertama", type=['jpg', 'jpeg', 'png'])
with kolom2:
    foto2 = st.file_uploader("Unggah Foto Orang Kedua", type=['jpg', 'jpeg', 'png'])

# 3. Jika kedua foto sudah diunggah
if foto1 and foto2:
    with kolom1:
        st.image(foto1, caption="Foto 1", use_container_width=True)
    with kolom2:
        st.image(foto2, caption="Foto 2", use_container_width=True)
    
    st.divider()
    
    # 4. Membuat Tombol Eksekusi
    if st.button("Mulai Bandingkan Wajah!", use_container_width=True):
        
        with st.spinner('Mesin AI sedang memindai wajah...'):
            try:
                nama_file1 = foto1.name
                nama_file2 = foto2.name
                
                with open(nama_file1, "wb") as f:
                    f.write(foto1.getbuffer())
                with open(nama_file2, "wb") as f:
                    f.write(foto2.getbuffer())
                
                hasil = DeepFace.verify(img1_path=nama_file1, img2_path=nama_file2)
                
                os.remove(nama_file1)
                os.remove(nama_file2)
                
                if hasil["verified"] == True:
                    st.success("✅ KESIMPULAN: WAJAH COCOK! AI yakin ini adalah orang yang sama.")
                else:
                    st.error("❌ KESIMPULAN: WAJAH BERBEDA! AI menilai ini adalah dua orang yang berbeda.")
                    
            except Exception as e:
                st.error(f"⚠️ Terjadi kendala sistem: {e}")

# --- TAMBAHAN HIASAN: FOOTER BAWAH ---
st.markdown("<br><br><p style='text-align: center; color: gray;'>Dibuat dengan 💻 oleh <b>RK STUDIO (MASAK AER)</b></p>", unsafe_allow_html=True)
