"""The cog for bf2042 portal"""
import discord
from discord.ext import commands
from discord import app_commands
from . import server_list


class BattleBit(commands.Cog, name="bb"):
    """Battlebit"""

    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot
        super().__init__()

    group = app_commands.Group(name="bb", description="Battlebit cog")
    group.allowed_installs = app_commands.AppInstallationType(guild=True, user=True)
    
    @group.command(
        name="serverlist",
        description="List all the servers based on a searchterm for Battlebit.",
    )
    async def serverlist(self, interaction: discord.Interaction, servername: str) -> None:
        """Battlebit servers"""
        await interaction.response.defer()
        await server_list.main(interaction, servername)

    @serverlist.error
    async def tools_error(self, interaction: discord.Interaction, _error) -> None:
        """Error handling"""
        embed = discord.Embed(color=0xE74C3C, description="Failed to get serverlist for battlebit")
        await interaction.followup.send(embed=embed)