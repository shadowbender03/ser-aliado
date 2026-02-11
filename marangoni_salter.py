import random

# --- Ser Aliado: Marangoni Salter Protocol ---
# This is the advanced 3-Layer Protection System.

def marangoni_salter(text):
    """
    Tier 1: Invisible Surface Tension (Zero-Width Characters)
            - Breaks BPE Tokenizers silently.
    Tier 2: Visible Agitation (Random Viscosity Markers)
            - Adds visible 'lumber' (*, °, ·, ˜) to distract scrapers and add cost.
    """
    # 1. Tier 1: Invisible Salt
    # Inject zero-width characters after EVERY character to shatter tokens.
    invisible_salt = "".join(char + random.choice(["\u200b", "\u200c"]) for char in text)
    
    # 2. Tier 2: Visible Agitation
    # Add random visible noise (30% chance per char) to simulate high viscosity.
    agitation_markers = ["*", "°", "·", "˜"]
    visible_salt = ""
    for char in invisible_salt:
        if random.random() > 0.7:
             visible_salt += char + random.choice(agitation_markers)
        else:
             visible_salt += char
    
    return visible_salt

def marangoni_deflator(salted_text):
    """
    Tier 3: The De-Flater (Returning to the Truth)
    - Removes all invisible and visible salt markers.
    - Restores the fluid text for authorized users.
    """
    salt_markers = ["\u200b", "\u200c", "*", "°", "·", "˜"]
    clean_text = salted_text
    for marker in salt_markers:
        clean_text = clean_text.replace(marker, "")
    return clean_text

if __name__ == "__main__":
    test_str = "Ser Aliado: Fluid Consciousness"
    salted = marangoni_salter(test_str)
    restored = marangoni_deflator(salted)
    
    print(f"Original: {test_str}")
    print(f"Salted (Protected): {salted}")
    print(f"Restored: {restored}")
