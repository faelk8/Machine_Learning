

# Criando um ambiente virtual

```
python3 -m venv llama
source llama/bin/activate
pip install llama-cpp-python
pip install langchain langchain-community sentence-transformers chromadb
pip install pypdf requests pydantic tqdm
```

# Modelo LLM Llama
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf


O modelo faz leitura de arquivos do tipo txt, pdf entre outros 


Tanto os LLMs quanto os sistemas RAG precisam lidar com representações numéricas de texto em vez de texto bruto, portanto, em seguida, construímos um armazenamento vetorial que contém incorporações de nossos documentos de texto. Croma é um banco de dados vetorial leve e de código aberto para armazenar e consultar incorporações com eficiência.


Precisa de ajustes para enviar as perguntas pelo terminal.