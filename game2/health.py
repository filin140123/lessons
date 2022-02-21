class HealthCounter:
    DEAD_HEALTH = 0

    def __init__(self, max_health=100, current_health=100):
        self.max_health = max_health
        self.current_health = current_health

    def __str__(self):
        return f"{self.current_health}/{self.max_health} hp"

    def health_up(self, x: int):
        self.current_health += x
        print(f"Character heals {x} hp.")
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def health_restored(self):
        self.current_health = self.max_health
        print("Character health fully restored.")

    def health_down(self, x: int):
        self.current_health -= x
        print(f"Character suffering {x} damage.")
        if self.current_health < HealthCounter.DEAD_HEALTH:
            self.current_health = HealthCounter.DEAD_HEALTH
            self.is_alive()

    def is_alive(self):
        return self.current_health != HealthCounter.DEAD_HEALTH


player_health = HealthCounter()
