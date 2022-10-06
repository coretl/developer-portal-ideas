VENV=/tmp/developer-portal-venv
if [ ! -e $VENV ]; then
    python3.9 -m venv $VENV
    $VENV/bin/python -m pip install -r requirements.txt
fi
$VENV/bin/sphinx-autobuild -WT docs build/html