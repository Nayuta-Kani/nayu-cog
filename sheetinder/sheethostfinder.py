import discord
from bs4 import BeautifulSoup
soupAvailable = True
from discord.ext import commands
from __main__ import send_cmd_help
import aiohttp
import re
import requests
from .utils.menu import * #Place the menu.py in ./cogs/util. I'm using a modified version of menu.py. Original Menu.py can be found from https://github.com/Lunar-Dust/Dusty-Cogs/blob/master/menu/menu.py


class sheet:
    def __init__(self, bot):
        self.bot = bot
        self.menu = Menu(bot)

    @commands.command(pass_context=True, no_pm=False)
    async def sheet(self, oops, * ctx):
        """Sheethost sheets finder"""
        query = '+'.join(ctx)
        #await self.bot.say("Query is: " + query)
        url = "https://www.google.com/search?q="+query+"+site%3Asheet.host" #build the web adress
        #response = requests.get('https://www.google.com/search?q=site:sheet.host+'+ query +'&gbv=1&sei=YwHNVpHLOYiWmQHk3K24Cw')
        url = "https://www.google.co.in/search?q==site:sheet.host+" + query
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"lxml")
        messages = []
        choice = []
        i = 1
        maxi = len(soup.select("cite"))
        for count in soup.select("cite"):
            if not "https://sheet.host/sheet/" in count.get_text(): #If it's not a sheethost sheet link, I'll decrease the total result count
                maxi -=1
        progress = discord.Embed(description='', color = 0xFFFFF)
        progress.add_field(name="Searching for: ", value = ' '.join(ctx))
        progress.add_field(name="Progress", value="Loading...")
        reply = await self.bot.say(embed=progress)

        for item in soup.select("cite"):
            targeturl = item.get_text()
            if "https://sheet.host/sheet/" in targeturl:
                newprogress = discord.Embed(description='', color = 0xFFFFF)
                newprogress.add_field(name="Searching for: ", value = ' '.join(ctx))
                newprogress.add_field(name="Progress", value="Loading " + str(i) + " of " + str(maxi))
                reply = await self.bot.edit_message(reply, embed=newprogress) #Updates the progress
                embed = discord.Embed(title="Search Results for: " + ' '.join(ctx), description="Menu will expire after 60 seconds of inactivity", color = 0xFFFFF)
                async with aiohttp.get(targeturl) as response: #Fetches the target url from the search result
                    targetSoup = BeautifulSoup(await response.text(), "lxml")
                try:
                    title = targetSoup.find(class_="sheet-header").find("span").get("content")
                    author = targetSoup.find(itemprop="creator").find("span").get("content")
                    preview = targeturl+"/image"
                    embed.add_field(name="Title", value=title)
                    embed.add_field(name="Arranger", value=author)
                    embed.set_image(url=preview) #Because there's no suffix I need to specify it's a url
                except:
                    embed.add_field(name="Error", value = "Soup dieded")
                embed.add_field(name = "Url: ", value=item.get_text())

                embed.set_footer(text="Page " + str(i) + " of " + str(maxi) + " | Provided by SheetHost")
                i+=1
                messages.append(embed)
        await self.menu.menu(oops, 3, messages, message=reply, timeout=60)


def setup(bot):
    bot.add_cog(sheet(bot))
