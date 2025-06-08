import discord
import sqlite3
import json

with open("config.json") as config_file:
    config = json.load(config_file)

TOKEN = config["token"]
CHANNEL_ID = int(config["channel_id"])
DB_PATH = "../database/ac_points.db"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def get_top_scores(limit=10):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS overtake_scores (driver TEXT, points INTEGER)")
    c.execute("SELECT driver, points FROM overtake_scores ORDER BY points DESC LIMIT ?", (limit,))
    top = c.fetchall()
    conn.close()
    return top

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        leaderboard = get_top_scores()
        msg = "**🏁 Top Overtake Drivers 🏁**\\n"
        for i, (driver, points) in enumerate(leaderboard, 1):
            msg += f"**{i}. {driver}** – {points} Punkte\\n"
        await channel.send(msg)

client.run(TOKEN)
