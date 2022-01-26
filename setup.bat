if not exist venv python -m venv venv
call venv\Scripts\activate.bat
@REM https://stackoverflow.com/questions/4228807/copy-files-without-overwrite
echo n | copy /-y config.env .env
pip install -r requirements.txt