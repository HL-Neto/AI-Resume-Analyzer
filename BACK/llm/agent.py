
from llm.pinecone    import splitter, pinecone
from langchain_google_genai import ChatGoogleGenerativeAI

def llm():

    doc_splitter = splitter()

    vector_store = pinecone(doc_splitter)

    model = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash"
    )

    # Pega todos os IDs únicos
    ids_curriculos = list({
        doc.metadata["id"]
        for doc in doc_splitter
    })



    # Analisa cada currículo
    for id_curriculo in ids_curriculos:


        # Pega somente os chunks desse currículo
        documentos = vector_store.similarity_search(
            "currículo completo",
            k=10,
            filter={
                "id": id_curriculo
            }
        )

        contexto = "\n\n".join(
            doc.page_content
            for doc in documentos
        )


        prompt = f"""
        Analise o currículo abaixo para a vaga de Assistente da Administração
        da MOTOMAR - Honda.

        VAGA:
        - CNH A/B é requisito obrigatório.
        - Experiência com entrega é um diferencial.
        - Entrega de motos entre unidades.
        - Seguir rotas e cronogramas.
        - Carregar e descarregar veículos.

        CURRÍCULO:
        {contexto}

        Informe:

        - Nome
        - Experiências relevantes
        - Pontos positivos
        - Pontos de atenção
        - Compatibilidade de 0 a 100
        - Classificação final
        """

        resposta = model.invoke(prompt)

        return resposta

