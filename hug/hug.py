import discord
from discord.ext import commands
from __main__ import send_cmd_help
import re
import requests
from .utils.menu import *
import json


class hug:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=False)
    async def hug(self, ctx):
        """Send a hug!"""
        try:
            data = requests.get("https://nekos.life/api/v2/img/hug")
            response = data.json()
            try:
                member = ctx.message.mentions[0]
            except:
                embed = discord.Embed(description='', color = 0xFF0000, title="You did not mention a user! Please try again!")
                await self.bot.say(embed=embed)
                return
            embed = discord.Embed(description='', color = 0xDD67FF, title="**" + str(ctx.message.author.name) + "** is hugging **" + str(member.name) + "** OwO")
            embed.set_footer(text="Requested by " + str(ctx.message.author) + " | Provided by nekos.life")
            embed.set_image(url = response['url'])
            await self.bot.say(embed=embed)
        except:
            embed = discord.Embed(description='', color = 0xFF0000, title="Something went wrong!")
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=False)
    async def slap(self, ctx):
        """Slap someone!"""
        try:
            data = requests.get("https://nekos.life/api/v2/img/slap")
            response = data.json()
            try:
                member = ctx.message.mentions[0]
            except:
                embed = discord.Embed(description='', color = 0xFF0000, title="You did not mention a user! Please try again!")
                await self.bot.say(embed=embed)
                return
            embed = discord.Embed(description='', color = 0xDD67FF, title="**" + str(ctx.message.author.name) + "** is slapping **" + str(member.name) + "** OwO")
            embed.set_footer(text="Requested by " + str(ctx.message.author) + " | Provided by nekos.life")
            embed.set_image(url = response['url'])
            await self.bot.say(embed=embed)
        except:
            embed = discord.Embed(description='', color = 0xFF0000, title="Something went wrong!")
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=False)
    async def kiss(self, ctx):
        """Send a kiss to someone!"""
        try:
            data = requests.get("https://nekos.life/api/v2/img/kiss")
            response = data.json()
            try:
                member = ctx.message.mentions[0]
            except:
                embed = discord.Embed(description='', color = 0xFF0000, title="You did not mention a user! Please try again!")
                await self.bot.say(embed=embed)
                return
            embed = discord.Embed(description='', color = 0xDD67FF, title="**" + str(ctx.message.author.name) + "** is kissing **" + str(member.name) + "** OwO")
            embed.set_footer(text="Requested by " + str(ctx.message.author) + " | Provided by nekos.life")
            embed.set_image(url = response['url'])
            await self.bot.say(embed=embed)
        except:
            embed = discord.Embed(description='', color = 0xFF0000, title="Something went wrong!")
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=False)
    async def pat(self, ctx):
        """Pat someone!"""
        try:
            data = requests.get("https://nekos.life/api/v2/img/pat")
            response = data.json()
            try:
                member = ctx.message.mentions[0]
            except:
                embed = discord.Embed(description='', color = 0xFF0000, title="You did not mention a user! Please try again!")
                await self.bot.say(embed=embed)
                return
            embed = discord.Embed(description='', color = 0xDD67FF, title="**" + str(ctx.message.author.name) + "** is patting **" + str(member.name) + "** OwO")
            embed.set_footer(text="Requested by " + str(ctx.message.author) + " | Provided by nekos.life")
            embed.set_image(url = response['url'])
            await self.bot.say(embed=embed)
        except:
            embed = discord.Embed(description='', color = 0xFF0000, title="Something went wrong!")
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=False)
    async def smug(self, ctx):
        """Be smug!"""
        try:
            data = requests.get("https://nekos.life/api/v2/img/smug")
            response = data.json()
            try:
                member = ctx.message.mentions[0]
            except:
                embed = discord.Embed(description='', color = 0xFF0000, title="You did not mention a user! Please try again!")
                await self.bot.say(embed=embed)
                return
            embed = discord.Embed(description='', color = 0xDD67FF, title="**" + str(ctx.message.author.name) + "** is smug at **" + str(member.name) + "** OwO")
            embed.set_footer(text="Requested by " + str(ctx.message.author) + " | Provided by nekos.life")
            embed.set_image(url = response['url'])
            await self.bot.say(embed=embed)
        except:
            embed = discord.Embed(description='', color = 0xFF0000, title="Something went wrong!")
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=False)
    async def poke(self, ctx):
        """Send a poke!"""
        try:
            data = requests.get("https://nekos.life/api/v2/img/poke")
            response = data.json()
            try:
                member = ctx.message.mentions[0]
            except:
                embed = discord.Embed(description='', color = 0xFF0000, title="You did not mention a user! Please try again!")
                await self.bot.say(embed=embed)
                return
            embed = discord.Embed(description='', color = 0xDD67FF, title="**" + str(ctx.message.author.name) + "** is poking **" + str(member.name) + "** OwO")
            embed.set_footer(text="Requested by " + str(ctx.message.author) + " | Provided by nekos.life")
            embed.set_image(url = response['url'])
            await self.bot.say(embed=embed)
        except:
            embed = discord.Embed(description='', color = 0xFF0000, title="Something went wrong!")
            await self.bot.say(embed=embed)

def setup(bot):
    bot.remove_command('hug')
    bot.add_cog(hug(bot))
