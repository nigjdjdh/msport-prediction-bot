import telegram
import requests
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'
M_SPORT_API_URL = 'https://api.m-sport.com/live_matches'

async def fetch_live_matches():
    response = requests.get(M_SPORT_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

async def send_prediction(prediction):
    bot = telegram.Bot(token=API_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=prediction)

async def main():
    while True:
        live_matches = await fetch_live_matches()
        if live_matches:
            # Placeholder for prediction logic
            for match in live_matches:
                prediction = f"Match: {match['team1']} vs {match['team2']} - Prediction: [Your prediction logic here]"
                await send_prediction(prediction)
        await asyncio.sleep(60)  # Wait for a minute before fetching again

if __name__ == '__main__':
    asyncio.run(main())