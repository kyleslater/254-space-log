Homework 2:
===========

Some friends and I play a space sim game called Elite: Dangerous. It features a procedurally-generated, 1:1 simulation of the Milky Way, of which humans of the 34th century have explored only a small part. Fortunately for the player community, which relies on it's own third-party tools to map discoveries, the game outputs very detailed plain-text logs. I recently took my small ship out into the black to explore on my own, and one of the logs for that is included in this homework.

Main requirements
-----------------
Form a group of no more than four people and, together, write a Python program that uses regular expressions to do the following:
1) Print the names of all of the star systems I visited during this log. ("event":"FSDJump")
2) Print the names of all of the planets I scanned during this log. ("event":"Scan")
3) Print the total number of terraformable planets I scanned during this log ("event:"Scan")
4) Print the total number of light years I traveled during this log. ("event":"FSDJump")

Secondary requirements
----------------------
- Choose *one* person to fork this repository. They will be the group leader, in that their fork will be the one graded. The leader must add all other members as collaborators to their repository (Settings > Collaborators).
- Each member will create a new branch for their work, and pick one item from the list of main requirements. Write the function definition for your requirement in a new file, and use it in the main file like in the example. When finished *and tested*, merge your work into the master branch.
	- **That means** no one else in the group should fork this original repo, and *every* group member must have commits visible in the git log. **Do not** simply email, copy/paste, or retype your code into one file, and have the leader make one commit to their repo. **Only the master branch will be graded. Anyone missing from the master branch will not have their work graded.**
- Every member of the group must complete one of the main requirements. If there are n < 4 members in the group, complete n main requirements in the order given. Extra work (item 4 completed in a 3-person group) will be ignored.

Example given
-------------
Print the total amount of hydrogen fuel consumed by jumps during this log.
