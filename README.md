# SimpleChat

Simple chat app using OpenAI API and OLLAMA.

## Getting started

1. clone the project from here

2. create and set the .env
```
   OPENAI_API_KEY="sk-***"
   LANGCHAIN_API_KEY ="lsv2_***"
   LANGCHAIN_PROJECT ="Project1"
```
3. set the venv for the porject. Python environment
```
   % python -m venv venv
   Mac/Linux: % source venv/bin/activate
   Windows: .\venv\Scripts\activate
```

4. install the dependencies within the venv
```
   % pip install -r requirements.txt
```

5. run ollama
```
% ollama run gemma2:2b
```

6. run the application 
```
   % streamlit run app.py
```

7. Check the langsmith (LLMOps)
```
   https://smith.langchain.com/
```

8. Run "deactivate" to exit venv environment

## License
For open source projects, say how it is licensed.

