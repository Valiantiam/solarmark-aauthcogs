"""
Recruitment Thread cog for aa-discordbot - https://github.com/pvyParts/allianceauth-discordbot

Creates a private thread for recruiters and recruits in your discord to manage recruitment of new members.
"""
# Cog Stuff
import logging
import discord
from discord.ext import commands

# AA Contexts
from django.conf import settings


# Validation Checks
if not hasattr(settings, "THREAD_CHANID"):
    raise ValueError("Thread Channel is not defined")

class Thread(commands.Cog)
	"""
	Creates private thread for recruits.
	"""
	
	def __init__(self, bot):
		self.bot = bot
		
	@discord.user_command(name="Recruit for EVE")
	async def thread(self, ctx, member: discord.Member)
	
	channel = bot.get_channel(settings.THREAD_CHANID) # define this!
	await channel.create_thread(name="RCT-{member.name}", message={@}, auto_archive_duration=4320, type=private_thread, reason=None)

	
	
def setup(bot):
    """
    Setup the cog
    :param bot:
    """
    bot.add_cog(Thread(bot))
