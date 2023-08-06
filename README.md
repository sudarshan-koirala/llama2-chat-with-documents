# Llama2-chat-with-documents
Simple Chainlit app to have interaction with your documents.

### Chat with your documents 🚀
- [Huggingface model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin) as Large Language model
- [LangChain](https://python.langchain.com/docs/get_started/introduction.html) as a Framework for LLM
- [Chainlit](https://docs.chainlit.io/overview) for deploying.
- [GGML](https://github.com/ggerganov/ggml) to run in commodity hardware (cpu)
- [CTransformers](https://github.com/marella/ctransformers) to load the model.

## System Requirements

You must have Python 3.9 or later installed. Earlier versions of python may not compile.  

---

## Steps to Replicate 

1. Fork this repository and create a codespace in GitHub as I showed you in the youtube video OR Clone it locally.
   ```
   git clone https://github.com/sudarshan-koirala/llama2-chat-with-documents.git
   cd llama2-chat-with-documents
   ```

2. Rename example.env to .env with `cp example.env .env`and input the HuggingfaceHub API token as follows. Get HuggingfaceHub API key from this [URL](https://huggingface.co/settings/tokens). You need to create an account in Huggingface webiste if you haven't already.
   ```
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
   ```
   
3. Create a virtualenv and activate it
   ```
   python3 -m venv .venv && source .venv/bin/activate
   ```

4. Run the following command in the terminal to install necessary python packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the following command in your terminal to create the embeddings and store it locally:
   ```
   python3 run ingest.py
   ```

6. Run the following command in your terminal to run the app UI:
   ```
   chainlit run main.py -w
   ```
