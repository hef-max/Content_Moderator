# 🛡️ Content Moderator API

Sistem API sederhana untuk moderasi teks secara real-time menggunakan model kecerdasan buatan. Fitur utama:
- Deteksi konten **toxic / tidak toxic**
- Klasifikasi topik teks: politics, sports, entertainment, technology, finance
- Logging otomatis teks yang toxic (opsional)

---

## 🚀 Fitur Utama

- ✅ REST API endpoint `/moderate`
- ✅ Model `unitary/toxic-bert` untuk deteksi toksisitas
- ✅ Model `facebook/bart-large-mnli` untuk klasifikasi topik (zero-shot)
- ✅ Frontend HTML testing sederhana (optional)
- ✅ Logging toxic messages ke file CSV

---

## 📦 Requirements

- Python 3.10+
- pip

### Install dependensi:
```bash
pip install -r requirements.txt
