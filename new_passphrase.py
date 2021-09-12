"""
words = the number of words you would like to compromise each passphrase of.
num = the number of passphrase you would like to generate.
dice_rolls = corrosponds to the word list. The number of times for each word you need to roll the dice inorder to look up a word in the list.
dice_sides = corrosponds to the word list. The original and most others are designed for standard 6 sided dice.
list_url = the url where the list can be found in two columns, tab delimited format.
"""
import random
import requests

def new_passphrase(words: int=4,num: int=1,seperator: str='-',dice_rolls: int=4, dice_sides: int=6, list_url: str="https://www.eff.org/files/2016/09/08/eff_short_wordlist_1.txt"):
    data = (requests.get(list_url)).text.splitlines()
    eff_list = []
    for l in data:
        eff_list.append(l.split('\t'))
    eff_list = dict(eff_list)
    pass_out = ""
    list_out = []
    for n in range(num):
        for w in range(words):
            result = ""
            for s in range(dice_rolls):
                result += str(random.randint(1,dice_sides))   
            if w == 0:
                pass_out += f'{eff_list[result]}'
            else: 
                pass_out += f'{seperator}{eff_list[result]}'
        if num == 1:
            return pass_out
        else:
            list_out.append(pass_out)
            pass_out = ""
    return list_out  
