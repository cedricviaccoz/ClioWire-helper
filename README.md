# Pulse posting script #

## Running the script ##

To work, this script needs the installation of the python module "Mastodon". To install it, run this command on your terminal :

```bash
pip install mastodon.py
```

This script allows you to post a file containing several pulses to an account on ClioWire. It needs some special manipulation the first time it is used (to set up the connection's credentials), otherwise its use is pretty straightforward, if your account user login is "Mark@epfl.ch", your password "1234", and the filename containing the pulse "file_of_pulses", then launching it can be done by typing :

```bash
python PulsePostScript.py Mark@epfl.ch 1234 file_of_pulses
```

If it is the first time you're using it you'll need to create some client and user credentials to be able to post on ClioWire. Thus select an "app name" (it can be anything you want, keep it short, it will be displayed on the bottom of your pulse) and type this command :

```bash
python PulsePostScript.py -first myAppName
```

If you want to do both things above at the same time (for some reason, maybe you don't want to waste time), you can combine the two command above into :


```bash
python PulsePostScript.py -first myAppName Mark@epfl.ch 1234 file_of_pulses
```

But further use of the script will need to drop the first two arguments ("-first" and myAppName, basically you use it like I described above), otherwise it will try to recreate the credentials, and you'll get nasty errors.

## How to organise the file containing pulses ##

The script works now with a file where the pulses are separated by a line break ('\n'). I'm not sure if you might produce pulses that have line break, if this is the case take contact with me, or modify the script accordingly. Note that this file should be located in the same place/folder of the script (otherwise you have to provide a filename that take into account the relative filepath)
