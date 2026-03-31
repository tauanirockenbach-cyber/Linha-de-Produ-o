import random

for i in range(20):
    nivel = random.uniform(0, 100)
    print(f"Nível dos tanques: {nivel:.2f} %")

    if nivel < 20 or nivel > 90:
        print("ALERTA!")