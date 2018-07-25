

# SIZE PREVIEWS MONITOR
![enter image description here](https://lh3.googleusercontent.com/ro-CNci4JZIgV2SDbTZtbMLEawQVIYW9U9pbs_4KZj1rgWDdknV7n3otCmMvLhZKgGP0VYjKayBzAQ)

Simple monitor for size previews app with Slack/Discord integration.

**Requires:**

 - Plucky `pip install plucky`
 - Requests `pip install requests`
 

**Instructions:**
 1. Be sure to have the above libraries installed
   2.  Edit the config.json file with your slack/discord webhook (add "/slack" at the end of the discord webhook)
    3. Start the monitor by clicking start or in an IDE of your choice.

**V1.0.2**
- Added release date/time to webhook
- code to push all live products from previews app to webhook (currently commented out)

**V1.0.3**
- Updated API Key 
- Added Mobile headers to request to avoid 403 error

**V1.0.4**
- Updated Mobile headers
- Removed requirements for API key
-  Added Proxy Support


