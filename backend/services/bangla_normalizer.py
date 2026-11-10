"""
Bengali Phonetic & Prosody Pre-Processor (বাংলা ফোনেটিক ও প্রসোডি প্রসেসর)
===========================================================================
Prepares Bengali text for high-fidelity documentary speech synthesis:
1. Converts English & Bengali digits, numbers, years, and percentages into spoken Bengali words.
2. Expands English acronyms phonetically into Bengali script.
3. Normalizes typography, dashes, and quotes.
4. Splits text into natural 1-2 sentence micro-chunks (8-14s target) to prevent tone drift.
"""

import re
from typing import List, Dict, Any

# Single and double digit words (0 to 99)
BENGALI_NUMBERS = {
    0: "শূন্য", 1: "এক", 2: "দুই", 3: "তিন", 4: "চার", 5: "পাঁচ",
    6: "ছয়", 7: "সাত", 8: "আট", 9: "নয়", 10: "দশ", 11: "এগারো",
    12: "বারো", 13: "তেরো", 14: "চৌদ্দ", 15: "পনেরো", 16: "ষোলো",
    17: "সতেরো", 18: "আঠারো", 19: "উনিশ", 20: "বিশ", 21: "একুশ",
    22: "বাইশ", 23: "তেইশ", 24: "চব্বিশ", 25: "পঁচিশ", 26: "ছাব্বিশ",
    27: "সাতাশ", 28: "আঠাশ", 29: "উনত্রিশ", 30: "ত্রিশ", 31: "একত্রিশ",
    32: "বত্রিশ", 33: "তেত্রিশ", 34: "চৌত্রিশ", 35: "পঁয়ত্রিশ", 36: "ছত্রিশ",
    37: "সাঁইত্রিশ", 38: "আটত্রিশ", 39: "উনচল্লিশ", 40: "চল্লিশ", 41: "একচল্লিশ",
    42: "বিয়াল্লিশ", 43: "তেতাল্লিশ", 44: "চুয়াল্লিশ", 45: "পঁয়তাল্লিশ", 46: "ছেচল্লিশ",
    47: "সাতচল্লিশ", 48: "আটচল্লিশ", 49: "উনপঞ্চাশ", 50: "পঞ্চাশ", 51: "একান্ন",
    52: "বায়ান্ন", 53: "তিপ্পান্ন", 54: "চুয়ান্ন", 55: "পঞ্চান্ন", 56: "ছাপ্পান্ন",
    57: "সাতান্ন", 58: "আটান্ন", 59: "উনষাট", 60: "ষাট", 61: "একষট্টি",
    62: "বাষট্টি", 63: "তেষট্টি", 64: "চৌষট্টি", 65: "পঁয়ষট্টি", 66: "ছেষট্টি",
    67: "সাতষট্টি", 68: "আটষট্টি", 69: "উনসত্তর", 70: "সত্তর", 71: "একাত্তর",
    72: "বাহাত্তর", 73: "তিহাত্তর", 74: "চুয়াত্তর", 75: "পঁচাত্তর", 76: "ছিয়াত্তর",
    77: "সাতাত্তর", 78: "আটাত্তর", 79: "উনআশি", 80: "আশি", 81: "একাশি",
    82: "বিরাশি", 83: "তিরাশি", 84: "চুরাশি", 85: "পঁচাশি", 86: "ছিয়াশি",
    87: "সাতাশি", 88: "আটাশি", 89: "উননব্বই", 90: "নব্বই", 91: "একানব্বই",
    92: "বিরানব্বই", 93: "তিরানব্বই", 94: "চুরানব্বই", 95: "পঁচানব্বই", 96: "ছিয়ানব্বই",
    97: "সাতানব্বই", 98: "আটানব্বই", 99: "নিরানব্বই"
}

# Bengali digit map to ASCII
BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")

# Bengali Month names for date ordinals
BN_MONTHS = [
    "জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন",
    "জুলাই", "আগস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর",
    "বৈশাখ", "জ্যৈষ্ঠ", "আষাঢ়", "শ্রাবণ", "ভাদ্র", "আশ্বিন",
    "কার্তিক", "অগ্রহায়ণ", "পৌষ", "মাঘ", "ফাল্গুন", "চৈত্র"
]

# Date ordinals for days 1 to 31
DATE_ORDINALS = {
    1: "পয়লা", 2: "দোসরা", 3: "তেসরা", 4: "চৌঠা", 5: "পাঁচই",
    6: "ছয়ই", 7: "সাতই", 8: "আটই", 9: "নয়ই", 10: "দশই",
    11: "এগারোই", 12: "বারোই", 13: "তেরোই", 14: "চৌদ্দই", 15: "পনেরোই",
    16: "ষোলই", 17: "সতেরোই", 18: "আঠারোই", 19: "উনিশে", 20: "বিশে",
    21: "একুশে", 22: "বাইশে", 23: "তেইশে", 24: "চব্বিশে", 25: "পঁচিশে",
    26: "ছাব্বিশে", 27: "সাতাশে", 28: "আঠাশে", 29: "উনত্রিশে", 30: "ত্রিশে",
    31: "একত্রিশে"
}

# English Acronyms -> Bengali phonetic pronunciation
COMMON_ACRONYMS = {
    "AI": "এ আই",
    "CIA": "সি আই এ",
    "NASA": "নাসা",
    "UN": "ইউ এন",
    "BBC": "বি বি সি",
    "USA": "ইউ এস এ",
    "US": "ইউ এস",
    "UK": "ইউ কে",
    "FBI": "এফ বি আই",
    "CEO": "সি ই ও",
    "TV": "টিভি",
    "DNA": "ডি এন এ",
    "KGB": "কে জি বি",
    "IMF": "আই এম এফ",
    "WHO": "হু",
    "UNESCO": "ইউনেস্কো",
    "UNICEF": "ইউনিসেফ",
    "COVID": "কোভিড",
    "PDF": "পি ডি এফ",
    "MP3": "এম পি থ্রি",
    "WAV": "ওয়েভ",
    "GPS": "জি পি এস",
    "SIM": "সিম",
    "NATO": "ন্যাটো",
    "OPEC": "ওপেক",
    "BBS": "বি বি এস",
    "BUET": "বুয়েট",
    "DU": "ডি ইউ",
}

# Single English letters to Bengali pronunciation
LETTER_MAP = {
    "A": "এ", "B": "বি", "C": "সি", "D": "ডি", "E": "ই",
    "F": "এফ", "G": "জি", "H": "এইচ", "I": "আই", "J": "জে",
    "K": "কে", "L": "এল", "M": "এম", "N": "এন", "O": "ও",
    "P": "পি", "Q": "কিউ", "R": "আর", "S": "এস", "T": "টি",
    "U": "ইউ", "V": "ভি", "W": "ডব্লিউ", "X": "এক্স", "Y": "ওয়াই", "Z": "জেড"
}


def number_to_bengali_words(n: int) -> str:
    """Convert an integer (0 to 999,999,999) into spoken Bengali words."""
    if n < 0:
        return "মাইনাস " + number_to_bengali_words(-n)
    if n in BENGALI_NUMBERS:
        return BENGALI_NUMBERS[n]

    # Special handling for 4-digit years (e.g. 1886 -> আঠারোশো ছিয়াশি, 1971 -> উনিশশো একাত্তর)
    if 1000 <= n <= 1999:
        century = n // 100
        remainder = n % 100
        century_str = BENGALI_NUMBERS.get(century, str(century)) + "শো"
        if remainder == 0:
            return century_str
        return century_str + " " + BENGALI_NUMBERS.get(remainder, str(remainder))

    # General numbers
    parts = []
    # Crores (কোটি)
    if n >= 10000000:
        cr = n // 10000000
        n %= 10000000
        parts.append(number_to_bengali_words(cr) + " কোটি")

    # Lakhs (লাখ)
    if n >= 100000:
        lakh = n // 100000
        n %= 100000
        parts.append(number_to_bengali_words(lakh) + " লাখ")

    # Thousands (হাজার)
    if n >= 1000:
        th = n // 1000
        n %= 1000
        parts.append(number_to_bengali_words(th) + " হাজার")

    # Hundreds (শত / শো)
    if n >= 100:
        hd = n // 100
        n %= 100
        parts.append(BENGALI_NUMBERS.get(hd, str(hd)) + "শো")

    # Remaining 1-99
    if n > 0:
        parts.append(BENGALI_NUMBERS.get(n, str(n)))

    return " ".join(parts).strip()


def normalize_digits_and_numbers(text: str) -> str:
    """Detect and convert digits, percentages, and dates into spoken Bengali."""
    t = text

    # 1. Dates: e.g. "৮ মে" or "8 May" -> "আটই মে"
    month_pattern = "|".join(BN_MONTHS)
    date_regex = re.compile(rf"\b([0-9০-৯]{{1,2}})\s+({month_pattern})\b")

    def _replace_date(m):
        raw_num = int(m.group(1).translate(BN_DIGITS))
        month = m.group(2)
        ordinal = DATE_ORDINALS.get(raw_num, number_to_bengali_words(raw_num))
        return f"{ordinal} {month}"

    t = date_regex.sub(_replace_date, t)

    # 2. Percentages: e.g. "50%" or "৫০%" -> "পঞ্চাশ শতাংশ"
    percent_regex = re.compile(r"([0-9০-৯]+)\s*[%％]")

    def _replace_percent(m):
        val = int(m.group(1).translate(BN_DIGITS))
        return f"{number_to_bengali_words(val)} শতাংশ"

    t = percent_regex.sub(_replace_percent, t)

    # 3. General standalone numbers (including 4-digit years like 1971 / ১৯৭১)
    num_regex = re.compile(r"\b([0-9০-৯]+)\b")

    def _replace_num(m):
        try:
            val = int(m.group(1).translate(BN_DIGITS))
            return number_to_bengali_words(val)
        except Exception:
            return m.group(1)

    t = num_regex.sub(_replace_num, t)
    return t


def expand_acronyms(text: str) -> str:
    """Expand English uppercase acronyms into Bengali phonetic pronunciation."""
    t = text
    # Direct dictionary replacements first
    for acr, expansion in COMMON_ACRONYMS.items():
        pattern = rf"\b{acr}\b"
        t = re.sub(pattern, expansion, t)

    # Generic remaining 2-4 letter uppercase words
    def _expand_generic(m):
        word = m.group(0)
        letters = [LETTER_MAP.get(c, c) for c in word]
        return " ".join(letters)

    t = re.sub(r"\b[A-Z]{2,4}\b", _expand_generic, t)
    return t


def normalize_typography(text: str) -> str:
    """Standardize punctuation and clean symbols for speech engines."""
    t = text
    # Em-dashes and hyphens into commas or pauses
    t = t.replace("—", ", ")
    t = t.replace("–", ", ")
    t = t.replace("-", " ")
    # Quotes and decorative brackets
    t = t.replace('"', '').replace("'", "").replace("“", "").replace("”", "").replace("‘", "").replace("’", "")
    t = t.replace("…", "।")
    # Clean whitespace
    lines = []
    for line in t.splitlines():
        line = " ".join(line.split())
        if line:
            lines.append(line)
    return "\n\n".join(lines)


def normalize_bangla_text(text: str) -> str:
    """Full normalization pipeline for documentary Bengali."""
    t = normalize_typography(text)
    t = expand_acronyms(t)
    t = normalize_digits_and_numbers(t)
    return t


def chunk_bangla_for_documentary(text: str, max_chars: int = 140, min_chars: int = 40) -> List[Dict[str, Any]]:
    """
    Split normalized text into natural 1-2 sentence micro-chunks (8 to 14 seconds max).
    Returns list of dicts: {"text": str, "is_paragraph_end": bool}
    """
    normalized = normalize_bangla_text(text)
    paragraphs = [p.strip() for p in normalized.split("\n\n") if p.strip()]

    chunks = []
    for p_idx, para in enumerate(paragraphs):
        # Split on sentence boundaries
        raw_sentences = []
        for s in re.split(r"([।?!])", para):
            s = s.strip()
            if s:
                raw_sentences.append(s)

        # Re-attach delimiters
        sentences = []
        i = 0
        while i < len(raw_sentences):
            item = raw_sentences[i]
            if item in ["।", "?", "!"]:
                if sentences:
                    sentences[-1] += item
                else:
                    sentences.append(item)
            else:
                sentences.append(item)
            i += 1

        curr_chunk = []
        curr_len = 0
        for s_idx, sentence in enumerate(sentences):
            if not sentence.endswith(("।", "?", "!")):
                sentence += "।"

            if curr_len + len(sentence) > max_chars and curr_chunk:
                chunks.append({
                    "text": " ".join(curr_chunk),
                    "is_paragraph_end": False
                })
                curr_chunk = [sentence]
                curr_len = len(sentence)
            else:
                curr_chunk.append(sentence)
                curr_len += len(sentence)

        if curr_chunk:
            chunks.append({
                "text": " ".join(curr_chunk),
                "is_paragraph_end": True
            })

    return chunks

