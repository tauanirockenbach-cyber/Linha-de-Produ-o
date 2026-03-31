import random

for i in range(20):
    ph = random.uniform(0, 30)
    print(f"Valor: { ph:.2f} pH")

    if  ph < 6 or ph > 8:
        print("ALERTA, pH fora do padrão")