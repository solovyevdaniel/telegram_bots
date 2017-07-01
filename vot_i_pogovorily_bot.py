import json
import requests


TOKENS_JSON = 'tokens.json'
BOT = 'vot_i_pogovorili_bot'
API_URL = "https://api.telegram.org/bot{bot_token}/"
MyURL = "https://example.com/hook"


with open(TOKENS_JSON) as tokens_json:
	tokens = json.load(tokens_json)
	BOT_TOKEN = tokens[BOT]
	API_URL = API_URL.format(bot_token=BOT_TOKEN)
