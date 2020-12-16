import json
import os
import shutil

from src import get

# main
if __name__ == '__main__':
    # file
    file_setting = './data/setting.json'
    file_updated = './data/updated.json'
    chdir = os.getcwd()

    # load setting.json
    f = open(file_setting, 'r')
    setting = json.load(f)
    username = setting["username"]
    backup_folder = setting["backup_folder"]

    # load updated.json
    f = open(file_updated, 'r')
    all_updated = json.load(f)

    # get repository list
    repos = get.get_json(
        'https://api.github.com/users/{0}/repos?per_page=100'.format(username))
    
    # update the backup
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    os.chdir(backup_folder)
    for r in repos:
        updated_at = r["updated_at"]
        html_url = r["html_url"]
        name = r["name"]
        if name not in all_updated or all_updated[name] != updated_at:
            print("\n>> update", name)
            if not os.path.exists('{0}'.format(name)):
                os.system('git clone {0}'.format(html_url))   # clone
            else:
                os.chdir('{0}'.format(name))
                os.system('git cehckout .')
                os.system('git pull')   # pull
                os.chdir('../')
            all_updated[name] = updated_at
    os.chdir(chdir)

    # save
    with open(file_updated, 'w') as outfile:
        json.dump(all_updated, outfile, indent=2)

    # exit
    exit()

