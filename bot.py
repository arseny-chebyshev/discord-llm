import discord
from discord.ext import commands
from config import DISCORD_BOT_TOKEN
from ai import AIService


class DiscordBot(commands.Bot):
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user or message.author.bot:
            return
        try:
            ai = AIService(message.author)
            answer = await ai.generate_message(message.content)
            await message.reply(
                answer.content
            )
        except Exception as e:
            print(f"Error occurred: {e}")
            await message.reply(
                "Sorry, I was unable to process your question."
            )


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    bot = DiscordBot(command_prefix='/', intents=intents)
    bot.run(token=DISCORD_BOT_TOKEN)
