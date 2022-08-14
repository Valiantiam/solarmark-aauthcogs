# solarmark-aauthcogs
AAuth Cogs for Solarmark

> **Warning** <br>
> This is built for Solarmark specifically. It is not guaranteed to work in any environment other than our own, and may have hard-coded values for some settings depending on our needs. Additionally, this app is in constant unpredictable development and may often not be in a working state. **If you aren't us, you probably shouldn't use this.**

## Features
A collection of cogs for use by the Solarmark gaming community and it's eve online leadership.

![image](https://user-images.githubusercontent.com/5394853/180701861-902796c6-7e01-46bc-bb50-75606287bd7f.png)

### Current cogs
Cog |  Purpose
--- | ---
`thread.py` | Add a right-click context menu and slash command for recruiters to create a private recruitment thread, automatically bringing in the recruit and all recruiters. Also handles thread archival settings via slash command.

## How to Install
*(Assumes a docker environment and does not use correct standards for installing. Really you/me should publish this to pypi.)*

1. Add `git+https://github.com/Valiantiam/solarmark-aauthcogs.git` to your requirements.txt
2. Configure your AA settings (`local.py`) as follows:
    - Add `'solarmark_aauthcogs',` to 'INSTALLED_APPS'
    - All below settings:
    
## Settings
Setting | Default | Description
--- | --- | ---
`SOLARMARK_GUILDID` | ` ` | ID of the Discord server in which the bot will be operating.
`SOLARMARK_RECRUIT_CHANID` | ` ` | ID of the channel you want the threads created in.
`SOLARMARK_TARGET_ROLEID` | ` ` | List of Role IDs, one of which must be present on the target to be valid for recruitment (must have visibility of SOLARMARK_RECRUIT_CHANID text channel).
`SOLARMARK_CORP_ROLEID` | ` ` | List of Role IDs that you don't want able to be recruited (such as those already in corp).
`SOLARMARK_RECRUITER_ROLEID` | ` ` | List of Role IDs that you want to be able to use the recruit action.
`SOLARMARK_LEADERSHIP_USERIDS` | ` ` | List of User IDs to include in the initial thread message (and therefore be automatically pulled into each thread).
`SOLARMARK_RECRUIT_MSG_1` | ` ` | The message that is posted to the thread on creation (also handles who is invited to the thread through the use of @mentions).
