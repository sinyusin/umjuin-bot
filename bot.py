import os
import random
import discord
from discord import app_commands
from discord.ext import commands

# ====== 봇 기본 설정 ======
# 토큰은 코드에 직접 적지 않고, Railway의 "Variables"(환경변수)에서 가져옵니다.
# Railway에서 변수 이름을 반드시 DISCORD_TOKEN 으로 설정해야 합니다.
TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)  # prefix는 안 쓰지만 discord.py 구조상 필요


# ====================================================
# 생존자 / 감시자 / 인격특성 목록
# ====================================================

SURVIVORS = [
    "행운아", "의사", "변호사", "도둑", "정원사", "마술사", "모험가", "용병",
    "샤먼", "공군", "기계공", "포워드", "맹인", "모향사", "카우보이", "무희",
    "선지자", "납관사", "탐사원", "주술사", "야만인", "곡예사", "항해사", "바텐더",
    "우편 배달부", "묘지기", "죄수", "곤충학자", "화가", "타자", "장난감 상인", "환자",
    "심리학자", "소설가", "여자아이", "우는 광대", "교수", "골동품 상인", "작곡가", "기자",
    "항공 전문가", "치어리더", "인형사", "화재조사관", "파로 부인", "기사", "기상학자", "궁수",
    "탈출 마스터", "환등사", "투우사", "무언극 아티스트",
]

HUNTERS = [
    "공장장", "광대", "사냥터지기", "리퍼", "거미", "붉은 나비", "노란 옷의 왕", "우산의 영혼",
    "사진사", "광기의 눈", "꿈의 마녀", "울보", "재앙의 도마뱀", "블러디 퀸", "수위 26호", "사도",
    "바이올리니스트", "조각가", "박사", "파멸의 바퀴", "나이아스", "밀랍인형사", "악몽", "서기관",
    "은둔자", "나이트 워치", "오페라 가수", "파이라이트", "시공의 그림자", "저름발이 판", "훌라발루",
    "잡화상", "당구 선수", "여왕벌", "치과의사", "마음의 짐승",
]

PERSONALITY_TRAITS = [
    "3시",
    "6시",
    "9시",
    "12시",
]


# ====== 봇이 켜졌을 때: 슬래시 명령어 동기화 ======
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"슬래시 명령어 {len(synced)}개 동기화 완료")
    except Exception as e:
        print(f"동기화 실패: {e}")
    print(f"{bot.user} 로 로그인 완료! 봇이 작동 중입니다.")


def pick_and_format(name, choices):
    if not choices:
        return f"{name} 목록이 비어있어요! 코드 안에 목록을 채워주세요."
    result = random.choice(choices)
    return f"🎲 {name}: **{result}**"


# ====== 생존자 뽑기 ======
@bot.tree.command(name="생존자", description="생존자 목록 중 하나를 랜덤으로 뽑아줍니다")
async def pick_survivor(interaction: discord.Interaction):
    await interaction.response.send_message(pick_and_format("생존자", SURVIVORS))


# ====== 감시자 뽑기 ======
@bot.tree.command(name="감시자", description="감시자 목록 중 하나를 랜덤으로 뽑아줍니다")
async def pick_hunter(interaction: discord.Interaction):
    await interaction.response.send_message(pick_and_format("감시자", HUNTERS))


# ====== 인격특성 뽑기 ======
@bot.tree.command(name="특성", description="인격특성 목록 중 하나를 랜덤으로 뽑아줍니다")
async def pick_trait(interaction: discord.Interaction):
    await interaction.response.send_message(pick_and_format("인격특성", PERSONALITY_TRAITS))


# ====== 여기 아래에 새로운 슬래시 명령어를 계속 추가하면 됩니다 ======
# 예시 템플릿:
#
# @bot.tree.command(name="명령어이름", description="설명")
# async def 함수이름(interaction: discord.Interaction):
#     await interaction.response.send_message("여기에 원하는 동작 작성")


# ====== 봇 실행 ======
bot.run(TOKEN)
