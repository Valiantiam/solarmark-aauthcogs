"""
Recruitment Thread cog for aa-discordbot - https://github.com/pvyParts/allianceauth-discordbot

Creates a private thread for recruiters and recruits in your discord to manage recruitment of new members.
"""

# Standard Library
import logging

# Third Party
from discord.ext import commands

# Django
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
		
	@commands.user_command(name="Create Recruit Thread"
	async def thread(self, ctx, member: disrod.Member)
	
	channel = bot.get_channel(600408850658623498) # define this!
	await channel.create_thread(name="RCT-{member.name}", message=None, auto_archive_duration=4320, type=private_thread, reason=None)
