#
###
#####
#######
#########
###########
#############
###############
#################
###################
#####################
#######################                            ###
#########################                       ######
###########################                 ##########
#############################            #############
###############################      #################
################################# ####################
################################   ###################
#############################        #################
##########################             ###############
######################                   #############
###################                        ###########
################                             #########
############                                   #######
#########                                        #####
######                                             ###
##                                                   #

#               Quetzal Sandbox Gen 1                #

import random
import sys


def version():
    print('Quetzal Sandbox Gen 1')
    print('Dual Word Generator')
    print('Version: 1.0')
    print('Author: Quetzal-Sama')

def args():
    args = sys.argv
    if '-h' in args or '--help' in args:
        print('Usage: python3 dual_word.py -wl <wordlist> [options]')
        print('Options:')
        print('-h, --help: Show this help message and exit.')
        print('-wl, --wordlist <wordlist>: Choose a wordlist.')
        print('-l, --look <word>: Search for specific word, attempts will be overpassed.')
        print('-a, --attempts <attempts>: Choose the number of attempts.')
        print('-sf, --show-first <attempts>: Show the first attempts.')
        print('-s, --show: Show all attempts.')
        print('-v, --version: Show version and exit.')
        sys.exit()
    if '-v' in args or '--version' in args:
        version()
        sys.exit()
    if len(args) < 2:
        print('Usage: python3 dual_word.py -wl <wordlist> [options], see --help for more info.')
        sys.exit(1)
    if '-wl' in args or '--wordlist' in args:
        pre_wordlist = args[args.index('-wl') + 1]
        wordlist = []
        for i in pre_wordlist.split():
            wordlist.append(i)
    else:
        print('Usage: python3 dual_word.py -wl <wordlist> [options], see --help for more info.')
        sys.exit(1)
    if '-l' in args or '--look' in args:
        lookword = args[args.index('-l') + 1]
    else:
        lookword = False
    if '-a' in args or '--attempts' in args:
        attempts = int(args[args.index('-a') + 1])
    else:
        attempts = 10
    if '-sf' in args or '--show-first' in args:
        showfirst = args[args.index('-sf') + 1]
    else:
        showfirst = False
    if '-s' in args or '--show' in args:
        show = True
    else:
        show = False
    return wordlist, lookword, attempts, show, showfirst

def randomizer(wordlist):
    result = ''
    elements = len(wordlist)
    for j in range(elements):
        word_random = random.choice(wordlist)
        word_range = len(word_random)
        word_min = round(word_range / (word_range + 1))
        word_max = round((word_range + word_range) - 1)
        result = result + word_random[(random.randrange(word_min)):(random.randrange(word_max))]
    return result

def boot():
    wordlist, lookword, attempts, show, showfirst = args()
    if lookword:
        print('Searching for:', lookword)
    if showfirst:
        print('Showing first:', showfirst)
    if show:
        print('Showing all attempts.')
    print('Wordlist:', wordlist)
    print('Attempts:', attempts)

    all_results = []
    look_results = []
    i = 0
    loops = 0
    max_attempts = attempts * len(wordlist)
    
    print('Max attempts:', max_attempts)

    while i < attempts:
        loops += 1
        random_word = randomizer(wordlist)
        if not random_word in all_results:
            all_results.append(random_word)
            i += 1
            if lookword:
                if lookword in random_word:
                    look_results.append(random_word)
                    i += 1
                else:
                    i -= 1
        if loops >= max_attempts:
            break
    
    if show:
        for i in range(len(all_results)):
            print('Result', i, '>', all_results[i])

    if lookword:
        for i in range(len(look_results)):
            print('Look', i, '>', look_results[i])
    
    if showfirst:
        for i in range(int(showfirst)):
            print('Attempt', i, '>', all_results[i])

boot()