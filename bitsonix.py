import numpy as np
import sounddevice as sd
import soundfile as sf   # For saving .wav
from scipy.fft import fft
import os
import pyfiglet  # ASCII heading
from termcolor import colored
from datetime import datetime
import glob
import sys

# Parameters
fs = 44100        # Sampling rate
duration = 0.1    # Seconds per bit
f0, f1 = 1000, 2000  # Frequencies for 0 and 1

# --- ENCODER ---
def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def bits_to_tone(bits):
    signal = np.array([])
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    for bit in bits:
        freq = f1 if bit == '1' else f0
        tone = np.sin(2*np.pi*freq*t)
        signal = np.concatenate((signal, tone))
    return signal

# --- DECODER ---
def tone_to_bits(signal):
    samples_per_bit = int(fs * duration)
    num_bits = len(signal) // samples_per_bit
    bits = ""
    for i in range(num_bits):
        chunk = signal[i*samples_per_bit:(i+1)*samples_per_bit]
        spectrum = np.abs(fft(chunk))
        freqs = np.fft.fftfreq(len(chunk), 1/fs)
        dominant_freq = freqs[np.argmax(spectrum[:len(spectrum)//2])]
        if abs(dominant_freq - f1) < abs(dominant_freq - f0):
            bits += '1'
        else:
            bits += '0'
    return bits

def bits_to_text(bits):
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

# --- MAIN ---
# Fancy heading
font = "slant"
banner = pyfiglet.figlet_format("BitSonix", font=font)  
print(colored(banner, "red"))  

print("====================================================")
print("====================================================")
print("||Created By- GODxCharLiE                         ||")
print("||#That is a tool for hide or secure your massage ||")
print("||   --(It is Text to BFSK-sound converter)--     ||")
print("||It stores output in  /Documents/Sound-Doc       ||")
print("====================================================")
print("====================================================")
print("                                                    ")

# --- Check folder existence ---
docs_path = os.path.join(os.path.expanduser("~"), "Documents", "Sound-Doc")
if not os.path.exists(docs_path):
    print(colored("[WARNING] Required folder '/Documents/Sound-Doc' not found!", "yellow"))
    choice = input("Do you want to create it? (y/n): ").strip().lower()
    if choice == "y":
        os.makedirs(docs_path)
        print(colored("[INFO] Folder created successfully!", "green"))
    else:
        print(colored("[EXIT] Folder not created. Program stopped.", "red"))
        sys.exit(1)

msg = input("Enter Your Msg : ")
bits = text_to_bits(msg)
signal = bits_to_tone(bits)

# Play the sound
sd.play(signal, fs)
sd.wait()

# Find latest sequence number
existing_files = glob.glob(os.path.join(docs_path, "hidden_message_*.wav"))
if existing_files:
    nums = []
    for f in existing_files:
        try:
            num = int(os.path.basename(f).split("_")[2])  # hidden_message_<num>_timestamp.wav
            nums.append(num)
        except:
            pass
    seq = max(nums) + 1 if nums else 1
else:
    seq = 1

# Timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# File name with sequence and timestamp
file_name = f"hidden_message_{seq}_{timestamp}.wav"
file_path = os.path.join(docs_path, file_name)

# Save audio
sf.write(file_path, signal, fs)

# Decode back
decoded_bits = tone_to_bits(signal)
decoded_msg = bits_to_text(decoded_bits)
