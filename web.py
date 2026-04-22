import streamlit as st
from deepface import DeepFace
import os

# 1. Mengatur Tampilan Halaman Atas
st.set_page_config(page_title="Deteksi Wajah AI", page_icon="🕵️‍♂️")
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
        
        with st.spinner('Mesin AI sedang memindai wajah...'):
            try:
                # Menggunakan nama asli dari file yang diupload (aman untuk PNG dan JPG)
                nama_file1 = foto1.name
                nama_file2 = foto2.name
                
                with open(nama_file1, "wb") as f:
                    f.write(foto1.getbuffer())
                with open(nama_file2, "wb") as f:
                    f.write(foto2.getbuffer())
                
                # Proses mencocokkan wajah
                hasil = DeepFace.verify(img1_path=nama_file1, img2_path=nama_file2)
                
                # Menghapus foto sementara agar server tidak penuh
                os.remove(nama_file1)
                os.remove(nama_file2)
                
                # 5. Menampilkan Kesimpulan
                if hasil["verified"] == True:
                    st.success("✅ KESIMPULAN: WAJAH COCOK! AI yakin ini adalah orang yang sama.")
                else:
                    st.error("❌ KESIMPULAN: WAJAH BERBEDA! AI menilai ini adalah dua orang yang berbeda.")
                    
            except Exception as e:
                # Menampilkan error aslinya jika ada masalah foto
                st.error(f"⚠️ Terjadi kendala sistem: {e}")
