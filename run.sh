if [ ! -d "TD5-venv" ]; then
  python3 -m venv ./TD5-venv
  pip3 install -r requirements.txt
  source "./TD5-venv/bin/activate"
  
fi

source TD5-venv/bin/activate
echo "activated"
python3 main.py



