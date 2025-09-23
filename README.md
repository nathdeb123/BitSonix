# 🔊 BitSonix

Convert your text into **BFSK-encoded sound waves** and hide your secret messages inside audio.  
Play, save, and decode them back — a simple but powerful tool for **sound-based steganography**.

---

## ✨ Features
- Text → Binary → BFSK sound encoding
- Sound → Binary → Text decoding
- Auto-save `.wav` files in `Documents/Sound-Doc/` with sequence & timestamp
- Real-time playback of generated sound
- Hacker-style CLI banner for aesthetic vibes
- **Smart folder handling**:  
  If `Documents/Sound-Doc` doesn’t exist, the tool asks if you want to create it.  
  - If **yes** → it creates the folder automatically.  
  - If **no** → the program exits safely.

---

## 📦 Requirements
Make sure you have **Python 3.8+** installed.  
Install dependencies using:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
numpy
sounddevice
soundfile
scipy
pyfiglet
termcolor
```

---

## 🚀 Usage

### 1. Run the tool
```bash
python bitsonix.py
```

### 2. Enter your message
```
Enter Your Msg : Hello World
```

### 3. Listen & Save
- The encoded sound plays instantly.
- The `.wav` file is saved in:
  ```
  ~/Documents/Sound-Doc/hidden_message_<seq>_<timestamp>.wav
  ```

### 4. Decoding
The program will auto-decode the generated sound back into your original text, so you can verify it’s working.

---

## 📂 Output Example
```
Documents/
└── Sound-Doc/
    ├── hidden_message_1_20250924_002934.wav
    ├── hidden_message_2_20250924_010512.wav
    └── ...
```

---

## 🔧 How It Works
- **Encoding:**  
  Each character → 8-bit binary → BFSK modulation (`1000 Hz` = 0, `2000 Hz` = 1).
- **Playback:**  
  Concatenates tones and streams via `sounddevice`.
- **Saving:**  
  Auto-increments sequence numbers, attaches timestamps.
- **Decoding:**  
  Uses FFT to detect dominant frequency → rebuilds binary → text.

---

## ⚠️ Disclaimer
This is **not encryption** — it’s encoding. Anyone with this script can decode your sound.  
For actual secure messaging, combine it with encryption before encoding.

---

## 👨‍💻 Author
Created by **GODxCharLiE** 🐉

---

## ✨ Extras (optional)
- Add CLI args with `argparse` for passing message, save path, or disabling playback.
- Package with **PyInstaller** for standalone executables.
- Extend to **Android (Kotlin)** for mobile BFSK messaging apps.
