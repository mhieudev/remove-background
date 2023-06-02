# Depend:
- Python 3.9.0
---
# Install Package:
### Install with env:    
```bash 
sudo rm -rf venv
python -m venv venv
source ./venv/bin/activate && pip install -r requirements.txt
```
### Install without env: 
```bash 
pip install -r requirements.txt
```
---
# Run
### Run without env:
```bash
cd server_file && python manage.py runserver {PORT}
``` 
- Replace: ```{PORT}```

### Run env:
```bash 
source ./venv/bin/activate && cd server_file && python manage.py runserver {PORT}
``` 
- Replace: ```{PORT}```
