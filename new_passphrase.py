import random
import requests

def new_passphrase(words=4,num=1,seperator='-',dice_sides=4):
    data = requests.get("https://www.eff.org/files/2016/09/08/eff_short_wordlist_1.txt")
    data = data.text.splitlines()
    eff_list = []
    for l in data:
        eff_list.append(l.split('\t'))
    eff_list = dict(eff_list)
    pass_out = ""
    list_out = []
    for n in range(num):
        for w in range(words):
            result = ""
            for s in range(dice_sides):
                result += str(random.randint(1,6))   
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
    
