import random
import requests
from typing import Union

def new_passphrase(
    words: int=4,
    num: int=1,
    seperator: str='-',
    dice_rolls: int=4,
    dice_sides: int=6,
    list_url: str="https://www.eff.org/files/2016/09/08/eff_short_wordlist_1.txt"
    ) -> Union[str, list]:
    """Generates one or more secure passphrases.

    Args:
        words (int, optional): The number of words to comprise the resultant passphrase. Defaults to 4.
        num (int, optional): The number of passphrases to generate. Defaults to 1.
        seperator (str, optional): The string separator between words. Defaults to '-'.
        dice_rolls (int, optional): Per the word list, how many dice rolls for each word lookup. Defaults to 4.
        dice_sides (int, optional): Per the word list, how many sides does the dice have. Defaults to 6.
        list_url (str, optional): The word list. Tab delimited, two column. Defaults to "https://www.eff.org/files/2016/09/08/eff_short_wordlist_1.txt".

    Returns:
        str: One Passphrase
        list: Multiple Passphrases

    Examples:
        str:
            new_passphrase()
            'oasis-tart-bleak-gains'

            new_passphase(words=10)
            'july-barge-icing-trio-dish-cure-plead-fence-sage-scuba'
        
        list:
            new_passphrase(num=3)
            ['vegan-chest-jury-crisp', 'wool-debug-smell-purse', 'widen-boat-fog-game']        
    """
    data = (requests.get(list_url)).text.splitlines()
    eff_list = []
    for l in data:
        eff_list.append(l.split('\t'))
    eff_list = dict(eff_list)
    str_out = ""
    list_out = []
    for n in range(num):
        for w in range(words):
            result = ""
            for s in range(dice_rolls):
                result += str(random.randint(1,dice_sides))   
            if w == 0:
                str_out += f'{eff_list[result]}'
            else: 
                str_out += f'{seperator}{eff_list[result]}'
        if num == 1:
            return str_out
        else:
            list_out.append(str_out)
            str_out = ""
    return list_out  
