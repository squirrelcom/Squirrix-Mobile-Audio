# Exit function
from sys import exit
from time import sleep

from lib.utils import prop, set_path
from lib.vfs import cleanup
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()



def _help():
    usage = '''
Usage: exit [options]
[options]:
-t (int)        exits after (int)
                time in seconds.
-h              Print this help.
'''
    print(usage)


def main(argv):
    # exit gets an empty arg list
    # now, shell doesnt send the
    # comm name anymore
    if '-h' in argv:
        _help()
        return
    if '-t' in argv:
        i = argv.index('-t') + 1
        try:
            t = int(argv[i])
            die(t)
        except ValueError:
            talk('"', argv[i], '" is not a valid time interval...', sep='')
            talk('Exiting with default time...')
        except IndexError:
            talk('You forgot to give the time...')
            talk('Exiting with default time...')
    die()


def die(t=2):
    talk('Stopping Squirrix Mobile...')
    sleep(1)
    talk('Closed Everything...')
    talk('will exit in', t, 'seconds...')
    sleep(t)
    if prop.get('save_state') == '0':
        set_path('root/')
        prop.set('prompt', '-def')
    cleanup()
    exit()
