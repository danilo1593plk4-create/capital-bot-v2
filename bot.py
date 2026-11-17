"""Capital Bot V2 — bot Discord com comandos de barra, sem Message Content Intent."""
import logging
import os

import discord
from discord import app_commands
from discord.ext import commands

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("capital_bot")


def get_guild_id() -> int | None:
    value = os.getenv("GUILD_ID", "").strip()
    if not value:
        return None
    if not value.isdigit():
        raise ValueError("GUILD_ID deve conter somente numeros (ID do servidor Discord).")
    return int(value)


class CapitalBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        # Comandos / não exigem Message Content Intent nem Members Intent.
        super().__init__(command_prefix="!", intents=intents, help_command=None)

    async def setup_hook(self):
        guild_id = get_guild_id()
        if guild_id:
            guild = discord.Object(id=guild_id)
            self.tree.copy_global_to(guild=guild)
            result = await self.tree.sync(guild=guild)
            log.info("Sincronizados %s comandos no servidor %s", len(result), guild_id)
        else:
            result = await self.tree.sync()
            log.info("Sincronizados %s comandos globais; podem demorar para aparecer", len(result))


bot = CapitalBot()


@bot.tree.command(name="ping", description="Verifica se o Capital Bot está funcionando")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Capital Bot online! Latência: {latency} ms.", ephemeral=True)


@bot.tree.command(name="ajuda", description="Mostra os comandos do Capital Bot")
async def ajuda(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Capital Bot | Ajuda",
        description="O bot está funcionando. Comandos disponíveis: **/ping** e **/ajuda**.",
        color=discord.Color.purple(),
    )
    embed.set_footer(text="Capital RP")
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.event
async def on_ready():
    log.info("Bot conectado como %s (ID %s)", bot.user, bot.user.id if bot.user else "?")


if __name__ == "__main__":
    token = os.getenv("TOKEN", "").strip()
    if not token:
        raise SystemExit("ERRO: configure TOKEN nas variaveis de ambiente da Altare.")
    bot.run(token)
