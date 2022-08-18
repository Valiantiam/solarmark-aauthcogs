"""
Recruitment Thread cog for aa-discordbot - https://github.com/pvyParts/allianceauth-discordbot

Creates a private thread for recruiters and recruits in your discord to manage recruitment of new members.
"""
# Cog Stuff
import discord
import re
from discord.ext import commands

# AA Contexts
from django.conf import settings

# Validation Checks - These values must be defined in server settings
if not hasattr(settings, "SOLARMARK_GUILDID"):
    raise ValueError("SOLARMARK_GUILDID is not defined.")
if not hasattr(settings, "SOLARMARK_RECRUIT_CHANID"):
    raise ValueError("SOLARMARK_RECRUIT_CHANID is not defined.")
if not hasattr(settings, "SOLARMARK_TARGET_ROLEID"):
    raise ValueError("SOLARMARK_TARGET_ROLEID is not defined.")
if not hasattr(settings, "SOLARMARK_CORP_ROLEID"):
    raise ValueError("SOLARMARK_CORP_ROLEID is not defined.")
if not hasattr(settings, "SOLARMARK_RECRUITER_ROLEID"):
	raise ValueError("SOLARMARK_RECRUITER_ROLEID is not defined.")
if not hasattr(settings, "SOLARMARK_LEADERSHIP_USERIDS"):
	raise ValueError("SOLARMARK_LEADERSHIP_USERIDS is not defined.")
if not hasattr(settings, "SOLARMARK_RECRUIT_MSG_1"):
    raise ValueError("SOLARMARK_RECRUIT_MSG_1 is not defined.")

# Returns the count of how many SOLARMARK_RECRUIT_MSG_# settings variables are available, assuming SOLARMARK_RECRUIT_MSG_1 will always exist
async def msgcount():
	i = 0
	while (hasattr(settings, "SOLARMARK_RECRUIT_MSG_" + str((i + 1)))):
		i += 1
	return i
	
# Returns whether the reaction clicked on by a user in recruitment is valid
async def valid_reaction(self, reaction, user):
	if reaction.message.channel.name == "RCT-" + user.name:
		if reaction.emoji == '\N{White Heavy Check Mark}':
			async for user in reaction.users():
				if user.id == self.bot.user.id:
					return True
	return False

class Recruit(commands.Cog):
	"""
	Creates private thread for recruits.
	"""
	
	def __init__(self, bot):
		self.bot = bot
	
	# Listener for added reactions to see whether additional recruitment messages should be sent
	@discord.Cog.listener()
	async def on_reaction_add(self, reaction, user):
		if await valid_reaction(self, reaction, user):
			msg = re.sub("<.*?>", "<@{}>", reaction.message.content)
			msgnum = await msgcount()
			for x in range(1, msgnum):
				if msg == eval("settings.SOLARMARK_RECRUIT_MSG_{}".format(x)):
					await reaction.message.clear_reactions()
					messageinfo = await self.bot.get_channel(reaction.message.channel.id).send(eval("settings.SOLARMARK_RECRUIT_MSG_{}".format(x + 1)))
					if x < (msgnum - 1):
						await messageinfo.add_reaction('\N{White Heavy Check Mark}')
					return

	# Checks to see whether a thread exists for the given user and returns the thread ID if so
	async def thread_exist(self, member):
		for thread in self.bot.get_channel(settings.SOLARMARK_RECRUIT_CHANID).threads:
			if thread.name == "RCT-" + member.name:
				return thread.id
		return 0

	# Checks whether the user who invoked the command is authorized to do so given their roles
	async def caller_authorized(self, ctx):
		for userrole in ctx.author.roles:
			for id in settings.SOLARMARK_RECRUITER_ROLEID:
				if userrole.id == id:
					return True
		return False

	# Checks to see if target user is already in Solarmark
	async def target_in_corp(self, member):
		for userrole in member.roles:
			for id in settings.SOLARMARK_CORP_ROLEID:
				if userrole.id == id:
					return True
		return False

	# Checks to see if the target has access to the EVE Online text channel
	async def target_has_role(self, member):
		for userrole in member.roles:
			for id in settings.SOLARMARK_TARGET_ROLEID:
				if userrole.id == id:
					return True
		return False

	# Runs through the various check methods to determine whether a given recruitment invocation is valid
	async def can_recruit(self, ctx, member):
		threadid = await self.thread_exist(member)
		if not await self.caller_authorized(ctx):
			await ctx.respond("You do not have permission to use this command.", ephemeral = True)
			return False
		elif await self.target_in_corp(member):
			await ctx.respond("That user is already in the corporation.", ephemeral = True)
			return False
		elif threadid > 0:
			await ctx.respond("That user already has an active recruitment thread: <#" + str(threadid) + ">", ephemeral = True)
			return False
		elif not await self.target_has_role(member):
			await ctx.respond("That user must have the EVE Online role present on their account.", ephemeral = True)
			return False
		return True

	# Sets up right-click user command for EVE recruitment
	@discord.user_command(name = "Recruit for EVE", guild_ids = [settings.SOLARMARK_GUILDID])
	async def recruit_user(self, ctx, member: discord.Member):
		if await self.can_recruit(ctx, member):
			channel = self.bot.get_channel(settings.SOLARMARK_RECRUIT_CHANID)
			threadname = "RCT-" + member.name
			messagetext = settings.SOLARMARK_RECRUIT_MSG_1.format(
				member.id,
				*settings.SOLARMARK_LEADERSHIP_USERIDS
			)
			threadinfo = await channel.create_thread(name = threadname, auto_archive_duration = 10080, type = discord.ChannelType.public_thread)
			messageinfo = await self.bot.get_channel(threadinfo.id).send(messagetext)
			if await msgcount() > 1:
				await messageinfo.add_reaction('\N{White Heavy Check Mark}')
			if ctx.author.id in settings.SOLARMARK_LEADERSHIP_USERIDS:
				await ctx.respond("Recruitment thread created: " + threadinfo.mention, ephemeral = True)
			else:
				await ctx.respond("Recruitment thread created!", ephemeral = True)

	# Sets up /recruit command for EVE recruitment
	@discord.command(description = "Recruit for EVE. Use an @ mention to choose the user.", guild_ids = [settings.SOLARMARK_GUILDID])
	async def recruit(self, ctx, member: discord.Member):
		if await self.can_recruit(ctx, member):
			channel = self.bot.get_channel(settings.SOLARMARK_RECRUIT_CHANID)
			threadname = "RCT-" + member.name
			messagetext = settings.SOLARMARK_RECRUIT_MSG_1.format(
				member.id,
				*settings.SOLARMARK_LEADERSHIP_USERIDS
			)
			threadinfo = await channel.create_thread(name = threadname, auto_archive_duration = 10080, type = discord.ChannelType.public_thread)
			messageinfo = await self.bot.get_channel(threadinfo.id).send(messagetext)
			if await msgcount() > 1:
				await messageinfo.add_reaction('\N{White Heavy Check Mark}')
			if ctx.author.id in settings.SOLARMARK_LEADERSHIP_USERIDS:
				await ctx.respond("Recruitment thread created: " + threadinfo.mention, ephemeral = True)
			else:
				await ctx.respond("Recruitment thread created!", ephemeral = True)

	# Allows users to have the bot update the auto-archive setting for a thread
	@discord.command(description = "Update thread expiration. Accepted values are 'now', '1h', '1d', '3d', '7d'.", guild_ids = [settings.SOLARMARK_GUILDID])
	async def archive(self, ctx, when: discord.Option(str)):
		when = when.lower()
		if not await self.caller_authorized(ctx):
			await ctx.respond("You do not have permission to use this command.", ephemeral = True)
		elif not (ctx.channel.type == discord.ChannelType.public_thread or ctx.channel.type == discord.ChannelType.private_thread):
			await ctx.respond("This command can only be used inside threads.", ephemeral = True)
		elif not re.match("now|1h|1d|3d|7d", when):
			await ctx.respond("That is not a valid option for 'when', please try again.", ephemeral = True)
		else:
			match when:
				case "now":
					await ctx.respond("Thread archived!", ephemeral = True)
					await ctx.channel.edit(archived = True)
				case "1h":
					await ctx.channel.edit(auto_archive_duration = 60)
					await ctx.respond("Thread auto-archive set to 1 hour!", ephemeral = True)
				case "1d":
					await ctx.channel.edit(auto_archive_duration = 1440)
					await ctx.respond("Thread auto-archive set to 1 day!", ephemeral = True)
				case "3d":
					await ctx.channel.edit(auto_archive_duration = 4320)
					await ctx.respond("Thread auto-archive set to 3 days!", ephemeral = True)
				case "7d":
					await ctx.channel.edit(auto_archive_duration = 10080)
					await ctx.respond("Thread auto-archive set to 1 week!", ephemeral = True)

# Set the bot up
def setup(bot):
    bot.add_cog(Recruit(bot))