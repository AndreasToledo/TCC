def analisar_argumentacao(texto):
    feedback = []
    texto_lower = texto.lower()

    # Competência 2: Repertório sociocultural
    exemplos_repertorio = ["segundo", "de acordo com", "conforme", "como diz", "conforme dados", "pesquisa", "ibge", "onu", "filósofo", "historiador"]
    repertorio = any(expr in texto_lower for expr in exemplos_repertorio)
    if repertorio:
        feedback.append("Competência 2: Muito bom! Você utilizou repertório sociocultural, como dados, citações ou referências, enriquecendo sua argumentação.")
    else:
        feedback.append("Competência 2: Considere inserir repertório sociocultural (dados, citações, exemplos históricos ou referências) para fortalecer seus argumentos.")

    # Competência 3: Clareza, progressão e fundamentação dos argumentos
    opinativos = {"acho", "penso", "acredito", "creio"}
    encontrados = [palavra for palavra in opinativos if palavra in texto_lower]
    if encontrados:
        feedback.append("Competência 3: Evite usar verbos como 'acho', 'penso', 'acredito' ou 'creio', pois deixam a argumentação subjetiva. Prefira argumentos baseados em fatos, dados ou referências.")
    else:
        feedback.append("Competência 3: Sua argumentação está objetiva e fundamentada, sem uso de expressões opinativas.")

    conectivos_argumentativos = {"portanto", "logo", "além disso", "por conseguinte", "dessa forma", "assim", "contudo", "porém"}
    conectivos_usados = [c for c in conectivos_argumentativos if c in texto_lower]
    if len(conectivos_usados) >= 2:
        feedback.append("Competência 3: Ótimo uso de conectivos argumentativos, o que garante progressão e clareza às ideias.")
    else:
        feedback.append("Competência 3: Procure usar mais conectivos argumentativos para melhorar a progressão e a ligação entre os argumentos.")

    # Competência 5: Proposta de intervenção detalhada
    termos_de_intervencao = {"governo", "educação", "campanha", "medida", "política pública", "sociedade", "família", "escola", "projeto"}
    encontrou_intervencao = any(p in texto_lower for p in termos_de_intervencao)
    detalhamento = any(expr in texto_lower for expr in ["deve", "deveria", "é necessário", "precisa", "urge", "fundamental que"])
    if encontrou_intervencao and detalhamento:
        feedback.append("Competência 5: Excelente! Sua proposta de intervenção está clara e detalhada, indicando agentes, ações e objetivos.")
    elif encontrou_intervencao:
        feedback.append("Competência 5: Sua redação apresenta uma proposta de intervenção, mas procure detalhar mais quem deve agir, como e com qual objetivo.")
    else:
        feedback.append("Competência 5: Não identifiquei uma proposta clara de intervenção social. Considere sugerir uma solução viável para o problema apresentado, detalhando agentes, ações e finalidade.")

    return feedback