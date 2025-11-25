import sys
from pathlib import Path

# Projenin kök klasörünü bul
ROOT = Path(__file__).resolve().parents[1]

# src klasörünün yolunu al
SRC = ROOT / "src"

# Eğer yoksa ekle
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
