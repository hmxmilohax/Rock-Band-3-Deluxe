# Rock-Band-3-Deluxe

![Header Image](dependencies/header.png)

# Table of Contents  
- [Rock-Band-3-Deluxe](#rock-band-3-deluxe)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
  - [Features](#features)
    - [Quality of Life](#quality-of-life)
    - [Authoring](#authoring)
    - [Additional Modifications](#additional-modifications)
  - [Setup](#setup)
    - [Actions](#actions)
    - [Repo-Setup](#repo-setup)
  - [Install](#install)
    - [Xenia-Emulator](#xenia-emulator)
    - [RPCS3-Emulator](#rpcs3-emulator)
    - [PS3-Hardware](#ps3-hardware)
    - [Xbox](#xbox)
  - [Optional-rb3\_plus-Keys-Upgrades](#optional-rb3_plus-keys-upgrades)
  - [Optional-Install-Custom-Highways](#optional-install-custom-highways)
  - [Songs](#songs)
  - [Dependencies](#dependencies)

# Introduction

This Repo contains everything you need to build an ark for Rock Band 3 Deluxe for PS3 or Xbox 360. For Wii, see the [Wii Branch](https://github.com/hmxmilohax/rock-band-3-deluxe/tree/wii)

## Features

### Quality of Life
* Max song limit increased to 8000. Above 5000 can lead to instability issues, use with caution.
* Song select ambient noise modifier, default disabled
* New menu, "RB3DX Menu", in game for additional modifications
* Selectable song speed and track speed by 5% increments
* Selectable venue framerate up to 60fps
* Selectable venues, including a "Black Venue" with decreased load times and system load
* Fast start executable modification by ihatecompvir
* Additional intro skip scripting to load the main menu by default and automatically start loading installed content
* Press select to restart the section in practice mode
* Default difficulty on first load is Expert
* Song title always visible modifier
* Keys on Guitar unlocked without meeting requirements
* Manual calibration adjusts by 1ms instad of 5ms


### Authoring
* Autoplay modifier for chart demos
* Gameplay watermarks to deter abuse of autoplay including -
    * Disabling autosave
    * Replacing endgame percentage with `BOT`
    * Manipulating MTV Overlay
* Cycle camera menu button - available in-game when autoplay is enabled
* Rock Revolution drums register as Pro Keys on PS3/RPCS3, to allow easy demos for pro instruments
* Guitar Hero World Tour drums register as Pro Guitar/Bass on PS3/RPCS3, to allow easy demos for pro instruments

### Additional Modifications
* Selectable colors per fret/note/sustain (It works on Pro Drums/non-Pro Keys too!)
* Selectable Overshell colors
* Huge variety of custom song sources supported
* All official exports, DLC, and RBN sorted into individual sources
* Auto activating drum modifier (no fills mode)
* Translations for Spanish, French, German
* Post processing toggle - disables/reenables post processing in-game, or in menus
* Screensaver mode - remove UI elements from menus to view the background vingette unobstructed (it will softlock your game, so be careful!)
* Nice (69%) and Awesome Choke (98-99%) callouts on solo completion
* New main menu music pulled from other Rock Band titles
* No crowd modifier
* No whammy effect modifier
* No sustain trails modifier
* Rock Band 2 Sustain look modifier
* Upgrades/fixes for tons of songs from [rb3_plus](https://github.com/rjkiv/rb3_plus)
* Compatibility with [RB3Enhanced](https://github.com/RBEnhanced/RB3Enhanced)
* Fast start, Song Blacklist, UGC Demo, Anti Debugger patches from [RB3Enhanced](https://github.com/RBEnhanced/RB3Enhanced) Embedded directly into DX binaries.

## Setup

NOTE: You WILL need a modded/hacked console to play this mod on console. I hope this is clear

### Actions

There are now pre compiled ARK files available in many flavors in the [Actions](https://github.com/hmxmilohax/rock-band-3-deluxe/actions) tab of this repo, as well as the [Nightly](https://nightly.link/hmxmilohax/rock-band-3-deluxe/workflows/build/main) link. These are ready to install files for RB3DX per platform. These arks have the following pre-built parameters.

* RB3DX-*platform*-Base - The default build of Rock Band 3 Deluxe
* RB3DX-*platform*-original-mids - Rock Band 3 Deluxe, but without any harmonies or chart updates
* RB3DX-*platform*-keys - A build of Rock Band 3 Deluxe with included additional keys upgrades from [rb3_plus](https://github.com/rjkiv/rb3_plus)
* RB3DX-PS3-stock-instrument-mapping - A build of Rock Band 3 Deluxe where GHWT and Rock Revolution kits on PS3 are restored to their correct controller mapping. Only useful if you have either of these two instruments and are playing on PS3 real hardware.

If using pre built actions, skip down to the [Install](#install) section of this readme and assume any mention of `_build` is the contents of your zip file you downloaded from the Actions tab.

### Repo-Setup
Setting up the Rock Band 3 Deluxe repo for the first time is meant to be as easy as possible.
As well, it is designed to allow you to automatically receive updates as the repo is updated.

Simply go to the [Releases](https://github.com/hmxmilohax/rock-band-3-deluxe/releases) of this repo and grab the `_init_repo` script for your platform. Currently there are .bat files for Windows and .sh files for linux, as well as a specific branch for Wii.

Included on the release page for ease of install are a couple dependencies, [Git for Windows](https://gitforwindows.org/), and [Dot Net 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime).
Git is required for you to take advantage of auto updating via github pulls. Dot Net is required to build an ARK/HDR file, the archive format the game needs to run. You cannot run any deluxe title without building an ark first.

In addition to this, you will also need to download Python in order to utilize the provided user scripts. These scripts were written and tested using Python 3.9, so it's highly recommended to get that version of Python or newer.

You can setup git with all default options, same with dot net.

Once the dependencies are installed, run `_init_repo.bat` in an **empty folder**. git will pull the repo and make sure you are completely up to date.

From then on simply run the build .py corresponding to the platform you are building for. This script will pull the repo again for updates, and build the ARK for you and spit it out in `\_build\xbox\gen` or `\_build\ps3\USRDIR\gen`

## Install

### Xenia-Emulator

To install on Xenia, copy your vanilla Xbox 360 1.0 arks to `\_build\xbox\gen`

then just navigate to `user_scripts` and run `build_xenia.py` to automatically build and run Rock Band 3 Deluxe.

### RPCS3-Emulator

**NOTE: Do not overwrite any disc files for your main game. DX is not made to overwrite the disc 1.0 vanilla files. DX goes in the location that updates are installed to on the PS3**

To install on rpcs3, copy all files/folders in `_build/ps3/` to `/dev_hdd0/game/BLUS30463/`

If the folder does not exist, create it. The game will need the included .bin file, and a built .ark/.hdr to function. The folder format in `/_build/ps3` matches how it should be installed.

Overwrite files if asked.

Run the build script again to pull any new updates committed to the repo and rebuild a new ark/hdr.

### PS3-Hardware

**NOTE: You WILL need a modded/hacked console to play this mod on console. I hope this is clear**

**NOTE: Do not overwrite any disc files for your main game. DX is not made to overwrite the disc 1.0 vanilla files. DX goes in the location that updates are installed to on the PS3**

To install on real PS3, you will have to install vanilla patch 1.05 on your ps3 first to register the update in your system.

Next, copy all files/folders in `_build/ps3/` to `/dev_hdd0/game/BLUS30463/`

If the folder does not exist, you have not installed vanilla patch 1.05. You need to do this first. The game will need the included .bin file, and a built .ark/.hdr to function. The folder format in `/_build/ps3` matches how it should be installed.

Overwrite files if asked.

Run the build script again to pull any new updates committed to the repo and rebuild a new ark/hdr.

### Xbox

**NOTE: You WILL need a modded/hacked console to play this mod on console. I hope this is clear**

On Xbox, copy the gen folder and the xex from `_build/xbox/` to the same location your base copy of Rock Band 3 lives.

If installing for the first time, make sure you rename the vanilla `default.xex` to `default_vanilla.xex` for safety.

Make sure you clear your song cache, as well as your system cache.

To clear song cache, navigate to `System Settings>Storage>Rock Band 3` and delete the song cache.

To clear system cache, navigate to `System Settings>Storage` and press Y to clear the system cache.

Also make sure to `disable` any enabled updates for Rock Band 3 in Aurora. Rock Band 3 Deluxe rolls TU5 into its base installation.

If you are also running [RB3Enhanced](https://github.com/RBEnhanced/RB3Enhanced), grab the optional folders in `/_build/_optional-xbox-rb3e-rawfiles/` and place the `config` and `ui` folders next to the `gen` folder on your Xbox.

Run the build script again to pull any new updates committed to the repo and rebuild a new ark/hdr.

## Optional-rb3_plus-Keys-Upgrades

[rb3_plus](https://github.com/rjkiv/rb3_plus) features optional key upgrades that you can install alongside RB3DX fairly easily. These upgrades include new audio files (moggs) for the upgraded songs. These take up additional file size and generally are a generation removed from the original audio mix with additional processing, but can be a great addition for any keys player.

You can simply download a build of Rock Band 3 Deluxe containing these upgrades from the [Actions](https://github.com/hmxmilohax/rock-band-3-deluxe/actions) tab of this repo.

## Optional-Install-Custom-Highways

This repo also supports the import of custom highways and groove/spotlights via the use of a bat script.

RB3DX includes a variety of custom highways by default, available via the "RB3DX Menu", but you can add your own with the following steps.

Simply drag in a .jpg/.png/.bmp into the `highways` folder in the "custom_textures" folder, then run `process_textures_highway.py`.

Or, drag in a .jpg/.png/.bmp into the `spotlights` folder in the "custom_textures" folder, then run `process_textures_spotlight.py`.

This will size your images accordingly (supports arbitrary resolutions), and convert them to the proper format for rb3 to read. Spotlights will be set to 50% opacity.

You will need to run the build script to again to create your new ARK and reinstall RB3DX to your desired platform.


## Songs

You can find song packs compatible with all Rock Band titles for both platforms on the [Spreadsheet](https://docs.google.com/spreadsheets/d/1-3lo2ASxM-3yVr_JH14F7-Lc1v2_FcS5Rv_yDCANEmk/edit#gid=0).

You can also use [Onyx Music Game Toolkit](https://github.com/mtolly/onyxite-customs) to generate your own custom song packs for Rock Band games.

## Dependencies

[Git for Windows](https://gitforwindows.org/) - CLI application to allow auto updating rb3dx repo files

[Dot Net 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime) - Needed to run ArkHelper

[Mackiloha](https://github.com/PikminGuts92/Mackiloha) - ArkHelper for building Rock Band 3 ARK - Superfreq for building .bmp_xbox highway images

[swap_rb_art_bytes.py](https://github.com/PikminGuts92/re-notes/blob/master/scripts/swap_rb_art_bytes.py) - py script for converting xbox images to ps3

[dtab](https://github.com/mtolly/dtab) - For serializing Rock Band dtb files

[python](https://www.python.org/downloads/) - for overall user script functionality (NOTE: 3.9 or newer is highly recommended!)
