# This import will give us our wrapper for the Pocketsphinx library which we can use to get the voice commands from the 
# user.
from pocket_sphinx_listener import PocketSphinxListener
import sys

def runMain():
    # Now we set up the voice recognition using Pocketsphinx from CMU Sphinx.
    # We can set debug for the listener here to see messages directly from Pocketsphinx
    pocketSphinxListener = PocketSphinxListener(debug=False)

    while True:
        try:
            # We can set debug here to see what the decoder thinks we are saying as we say it
            command = pocketSphinxListener.getCommand(debug=True).lower()
    
        # Exit when control-c is pressed
        except (KeyboardInterrupt, SystemExit):
            print 'People sometimes make mistakes, Goodbye.'
            sys.exit()    
    
if __name__ == '__main__':
    runMain()
