import sys
import random

attackers = {'Sledge':['Shotgun', 'L85'], 'Thatcher':['L85', 'Shotgun', 'AR-33'], 
            'Ash':['G36C', 'R4-C'], 'Thermite':['M1014', '556xi'],
            'Twitch':['F2' , '417', 'Shotgun'], 'Monty':['Swagnum', 'P9'],
            'Fuze':['LMG', 'AK-12', 'Shield + Makarov', 'Shield + Wimpy Pistol'],
            'IQ':['552', 'Aug A2', 'Terrible LMG'], 'Buck':['AR', 'DMR'],
            'Capitao':['308', 'LMG'], 'Blackbeard':['Scar-H', 'DMR'],
            'Hibana':['Type 89', 'SuperNova'], 'Jackal':['C7E', 'PDW', 'Shotgun'],
            'Ying':['LMG', 'Shotgun'], 'Zofia':['AK', 'LMG'],
            'Dokkaebi':['EBR', 'Meme Cannon']}

defenders = {'Smoke':['SMG', 'Shotgun'], 'Mute':['SMG', 'Shotgun'],
            'Castle':['SMG', 'Shotgun'], 'Pulse':['SMG', 'Shotgun'],
            'Doc':['MP5', 'P90', 'Shotgun'], 'Rook':['MP5', 'P90', 'Shotgun'],
            'Kapkan':['SMG', 'Sassy-G'], 'The Lord':['SMG', 'Sassy-G'],
            'Jaeger':['416', 'Shotgun'], 'Bandit':['Mp7', 'Shotgun'],
            'Frost':['SMG', 'Sniper90'], 'Valk':['MPX', 'SPAS-12'],
            'Cav':['SMG', 'SPAS-15'], 'Echo':['MP5', 'SuperNova'],
            'Mira':['Vector', 'Shotgun'], 'Lesion':['SMG', 'DU Shotty'],
            'Ela':['SMG', 'Shotgun'], 'Vigil':['K1A', 'Meme Cannon']}


def main():
    # Grab round type from command line, if not specified, exit
    round_type = sys.argv[1]
    if round_type != 'defense' and round_type != 'attack':
        print('Invalid round type.')
        sys.exit(0)
    if round_type == 'defense':
        defender = random.choice(list(defenders.keys()))
        weapon = random.choice(defenders[defender])
        print(defender, weapon)
    else:
        attacker = random.choice(list(attackers.keys()))
        weapon = random.choice(attackers[attacker])
        print(attacker, weapon)
    #print('In main')


if __name__ == '__main__':
	main()