"""
Recruitment Thread cog for aa-discordbot - https://github.com/pvyParts/allianceauth-discordbot

Creates a private thread for recruiters and recruits in your discord to manage recruitment of new members.
"""
# Cog Stuff
import logging
logger = logging.getLogger(__name__)
import discord
from discord.ext import commands

# AA Contexts
from django.conf import settings

# Validation Checks - These values must be defined in server settings
#if not hasattr(settings, "SOLARMARK_RECRUIT_CHANID"):
#    raise ValueError("Recruitment base channel is not defined")
#if not hasattr(settings, "SOLARMARK_RECRUIT_MSG"):
#    raise ValueError("Recruitment message is not defined")
#if not hasattr(settings, "SOLARMARK_CORP_ROLEID"):
#    raise ValueError("Recruitment role ID is not defined")
#if not hasattr(settings, "SOLARMARK_RECRUITER_ROLEID"):


class Recruit(commands.Cog):
	"""
	Creates private thread for recruits.
	"""
	
	def __init__(self, bot):
		self.bot = bot

	async def thread_exist(self, member):
		for thread in self.get_channel(settings.SOLARMARK_RECRUIT_CHANID).threads:
			if thread.name == "RCT-" + member.name:
				return True
		return False

	async def caller_authorized(ctx):
		for userrole in ctx.author.roles:
			if userrole.id == settings.SOLARMARK_RECRUITER_ROLEID:
				return True
		return False

	async def target_not_in_corp(member):
		for userrole in member.roles:
			if userrole.id == settings.SOLARMARK_CORP_ROLEID:
				return False
		return True

	async def can_recruit(self, ctx, member):
		if not await self.caller_authorized(ctx):
			await ctx.respond("You do not have permission to use this command.", ephemeral = True)
			return False
		if not await self.target_not_in_corp(member):
			await ctx.respond("That user is already in the corporation.", ephemeral = True)
			return False
		if await self.thread_exist(self, member):
			await ctx.respond("That user already has an active recruitment thread.", ephemeral = True)
			return False
		return True

	@discord.user_command(name="Recruit for EVE")
	async def recruit(self, ctx, member: commands.Member):
		if await self.can_recruit(self, ctx, member):
			channel = self.get_channel(settings.SOLARMARK_RECRUIT_CHANID)
			threadname = "RCT-" + member.name
			messagetext = settings.SOLARMARK_RECRUIT_MSG.format(
				member.id,
				97032350247972864,
				97049182073786368,
				72091276689801216
			)
			threadinfo = await channel.create_thread(name=threadname, auto_archive_duration=10080, type=discord.ChannelType.private_thread)
			await self.get_channel(threadinfo.id).send(messagetext)
			await ctx.respond("Recruitment thread created!", ephemeral = True)

# Set the bot up
def setup(bot):
    bot.add_cog(Recruit(bot))
