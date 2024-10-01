import discord
from discord import app_commands
from discord.ext import commands

class ChannelLock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="lock_channel", description="Lock the specified channel to prevent @everyone from sending messages.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lock_channel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        """Locks a channel by denying @everyone permission to send messages."""
        overwrite = channel.overwrites_for(interaction.guild.default_role)
        overwrite.send_messages = False

        await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        await interaction.response.send_message("🔒", ephemeral=False)

    @app_commands.command(name="unlock_channel", description="Unlock the specified channel to allow @everyone to send messages.")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def unlock_channel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        """Unlocks a channel by allowing @everyone permission to send messages."""
        overwrite = channel.overwrites_for(interaction.guild.default_role)
        overwrite.send_messages = True

        await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        await interaction.response.send_message("🔓", ephemeral=False)

async def setup(bot):
    await bot.add_cog(ChannelLock(bot))
