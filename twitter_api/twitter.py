import tweepy
import time

# 取得した各種キーを格納-----------------------------------------------------
CONSUMER_KEY ="ZQEUqQ40o2QrHRXhWgki33ZKP"
CONSUMER_SECRET ="iEHWOEJo2J1Q1Ie1zjeo1CjNKx8OpJo6tW8YN5DarF94YpQrEG"
ACCESS_TOKEN="956851574780829696-mNvZWTmhJS6lcbyFWH8agFFo40yn035"
ACCESS_SECRET ="OFdNTPVRMe6aCvzP43VwGrjtUk98LNAYAW64Vi77fS0bu"

# OAuthHandlerインスタンスの作成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# ツイートの検索
q_list = "映画"
count  = 1
count_now = 0
not_count = 0

for q in q_list:
    print(q)
    search_results = api.search(q=q, count=count)
    for result in search_results:
        tweet_id = result.id
        user_id  = result.user._json['id']
        try:
        # いいね押下
            api.create_favorite(tweet_id)
            count_now = count_now + 1
            print("count_now = " + str(count_now))
            print("not_count = " + str(not_count))
            print("total = " + str(count_now + not_count))
            print("----------------------")

        except Exception as e:
            print(e)

            if (e.api_code == 429 or e.api_code is None):
                print("count_now = " + str(count_now))
                print("not_count = " + str(not_count))
                print("total = " + str(count_now + not_count))
                print("----------------------")
                print("60分間スリープします")
                time.sleep(60*60)
            else:
                not_count = not_count + 1
                print("count_now = " + str(count_now))
                print("not_count = " + str(not_count))
                print("total = " + str(count_now + not_count))
                print("----------------------")

print("処理を終了します。")
print("count_now = " + str(count_now))
print("not_count = " + str(not_count))
print("total = " + str(count_now + not_count))
