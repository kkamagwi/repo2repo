import os
import re


"""
'git config --system http.sslCAInfo /home/javl/git-certs/cert.pem'   

"""


def pull_branch(source_repo_adress, source_branch, sourse_id):
    # split = re.split('/', source_repo_adress)
    # project_folder = split[-1][:-4]	

    # # os.makedirs(f'repos/', exist_ok=True)
    # # os.system(f'cd repos')
    # os.makedirs(f'{project_folder}', exist_ok=True)
    # os.system('git init')
    # os.system(f'cd {project_folder}')
    # os.system(f'git clone {source_repo_adress}')
    # os.system(f'git remote add s{sourse_id} {source_repo_adress}')
    os.system(f'git pull s{sourse_id} {source_branch}')
    os.system(f'git fetch s{sourse_id}')
    
    os.system(f'git checkout --track s{sourse_id}/{source_branch}')


def push_branch(destination_repo_adress, destination_branch, destination_id):
    os.system(f'git remote add d{destination_id} {destination_repo_adress}')
    # os.system(f'git pull d{destination_id}')
    os.system(f'git fetch d{destination_id}')
    os.system(f'git branch -M {destination_branch}')
    os.system(f'git push d{destination_id} {destination_branch}')

