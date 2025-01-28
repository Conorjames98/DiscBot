import discord 
from discord.ext import commands


class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="clear", description="Clear messages in a channel.")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        deleted = await interaction.channel.purge(limit=amount + 1)  # Include the command message
        message = f"Successfully deleted {len(deleted) - 1} messages."  # Adjust for command message
        if not deleted:
            message = "No messages were found to delete."
        await interaction.response.send_message(message)


async def setup(bot):
    await bot.add_cog(ClearCog(bot))
