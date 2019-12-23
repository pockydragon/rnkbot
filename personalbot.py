# Libraries used
import discord
import os
import random
import math

# External libraries from pathing
from discord.ext import commands

# Header Details
__author__ = 'William Kuang'
__copyright__ = 'Copyright 2019, Project RenektonBot'
__credits__ = 'William Kuang'
__version__ = '1.0'
__maintainer__ = 'William Kuang'
__email__ = 'william.kuang9@gmail.com'
__status__ = 'In Progress'

# Discord Bot Token
token = "NjU4MjMyODMwMzc5MTYzNzU4.Xf8xmA.llNwyTn5eyODHoTcUC4p_NZI254"

# Creates prefix for calling commands
bot = commands.Bot(command_prefix='!')

# Event Pass Token Constants
CONSTANT_SR_TOKEN_WIN = 12
CONSTANT_SR_TOKEN_LOSE = 8
CONSTANT_ARAM_TOKEN_WIN = 8
CONSTANT_ARAM_TOKEN_LOSE = 4

# Confirms that the bot has successfully connected to the Discord API.
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Calculates the potential max wins or losses needed to reach a desired amount based on
# the current amount of tokens for ARAM.
@bot.command(name='token_aram')
async def token_calculate_aram(self, initial: int, final: int):
  if isinstance(initial, int) or isinstance(final, int):
    if initial <= final:
      difference = final - initial
      gains1 = difference/CONSTANT_ARAM_TOKEN_WIN
      gains2 = difference/CONSTANT_ARAM_TOKEN_LOSE
      gains1 = math.ceil(gains1)
      gains2 = math.ceil(gains2)
      embed=discord.Embed(title="Token Calculation (ARAM)", description="You need to win this many games max in order to reach your goal:")
      embed.add_field(name="Wins", value=gains1, inline=True)
      embed.add_field(name="Losses", value=gains2, inline=True)
      embed.add_field(name="Current", value=initial, inline=True)
      embed.add_field(name="Goal", value=final, inline=True)
      embed.set_footer(text="Note: This is only the theoretical max wins or losses you need to reach your target.")
      await self.send(embed=embed)

# Calculates the potential max wins or losses needed to reach a desired amount based on
# the current amount of tokens for Summoner's Rift.
@bot.command(name='token_sr')
async def token_calculate_sr(self, initial1: int, final1: int):
  if isinstance(initial, int) or isinstance(final, int):
    if initial1 <= final1:
      diff = final1 - initial1
      gain1 = diff/CONSTANT_SR_TOKEN_WIN
      gain2 = diff/CONSTANT_SR_TOKEN_LOSE
      gain1 = math.ceil(gain1)
      gain2 = math.ceil(gain2)
      embed=discord.Embed(title="Token Calculation (Summoner's Rift)", description="You need to win this many games max in order to reach your goal:")
      embed.add_field(name="Wins", value=gain1, inline=True)
      embed.add_field(name="Losses", value=gain2, inline=True)
      embed.add_field(name="Current", value=initial1, inline=True)
      embed.add_field(name="Goal", value=final1, inline=True)
      embed.set_footer(text="Note: This is only the theoretical max wins or losses you need to reach your target.")
      await self.send(embed=embed)


bot.run(token)
