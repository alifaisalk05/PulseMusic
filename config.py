# Copyright (c) 2025 @SUDEEPBOTS <HellfireDevs>
# Location: delhi,noida
#
# All rights reserved.
#
# This code is the intellectual SUDEEPBOTS.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: sudeepgithub@gmail.com

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Telegram API Setup
API_ID = int(getenv("API_ID")) if getenv("API_ID") else None
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_USERNAME = getenv("BOT_USERNAME")

# Database & Administration
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID")) if getenv("LOGGER_ID") else None
OWNER_ID = int(getenv("OWNER_ID")) if getenv("OWNER_ID") else None

# Limits & Durations
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "0"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "0"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "0"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "0"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "0"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "0"))

# Bot Behavior
COMMAND_HANDLER = getenv("COMMAND_HANDLER", "").split() + [""]
RENDER = getenv("RENDER", "false").lower() == "true"
PING_URL = getenv("PING_URL")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "false").lower() == "true"
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "true").lower() == "true"
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "0"))

# Hosting & Repositories
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
GIT_TOKEN = getenv("GIT_TOKEN")

# Support Channels
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")
SUPPORT_CHAT = getenv("SUPPORT_CHAT")

# Spotify & External APIs
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")
BASE_URL = getenv("BASE_URL")
API_KEY = getenv("API_KEY")

# Pyrogram Sessions
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# State & Runtime Caches
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

# UI & Banner URLs
START_IMG_URL = getenv("START_IMG_URL")
PING_IMG_URL = getenv("PING_IMG_URL")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL")
STATS_IMG_URL = getenv("STATS_IMG_URL")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL")
STREAM_IMG_URL = getenv("STREAM_IMG_URL")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL")


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

VALID_EMOJII = ["🔥", "💋", "🥺", "😒", "💖", "💘", "💕", "✨", "🥰", "🍌", "💔", "😓", "🫧"]

EFFECT_IDS = [
    5046509860389126442,
    5107584321108051014,
    5104841245755180586,
    5159385139981059251,
]
