# ppomppu_naver_point_telegram_bot
Searching ppomppu (네이버) and sending result with Telegram bot

# Requirement
* Python 3

# How to install
## 1. Create or inject `.env` file using `config.env`
* `FULL_URL` is ppomppu URL for searching Naver Point(네이버 페이 포인트) article. It's almost default.
* `TELEGRAM_TOKEN` is bot id created by Telegram's bot father (https://t.me/botfather)
* `TELEGRAM_DEFAULT_CHAT_ID` is default Chat ID if you have known chat id from created bot
# (Option) 2. Make virtual running environment
* `python -m venv venv`
* `source ./venv/bin/activate` (Linux) or `.\venv\Scripts\activate.bat` (Windows)
## 3. Install library
### `pip install -r requirements.txt`
# How to Run
## Run like daemon
`python main.py`
## Run Unit test
`python unit_test.py`

It loops page searching and sending every 10 seconds.

# Caveat
Use own discretion