from instabot import Bot

bot = Bot()

bot.login(username="normiethors",password='######')

bot.follow("chakrastraa")
bot.upload_photo("C:/Users/hp/OneDrive/Desktop/Berserk.jpg",caption="...")
#bot.unfollow("chakrastraa")

bot.send_message("If it is working, Do not touch it",["heisunburger","sidd_3577","abhishek.y.strings"])

followers=bot.get_user_followers("normiethors")

for follower in followers:
    print(bot.get_user_info(follower))
    
