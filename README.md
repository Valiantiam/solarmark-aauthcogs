# solarmark-aauthcog
AAuth Cogs for Solarmark

> **Warning** <br>
> This is built for Solarmark specifically. It is not guaranteed to work in any environment other than our own, and may have hard-coded values for some settings depending on our needs. Additionally, this app is in constant unpredictable development and may often not be in a working state. **If you aren't us, you probably shouldn't use this.**

## Features
A collection of cogs for use by the Solarmark gaming community and it's eve online leadership.

### Current cogs
Cog |  Purpose
--- | ---
`thread.py` | Add a context menu for recruiters to right click on a user and createa private recruitment thread.

## How to Install
*(Assumes a docker environment and does not use correct standards for installing. Reall you/me should publish this to pypi.)*

1. Add `git+https://github.com/Valiantiam/solarmark-aauthcog.git` to your requirements.txt
2. Configure your AA settings (`local.py`) as follows:
    - Add `'solarmark-aauthcog',` to 'INSTALLED_APPS'
    - All below settings:
    
## Settings
Setting | Default | Description
--- | --- | ---
`SOLARMARK_AAUTHCOG_THREAD_CHANID` | ` ` | ID of the channel you want threads created in.
