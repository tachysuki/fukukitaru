# インストールした discord.py を読み込む
import discord
import tweepy
import time
import traceback
import datetime
import random

# Discord
TOKEN = 'hogehoge12345678'

#Twitter
API_KEY = "hogehoge12345678"
API_SECRET_KEY = "hogehoge12345678"
ACCESS_TOKEN = "12345678-hogehoge"
ACCESS_TOKEN_SECRET = "hogehoge12345678"

# 接続に必要なオブジェクトを生成
client = discord.Client()
tweetid = 1601230194718621699
global isfirstloop
isfirstloop = True
global screen_id
screen_id = None
chanting = ['エコエコアザラシ...エコエコオットセイ...。運勢よ〜〜〜〜カムトゥミー！','ふんにゃか〜...はんにゃか〜...。今日の運勢を示したまえーっ！']



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

def get_user_timeline(screen_id):
    api = twitter_api()
    #tweets = tweepy.Cursor(api.user_timeline, screen_name='uranai_' + user_list[screen_id][0] , since_id=latestid).items()
    tweets = tweepy.Cursor(api.user_timeline, screen_name='uranai_' + user_list[screen_id][0], since_id=user_list[screen_id][2]).items()
    #tweets = tweepy.Cursor(api.search_tweets, q='from:uma_musu since:%Y-%m-%d').items()
    #while tweets == None:
    while tweets == None:
        #tweets = tweepy.Cursor(api.user_timeline, screen_name='uranai_' + user_list[screen_id][0], since_id=latestid).items()
        tweets = tweepy.Cursor(api.user_timeline, screen_name='uranai_' + user_list[screen_id][0], since_id=user_list[screen_id][2]).items()
        #tweets = tweepy.Cursor(api.search_tweets, q='from:uma_musu since:%Y-%m-%d').items()

    for tweet in tweets:
        return [tweet.text, tweet.id]


def twitter_api() -> tweepy.API:
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)







#get_user_timeline()
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    print('Ready to sent message')
    #message.channel.send('Ready to send tweets. Please input start')

# メッセージ受信時に動作する処理
#get_datas = get_user_timeline(tweetid)
#print(get_datas[0])


@client.event
async def on_message(message):
    try:
        global isfirstloop
        global screen_id
        global chanting
        # メッセージ送信者がBotだった場合は無視する
        get_datas = ''
        oldtext = ''
        #screen_id = None
        print('Running...')


        if isfirstloop:
        #await message.channel.send(get_datas[0])
            print('message:' + str(message.content))
            #if message.content in key_message or message.content == "救いはないのですか...?":
            if "フクキタル" in message.content and "シラオキ様の御加護" in message.content or "救いはないのですか...?" in message.content:
            #if message.content.startswith("救いはないのですか...?"):
            #if message.content == "救いはないのですか...?":
                print('message:' + str(message.content))
                #oldesttext = get_user_timeline(2)[1]
                #oldtext = get_user_timeline(1)
                def check(msg):
                    return msg.author == message.author

                if isfirstloop:
                    await message.channel.send("はい！マチカネフクキタルです！")
                    isfirstloop = False
                
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
                
                print(str(get_user_timeline(screen_id)))
                get_datas = [get_user_timeline(screen_id)[0],get_user_timeline(screen_id)[1]]
                #latestid = get_user_timeline(latestid)[1]
                if oldtext == None:
                    while oldtext == None:
                        oldtext = get_user_timeline(screen_id)[0]
                
                await message.channel.send(random.choice(chanting))
                time.sleep(3)
                await message.channel.send(get_datas[0])
                latestid = get_datas[1]

                while True:
                    try:
                        dt_now = datetime.datetime.now()
                        if dt_now.strftime('%H:%M:%S') == '00:00:00':
                            while dt_now.minute < 10:
                                get_datas = get_user_timeline(screen_id)
                                print(get_datas)

                                try:
                                    if get_datas[0] != oldtext and get_datas[0] != None:
                                        print('get_datas[0]: ' + str(get_datas[0]))
                                        print('oldtext: ' + str(oldtext))
                                        oldtext = get_datas[0]

                                        if get_datas[0] != None:
                                            await message.channel.send(random.choice(chanting))
                                            time.sleep(3)
                                            await message.channel.send(get_datas[0])
                                            latestid = get_datas[1]
                                            if latestid == None:
                                                while latestid == None:
                                                    latestid = get_datas[1]
                                except:
                                    pass
                                
                                time.sleep(60)


                    except tweepy.errors.TooManyRequests:
                        await message.channel.send("むっ...! 水晶玉に汚れが!")
                        time.sleep(60)

                    except discord.errors.HTTPException:
                        get_datas[0] = get_user_timeline(screen_id)[0]

                        if get_datas[0] != oldtext and get_datas[0] != None:
                                    print('get_datas[0]: ' + str(get_datas[0]))
                                    print('oldtext: ' + str(oldtext))
                                    oldtext = get_datas[0]

                                    if get_datas[0] != None:
                                        await message.channel.send(random.choice(chanting))
                                        time.sleep(3)
                                        await message.channel.send(get_datas[0])
                                        latestid = get_datas[1]
                                        if latestid == None:
                                            while latestid == None:
                                                latestid = get_datas[1]


                    except tweepy.errors.TwitterServerError:
                        print('Stop by ServerError')
                        time.sleep(60)

                    except tweepy.errors.TweepyException:
                        pass

                    except:
                        await message.channel.send("ふんぎゃろおおー！")
                        await message.channel.send(traceback.format_exc())
                        break


                    time.sleep(1)
    except:
            await message.channel.send("ふんぎゃろおおー！")
            await message.channel.send(traceback.format_exc())
            pass

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
