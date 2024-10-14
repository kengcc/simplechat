# SimpleChat

Simple chat app using OpenAI API and OLLAMA.

## Getting started

1. clone the project from 
```
'https://gitlab.tmrnd.com.my/Project-Sandbox/langchain/simplechat.git'
```

2. create and set the .env
```
   OPENAI_API_KEY="sk-***"
   LANGCHAIN_API_KEY ="lsv2_***"
   LANGCHAIN_PROJECT ="Project1"
```
3. set the venv for the porject. Python environment
```
   % python -m venv venv
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

## Push to master
```
%git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://gitlab.tmrnd.com.my/Project-Sandbox/langchain/simplechat.git'

To fix it
git add .
git commit -m "message"
git remote add origin https://gitlab.com/*******.git
git branch -M main
git push -uf origin main
```

## License
For open source projects, say how it is licensed.

