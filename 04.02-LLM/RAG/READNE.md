# 🤖 Guia Prático para Construir Aplicações RAG Locais com LangChain

Este repositório contém um guia passo a passo para construir aplicações RAG (**Retrieval-Augmented Generation**) de forma local utilizando a biblioteca **LangChain**.

O objetivo é mostrar como conectar modelos de linguagem com bases de conhecimento próprias (documentos locais, bancos de dados, PDFs, etc.), tornando as respostas mais precisas, confiáveis e contextualizadas — sem depender de APIs externas.

---

## 📌 O que é uma aplicação RAG?

RAG é uma técnica que combina:

- **Recuperação de informações**: busca em uma base de dados/vector store por documentos relevantes.
- **Geração de linguagem natural**: usa um modelo de linguagem (LLM) para gerar respostas com base nos documentos encontrados.

Isso permite criar **chatbots, assistentes, buscadores inteligentes e FAQs dinâmicos** com conhecimento especializado.

---

## 🧰 Tecnologias Utilizadas

- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss) para vetorização e busca de documentos
- [ChromaDB](https://www.trychroma.com/) ou [Weaviate](https://weaviate.io/) como alternativa de vector store
- Modelos LLM locais via:
  - [GPT4All](https://github.com/nomic-ai/gpt4all)
  - [LLAMA.cpp](https://github.com/ggerganov/llama.cpp)
  - [Ollama](https://ollama.ai/)
- Leitura de documentos com `langchain.document_loaders` (PDF, TXT, DOCX, etc)

---

## 📦 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/guia-pratico-rag-langchain.git
cd guia-pratico-rag-langchain
```