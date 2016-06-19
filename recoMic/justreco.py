# The following import will allow us to view exceptions with a good level of detail in the case of something unexpected.
import sys, traceback

# time package has a sleep(seconds) func
import time

# import subprocess package to run festival tts
import subprocess

# This import will give us our wrapper for the Pocketsphinx library which we can use to get the voice commands from the 
# user.
from pocket_sphinx_listener import PocketSphinxListener

# Commands in the grammar
#   turn on the kitchen light
#   turn off the kitchen light
#   turn on the bedroom light
#   turn off the bedroom light
#   turn on the roomba
#   turn off the roomba
#   roomba clean
#   roomba go home


def runMyMain():

    # Now we set up the voice recognition using Pocketsphinx from CMU Sphinx.
    pocketSphinxListener = PocketSphinxListener()

    # We want to run forever, or until the user presses control-c, whichever comes first.
    while True:
        try:
            command = pocketSphinxListener.getCommand().lower()

 #   for a grammar that looks like TURN <state> <device>
 #           if command.startswith('turn'):
 #               onOrOff = command.split()[1]
 #               deviceName = ''.join(command.split()[2:])
 #               do something   
 #   for a grammar that looks like ROOMBA <action>
 #           elif command.startswith('roomba'):
 #               action = ' '.join(command.split()[1:])
 #               if action == 'clean':
 #                   roomba.clean()
 #               if action == 'go home':
 #                   roomba.goHome()
        # speak what was heard
 #           filename = '_tmp.txt'
#	    file=open(filename,'w')
#	    file.write(command)
#	    file.close()
#	    subprocess.call('festival --tts '+filename, shell=True)
#	    subprocess.call('rm -f '+filename, shell=True)
 
        # This will allow us to be good cooperators and sleep for a second.
            print "I'm thinking now"
	    time.sleep(1)

        except (KeyboardInterrupt, SystemExit):
            print 'Goodbye.'
            sys.exit()
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                      limit=2,
                                      file=sys.stdout)
            sys.exit()


runMyMain()

