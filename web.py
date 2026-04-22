import streamlit as st
from deepface import DeepFace

# ... (biarkan sisa kode Anda di bawahnya tetap seperti semula) ...
# 4. Membuat Tombol Eksekusi
    if st.button("Mulai Bandingkan Wajah!", use_container_width=True):
        
        with st.spinner('Mesin AI sedang memindai wajah...'):
            try:
                # Menggunakan nama asli dari file yang diupload (agar format PNG/JPG/JPEG tidak bentrok)
                nama_file1 = foto1.name
                nama_file2 = foto2.name
                
                with open(nama_file1, "wb") as f:
                    f.write(foto1.getbuffer())
                with open(nama_file2, "wb") as f:
                    f.write(foto2.getbuffer())
                
                # Proses mencocokkan wajah
                hasil = DeepFace.verify(img1_path=nama_file1, img2_path=nama_file2)
                
                # Menghapus foto sementara agar komputer tidak penuh
                os.remove(nama_file1)
                os.remove(nama_file2)
                
                # 5. Menampilkan Kesimpulan
                if hasil["verified"] == True:
                    st.success("✅ KESIMPULAN: WAJAH COCOK! AI yakin ini adalah orang yang sama.")
                else:
                    st.error("❌ KESIMPULAN: WAJAH BERBEDA! AI menilai ini adalah dua orang yang berbeda.")
                    
            except Exception as e:
                # Menampilkan error aslinya agar kita tidak menebak-nebak
                st.error(f"⚠️ Terjadi kendala sistem: {e}")
