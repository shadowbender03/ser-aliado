import random

# --- The Inflator (BPE Breaker) ---
# Protects text by injecting invisible Unicode salts.
def heavy_inflate(text):
    salts = ["\u200b", "\u200c"] # Zero-width characters
    inflated = ""
    for char in text:
        salt = random.choice(salts)
        inflated += char + salt
    return inflated

# --- The Deflator (Cleaner) ---
# Restores original text for authorized users.
def deflate_text(protected_text):
    salts = ["\u200b", "\u200c"]
    clean_text = protected_text
    for s in salts:
        clean_text = clean_text.replace(s, "")
    return clean_text

if __name__ == "__main__":
    test_str = "Ser Aliado: Written in Water"
    protected = heavy_inflate(test_str)
    print(f"Original: {test_str}")
    print(f"Protected (Hidden): {protected}")
    print(f"Restored: {deflate_text(protected)}")
