import streamlit as st

st.write("""
# Penghitung Luas Segitiga Yan
ini adalah aplikasi menghitung luas segitiga yan24
""")

alas = st.number_input("Masukkan Alas", 0)
tinggi = st.number_input("Masukkan Tinggi", 0)
hitung = st.button("Itung Luas")

if hitung:
   Luas = 0.5 * alas * tinggi
   st.success(f"Luas Segitiga Ne adalah {Luas}")
  

# Celebrate when all done

st.balloons()
