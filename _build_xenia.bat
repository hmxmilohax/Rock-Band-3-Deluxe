git pull https://github.com/hmxmilohax/rock-band-3-deluxe main
"%~dp0\dependencies/arkhelper" dir2ark "%~dp0\_ark" "%~dp0\_xenia\gen" -n "patch_xbox" -e -v 6
"%~dp0\_xenia\xenia_canary" "%~dp0\_xenia\default.xex"
pause