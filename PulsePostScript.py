from mastodon import Mastodon
import sys
import os

DOMAIN_NAME='https://cliowire.dhlab.epfl.ch'
CLIENT_CRED='_clientcred.secret'
USER_CRED='_usercred.secret'

def main(args):
    if(len(args) <= 1):
        failure("Congratulation, you can read regex correctly ! Now relaunch the script with arguments please.")
        display_line_cmd_info()
    if(len(args) == 2):
        failure("Not enough arguments, or you know your regex really well.")
        display_line_cmd_info()
    else:
        if args[1] == '-first':
            register_app(args[2])
            args = args[2:]
        argN = len(args)
        if argN is not 0:
            if argN < 3:
                failure("Not enough arguments. To work correctly, needs at least the user login, the password,"+
                    " and the name of the file containing the pulses.")
                display_line_cmd_info()
            else:
                pulses = open(args[3], 'r').readlines()
                appName = retrieve_app_name()
                cliowire = log_in(appName, args[1], args[2]) 
                post_content(cliowire, pulses)




def display_line_cmd_info():
    print("Usage of this program : (some knowledege of regex required to understand the following line) "+
          "\npython PulsePostScript (-first appName)? (userLogin userPassword csvFileOfPulses)?" +
          "\n\nIf it is the very first time you're using this script, put as first argument \"-first\""+
          " and then give a name of your liking to your app."
          "\nOtherwise don't forget to put the user login of your account, the password, and then "+
          "the name of the file containing the pulse you wish to post in this precise order.")

# Register app - only once!
def register_app(appName):
    Mastodon.create_app(
     appName,
     api_base_url = DOMAIN_NAME,
     to_file = appName + CLIENT_CRED
    )

def retrieve_app_name():
    filesInFolder = os.listdir()
    files = list(filter(lambda x: x.endswith(CLIENT_CRED), filesInFolder))
    nmbOfFiles = len(files)
    if(nmbOfFiles == 0):
        failure("No credential files were created, be sure to run at least"+
            " once this program with the command line \"-first\" followed by an "+
            "app name before trying to post pulses")
    elif(nmbOfFiles > 1):
        failure("There is too much credential files (.secret) present in "+
            "this folder to proceed to log in. Either delete all unnecessary"+
            " .secret files, or delete them all, and relaunch this script "+
            "he command line \"-first\" followed by an app name ")
    else:
        return files[0][:-len(CLIENT_CRED)]


def post_content(api_instance, pulses):
    for p in pulses:
        api_instance.toot(p)

def failure(msg):
    print(msg)


def log_in(appName, userLogin, userPswd):
    mastodon = Mastodon(
        client_id = appName+CLIENT_CRED,
        api_base_url = DOMAIN_NAME
    )

    mastodon.log_in(
        userLogin,
        userPswd,
        to_file = appName+USER_CRED
    )

    # Create actual API instance
    return Mastodon(
        client_id = appName+CLIENT_CRED,
        access_token = appName+USER_CRED,
        api_base_url = DOMAIN_NAME
    )

main(sys.argv)