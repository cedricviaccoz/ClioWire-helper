###Pulse posting script###

##Running the script##

To work, this script needs the installation of the python module "Mastodon". To install it, run this command on your terminal :

'''
pip install mastodon.py
'''

This script allows you to post a file containing several pulses to an account on ClioWire. It needs some special manipulation the first time it is used (to set up the connection's credits), otherwise its use is pretty straightforward, if your account user login is "Mark@epfl.ch", your password "1234", and the filename containing the pulse "file_of_pulses", then launching it can be done by typing :

'''
python PulsePostScript.py Mark@epfl.ch 1234 file_of_pulses

'''

If it is the first time you're using it you'll need to create some client and user credits to be able to post on ClioWire. Thus select an "app name" (it can be anything you want, keep it short, it will be displayed on the bottom of your pulse) and type this command :

'''
python PulsePostScript.py -first myAppName
'''

If you want to do both things above at the same time (let's say you only want to post pulses once in your life and then never have to deal with it), you can combine the two command above into :

'''
python PulsePostScript.py -first myAppName Mark@epfl.ch 1234 file_of_pulses
'''

##How to organise the file containing pulses##

The script works now with a file where the pulses are separated by a line break ('\n'). I'm not sure if you might produce pulses that have line break, if this is the case take contact with me, or modify the script accordingly.
