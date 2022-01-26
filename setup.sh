#/bin/bash
# https://stackoverflow.com/questions/41868707/check-if-directory-does-not-exist
if [ ! -d "./venv" ]; then
	python -m venv venv
fi
source ./venv/bin/activate
# https://stackoverflow.com/questions/9392735/linux-how-to-copy-but-not-overwrite/19997505
cp -n config.env .env
pip install -r requirements.txt
