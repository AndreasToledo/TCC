import sys
import io
import json
import re

from argumentacao import analisar_argumentacao
from coesao import analisar_coesao
from estrutura import analisar_estrutura

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def extrai_competencia(msg):
    m = re.match(r"Competência (\d+):", msg)
    return int(m.group(1)) if m else 99  # 99 para mensagens sem competência

if __name__ == "__main__":
    texto = sys.stdin.buffer.read().decode('utf-8').strip()

    feedbacks = []
    feedbacks.extend(analisar_argumentacao(texto))
    feedbacks.extend(analisar_coesao(texto))
    feedbacks.extend(analisar_estrutura(texto))

    # Ordena os feedbacks pela competência
    feedbacks.sort(key=extrai_competencia)

    resultado_json = json.dumps({"feedback": feedbacks}, ensure_ascii=False)
    print(resultado_json)