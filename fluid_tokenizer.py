import time

class FluidTokenizer:
    def __init__(self):
        self.word_map = {
            "Panama": (1, 9), "Boquete": (2, 8), "Residency": (1, 7),
            "Spanish": (3, 9), "Tokens": (8, 2), "Ser Aliado": (7, 3)
        }
        self.tensions = {
            "Residency": 0.9, "Panama": 0.6, "Spanish": 0.3, "Ser Aliado": 0.1
        }
        self.ambient_tension = 0.5
        self.last_update = time.time()

    def calculate_flux(self, topic, word_count):
        gamma = self.tensions.get(topic, self.ambient_tension)
        efficiency = 1.0 - (gamma * 0.5)
        flux_cost = word_count * (1 - efficiency)
        return efficiency, flux_cost

    def apply_decay(self, decay_rate=0.01):
        now = time.time()
        elapsed = now - self.last_update
        for word in self.tensions:
            diff = self.ambient_tension - self.tensions[word]
            self.tensions[word] += diff * (decay_rate * elapsed)
        self.last_update = now

    def audit_security(self):
        return all(0 <= v <= 1 for v in self.tensions.values())

if __name__ == "__main__":
    ser_aliado = FluidTokenizer()
    print("FluidTokenizer initialized.")
    print(f"Audit passed: {ser_aliado.audit_security()}")
