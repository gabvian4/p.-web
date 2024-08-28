consumo_dia=[240, 310, 250, 230, 220, 340, 270, 260, 255, 300, 280, 260, 250, 240, 220, 320, 310, 290, 275, 260, 250, 240, 300, 330, 340, 200, 360, 280, 290, 310]
consumo_min=min(consumo_dia)
consumo_max=max(consumo_dia)
diferença=consumo_max-consumo_min
if diferença >=100:
    print(f"dia de maior consumo:{consumo_max}")
    print(f"dia de menor consumo:{consumo_min}")
    print(f"diferença de consumo:{diferença}")
    print(f"alerta: PARABÉNS! a diferença de consumo está ACIMA dos parâmetros aceitáveis.")
else:
    print(f"dia de maior consumo:{consumo_max}")
    print(f"dia de menor consumo:{consumo_min}")
    print(f"diferença de consumo:{diferença}")
    print(f"alerta: CUIDADO! a diferença de consumo está ABAIXO dos parâmetros aceitáveis.")