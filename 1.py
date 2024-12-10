import streamlit as st
import pandas as pd
import random

# Tabel hubungan antara penyakit dan gejala
rules = [
    {"hypothesis": "Diabetes (P1)", "evidence": ["G27", "G28", "G39", "G40"]},
    {"hypothesis": "Ginjal Kronis (P2)", "evidence": ["G5", "G13", "G25", "G36"]},
    {"hypothesis": "Sindrom Nefrotik (P3)", "evidence": ["G33", "G34", "G35"]},
    {"hypothesis": "Infeksi Saluran Kemih (P4)", "evidence": ["G3", "G4", "G10"]},
    {"hypothesis": "Obstruksi Saluran Kemih (P5)", "evidence": ["G9", "G14", "G17"]},
    {"hypothesis": "Pielonefritis / Infeksi Ginjal (P6)", "evidence": ["G5", "G8", "G18"]},
    {"hypothesis": "Sistitis (P7)", "evidence": ["G3", "G7", "G12"]},
    {"hypothesis": "Nefropati Diabetik (P8)", "evidence": ["G5", "G33", "G41"]},
]

# Tabel deskripsi gejala
symptom_descriptions = {
    "G1": "Buang air kecil lebih dari 5 sampai 8 kali sehari",
    "G2": "Perasaan urine tidak sepenuhnya keluar setelah buang air kecil",
    "G3": "Urine yang keluar tidak seperti biasa",
    "G4": "Sensasi terbakar atau perih saat buang air kecil",
    "G5": "Urin berwarna merah",
    "G6": "Rasa selalu ingin buang air kecil dan tidak bisa ditahan",
    "G7": "Frekuensi buang air kecil sering tapi jumlah urine yang sedikit",
    "G8": "Disfungsi seksual",
    "G9": "Nyeri saat buang air kecil",
    "G10": "Rasa sakit atau sensasi terbakar pada perut bagian bawah",
    "G11": "Kandung kemih membesar terkadang terasa di bagian bawah perut tepat di atas tulang kemaluan",
    "G12": "Perut bagian samping (pinggul) mengalami rasa sakit",
    "G13": "Seperti ada tekanan pada panggul",
    "G14": "Nyeri pada perut",
    "G15": "Nyeri punggung",
    "G16": "Kram otot",
    "G17": "Sesak nafas",
    "G18": "Cegukan berlebih",
    "G19": "Pernapasan lebih dari 12 sampai 20 kali permenit",
    "G20": "Nyeri pada dada",
    "G21": "Susah tidur",
    "G22": "Mendengkur saat tidur",
    "G23": "Kehilangan kesadaran",
    "G24": "Sakit kepala",
    "G25": "Lemas",
    "G26": "Tubuh mudah merasa lelah",
    "G27": "Sering merasa haus",
    "G28": "Selalu merasa lapar",
    "G29": "Kehilangan nafsu makan",
    "G30": "Berat badan menurun atau bertambah lebih dari 1,5 sampai 2,5 kg perminggu",
    "G31": "Mual",
    "G32": "Muntah",
    "G33": "Pembengkakan pada pergelangan kaki, kaki atau tangan",
    "G34": "Pembengkakan sekitar mata",
    "G35": "Suhu badan diatas 38 derajat celcius",
    "G36": "Tubuh kadang dingin atau menggigil",
    "G37": "Tekanan darah diatas 140/90 mm Hg",
    "G38": "Penglihatan kabur",
    "G39": "Kurang konsentrasi",
    "G40": "Kulit terasa gatal",
    "G41": "Luka tidak lebih dari 7 sampai 21 hari",
    "G42": "Berat badan menurun atau bertambah secara drastis",
    "G43": "Luka sulit sembuh",
    "G44": "Nafas Lebih Cepat",
    "G45": "Urin terdapat darah",
    "G46": "Tekanan Darah Tinggi",
    "G47": "Menurunan ketajaman mental",
    "G48": "Demam tinggi",
    "G49": "Sering buang air kecil"
}

# Fungsi diagnosa berdasarkan aturan
def diagnose_by_rules(input_symptoms):
    matched_rules = []
    for rule in rules:
        matched_symptoms = [symptom for symptom in rule["evidence"] if symptom in input_symptoms]
        match_percentage = len(matched_symptoms) / len(rule["evidence"]) * 100
        if match_percentage >= 50:
            matched_rules.append({"hypothesis": rule["hypothesis"], "match_percentage": match_percentage})
    matched_rules.sort(key=lambda x: x["match_percentage"], reverse=True)
    return matched_rules

# Streamlit UI
st.set_page_config(page_title="Sistem Pakar Deteksi Penyakit Ginjal", layout="wide", initial_sidebar_state="expanded")

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Sistem Pakar Deteksi Penyakit Ginjal</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #4CAF50;'>Masukkan gejala yang Anda alami untuk mendapatkan diagnosis awal</h4>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Form gejala
with st.form("diagnosis_form"):
    st.markdown("<h5 style='color: #4CAF50;'>Pilih gejala yang Anda alami:</h5>", unsafe_allow_html=True)
    selected_symptoms = st.multiselect(
        "",
        options=symptom_descriptions.keys(),
        format_func=lambda x: f"{x}: {symptom_descriptions[x]}"
    )
    submit_button = st.form_submit_button("Diagnosa")

# Proses diagnosa
if submit_button:
    if selected_symptoms:
        results = diagnose_by_rules(selected_symptoms)
        if results:
            st.markdown("<h3 style='color: #4CAF50;'>Diagnosis Awal:</h3>", unsafe_allow_html=True)
            for result in results:
                st.markdown(f"<p style='color: #333;'>- <strong>{result['hypothesis']}</strong> (Kecocokan: {result['match_percentage']:.2f}%)</p>", unsafe_allow_html=True)
        else:
            st.warning("Tidak ada penyakit yang cocok dengan gejala yang dimasukkan.")
    else:
        st.error("Harap pilih minimal satu gejala untuk diagnosa.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>© 2024 Sistem Pakar Deteksi Penyakit Ginjal</p>", unsafe_allow_html=True)
