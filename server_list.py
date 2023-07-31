import json
import aiohttp
import discord
import urllib.parse
from global_mapping import battlebit as BATTLEBIT

async def main(interaction: discord.Interaction, searchterm: str):
    async with aiohttp.ClientSession() as session:
        url = "https://publicapi.battlebit.cloud/Servers/GetServerList"
        async with session.get(url) as r:
            result = await r.text()
            servers = json.loads(result.lstrip('\ufeff'))
            
    total = 0
    embed = discord.Embed(color=0xFFA500, title=f"{searchterm} - BattleBit Servers",)
    for server in servers:
        if server.get("IsOfficial", False):
            server["Name"] = f'[Official] - {server.get("Name", "")}'
        else:
            server["Name"] = f'[Community] - {server.get("Name", "")}'
        if searchterm.lower() in server.get("Name", "").lower():
            if total > 10:
                break
            total += 1
            embed.add_field(
                name=server.get("Name"),
                value=f"on **{server.get('Map', '')}** with **{server.get('Players', 0)}/{server.get('MaxPlayers', 0)}[{server.get('QueuePlayers', 0)}]** players, **{BATTLEBIT.MODES.get(server.get('Gamemode', ''), server.get('Gamemode', ''))}**\n",
                inline=False,
            )
    # footer
    embed.add_field(
        name="\u2063",
        value=f"[Open serverlist](https://gametools.network/servers?search={urllib.parse.quote(searchterm)}&game=battlebit)",
        inline=False,
    )
    await interaction.followup.send(embed=embed)