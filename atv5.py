import random

for i in range(20):
    temperatura = random.uniform(0, 30)
    print(f"Temperatura: {temperatura:.2f} °C")

    if temperatura < 0.5:
        print("ALERTA, temperatura fora do limite!")