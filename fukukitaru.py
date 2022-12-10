# インストールした discord.py を読み込む
import discord
import tweepy
import time
import traceback
import datetime

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


def get_user_timeline(latestid):
    api = twitter_api()
    tweets = tweepy.Cursor(api.user_timeline, screen_name='uranai_futagoza' , since_id=latestid).items()
    #tweets = tweepy.Cursor(api.search_tweets, q='from:uma_musu since:%Y-%m-%d').items()
    if tweets == None:
        tweets = tweepy.Cursor(api.user_timeline, screen_name='uranai_futagoza', since_id=latestid).items()
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
get_datas = get_user_timeline(tweetid)
print(get_datas[0])

@client.event
async def on_message(message):
    tweetid = 1601230194718621699
    # メッセージ送信者がBotだった場合は無視する
    get_datas = ''
    oldesttext = ''
    oldtext = ''
    print('Running...')
    #await message.channel.send(get_datas[0])
    if message.content in "フクキタル" and "シラオキ様の御加護" or message.content == "救いはないのですか...?":
        #oldesttext = get_user_timeline(2)[1]
        #oldtext = get_user_timeline(1)
        await message.channel.send("はい！マチカネフクキタルです！")
        get_datas = [get_user_timeline(tweetid)[0],get_user_timeline(tweetid)[1]]
        #latestid = get_user_timeline(latestid)[1]
        if oldtext == None:
            while oldtext == None:
                oldtext = get_user_timeline(tweetid)[0]
        await message.channel.send(get_datas[0])
        latestid = get_datas[1]

        while True:
            try:
                dt_now = datetime.datetime.now()
                if dt_now.strftime('%H:%M:%S') == '00:00:00':
                    while dt_now.minute < 10:
                        get_datas = get_user_timeline(latestid)
                        print(get_datas)

                        try:
                            if get_datas[0] != oldtext and get_datas[0] != None:
                                print('get_datas[0]: ' + str(get_datas[0]))
                                print('oldtext: ' + str(oldtext))
                                oldtext = get_datas[0]

                                if get_datas[0] != None:
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
                get_datas[0] = get_user_timeline(latestid)[0]

                if get_datas[0] != oldtext and get_datas[0] != None:
                               print('get_datas[0]: ' + str(get_datas[0]))
                               print('oldtext: ' + str(oldtext))
                               oldtext = get_datas[0]

                               if get_datas[0] != None:
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

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
