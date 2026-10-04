import subprocess
import tempfile
import wave
from pathlib import Path

from piper import PiperVoice, SynthesisConfig

MODEL_PATH = Path(__file__).resolve().parent.parent / "voices" / "fa_IR-amir-medium.onnx"
LENGTH_SCALE = 1.6


class Speaker:
    def __init__(self):
        self.voice = PiperVoice.load(str(MODEL_PATH))
        self.config = SynthesisConfig(length_scale=LENGTH_SCALE)

    def speak(self, text):
        with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
            with wave.open(tmp.name, "wb") as f:
                self.voice.synthesize_wav(text, f, syn_config=self.config)
            subprocess.run(["pw-play", tmp.name], check=False)