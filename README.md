# ChatGPT-Telegram-Bot
A Telegram Bot capable of interacting with OpenAI's ChatGPT model using revChatGPT and python-telegram-bot.org


### Setup 
1. Clone this repository into your working directory 
2. Ensure that all requirements are met and make sure that you have [chromedriver](https://chromedriver.chromium.org/) added to your PATH
```
pip install -r requirements.txt
```
3. Ensure that you have created both an OpenAI account (to interface with ChatGPT) and registered with @BotFather on telegram
4. Create a new config.json in the working directory
```
{
  "session_token":"<YOUR SESSION TOKEN>",
  "API_Key" : "<Your Telegram API KEY>"
}
```
5. 
```
python main.py
```

## To get ur session token 
1. Sign into [ChatGPT](https://chat.openai.com/chat) 
2. Inspect Element (f12) and go to the Application tab
3. Your session token will be under the field "__Secure-next-auth.session-token"


## Usage Notes
The bot is configured such that any input will be considered a message for ChatGPT. This means you do not need to add '/' before each command like most telegram bots. This design decision was made because the bot is meant purely as a portable interface to interact with the model. 

You will have to keep your machine running to use the bot. One workaround is to create a flask landing page on [Replit](https://replit.com/~) and use [Uptime Robot](https://uptimerobot.com/) to keep it running perpertually. However, Replit's chromedriver support is not the most straightforward to use.
