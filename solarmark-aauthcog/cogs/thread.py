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


# Validation Checks - THREAD_CHANID and THREAD_MSG must be defined in server settings
if not hasattr(settings, "THREAD_CHANID"):
    raise ValueError("Thread Channel is not defined")
if not hasattr(settings, "THREAD_MSG"):
    raise ValueError("Thread Message is not defined")

class Thread(commands.Cog):
	"""
	Creates private thread for recruits.
	"""
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.user_command(name="Recruit for EVE")
	async def recruit(self, ctx, member: commands.Member):
		channel = commands.get_channel(settings.THREAD_CHANID)
		threadname = "RCT-" + member.name
		messagetext = settings.THREAD_MSG.format(member.name)
		await channel.create_thread(name=threadname, message=messagetext, auto_archive_duration=10080, type=private_thread, reason=None)


def setup(bot):
    """
    Setup the cog
    :param bot:
    """

    bot.add_cog(Thread(bot))
