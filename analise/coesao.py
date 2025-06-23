import spacy

from collections import Counter

nlp = spacy.load("pt_core_news_sm")

def analisar_coesao(texto):
    feedback = []
    doc = nlp(texto)

    # Análise do tamanho das frases
    frases_longas = [sent for sent in doc.sents if len(sent) > 30]
    if frases_longas:
        feedback.append("Competência 4: Algumas frases estão longas demais. Considere dividi-las para facilitar a leitura e evitar que o leitor se perca. Frases mais curtas ajudam na clareza e compreensão do texto.")
    else:
        feedback.append("Competência 4: Ótimo! Suas frases estão bem distribuídas, tornando o texto mais claro, objetivo e agradável de ler.")

    # Análise de repetição de palavras
    palavras = [t.text.lower() for t in doc if not t.is_punct and not t.is_stop]
    contagem = Counter(palavras)
    repetidas = [p for p, freq in contagem.items() if freq > 4]
    if repetidas:
        feedback.append(f"Competência 4: Evite repetição excessiva de palavras como: {', '.join(repetidas[:3])}. Procure utilizar sinônimos e variar o vocabulário para enriquecer o texto e evitar monotonia.")
    else:
        feedback.append("Competência 4: Muito bom! Não há repetição excessiva de palavras, o que demonstra riqueza vocabular e contribui para a qualidade do texto.")

    # Análise de conectivos
    conectivos = {
        "portanto", "contudo", "entretanto", "além disso", "porém", "logo", "ou seja", "assim", "dessa forma", "todavia", "no entanto", "consequentemente", "por conseguinte"
    }
    usados = set(t.text.lower() for t in doc if t.text.lower() in conectivos)
    if len(usados) == 0:
        feedback.append("Competência 4: Não foram encontrados conectivos no texto. O uso de conectivos é fundamental para garantir a coesão e a ligação lógica entre as ideias. Procure inserir conectivos variados ao longo dos parágrafos.")
    elif len(usados) < 2:
        feedback.append("Competência 4: Poucos conectivos encontrados. Varie e utilize mais conectivos para melhorar a coesão e a fluidez entre as ideias e parágrafos.")
    else:
        feedback.append("Competência 4: Excelente uso de conectivos! Isso garante coesão, fluidez e uma progressão lógica entre as ideias do texto.")

    # Análise de referência pronominal
    pronomes = [t.text.lower() for t in doc if t.pos_ == "PRON"]
    if len(pronomes) < 3:
        feedback.append("Competência 4: Pouco uso de pronomes. O uso adequado de pronomes pode evitar repetições e tornar o texto mais coeso.")
    else:
        feedback.append("Competência 4: Bom uso de pronomes, o que contribui para evitar repetições e garantir coesão referencial.")

    return feedback