import praw
from collections import defaultdict
from configobj import ConfigObj
import json
def download_comments(username):
    config = ConfigObj('config.ini')
    reddit = praw.Reddit(client_id=config['client_id'],
                        client_secret=config['client_secret'],
                        user_agent='web:user_similarity:v0.0.1 (by /u/spez)')
    user = reddit.redditor(username)
    comment_list = []
    for comment in user.comments.new(limit=None):
        comment_list.append(comment.body)
    return comment_list

def save_file(data, filename):
    with open(filename, mode='w') as f:
        f.write(json.dumps(data))

def download_and_save(username):
    data = download_comments(username)
    save_file(data, './data/' + username + '.data')

def main():
    sample_reddit_users = ['brigodon', 'rotorcowboy', 'Abe_lincolin', 'Thehealeroftri', 'User_Name13', 'maxwellhill', 'illuminatedwax', 'axolotl_peyotl', 'Rlight', 'straydog1980', 'themightiestduck', 'qgyh2', 'BritishEnglishPolice', 'IAmAN00bie', 'manbra', 'MaiaNyx', 'nix0n', 'Jux_', 'awildsketchappeared', 'iBleeedorange', 'CycleModRecs', 'vrckid', 'ManWithoutModem', 'danrennt98', 'AutoModerator', 'Donald_Keyman', 'shadowman3001', 'lanismycousin', 'Geekymumma', 'MrWeiner', 'Vmoney1337', 'theBelatedLobster', 'RamsesThePigeon', 'way_fairer', 'Ambiguously_Ironic', 'PrinceCamelton', 'kijafa', 'StickleyMan', 'JavaReallySucks', 'Elaus', 'thunderbert80', 'boib', 'APOSTOLATE', 'IAmTheRedWizards', 'SomeCalcium', 'warlizard', 'anutensil', 'zomboi', 'dick-nipples', '-eDgaR-', 'smeeee', 'Painmatrix', 'GoldCountach', 'Poem_for_your_sprog', 'ketralnis', 'drumcowski', 'Dacvak', 'X019', 'shadydentist', 'Slouching2Bethlehem', 'jedberg', 'Iraniangenius', 'pithyretort', 'DaedalusMinion', 'stopscopiesme', 'girafa', '_vargas_']
    for user in sample_reddit_users:
        try:
            download_and_save(user)
        except Exception as e:
            print user, ":", e.message

if __name__ == '__main__':
    main()