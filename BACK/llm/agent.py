
from BACK.llm.pinecone import splitter, pinecone
from langchain_google_genai import ChatGoogleGenerativeAI


def extrair_texto(conteudo):
    if isinstance(conteudo, str):
        return conteudo

    if isinstance(conteudo, list):
        partes = []

        for parte in conteudo:
            if isinstance(parte, str):
                partes.append(parte)

            elif isinstance(parte, dict):
                if parte.get("type") == "text":
                    texto = parte.get("text", "")
                    if isinstance(texto, str):
                        partes.append(texto)

        return "\n".join(partes)

    if isinstance(conteudo, dict):
        texto = conteudo.get("text", "")
        return texto if isinstance(texto, str) else ""

    return ""


def llm():
    doc_splitter = splitter()

    if not doc_splitter:
        return []

    vector_store = pinecone(doc_splitter)

    model = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite"
    )

    ids_curriculos = list(dict.fromkeys(
        doc.metadata["id"]
        for doc in doc_splitter
        if doc.metadata.get("id") is not None
    ))

    resultados = []

    for id_curriculo in ids_curriculos:
        documentos = vector_store.similarity_search(
            "currículo completo",
            k=10,
            filter={"id": id_curriculo}
        )

        if not documentos:
            continue

        contexto = "\n\n".join(
            doc.page_content
            for doc in documentos
        )

        prompt = f"""
Analise o currículo abaixo para a vaga de Assistente da Administração
da MOTOMAR - Honda.

REQUISITOS DA VAGA:
- CNH A/B é requisito obrigatório.
- Experiência com entrega é um diferencial.
- Entrega de motos entre unidades.
- Seguir rotas e cronogramas.
- Carregar e descarregar veículos.

CURRÍCULO:
{contexto}

INSTRUÇÕES:
- Analise somente as informações presentes no currículo.
- Não invente informações sobre o candidato.
- Se a CNH não estiver mencionada, informe:
  "CNH não informada — requisito não confirmado".
- Não considere ausência de informação como prova de falta de experiência.
- Apresente a análise em português, de forma clara e objetiva.

INFORME:
- Nome do candidato.
- Experiências relevantes.
- Pontos positivos.
- Pontos de atenção.
- Compatibilidade de 0 a 100.
- Classificação final.
"""

        resposta = model.invoke(prompt)
        conteudo = extrair_texto(resposta.content)

        resultados.append({
            "candidato_id": str(id_curriculo),
            "analise": conteudo
        })

    return resultados
