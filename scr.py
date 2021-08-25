import os
from github import Github
import requests


class Repo:
    # TODO change customer to target and devs to source
    customer_access_token = os.environ.get("customer_access_token", 
                                            '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')
    # customer_url = "https://raw.githubusercontent.com/kkamagwi/bot28/master/bot.py"
    # req = requests.get(url=customer_url)
    # if req.status_code == requests.codes.ok:
    #     file_content = req.text
    file_content = 'req.text'
    customer_repo = "kkamagwi/generic"
    customer_branch="test"
    file_name = 'scr12.py'
    # TODO get file names
    commit_name = 'commit_name123'
    # TODO get all commits names


    # DEVs info
    devs_access_token = os.environ.get("devs_access_token", 
                                        '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')
    destination_branch = 'test'
    def get_branches(self, g):
        repo = g.get_repo(self.customer_repo)
        return list(repo.get_branches())

    def pull(self):
        try:
            # using an access token
            g = Github(self.devs_access_token)
        except:
            # Github Enterprise with custom hostname
            g = Github(base_url="https://{hostname}/api/v3", login_or_token=self.devs_access_token)
        repo = g.get_repo(self.customer_repo)

        try:
            branch = repo.get_branch(branch=self.customer_branch)
        except:
            repo = g.get_repo(self.customer_repo)
            last_branch = list(repo.get_branches())[-1].name
            sb = g.get_repo(self.customer_repo).get_branch(last_branch)
        last_branch = list(repo.get_branches())[-1].name
        sb = g.get_repo(self.customer_repo).get_branch(last_branch)
        print(sb.commit.sha)
    


    def push(self):
        try:
            # using an access token
            g = Github(self.customer_access_token)
        except:
            # Github Enterprise with custom hostname
            # TODO make credatial for Enterprise
            g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
        
        # Get or create branch
        repo = g.get_repo(self.customer_repo)
        try:
            repo.get_branch(branch=self.customer_branch)
        except:
            repo = g.get_repo(self.customer_repo)
            last_branch = list(repo.get_branches())[-1].name
            sb = g.get_repo(self.customer_repo).get_branch(last_branch)
            repo.create_git_ref(ref='refs/heads/' + self.customer_branch, sha=sb.commit.sha)
        
        

        # Create file
        repo.create_file(self.file_name, 
                        self.commit_name, 
                        self.file_content)

        # TODO update file
        contents = repo.get_contents(self.file_name, ref="test")
        repo.update_file(contents.path, self.commit_name, self.file_content, contents.sha, branch=self.destination_branch)

r = Repo()
r.pull()
