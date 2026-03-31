import random

for i in range(20):
    consumo = random.uniform(0, 1000)
    print(f"Consumo: {consumo:.2f} kWh")

    if consumo < 500:
        print("ALERTA")