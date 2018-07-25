from requests import *
import json
from time import *
import plucky
import re
from pybase.classes.logger import logger
log = logger().log

class Monitor:
    def __init__(self):

        with open("Config.json") as tsk:
            self.t  = json.load(tsk)

        self.forever        = True
        self.url            = "https://mosaic-platform.mesh.mx/stores/size/content?channel=iphone-mosaic"
        self.webhook        = self.t["Webhook"]
        self.session        = Session()
        self.pidArray       = []
        self.scrapeArray    = []
        self.removepids     = []
        self.sleep          = self.t["Delay"]
        self.headers        ={"user-agent":"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"}

        try:

            self.page       = self.session.get(url=self.url,headers=self.headers).json()["products"]

        except Exception:
            log("Cannot get information off app, please check your internet and try again", "error")
            exit()

        print("Current shoes on app:")
        print("")

        for products in range(len(self.page)):
            self.pidArray.append(self.page[products]["ID"])
            print("- {}".format(self.page[products]["name"]))

            # slackMessage = {
            #     "attachments": [
            #         {
            #             "author_name": "New Item",
            #             "fallback": "",
            #             "title": "{}".format(self.page[products]["name"]),
            #             "title_link": "https://size-mosaic-webapp.mesh.mx/#/product/{}".format(self.page[products]["ID"]),
            #             "fields": [
            #                 {
            #                     "title": "PID:",
            #                     "value": "{}".format(self.page[products]['ID']),
            #                     "short": True
            #                 },
            #                 {
            #                     "title": "Sizes:",
            #                     "value": "{}".format(plucky.plucks(self.page[products]["options"], 'name')),
            #                     "short": True
            #                 },
            #                 {
            #                     "title": "Release Date",
            #                     "value": "{}, {} GMT".format(self.page[products]['launchDate'].split("T")[0], re.search('T(.*):', self.page[products]["launchDate"]).group(1)),
            #                     "short": False
            #                 }
            #             ],
            #             "image_url": "{}".format(self.page[products]["mainImage"]["original"]),
            #
            #             "color": "#00FF00"
            #         }]
            #
            # }
            #
            # self.session.post(
            #     url=self.webhook,
            #     data=json.dumps(slackMessage)
            # )



        print("")
        print("Number of shoes on app: {}".format(len(self.pidArray)))
        print("")


        log("Monitor Started Succesfully", "success")




    def scrape(self):

        try:

            while self.forever:
                scrape          = self.session.get(url=self.url).json()["products"]

                for products in range(len(scrape)):
                    self.scrapeArray.append(scrape[products]["ID"])


                    if self.scrapeArray[products] not in self.pidArray:

                        slackMessage = {
                            "attachments" : [
                                {
                                    "author_name"   : "New Item",
                                    "fallback"      : "",
                                    "title"         : "{}".format(scrape[products]["name"]),
                                    "title_link"    : "https://size-mosaic-webapp.mesh.mx/#/product/{}".format(scrape[products]["ID"]),
                                    "fields": [
                                        {
                                            "title" : "PID:",
                                            "value" : "{}".format(scrape[products]['ID']),
                                            "short" : True
                                        },
                                        {
                                            "title" : "Sizes:",
                                            "value" : "{}".format(plucky.plucks(scrape[products]["options"], 'name')),
                                            "short" : True
                                        },
                                        {
                                            "title" : "Release Date",
                                            "value" : "{}, {} GMT".format(scrape[products]['launchDate'].split("T")[0],re.search('T(.*):', scrape[products]["launchDate"]).group(1)),
                                            "short" : False

                                        }
                                    ],
                                    "image_url"     : "{}".format(scrape[products]["mainImage"]["original"]),

                                    "color"         : "#00FF00"
                                }]

                        }

                        self.session.post(
                            url     = self.webhook,
                            data    = json.dumps(slackMessage)
                        )

                        log("PID: {},Name: {} added to app".format(scrape[products]["ID"],scrape[products]["name"]), "success", "addedPIDs.txt")


                        self.pidArray.append(scrape[products]["ID"])



                for pids in range(len(self.pidArray)):

                    if self.pidArray[pids] not in self.scrapeArray:

                        self.removepids.append(pids)


                count = 0


                for rPids in range(len(self.removepids)):
                    log("PID: {} removed from app".format(self.pidArray[self.removepids[rPids - count]]), "error")

                    self.pidArray.pop(int(self.removepids[rPids]) - count)

                    count = count + 1

                self.scrapeArray    = []
                self.removepids     = []

                sleep(int(self.sleep))

        except Exception:
            log("Something went wrong. Restarting Monitor", "error")
            self.scrape()
            sleep(int(self.sleep))




Monitor().scrape()