from datetime import datetime
import discord
import os

from config.settings import DISCORD_SERVICE

class DiscordService(discord.Client):
    def __init__(self,image_path:str = "output/quoteImg.jpg",attribution: str = "Image by Unsplash"):
        super().__init__(intents=discord.Intents.default())
        self.token = os.getenv("DISCORD_BOT_TOKEN")
        self.image_path = image_path
        self.attribution = attribution

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        await self.send_quote_image()
        await self.close()
    
    async def send_quote_image(self):
        guild = discord.utils.get(self.guilds, name=DISCORD_SERVICE["guild_name"])
        if not self.guilds:
            print("❌ Bot is not connected to any guild (server).")
            return

        # Get the first server the bot is in
        guild = self.guilds[0]

        channel = discord.utils.get(guild.text_channels, name=DISCORD_SERVICE["channel_name"])
        if not channel:
            print(f"Channel, {channel} not found.")
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=True),
            }
            channel = await guild.create_text_channel('daily-quotes', overwrites=overwrites)
        
        with open(self.image_path, 'rb') as image_file:
            file = discord.File(image_file, filename="quoteImg.jpg")
            embed = discord.Embed(title=DISCORD_SERVICE["title"], description=DISCORD_SERVICE["attribution"]+ " by " + self.attribution, color=discord.Color.blue())
            embed.set_image(url="attachment://quoteImg.jpg")
            await channel.send(file=file, embed=embed)


    def run(self):
        super().run(self.token)