import discord
import datetime as DT
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Game
import urllib
from urllib import parse
import json

BotToken = "토큰을 입력하세요"
client = discord.Client()
NowToday = str(DT.datetime.now())

@client.event
async def on_ready():
    print(NowToday + "  << {0.user} >> 구동이 시작되었습니다.".format(client))
    StatsText = discord.Game("{}개의 서버에서 작동".format(len(client.guilds)))            
    await client.change_presence(status=discord.Status.dnd, activity=StatsText)


@client.event
async def on_message(message):
        if message.author == client.user:
            return

        if message.content == "`도움말" or message.content == "`help":
            HelpEmbed = discord.Embed(color=0xfef47a)
            HelpEmbed.set_author(name="명령어",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
            HelpEmbed.add_field(name="몬스터 정보", value="``몬스터 [몬스터명]`", inline=True)
            HelpEmbed.add_field(name="장식주 정보", value="``장식주 [장식주명]`", inline=True)
            HelpEmbed.add_field(name="호석 정보", value="``호석 [호석명]`", inline=True)
            HelpEmbed.add_field(name="몬스터 종류정보", value="``몬스터종류 [종류명]`", inline=True)            
            await message.channel.send(embed=HelpEmbed)

        if message.content.startswith('`몬스터'):
            if message.content.split()[0] == ('`몬스터'):
                try:
                    with open('data/mh/monsterdata.json', encoding='utf-8') as MonsterData:
                        Monsterload = json.load(MonsterData)
                    InputMsg = message.content.split()[1:]
                    InputMsg2 = (" ".join(InputMsg))
                    ErrorNum = 0
                    for Monster in Monsterload:
                        if InputMsg2 == Monster['name']:
                            MonsterName = Monster['name']
                            MonsterImage = Monster['image']
                            MonsterBook = Monster['book']
                            MonsterGubun = Monster['gubun']
                            MonsterNick = Monster['nick']
                            MonsterType = Monster['type']
                            MonsterWeaknessFire = Monster['weakness']['fire']
                            MonsterWeaknessWater = Monster['weakness']['water']
                            MonsterWeaknessThunder = Monster['weakness']['thunder']
                            MonsterWeaknessIce = Monster['weakness']['ice']
                            MonsterWeaknessDragon = Monster['weakness']['dragon']
                            MonsterDebuffPoison = Monster['debuff']['poison']
                            MonsterDebuffSleed = Monster['debuff']['sleep']
                            MonsterDebuffParalysis = Monster['debuff']['paralysis']
                            MonsterDebuffExplosion = Monster['debuff']['explosion']
                            MonsterDebuffFaint = Monster['debuff']['faint']
                            MonsterWeaknessTotal = ("불　 > " + str(MonsterWeaknessFire) + "\n물　 > " + str(MonsterWeaknessWater) + "\n번개 > " + str(MonsterWeaknessThunder) + "\n얼음 > " + str(MonsterWeaknessIce) + "\n용 　> " + str(MonsterWeaknessDragon) + "\n")
                            MonsterDebuffTotal = ("독 　> " + str(MonsterDebuffPoison) + "\n수면 > " + str(MonsterDebuffSleed) + "\n마비 > " + str(MonsterDebuffParalysis) + "\n폭발 > " + str(MonsterDebuffExplosion) +  "\n기절 > " + str(MonsterDebuffFaint) + "\n")
                            MonsterEmbed = discord.Embed(title=MonsterName, color=0xfef47a)
                            MonsterEmbed.set_author(name="몬스터정보",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
                            MonsterEmbed.set_thumbnail(url=MonsterImage)
                            MonsterEmbed.add_field(name="■종류", value=MonsterType, inline=True)
                            MonsterEmbed.add_field(name="■별명", value=MonsterNick, inline=True)
                            MonsterEmbed.add_field(name="■구분", value=MonsterGubun, inline=True)
                            MonsterEmbed.add_field(name="■속성약점", value=MonsterWeaknessTotal, inline=True)
                            MonsterEmbed.add_field(name="■상태이상", value=MonsterDebuffTotal, inline=True)
                            MonsterEmbed.set_image(url=MonsterBook)
                            await message.channel.send(embed=MonsterEmbed)
                        else:
                            if InputMsg2 == "":
                                await message.channel.send("사용법 : ``몬스터 [몬스터명]`")
                                break
                            Errorarr = []
                            ErrorNum = ErrorNum + 1
                            if ErrorNum == 71:
                                for MonsterError in Monsterload:
                                    if InputMsg2 in MonsterError['name']:
                                        Errorarr.append("`" + MonsterError['name'] + "`")
                                ErrorarrJoin = (" ".join(Errorarr)) 
                                MonsterEmbed = discord.Embed(color=0xfef47a)
                                MonsterEmbed.set_author(name="검색오류",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
                                MonsterEmbed.add_field(name="■비슷한 몬스터명", value=ErrorarrJoin, inline=True)
                                await message.channel.send(embed=MonsterEmbed)
                except Exception:
                    await message.channel.send("사용법 : ``몬스터 [몬스터명]`")
        TypeTotal = []
        if message.content.startswith('`몬스터종류'):
            if message.content.split()[0] == ('`몬스터종류'):
                try:
                    with open('data/mh/monsterdata.json', encoding='utf-8') as MonsterData:
                        Monsterload = json.load(MonsterData)
                    InputMsg = message.content.split()[1:]
                    InputMsg2 = (" ".join(InputMsg))
                    for Monster in Monsterload:
                        if InputMsg2 == Monster['type']:
                            MonsterName = Monster['name']
                            MonsterType = Monster['type']
                            MonsterWeaknessFire = Monster['weakness']['fire']
                            MonsterWeaknessWater = Monster['weakness']['water']
                            MonsterWeaknessThunder = Monster['weakness']['thunder']
                            MonsterWeaknessIce = Monster['weakness']['ice']
                            MonsterWeaknessDragon = Monster['weakness']['dragon']
                            MonsterDebuffPoison = Monster['debuff']['poison']
                            MonsterDebuffSleed = Monster['debuff']['sleep']
                            MonsterDebuffParalysis = Monster['debuff']['paralysis']
                            MonsterDebuffExplosion = Monster['debuff']['explosion']
                            MonsterDebuffFaint = Monster['debuff']['faint']
                            MonsterWeaknessTotal = ("불　 > " + str(MonsterWeaknessFire) + "\n물　 > " + str(MonsterWeaknessWater) + "\n번개 > " + str(MonsterWeaknessThunder) + "\n얼음 > " + str(MonsterWeaknessIce) + "\n용 　> " + str(MonsterWeaknessDragon) + "\n")
                            MonsterDebuffTotal = ("독 　> " + str(MonsterDebuffPoison) + "\n수면 > " + str(MonsterDebuffSleed) + "\n마비 > " + str(MonsterDebuffParalysis) + "\n폭발 > " + str(MonsterDebuffExplosion) +  "\n기절 > " + str(MonsterDebuffFaint) + "\n")
                            TypeTotal.append(MonsterName)
                    TypeRealTotal = ('\n'.join(TypeTotal))    
                    TypeEmbed = discord.Embed(title=MonsterType, color=0xfef47a)
                    TypeEmbed.set_author(name="몬스터종류정보",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
                    TypeEmbed.add_field(name="■몬스터명", value=TypeRealTotal, inline=True)
                    await message.channel.send(embed=TypeEmbed)
                except Exception:
                    await message.channel.send("사용법 : ``몬스터종류 [고룡종ㅣ비룡종ㅣ수룡종ㅣ아룡종ㅣ어룡종ㅣ조룡종ㅣ아수종ㅣ잔존생물]`")
    
        if message.content.startswith('`장식주'):
            if message.content.split()[0] == ('`장식주'):
                try:
                    with open('data/mh/jeweldata.json', encoding='utf-8') as JewelData:
                        Jewelload = json.load(JewelData)
                    InputMsg = message.content.split()[1:]
                    InputMsg2 = (" ".join(InputMsg))
                    ErrorNum = 0
                    for Jewel in Jewelload:
                        if InputMsg2 == Jewel['name']:
                            JewelName = Jewel['name']
                            JewelSlotLevel = Jewel['slot_level']
                            JewelRare = (Jewel['rare'])
                            JewelSkillTotal = []
                            for Jewel2 in Jewel['skills']:
                                JewelSkillName = ( "▶" + Jewel2['name'] )
                                JewelSkillTotal.append(JewelSkillName)
                                for Jewel3 in Jewel2['detail']:
                                    JewelSkillLV2= Jewel3['level']
                                    JewelSkillDescription = Jewel3['description']
                                    Jewel3Total = ("{} -> {}".format(JewelSkillLV2, JewelSkillDescription))
                                    JewelSkillTotal.append(Jewel3Total)
                            JewelSkillInfoRealTotal = ('\n'.join(JewelSkillTotal))
                            JewelEmbed = discord.Embed(title=JewelName, color=0xfef47a)
                            JewelEmbed.set_author(name="장식주정보",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
                            JewelEmbed.add_field(name="■희귀도", value=JewelRare, inline=True)
                            JewelEmbed.add_field(name="■슬롯레벨", value=JewelSlotLevel, inline=True)
                            JewelEmbed.add_field(name="■스킬정보", value=JewelSkillInfoRealTotal, inline=False)
                            await message.channel.send(embed=JewelEmbed)
                        else:
                            if InputMsg2 == "":
                                await message.channel.send("사용법 : ``장식주 [장식주명]`")
                                break
                            ErrorNum = ErrorNum + 1
                            if ErrorNum == 407:
                                Errorarr = []
                                for JewelError in Jewelload:
                                    if InputMsg2 in JewelError['name']:
                                        Errorarr.append("`" + JewelError['name'] + "`")
                                ErrorarrJoin = (" ".join(Errorarr))
                                JewelEmbed = discord.Embed(color=0xfef47a)
                                JewelEmbed.set_author(name="검색오류",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
                                JewelEmbed.add_field(name="■비슷한 장식주명", value=ErrorarrJoin, inline=True)
                                await message.channel.send(embed=JewelEmbed)
                        
                except Exception:
                    await message.channel.send("사용법 : ``장식주 [장식주명]`")
        if message.content.startswith('`장식품'):
            if message.content.split()[0] == ('`장식품'):
                try:
                    with open('data/mh/jeweldata.json', encoding='utf-8') as JewelData:
                        Jewelload = json.load(JewelData)
                    InputMsg = message.content.split()[1:]
                    InputMsg2 = (" ".join(InputMsg))
                    ErrorNum = 0
                    for Jewel in Jewelload:
                        if InputMsg2 == Jewel['name']:
                            JewelName = Jewel['name']
                            JewelSlotLevel = Jewel['slot_level']
                            JewelRare = (Jewel['rare'])
                            JewelSkillTotal = []
                            for Jewel2 in Jewel['skills']:
                                JewelSkillName = ( "▶" + Jewel2['name'] )
                                JewelSkillTotal.append(JewelSkillName)
                                for Jewel3 in Jewel2['detail']:
                                    JewelSkillLV2= Jewel3['level']
                                    JewelSkillDescription = Jewel3['description']
                                    Jewel3Total = ("{} -> {}".format(JewelSkillLV2, JewelSkillDescription))
                                    JewelSkillTotal.append(Jewel3Total)
                            JewelSkillInfoRealTotal = ('\n'.join(JewelSkillTotal))
                            JewelEmbed = discord.Embed(title=JewelName, color=0xfef47a)
                            JewelEmbed.set_author(name="장식품정보",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
                            JewelEmbed.add_field(name="■희귀도", value=JewelRare, inline=True)
                            JewelEmbed.add_field(name="■슬롯레벨", value=JewelSlotLevel, inline=True)
                            JewelEmbed.add_field(name="■스킬정보", value=JewelSkillInfoRealTotal, inline=False)
                            await message.channel.send(embed=JewelEmbed)
                        else:
                            if InputMsg2 == "":
                                await message.channel.send("사용법 : ``장식품 [장식품명]`")
                                break
                            ErrorNum = ErrorNum + 1
                            if ErrorNum == 407:
                                Errorarr = []
                                for JewelError in Jewelload:
                                    if InputMsg2 in JewelError['name']:
                                        Errorarr.append("`" + JewelError['name'] + "`")
                                ErrorarrJoin = (" ".join(Errorarr))
                                JewelEmbed = discord.Embed(color=0xfef47a)
                                JewelEmbed.set_author(name="검색오류",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
                                JewelEmbed.add_field(name="■비슷한 장식품명", value=ErrorarrJoin, inline=True)
                                await message.channel.send(embed=JewelEmbed)
                except Exception:
                    await message.channel.send("사용법 : ``장식품 [장식품명]`")
        if message.content.startswith('`호석'):
            if message.content.split()[0] == ('`호석'):
                try:
                    with open('data/mh/charmdata.json', encoding='utf-8') as CharmData:
                        Charmload = json.load(CharmData)
                    InputMsg = message.content.split()[1:]
                    InputMsg2 = (" ".join(InputMsg))
                    CharmSkillsInfo = []
                    CharmUpTotal = []
                    ErrorNum = 0
                    for Charm in Charmload:
                        if InputMsg2 == Charm['name']:
                            CharmName = Charm['name']
                            CharmMaxLevel = Charm['max_level']
                            for Charm2 in Charm['skills_info']:
                                Charmname2 = Charm2['name']
                                CharmSITotal = ("▶" + Charmname2 )
                                CharmSkillsInfo.append(CharmSITotal)
                                for Charm3 in Charm2['detail']:
                                    CharmSkillLevel = Charm3['name']
                                    CharmSkillDescription = Charm3['description']
                                    CharmSkillDetailTotal = (CharmSkillLevel + " - " + CharmSkillDescription )
                                    CharmSkillsInfo.append(CharmSkillDetailTotal)
                            for Charm4 in Charm['upgrade_info']:
                                CharmUpLevel = Charm4['level']
                                CharmUpLevelInfo = ("\nLV.{} : ".format(CharmUpLevel))
                                CharmUpTotal.append(CharmUpLevelInfo)
                                for Charm5 in Charm4['items']:
                                    CharmUpname = Charm5['name']
                                    CharmUpCount = Charm5['count']
                                    CharmUpItems = ("`{} {}개`".format(CharmUpname, CharmUpCount))
                                    CharmUpTotal.append(CharmUpItems)
                            CharmSkillALLTOTAL = ('\n'.join(CharmSkillsInfo)) 
                            CharmUPALLTOTAL = ('\t'.join(CharmUpTotal))       
                            CharmEmbed = discord.Embed(title=CharmName, color=0xfef47a)
                            CharmEmbed.set_author(name="호석정보",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
                            CharmEmbed.add_field(name="■최대레벨", value=CharmMaxLevel, inline=True)
                            CharmEmbed.add_field(name="■호석정보", value=CharmSkillALLTOTAL, inline=False)
                            CharmEmbed.add_field(name="■업그레이드재료정보", value=CharmUPALLTOTAL, inline=False)
                            await message.channel.send(embed=CharmEmbed)  
                        else:
                                if InputMsg2 == "":
                                    await message.channel.send("사용법 : ``호석 [호석명]`")
                                    break
                                Errorarr = []
                                ErrorNum = ErrorNum + 1
                                if ErrorNum == 107:
                                    for CharmError in Charmload:
                                        if InputMsg2 in CharmError['name']:
                                            Errorarr.append("`" + CharmError['name'] + "`")
                                    ErrorarrJoin = (" ".join(Errorarr)) 
                                    CharmEmbed = discord.Embed(color=0xfef47a)
                                    CharmEmbed.set_author(name="검색오류",icon_url="https://cdn.discordapp.com/attachments/778205742020558848/778995423917506600/robot-1214536_1280.png")
                                    CharmEmbed.add_field(name="■비슷한 호석명", value=ErrorarrJoin, inline=True)
                                    await message.channel.send(embed=CharmEmbed)                  
                except Exception:
                    await message.channel.send("사용법 : ``호석 [호석명]`")

client.run(BotToken)