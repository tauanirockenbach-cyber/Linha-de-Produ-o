import random

for i in range(20):
    velocidade = random.uniform(0, 3)
    print(f"velocidade: {velocidade:.2f} m/s")

    if velocidade < 0.5:
        print("ALERTA, a esteira está muito devagar")