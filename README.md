Twitter Bot Starter Kit
=======================

So you've decided to make a twitter bot of your very own. Good choice. There's a bit of setup to do before we get to the fun part.

This tutorial drew inspiration from Molly White's, which is available at http://blog.mollywhite.net/twitter-bots-pt1/

### Download the code

First step is to fork this repo to your own account. It will be important to have a version that *you're* allowed to edit when it comes time to deploy your bot.

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea89b34ea8157334263b54/da1b7338bbd61fb73c5cd86d3abcd50a/capture.png)

Now, go to your fork and click the green `clone or download` button:

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea8149225a23a2ae6e3a59/8a97e1045a247f2d44fdded010e28850/capture.png)

You may have to click "use https" if you haven't set up an ssh key on your computer. If you don't know what that means, you want the "use https" link.

Take the link from that box and run `git clone https://github.com/YOUR_USERNAME/twitter-bot-starter-kit.git` in a terminal. This will download a copy of the code to your computer.

### Make a new twitter account.
Go to https://twitter.com/signup . You'll have to add a phone number, or you won't be able to create an app. (Don't worry, you can change your name and twitter handle later)

- **Problem:** You already have a twitter account associated with your phone number.
- **Solution:** I don't know if twitter has updated their rules since Molly White's tutorial was written, but I didn't have a problem. They let me add a phone number, even though it's already in use. ¯\\\_(ツ)\_/¯

### Create a twitter app

Logged in with your bot account, go to https://apps.twitter.com/app/new to make an app. Fill out the fields. When you're done, you should be able to see your Consumer Key and Consumer Secret:

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea7d85c4421fc6ad8495f6/07647a311605cd4856c8a84d1c3a34c2/capture.png)

You will also be able to make an Access Token, lower on that same page:

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea7d58355eeb6bc7dcc903/7c5b22c137f1b9fab96f61d405911faf/capture.png)

## make a secrets.py file

This file will stay on your computer and should never make it to github. Here's an example of what it should look like:

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea7e16cb2f067ca2be3925/3d151e9573ef821fa0376b902fd61b6b/capture.png)

(Don't worry, I've changed all my keys since taking these screenshots)

## install requirements

We're using the `tweepy` library to talk to twitter from python. You'll need to install it.

`pip install tweepy`

## Try it out!

At this point, you should be able to run your bot locally. Run it with `python bot.py` to post a tweet (you can always delete it if it doesn't fit with the theme you end up choosing)

## Make your bot!

Change `bot.py` to post whatever you like. Some ideas, if you're looking for inspiration:

- [@TwoHeadlines](https://twitter.com/twoheadlines)
![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea8ab4a108e72243939651/c155d08814be16f532b66db098bb9ea7/capture.png)

- [@wikisext](https://twitter.com/wikisext)
![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea8acccbb284f4daf92760/8784e64eeb3be19df5cd3165c22bd790/capture.png)

- [@portmanteau_bot](https://twitter.com/portmanteau_bot)
![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea8d6ed22630dccaf5b531/bfa9a74e723ae598203e946e6e7c32e9/capture.png)

- [Accidental Haiku](https://twitter.com/accidental575)
![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea8dc295326d064a270c5e/2e81db6e643ca289e5301183d9e3e892/capture.png)

- Many others at http://tinysubversions.com/

### Resources for building your bot

Again, copied from http://blog.mollywhite.net/twitter-bots-pt2/

- News headlines: [Guardian API](http://open-platform.theguardian.com/), [Google News RSS](http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&output=rss) (needs to be parsed)
- News headlines filter ("tact"): [offensive.py](https://github.com/molly/CyberPrefixer/blob/master/offensive.py)
- HTML parsing: [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
- Parts-of-speech tagging: [topia.termextract](https://pypi.python.org/pypi/topia.termextract/)
- Word and dictionary magic: [Wordnik](https://www.wordnik.com/)
- Rhymes: [RhymeBrain API](http://rhymebrain.com/api.html)
- Weather information: [Forecast.io API](https://developer.forecast.io/)
- Markov chaining: [Markovify](https://github.com/jsvine/markovify)
- [Interesting corpora](https://github.com/dariusk/corpora)

Also, check out [Basic Twitter bot etiquette](http://tinysubversions.com/2013/03/basic-twitter-bot-etiquette/)

## Deploying to heroku

We'll set up automatic deployment so that any changes you push to github will be deployed on heroku right away.

Create a heroku account, and make an app. Choose 'Python' for the runtime. On the 'deploy' tab of your new app's page, click 'Connect to Github":

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea82f3b92b8402db39feaf/5fd8a8bc00ac731404809623bffcec61/capture.png)

This should make *another* button that says "Connect to GitHub". Click that one too. You may get a popup from github that asks you if you want to trust Heroku.

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea8312ae626d4768039eb9/1088c16abfb4cb62d24c62936358f2f9/capture.png)

Choose your repository, which is probably still called `twitter-bot-starter-kit` and click connect.

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea833c63f035a963fd4d56/132af2f506395902be59069597555e83/capture.png)

Now that we're connected, turn on automatic deploys.

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea8380ba7b1277b3a4c5ac/fa38d993a6ecc30f8d211c54d812d0f1/capture.png)

Any time you push changes to your `master` branch on github, heroku will update with the newest version of the code.

## Heroku environment variables

Heroku doesn't have access to your `secrets.py` file, so we need to give it that data some other way. Go to the settings tab in heroku and click "Reveal Config Variables".

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea8495a5ffb079dc0ac354/d84bf29c9cebde373f51562e39b4db69/capture.png)

Add your `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_KEY`, and `ACCESS_SECRET` to the Config Vars table, copying the values from your `secrets.py` file.

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea8586148730768569c112/e3ab8e1b58ffb0e5a196d951f65993e8/capture.png)

## Running on Heroku

Now we need to schedule our bot to run periodically. From the resources tab, search for an Add-on called "Heroku Scheduler"

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea85eb1145db7310bab937/a0b9aaa661c9846fa5c0ebb621fdc10c/capture.png)

It looks like they're gonna make you put credit card information in to add the scheduler. It didn't charge me though.

Click the "Heroku Scheduler" row that now appears on your Resources page. This will open a new page, where you can set up how often you want your bot to run. Twitter will block bots that post too often, so I don't recommend choosing every 10 minutes.

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/59ea86bf5d6a2ca30f7aaaf3/b1c147911be2fc16ee91802751ed8722/capture.png)

## Success!

That should be it!
# twitter-bot
