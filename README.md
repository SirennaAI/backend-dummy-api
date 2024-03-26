#create enviroment
python3 -m venv .venv

#activate enviroment
source .venv/bin/activate

#instal package
pip3 install -r requirements.txt

#run project
uvicorn main:app --host 0.0.0.0 --port 8000 --reload