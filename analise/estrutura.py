def analisar_estrutura(texto):

    feedback = []
    paragrafos = [p.strip() for p in texto.strip().split("\n") if p.strip()]

    # Estrutura geral
    if len(paragrafos) < 3:
        feedback.append("Competência 2: A redação possui poucos parágrafos. Idealmente, deve conter introdução, desenvolvimento e conclusão para garantir uma estrutura completa e bem organizada.")
    else:
        feedback.append("Competência 2: Ótimo! Sua redação apresenta uma estrutura adequada, com introdução, desenvolvimento e conclusão bem definidos.")

    # Introdução
    if paragrafos:
        introducao = paragrafos[0].lower()
        if any(palavra in introducao for palavra in ["tema", "questão", "discutir", "problema", "contexto"]):
            feedback.append("Competência 2: A introdução contextualiza bem o tema, apresentando claramente o assunto a ser discutido.")
        else:
            feedback.append("Competência 2: A introdução poderia contextualizar melhor o tema proposto, apresentando claramente o assunto que será discutido.")

        # Desenvolvimento
        if len(paragrafos) > 2:
            desenvolvimento = paragrafos[1:-1]
            if any(len(p.split()) > 40 for p in desenvolvimento):
                feedback.append("Competência 2: Os parágrafos de desenvolvimento estão extensos. Considere dividi-los para facilitar a leitura e a organização das ideias.")
            else:
                feedback.append("Competência 2: Os parágrafos de desenvolvimento estão bem distribuídos, facilitando a compreensão e a progressão dos argumentos.")

        # Conclusão
        conclusao = paragrafos[-1].lower()
        if any(palavra in conclusao for palavra in ["portanto", "conclui", "em suma", "dessa forma", "assim", "por fim", "em conclusão"]):
            feedback.append("Competência 2: A conclusão está bem sinalizada e encerra o texto de forma adequada, retomando o tema e apresentando um fechamento claro.")
        else:
            feedback.append("Competência 2: A conclusão poderia ser mais clara e bem sinalizada, utilizando conectivos conclusivos para encerrar o texto e retomar o tema.")

    return feedback