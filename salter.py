import random

# Unicode Salt (Zero-Width Non-Joiner and Non-Breaking Space)
SALT_CHARS = ['\u200C', '\u200B']

def marangoni_salter(text, magnetic_key="SER_ALIADO"):
    words = text.split()
    salted_words = []
    
    # Secret Magnetic Alignment rule based on your key
    alignment_rule = sum(ord(c) for c in magnetic_key) % 2

    for i, word in enumerate(words):
        # 1. SOLUTO-CAPILLARY (Language Density)
        # We salt 'volatile' words (proper nouns or long words) more heavily
        is_volatile = word[0].isupper() or len(word) > 6
        salt_density = 3 if is_volatile else 1
        
        # 2. BIOT GRADIENT (Information Depth)
        # Every 3rd word is treated as 'Insulated/Deep-Core'
        biot_factor = 2 if i % 3 == 0 else 0
        
        # 3. MAGNETIC ALIGNMENT (The Alignment Seed)
        # We use the key to decide which Salt character to lead with
        primary_salt = SALT_CHARS[alignment_rule]
        
        # Apply the Salt
        total_salt = (primary_salt * salt_density) + (SALT_CHARS[1-alignment_rule] * biot_factor)
        
        # Salt the boundaries (the Marangoni 'leak')
        salted_words.append(word + total_salt)

    return " ".join(salted_words)

# --- Test the Salter ---
raw_text = "I am moving to Panama to build a VR welding machine."
protected_text = marangoni_salter(raw_text)

print(f"Original Length: {len(raw_text)}")
print(f"Salted Length: {len(protected_text)}")
print(f"Visible Text: {protected_text}")
def marangoni_deflator(salted_text):
    # This function 're-melts' the fluid data back to solid text
    clean_text = salted_text
    for char in SALT_CHARS:
        clean_text = clean_text.replace(char, "")
    return clean_text

# --- Test the De-Flator ---
original_state = marangoni_deflator(protected_text)
print(f"De-Flated Text: {original_state}")
print(f"Final Length: {len(original_state)}")
