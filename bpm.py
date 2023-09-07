import librosa
from mutagen.flac import FLAC

# Load audio file
audio_file = "/Volumes/navidrome/Daft Punk/Homework (25th Anniversary Edition)/07 Around the World.flac"
try:
    audio, sr = librosa.load(audio_file)
except Exception as e:
    print(f"Error loading audio file: {e}")
    exit(1)

# Extract BPM
try:
    bpm, _ = librosa.beat.beat_track(y=audio, sr=sr)
except Exception as e:
    print(f"Error extracting BPM: {e}")
    exit(1)

print(f"BPM: {bpm}")

# Add BPM to FLAC metadata using mutagen
try:
    flac = FLAC(audio_file)
    flac['BPM'] = str(bpm)
    flac.save()
    print("BPM added to metadata.")
except Exception as e:
    print(f"Error adding BPM to metadata: {e}")
    exit(1)
