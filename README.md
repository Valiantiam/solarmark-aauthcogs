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
`thread.py` | Add a context menu for recruiters to right click on a user and create a private recruitment thread, auotmaically bringing in the recruit and all recruiters.

## How to Install
*(Assumes a docker environment and does not use correct standards for installing. Really you/me should publish this to pypi.)*

1. Add `git+https://github.com/Valiantiam/solarmark-aauthcogs.git` to your requirements.txt
2. Configure your AA settings (`local.py`) as follows:
    - Add `'solarmark_aauthcogs',` to 'INSTALLED_APPS'
    - All below settings:
    
## Settings
Setting | Default | Description
--- | --- | ---
`SOLARMARK_RECRUIT_CHANID` | ` ` | ID of the channel you want threads created in.
`SOLARMARK_RECRUIT_ROLEID` | ` ` | ID of the discord role you want to allow to use the command.
`SOLARMARK_RECRUIT_MSG` | ` ` | The Message that is posted to the thread on creation.
