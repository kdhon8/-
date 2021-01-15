import asyncio
import discord

client = discord.Client()

# 복사해 둔 토큰을 your_token에 넣어줍니당
token = "Nzk5MDk2Mzg2MDAzMDA5NTg2.X_-mgA.FkIr0UQSwtsVbl91nV4Y6WHryNo"

# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print("로그인 된 봇:") #화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("===========")
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("안녕하세요? 크드봇입니다")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("아직 개발 중이예요~")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
        


# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!인증'):
        channel = message.channel
        await channel.send('그 기능은 아직 개발 중이에요!')

client.run(token)
#[출처] 파이썬으로 디스코드 봇 만들기_02.간단 코드 만들기|작성자 잠냥
