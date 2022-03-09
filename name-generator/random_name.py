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

greek_alphabet = [
	['Α', 'α', 'Alpha', 'a'],
	['Β', 'β', 'Beta', 'b'],
	['Γ', 'γ', 'Gamma', 'g'],
        ['Δ', 'δ', 'Delta', 'd'],
        ['Ε', 'ε', 'Epsilon', 'e'],
        ['Ζ', 'ζ', 'Zeta', 'z'],
        ['Η', 'η', 'Eta', 'h'],
        ['Θ', 'θ', 'Theta', 'th'],
        ['Ι', 'ι', 'Iota', 'i'],
        ['Κ', 'κ', 'Kappa', 'k'],
        ['Λ', 'λ', 'Lambda', 'l'],
        ['Μ', 'μ', 'Mu', 'm'],
        ['Ν', 'ν', 'Nu', 'n'],
        ['Ξ', 'ξ', 'Xi', 'x'],
        ['Ο', 'ο', 'Omicron', 'o'],
        ['Π', 'π', 'Pi', 'p'],
        ['Ρ', 'ρ', 'Rho', 'r'],
        ['Σ', 'σ | ς', 'Sigma', 's'],
        ['Τ', 'τ', 'Tau', 't'],
        ['Υ', 'υ', 'Upsilon', 'u'],
        ['Φ', 'φ', 'Phi', 'ph'],
        ['Χ', 'χ', 'Chi', 'xh'],
        ['Ψ', 'ψ', 'Psi', 'ps'],
        ['Ω', 'ω', 'Omega', 'o'],
]

constelations = [
        ['Andromeda', 'N', 'Andromeda'],
        ['Antlia', 'S', 'Airpump'],
        ['Aquila', 'N', 'Eagle'],
        ['Carina', 'S', 'Keel'],
        ['Centaurus', 'S', 'Centaur'],
        ['Cetus', 'S', 'Whale'],
        ['Chameleon', 'S', 'Chameleon'],
        ['Crater', 'S', 'Cup'],
        ['Delphinus', 'N', 'Dolphin'],
        ['Dorado', 'S', 'Swordfish'],
        ['Draco', 'N', 'Dragon'],
        ['Horologium', 'S', 'Clock'],
        ['Hydra', 'N', 'Sea Serpent'],
        ['Leo', 'Z', 'Lion'],
        ['Lepus', 'S', 'Hare'],
        ['Libra', 'Z', 'Scales'],
        ['Lupus', 'S', 'Wolf'],
        ['Lynx', 'N', 'Lynx'],
        ['Monoceros', 'S', 'Unicorn'],
        ['Orion', 'S', 'Orion'],
        ['Pegasus', 'N', 'Pegasus'],
        ['Phoenix', 'S', 'Phoenix'],
        ['Telescopium', 'S', 'Telescope'],
]

chinese_zodiac = [
        ['Rat', '鼠'],
        ['Ox', '牛'],
        ['Tiger', '虎'],
        ['Rabbit', '兔'],
        ['Dragon', '龙'],
        ['Snake', '蛇'],
        ['Horse', '马'],
        ['Goat', '羊'],
        ['Monkey', '猴'],
        ['Rooster', '鸡'],
        ['Dog', '狗'],
        ['Pig', '猪'],
]

def version():
        print('Quetzal Sandbox Gen 1')
        print('Random Name Generator')
        print('Version: 1.2')
        print('Author: Quetzal-Sama')

def randomizer(list):
        # Randomize
        random.shuffle(list)
        # Select
        name = random.choice(list)
        # Print
        print(end=' | ')
        for i in name:
                print(i, end=' | ')
        return name
        
def main():
        # Check args
        args = sys.argv
        # Check version
        if '-v' in args or '--version' in args:
                version()
                sys.exit()
        # Check -h or --help
        if '-h' in args or '--help' in args:
                print('Usage: random_name.py [options]\n')
                print('Options:')
                print('  -c, --constellation  Generate a constellation name.')
                print('  -g, --greek          Generate a greek name.')
                print('  -z, --zodiac         Generate a Chinese zodiac name.')
                print('  -h, --help           Show this help.')
                sys.exit()
        # Check args
        if len(args) < 2:
                print('Usage: random_name.py [options], use -h or --help for more information.')
                sys.exit()
        # Check -c or --constellation
        if '-c' in args or '--constellation' in args:
                randomizer(constelations)
                sys.exit()
        # Check -g or --greek
        if '-g' in args or '--greek' in args:
                randomizer(greek_alphabet)
                sys.exit()
        # Check -z or --zodiac
        if '-z' in args or '--zodiac' in args:
                randomizer(chinese_zodiac)
                sys.exit()

main()