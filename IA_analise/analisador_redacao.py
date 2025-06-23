from estrutura import verificar_estrutura
from coesao import analisar_coesao
from argumentacao import avaliar_argumentacao

def analisar_redacao(texto: str) -> list[str]:
    feedback = []

    feedback.extend(verificar_estrutura(texto))
    feedback.extend(analisar_coesao(texto))
    feedback.extend(avaliar_argumentacao(texto))

    return feedback
