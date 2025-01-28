import discord
from discord.ext import commands

class InfoCog(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="info", description="Check the bot's information.")
    async def info(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=self.create_info_embed())  # Call the embed creation function

    def create_info_embed(self):
        embed = discord.Embed(title="Bot Information", description="A moderation & tool discord bot.", color=0x00ff00)
        embed.add_field(name="Creator", value="---------", inline=False)
        embed.add_field(name="Version", value="1.0.0", inline=False)
        embed.add_field(name="Github", value="[https://github.com/Conorjames98]")
        return embed 

async def setup(bot):
    await bot.add_cog(InfoCog(bot))