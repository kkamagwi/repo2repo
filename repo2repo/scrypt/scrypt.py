import os

origin = 'origin'
path_to_folder = '../git_project'


# clone code and add origin
def clone(source_repo_adress):
    # SSL auth
    os.system('git config --system http.sslCAInfo /home/javl/git-certs/cert.pem')   

    os.makedirs(path_to_folder)
    os.system('git init')
    os.system(f'git clone {source_repo_adress}')
    os.system(f'git add {origin} {source_repo_adress}')

def pull_branch(source_branch):
    os.system(f'git pull {origin} {source_branch}')


def push_branch(destination_repo_adress, destination_branch, source_branch):
    # os.system('git add .')
    # commit_name = str(os.system('git log -1 --pretty=%B'))[:-1]
    # os.system(f'git commit -m "{commit_name}"')
    # git remote add [url]
    os.system(f'git checkout -b {destination_branch}')
    # git remote add origin3 https://github.com/kkamagwi28/test.git
    os.system(f'git push {destination_repo_adress} {source_branch}:{destination_branch}')

