import requests
from pprint import pprint
import base64
from github import Github
from pprint import pprint

# github username
#username = "alantrivandrum"
# url to request
#url = f"https://api.github.com/users/{username}"
# make the request and return the json
#user_data = requests.get(url).json()
# pretty print JSON data
#pprint(user_data)
username = "alantrivandrum"
token = "b68d278003effe737b9654e88d183ca88a1eb43a"
# pygithub object
g = Github(token)
# get that user by username
user = g.get_user(username)
#print(user.get_repos)


def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    #print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    print("")
    # the date of the last git push
    #print("Date of last push:", repo.pushed_at)
    # home website (if available)
    #print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    #print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    #print("-"*50)
    # repository content (files & directories)
    #print("Contents:")
    #for content in repo.get_contents(""):
    #    print(content)
    #try:
        # repo license
    #    print("License:", base64.b64decode(repo.get_license().content.encode()).decode())
    #except:
    #    pass

def getRepoCommits(repo):
    try:
        if repo.get_commits() is not None:
            commits = repo.get_commits().totalCount
            print(f"Number of commits: {commits}")
    except:
        print("Number of commits: 0")
    


count = 0
for repo in user.get_repos():
    count =  count + 1
    if repo is not None:
        print("---------------------------------------------------------------------------------")
        print(f"{count}: ")
        print_repo(repo)
        getRepoCommits(repo)
        print("---------------------------------------------------------------------------------")
