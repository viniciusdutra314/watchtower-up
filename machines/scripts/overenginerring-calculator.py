#!/usr/bin/env python


print(r"""
  ╭──────────────────────────────────────╮
  │  ⚙  OVERENGINEERING CALCULATOR       │
  │  ──────────────────────────────────  │
  │  Otimize menos. Faça mais            │
  ╰──────────────────────────────────────╯
""")


import math
tempo_setup=int(input("Tempo de setup estimado (m): "))
tempo_economizado=int(input("Economia por uso (m): "))
vezes_usado_por_dia=int(input("Vezes por dia usado: "))


if tempo_economizado * vezes_usado_por_dia == 0:
    print("💀 Essa melhoria nunca vai se pagar!")
elif tempo_setup > vezes_usado_por_dia * tempo_economizado:
    print("🚫 Não compensa fazer hoje!")
    print(f"⏳ Vai demorar {math.ceil(tempo_setup / (vezes_usado_por_dia * tempo_economizado))} dias para compensar.")
    print("📝 Anote a ideia e volte ao trabalho! 📚")
else:
    print("✅ Investimento aprovado!")
    print("🚀 Vai lá, campeão!")

