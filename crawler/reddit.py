import praw
from collections import defaultdict
from configobj import ConfigObj

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
        f.write(str(data))

def download_and_save(username):
    data = download_comments(username)
    save_file(data, './data/' + username + '.data')

def main():
    top20_redditor = ["StickleyMan", "_vargas_","Unidan", "Iraniangenius", "awildsketchappeared", "Painmatrix", "straydog1980", "RamsesThePigeon", "-eDgaR-", "Jux_", "APOSTOLATE", "kijafa", "Thehealeroftri", "warlizard", "danrennt98", "smeeee", "Donald_Keyman", "dick-nipples", "Poem_for_your_sprog"]
    random_redditor = ['shadowman3001', 'PrinceCamelton', 'thunderbert80', 'Dacvak',
                       'Rlight','nix0n','manbra', 'Geekymumma', 'lanismycousin',
                       'qgyh2', 'maxwellhill', 'BritishEnglishPolice', 'anutensil',
                       'girafa', 'theBelatedLobster', 'SomeCalcium', 'Vmoney1337',
                       'iBleeedorange', 'AutoModerator', 'drumcowski', 'ManWithoutModem',
                       'stopscopiesme', 'IAmAN00bie', 'Dacvak', 'jedberg', 'ketralnis',
                       'shadydentist', 'qgyh2', 'ketralnis', 'X019', 'rotorcowboy', 'illuminatedwax',
                       'axolotl_peyotl', 'User_Name13', 'Ambiguously_Ironic', 'DaedalusMinion',
                       'pithyretort', 'boib', 'brigodon', 'themightiestduck', 'IAmTheRedWizards',
                       'Abe_lincolin', 'zomboi', 'CycleModRecs']
    for user in random_redditor:
        try:
            download_and_save(user)
        except Exception as e:
            print user, ":", e.message

if __name__ == '__main__':
    main()