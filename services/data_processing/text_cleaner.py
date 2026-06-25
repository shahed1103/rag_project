import re
import unicodedata

# =========================
# Precompiled patterns
# =========================

ARABIC_DIACRITICS = re.compile(r'[ًٌٍَُِّْـ]')
TATWEEL = re.compile(r'ـ+')

CONTROL_CHARS = re.compile(r'[\x00-\x1F\x7F-\x9F]')

OCR_NOISE_CHARS = re.compile(r'[•■□▪◆◇★☆●◦●♦♥♣♠]')
LATIN_NOISE = re.compile(r'[^\u0600-\u06FF0-9a-zA-Z\s]')

MULTISPACE = re.compile(r'\s+')
MULTINEWLINE = re.compile(r'\n+')

SINGLE_CHAR_ARABIC = re.compile(r'\b[\u0600-\u06FF]\b')

PAGE_NUMBERS = re.compile(r'(?<!\d)\b\d{1,4}\b(?!\d)')

WEIRD_SYMBOLS_RATIO = re.compile(r'[ª«»½¾¢£¤¥¦§¨©®°±²³]')


# =========================
# Main function
# =========================

def clean_text(text: str) -> str:
    if not text:
        return ""

    # -------------------------
    # 1. Unicode normalization
    # -------------------------
    text = unicodedata.normalize("NFKC", text)

    # -------------------------
    # 2. Fix encoding issues
    # -------------------------
    text = text.replace("\r", "\n")
    text = text.replace("\u200f", "").replace("\u200e", "")

    # -------------------------
    # 3. Remove control chars
    # -------------------------
    text = CONTROL_CHARS.sub(" ", text)

    # -------------------------
    # 4. Remove diacritics + tatweel
    # -------------------------
    text = ARABIC_DIACRITICS.sub("", text)
    text = TATWEEL.sub("", text)

    # -------------------------
    # 5. Normalize Arabic letters
    # -------------------------
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ى', 'ي', text)
    text = re.sub(r'ؤ', 'و', text)
    text = re.sub(r'ئ', 'ي', text)

    # -------------------------
    # 6. Remove OCR noise symbols
    # -------------------------
    text = OCR_NOISE_CHARS.sub(" ", text)
    text = WEIRD_SYMBOLS_RATIO.sub(" ", text)

    # -------------------------
    # 7. Remove page numbers (smart filtering)
    # -------------------------
    text = PAGE_NUMBERS.sub(" ", text)

    # -------------------------
    # 8. Remove non-Arabic/English/Numbers
    # -------------------------
    text = LATIN_NOISE.sub(" ", text)

    # Remove Arabic punctuation
    text = re.sub(r"[؟،؛:!\"'()\[\]{}<>«»]", " ", text)

    # -------------------------
    # 9. Clean single letters (careful)
    # -------------------------
    # text = SINGLE_CHAR_ARABIC.sub(" ", text)

    # -------------------------
    # 10. Normalize spaces
    # -------------------------
    text = MULTISPACE.sub(" ", text)
    text = MULTINEWLINE.sub("\n", text)

    # -------------------------
    # 11. Line processing (IMPORTANT FOR RAG)
    # -------------------------
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if len(line) < 3:
            continue

        letters = sum(ch.isalpha() for ch in line)
        digits = sum(ch.isdigit() for ch in line)

        # remove garbage lines
        if letters == 0 and digits > 3:
            continue

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()