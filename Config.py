import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6126928682:AAEKu_wr9g_gd2kpMiXT-vCHkpXotqp54EQ)
    STRING_SESSION = os.environ.get("STRING_SESSION", BQBDgRyo6FOYYggldQByAwITn8dLzN-Z7vH41bXsEOQIVc-jiw6jx92bi-3HoGZtPZ4Rk4PQ960gLGYFJvixqiKgHcahE4p0c8BatK1LW3EU-jyyLxiHjc27F3XFffxJFzwqaXeYbrfKi6wS7paIOl5RKe9lHe758KK9wzargwl2Sh0_uxTuD--lPQH0BVWA7PtNwe51p1zF5sDs9EtMQgcfHpmWZFf2crbRtNl3U9yKfmasg8V-akV-B_BOBQC_FT2QoUpWYAwC6mn8O3R8Xr6jtbE6iRwNZ3ZZMKSC4LijsS3gtoy-puPHcs9ZDCFs2zd5dh1tUz6wmGtpdsi99q1GAAAAAWQm6CEA)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
