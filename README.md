# antiban
Discord bot to unban entire ban list. Good if a rouge mod did a total purge. 

Instructions: 
* To run, download antiban.py.
* Then, copy and paste in the token into the file. If you don't know what that is, the first half of this tutorial should cover it: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
* Adjust the write and file_path flags if need be. As is, everyone you unban will have their usernames written to a text file called "list.txt." Changing write to false will make that not happen. If you want to write to a new file, make sure you've created it in the same folder that antiban.py is in.
* Then run `Python3 antiban.py` in the terminal. Before you do that you will need to navigate to the proper folder, using `cd yourfilepath`. You may have to use Pip3 to download discord.py like this `Pip3 install discord`
* Then, just type `$unban` in the server to unban everyone. You will need unban privs. 
