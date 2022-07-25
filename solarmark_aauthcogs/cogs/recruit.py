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
		for thread in self.bot.get_channel(600408850658623498).threads:
			if thread.name == "RCT-" + member.name:
				return True
		return False

	async def caller_authorized(self, ctx):
		for userrole in ctx.author.roles:
			if userrole.id == 998839417093488654:
				return True
		return False

	async def target_not_in_corp(self, member):
		for userrole in member.roles:
			if userrole.id == 998968946365583430:
				return False
		return True

	async def can_recruit(self, ctx, member):
		if not await self.caller_authorized(ctx):
			await ctx.respond("You do not have permission to use this command.", ephemeral = True)
			return False
		if not await self.target_not_in_corp(member):
			await ctx.respond("That user is already in the corporation.", ephemeral = True)
			return False
		if await self.thread_exist(member):
			await ctx.respond("That user already has an active recruitment thread.", ephemeral = True)
			return False
		return True

	@discord.user_command(name="Recruit for EVE")
	async def recruit(self, ctx, member: discord.Member):
		if await self.can_recruit(ctx, member):
			channel = self.bot.get_channel(600408850658623498)
			threadname = "RCT-" + member.name
			messagetext = "\u200b\n\nWelcome <@{}>!\n\nThis is your private thread for moving through the recruitment process with Solarmark. We are happy to have you here and explore having you join the corp!\n\n<@{}> is our CEO.\n<@{}> and <@{}> are our recruitment directors.\n\nWe’re here to answer any questions you have about joining Solarmark.\n\nThe first step in this process will be to set yourself up in AAuth, which is our corporation management tool. This will allow us to take a look at your character(s) and also manages our other services that you'll interact with if you end up joining us.\n\n1. Go to https://aauth.solarmark.io/ and log in with your main character. Provide a valid email as well.\n2. Once logged in, on the dashboard, use the 'Add Character' button to add all your related characters.\n3. Once all characters are added, go to https://aauth.solarmark.io/member-audit/launcher and make sure all your characters are added there as well. If they are not, please manually add them via the 'Register' button.\n4. Still in Member Audit, confirm that all characters have the small white eye icon next to their name. If they do not, click the yellow eye button below their portrait. This gives Solarmark leadership access to view those characters.\n5. Go to https://aauth.solarmark.io/services/ and click the activate button for the Discord service. This will get your Discord account linked to your AAuth account for automated role management.\n\nIf you run into any issues, please message us here and we'll work through them with you.\n\nOnce the AAuth steps above are complete, our process generally is the following:\n1. Q/A back and forth here.\n2. Character(s) background check.\n3. Voice Comms Interview.\n4. Acceptance into corp, assuming everyone is a happy fit.\n\nLooking forward to getting to know each other, feel free to ask any questions and we will take turns responding as available, o7!".format(
				member.id,
				72091276689801216,
				72091276689801216,
				72091276689801216
			)
			threadinfo = await channel.create_thread(name=threadname, auto_archive_duration=10080, type=discord.ChannelType.public_thread)
			await bot.get_channel(threadinfo.id).send(messagetext)
			await ctx.respond("Recruitment thread created!", ephemeral = True)

bot.run(os.getenv('DISCORD_TOKEN'))

				member.id,
				97032350247972864,
				97049182073786368,
				72091276689801216
			)
			threadinfo = await channel.create_thread(name=threadname, auto_archive_duration=10080, type=discord.ChannelType.private_thread)
			await self.bot.get_channel(threadinfo.id).send(messagetext)
			await ctx.respond("Recruitment thread created!", ephemeral = True)

# Set the bot up
def setup(bot):
    bot.add_cog(Recruit(bot))