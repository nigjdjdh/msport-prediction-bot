# M-Sport Virtual Football Prediction Bot

## Overview
The M-Sport virtual football prediction bot is a Telegram bot that helps users predict outcomes of virtual football matches. This document provides comprehensive information on setting up the bot, obtaining necessary tokens, configuring environment variables, running it locally, and deploying it on Railway.

## Getting Started

### Prerequisites
- Basic understanding of Python
- A Telegram account
- Access to Railway for deployment

### Step 1: Create a Telegram Bot Token
1. Open Telegram and search for the **BotFather**.
2. Start a chat with the BotFather and use the `/newbot` command.
3. Follow the prompts to name your bot and get a unique token. Save this token securely; you'll need it later.

### Step 2: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/nigjdjdh/msport-prediction-bot.git
cd msport-prediction-bot
```

### Step 3: Configure Environment Variables
Create a `.env` file in the root of the project and include the following:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```
Replace `your_telegram_bot_token` with the token you obtained from BotFather.

### Step 4: Install Required Packages
Make sure you have Python installed. You can install the required packages using pip:
```bash
pip install -r requirements.txt
```

### Step 5: Run the Bot Locally
You can run the bot locally to test it:
```bash
python main.py
```

### Deployment on Railway
1. Go to [Railway](https://railway.app/) and sign up or log in.
2. Create a new project and connect it to your GitHub repository.
3. Add your environment variables in the Railway dashboard under the **Variables** section.
4. Set up a deployment by following Railway's prompts. Your bot should be live shortly after this.

## Conclusion
You are now ready to use the M-Sport virtual football prediction Telegram bot! For further information and updates, please refer to the repository or contact the maintainer.

## License
This project is licensed under the MIT License.