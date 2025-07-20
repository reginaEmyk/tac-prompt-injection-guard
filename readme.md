BUILD & RUN
````
docker build -t gemini-rag-app . && docker run -p 8501:8501 --env-file .env gemini-rag-app
```