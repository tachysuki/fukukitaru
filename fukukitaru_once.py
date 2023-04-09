# インストールした discord.py を読み込む
import discord
import tweepy
import time
import traceback
import datetime
import random


# Discord
TOKEN = 'hogehoge12345678'



# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())
tweetid = 1601230194718621699
global screen_id
screen_id = None
chanting = ['エコエコアザラシ...エコエコオットセイ...。運勢よ〜〜〜〜カムトゥミー！','ふんにゃか〜...はんにゃか〜...。今日の運勢を示したまえーっ！']

omikuji = ['大吉','中吉','小吉','吉','末吉','凶','大凶']





user_list = [['mizugaam','みずがめ座',1601230194098212864],
            ['uozaa','うお座',1601230194882146304],
            ['ohitsujj','おひつじ座',1601230195893358592],
            ['oushiza','おうし座',1601230194987057155],
            ['futagoza','ふたご座',1601230194718621699],
            ['kanizaa','かに座',1601230195033538560],
            ['shishiza','しし座',1601592581280129027],
            ['otomez','おとめ座',1601230195725578240],
            ['tenbinza','てんびん座',1601230195108630531],
            ['sasoriza','さそり座',1601230194739580928],
            ['itezaa','いて座',1601230194613751809],
            ['yagizaa','やぎ座',1601230195075166210]]

import login

def get_user_timeline(screen_id, latestid):
    tweets = tweepy.Cursor(login.api.user_timeline, screen_name='uranai_' + user_list[screen_id][0], since_id=latestid).items()

    while tweets == None:
        tweets = tweepy.Cursor(login.api.user_timeline, screen_name='uranai_' + user_list[screen_id][0], since_id=latestid).items()

    for tweet in tweets:
        return [tweet.text, tweet.id]










# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    print('Ready to sent message')

# メッセージ受信時に動作する処理



@client.event
async def on_message(message):

    try:
        global screen_id
        #global chanting
        # メッセージ送信者がBotだった場合は無視する
        get_datas = ''
        oldtext = ''
        #screen_id = None
        print('Running...')


        #if "フクキタル" in message.content and "シラオキ様の御加護" in message.content or "フクちゃん先輩" in message.content and "シラオキ様の御加護" in message.content or "救いはないのですか...?" in message.content:

        if "フクキタル" in message.content and "シラオキ様の御加護" in message.content or "救いはないのですか...?" in message.content or "フクちゃん先輩" in message.content and "シラオキ様の御加護" in message.content:
        #if "テスト" in message.content:
                print('message:' + str(message.content))

                def check(msg):
                    return msg.author == message.author


                await message.channel.send("はい！マチカネフクキタルです！")


                while screen_id == None:
                    print("send どの星座")
                    await message.channel.send("どの星座の運勢を見たいですか？")
                    wait_message = await client.wait_for("message",check=check)
                    print('message:' + str(wait_message.content))

                    for i in range(0,13):
                        try:
                            print(user_list[i][1])
                        except:
                            pass
                        if i == 12:
                            await message.channel.send("トレーナーさん！ちゃんと入れてください！")
                            break
                        elif user_list[i][1] in str(wait_message.content):
                            print(user_list[i][1])
                            #print(str(wait_message.content))
                            screen_id = i
                            print('screen_id:' + str(screen_id))
                            await message.channel.send(user_list[screen_id][1] + "の運勢ですね！わかりました！")
                            break

                print(str(get_user_timeline(screen_id,user_list[screen_id][2])))
                get_datas = [get_user_timeline(screen_id,user_list[screen_id][2])[0],get_user_timeline(screen_id,user_list[screen_id][2])[1]]

                if oldtext == None:
                    while oldtext == None:
                        oldtext = get_user_timeline(screen_id,user_list[screen_id][2])[0]

                await message.channel.send(random.choice(chanting))
                time.sleep(3)
                await message.channel.send(get_datas[0])
                screen_id = None


        elif 'おみくじ' in message.content:
            await message.channel.send(random.choice(chanting))
            time.sleep(3)
            await message.channel.send(random.choice(omikuji) + "ですっ!")





    except:
            await message.channel.send("ふんぎゃろおおー！")
            await message.channel.send(traceback.format_exc())
            pass

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
