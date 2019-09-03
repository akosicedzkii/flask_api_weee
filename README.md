# flask_api_weee

python -m venv env

source env/bin/activate

pip install -r requirements.txt

RUN FLASK_APP=run.py FLASK_DEBUG=1 flask run
