"""
Hooking into the auth system
"""

# Alliance Auth
from allianceauth import hooks

# Only register the cog when aadiscordbot is installed
if allianceauth_discordbot_active():
    @hooks.register("discord_cogs_hook")
    def register_cogs():
        """
        Registering our discord cogs
        """

        return [
            "sp;ar,arl=aaitjcog.thread",
        ]
