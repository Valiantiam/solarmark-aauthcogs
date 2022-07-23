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


# Validation Checks - SOLARMARK_THREAD_CHANID and SOLARMARK_THREAD_MSG must be defined in server settings
if not hasattr(settings, "SOLARMARK_THREAD_CHANID"):
    raise ValueError("Thread Channel is not defined")
if not hasattr(settings, "SOLARMARK_THREAD_MSG"):
    raise ValueError("Thread Message is not defined")

class Thread(commands.Cog):
	"""
	Creates private thread for recruits.
	"""
	
	def __init__(self, bot):
		self.bot = bot

	async def is_corp_member(ctx):
		for userrole in ctx.author.roles:
		return ctx.author.roles 
		
	@commands.user_command(name="Recruit for EVE")
	@commands.check(is_corp_member)
	async def recruit(self, ctx, member: commands.Member):
		channel = commands.get_channel(settings.SOLARMARK_THREAD_CHANID)
		threadname = "RCT-" + member.name
		messagetext = settings.SOLARMARK_THREAD_MSG.format(member.name)
		await channel.create_thread(name=threadname, message=messagetext, auto_archive_duration=10080, type=private_thread, reason=None)
	
	
def setup(bot):
    """
    Setup the cog
    :param bot:
    """
    bot.add_cog(Thread(bot))