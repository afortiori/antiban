# antiban
Discord bot to unban entire ban list. Good if a rouge mod did a total purge. 

Instructions: 
* To run, download antiban.py.
* Then, copy and paste in your token into the file and configure OAuth2 in Discord Developer Portal. If you don't know what that is, the first half of this tutorial should cover it: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
* Adjust the write flag and file_path variable if need be. As is, everyone you unban will have their usernames appended to a text file called "list.txt." Changing write to false will make that not happen. You can change the path of the file it's written to by changing file_path. If you want to write to a different file, make sure you've created it and the path to it is correct.
* Then run `Python3 antiban.py` in the terminal. Before you do that you will need to navigate to the proper folder, using `cd yourfilepath`. You may have to use Pip3 to download discord.py like this `Pip3 install discord`. Do this in a virtual enviroment if you'd like. 
* Then, just type `$unban` in the server to unban everyone. You will need unban privs. 
