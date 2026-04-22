import os
import sys
# Memaksa server membuang OpenCV yang rusak dan menggantinya dengan versi Headless
os.system(f"{sys.executable} -m pip uninstall -y opencv-python")
os.system(f"{sys.executable} -m pip install opencv-python-headless")

import streamlit as st
from deepface import DeepFace

# ... (biarkan sisa kode Anda di bawahnya tetap seperti semula) ...
st.title("Aplikasi Pencocok Wajah AI 🕵️‍♂️")
st.write("Silakan unggah dua foto untuk mengecek apakah mereka adalah orang yang sama.")

# 2. Membuat Dua Kolom untuk Upload Foto Kiri dan Kanan
kolom1, kolom2 = st.columns(2)

with kolom1:
    foto1 = st.file_uploader("Unggah Foto Orang Pertama", type=['jpg', 'jpeg', 'png'])
with kolom2:
    foto2 = st.file_uploader("Unggah Foto Orang Kedua", type=['jpg', 'jpeg', 'png'])

# 3. Jika kedua foto sudah diunggah oleh pengguna
if foto1 and foto2:
    # Tampilkan preview foto di website
    with kolom1:
        st.image(foto1, caption="Foto 1", use_container_width=True)
    with kolom2:
        st.image(foto2, caption="Foto 2", use_container_width=True)
    
    st.divider() # Membuat garis pembatas
    
    # 4. Membuat Tombol Eksekusi
    if st.button("Mulai Bandingkan Wajah!", use_container_width=True):
        
        # Animasi loading saat AI berpikir
        with st.spinner('Mesin AI sedang memindai wajah...'):
            try:
                # Karena DeepFace butuh membaca file fisik, kita simpan sementara foto yang diupload
                with open("temp1.jpg", "wb") as f:
                    f.write(foto1.getbuffer())
                with open("temp2.jpg", "wb") as f:
                    f.write(foto2.getbuffer())
                
                # Proses mencocokkan wajah
                hasil = DeepFace.verify(img1_path="temp1.jpg", img2_path="temp2.jpg")
                
                # Menghapus foto sementara agar komputer tidak penuh
                os.remove("temp1.jpg")
                os.remove("temp2.jpg")
                
                # 5. Menampilkan Kesimpulan di Layar Website
                if hasil["verified"] == True:
                    st.success("✅ KESIMPULAN: WAJAH COCOK! AI sangat yakin ini adalah orang yang sama.")
                else:
                    st.error("❌ KESIMPULAN: WAJAH BERBEDA! AI menilai ini adalah dua orang yang berbeda.")
                    
            except Exception as e:
                # Jika foto blur, membelakangi kamera, atau tidak ada wajah
                st.warning("⚠️ Maaf, AI tidak bisa menemukan wajah yang jelas pada salah satu foto. Coba gunakan foto lain yang menghadap ke depan.")
