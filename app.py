import streamlit as st
import json
import os

# File untuk menyimpan data
DATA_FILE = "guestbook.json"

# ------------------ Fungsi Simpan & Load ------------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ Tampilan CSS (Dark & Light Mode) ------------------
def load_css():
    st.markdown("""
    <style>
        body { font-family: 'Arial', sans-serif; }
        .title { text-align: center; font-size: 36px; font-weight: bold; margin-bottom: 20px; }
        .form-container { max-width: 600px; margin: auto; padding: 20px; border-radius: 10px; }
        .dark-mode { background-color: #1e1e1e; color: white; }
        .light-mode { background-color: #f8f9fa; color: black; }
        .btn-submit { background-color: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 5px; }
        .btn-clear { background-color: #e74c3c; color: white; border: none; padding: 10px 20px; border-radius: 5px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #333; color: white; }
    </style>
    """, unsafe_allow_html=True)

# ------------------ Main Program ------------------
def main():
    st.set_page_config(page_title="Buku Tamu Online", layout="centered")
    load_css()

    # Mode (Dark / Light)
    mode = st.toggle("🌙 Dark Mode / ☀ Light Mode", value=True)
    theme_class = "dark-mode" if mode else "light-mode"
    st.markdown(f"<div class='{theme_class}'><div class='form-container'>", unsafe_allow_html=True)

    st.markdown("<h1 class='title'>Buku Tamu Online</h1>", unsafe_allow_html=True)

    data = load_data()

    # ------------------ Form Input ------------------
    with st.form("guest_form", clear_on_submit=True):
        nama = st.text_input("Nama")
        kontak = st.text_input("Kontak")
        instansi = st.text_input("Institusi / Asal")
        tujuan = st.text_input("Tujuan Kunjungan")
        catatan = st.text_area("Catatan (opsional)")

        submit = st.form_submit_button("Kirim")
        if submit:
            if nama and kontak and instansi and tujuan:
                data.append({
                    "nama": nama,
                    "kontak": kontak,
                    "instansi": instansi,
                    "tujuan": tujuan,
                    "catatan": catatan
                })
                save_data(data)
                st.success("✅ Data berhasil disimpan!")
            else:
                st.warning("⚠ Harap isi semua field wajib!")

    # Tombol Hapus Semua
    if st.button("🗑 Hapus Semua Data"):
        data = []
        save_data(data)
        st.success("✅ Semua data berhasil dihapus!")

    # ------------------ Tampilkan Data ------------------
    if data:
        st.subheader("📋 Data Tamu")
        st.table(data)
    else:
        st.info("Belum ada data tamu.")

    st.markdown("</div></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
