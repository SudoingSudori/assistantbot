from discord.ext import commands
import asyncio

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="~")

async def main():
    bot = Bot()
    await bot.start()

asyncio.run(main())