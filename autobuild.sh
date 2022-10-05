if [ ! -e venv ]; then
    python3.9 -m venv venv
    venv/bin/python -m pip install -r requirements.txt
fi
venv/bin/sphinx-autobuild -WT docs build/html