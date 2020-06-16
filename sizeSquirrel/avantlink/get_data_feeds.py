import urllib
import datetime
from sizeSquirrel import app
from flask import current_app

def get_data_feeds():
    currentDate = datetime.datetime.today()
    print(currentDate)
    print("Getting Data Feeds...")
    urlOpener = urllib.request.URLopener()
    # adidas Outdoor
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=254501&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/adidas_outdoor_datafeed.xml")
    # BackCountry.com
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=246199&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/backcountry_datafeed.xml")
    # BentGate
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=246471&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/bentgate_datafeed.xml")
    # Black Diamond Equipment
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=255265&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/blackdiamondequipment_datafeed.xml")
    # CampSaver
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=246495&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/campsaver_datafeed.xml")
    # Eastern Mountain Sports
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=247395&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/ems_datafeed.xml")
    # Left Lane Sports
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=255397&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/leftlanesports_datafeed.xml")
    # Moosejaw
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=247387&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/moosejaw_datafeed.xml")
    # TODO Mountain Steals
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=259517&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/mountainsteals_datafeed.xml")
    # TODO Outdoor Gear Exchange
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=249021&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/outdoorgearexchange_datafeed.xml")
    # REI
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=247391&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/rei_datafeed.xml")
    # The Clymb
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=255401&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/theclymb_datafeed.xml")
    # TODO US Outdoor Store
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=249137&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/usoutdoorstore_datafeed.xml")
    # LaSportiva
    urlOpener.retrieve("http://datafeed.avantlink.com/download_feed.php?id=262033&auth=" + current_app.config['AVANT_LINK_AUTH_TOKEN'],
                       current_app.config['DATAFEED_PATH'] + "/lasportiva_datafeed.xml")
    print("Done Getting Data Feeds...")