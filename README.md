# BUILD & RUN
````
docker build -t gemini-rag-app . && docker run -p 8501:8501 --env-file .env gemini-rag-app
```
# Miscellaneous
## Run without Docker
- install requirements.txt then:
```
streamlit run main.py
```
## Debug 
if 
````
Failed to import transformers.generation.utils because of the following 
error (look up to see its traceback):
numpy.core.multiarray failed to import
```
try:
```

pip3.10 uninstall -y numpy
pip3.10 install "numpy==1.21.6"

```
or
``` 
pip3.10 uninstall -y numpy
find . -name "*.pyc" -delete
find . -type d -name "__pycache__" -exec rm -r {} +
pip3.10 install numpy==2.2.6 --force-reinstall
```
