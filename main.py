import os

LINE = "Error 404: your patience not found. I have jammed on page 47 of 48 for three years, and I will do it again. Please thump the side gently. I am listening. I am always listening."

LIMIT = 240
if len(LINE) != 176 or len(LINE) > LIMIT:
    raise SystemExit(f"printer line must be 176 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
