#!/usr/bin/python
# -*- coding: utf-8 -*-

# Gak keren bro kalo lu recode gak nyantumin nama author

# MIT License

# Copyright (c) 2023  [ Dvanmeploph - ( Ferly Afriliyan - Livian-xyz ) ] -

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#      Copyright (C) 2023  Itsmeafriliyan (https://github.com/Itsmeafriliyan)
#

import os
import sys
import json
import csv
import six
import requests

info = """
[-] Username  : %s

[-] Name      : %s
[-] Followers : %s
[-] Following : %s

[-] Location  : %s
[-] Email     : %s
[-] Twitter   : %s
[-] Blog      : %s
[-] Company   : %s
[-] Hireable  : %s

[-] Total Repository : %s
[-] Total Gists      : %s
[-] Joined Github at : %s
[-] Recent Activity  : %s

[-] Github URL   : https://github.com/%s
[-] Repositories : https://github.com/%s/repositories
[-] Avatar       : %s
"""

def status(user):
    main = requests.get("https://api.github.com/users/%s" % (user))
    if main.status_code == 200:
        pass
    elif main.status_code == 404:
        print('No Github Account with that Username !')
        sys.exit()
    else:
        print('Github api issue. Try again After Some Time')
        sys.exit()

def stats(user):
    status(user)
    main = requests.get("https://api.github.com/users/%s" % (user))
    dump = json.loads(main.text)

    h1 = dump['login']
    h2 = dump['name']
    h3 = dump['followers']
    h4 = dump['following']
    h5 = dump['location']
    h6 = dump['email']
    h7 = dump['twitter_username']
    h8 = dump['blog']
    h9 = dump['company']
    h10 = dump['hireable']
    h11 = dump['public_repos']
    h12 = dump['public_gists']
    h13 = dump['created_at']
    h14 = dump['updated_at']
    h15 = dump['avatar_url']

    print(info % (h1, h2, h3, h4, h5, h6, h7, h8,
          h9, h10, h11, h12, h13, h14, h1, h1, h15))

    orgs = requests.get("https://api.github.com/users/%s/orgs" % (user))
    orgs_dump = json.loads(orgs.text)
    for hulu in orgs_dump:
        print('[-] Organization : {} '.format(hulu['login']))

    stats=[]
    total_star, total_fork = 0, 0

    if h11 > 100: page_c = (h11 // 100) + 1
    else: page_c = 1

    for i in range(page_c):
        repos = requests.get("https://api.github.com/users/%s/repos?page=%s&per_page=100" % (user,i+1))
        repo_dump = json.loads(repos.text)
        for x in repo_dump:
            stats.append((x['name'],x['stargazers_count'],x['forks_count'],x['clone_url']))
            total_star += int(x['stargazers_count'])
            total_fork += int(x['forks_count'])

    print('')
    print('[-] Total Stars  : '+str(total_star))
    print('[-] Total Forks  : '+str(total_fork))
    print('')

    save_repo = six.moves.input('[-] Save Repository List as .csv ? [Y/n] : ')
    print('')

    if save_repo == "y" or save_repo == "Y":
        with open("%s.csv" % (user), "w") as f:
            output=csv.writer(f, lineterminator='\n')
            output.writerow(['Repository Name','Total Stars','Total Forks','Clone URL'])
            for row in stats:
                output.writerow(row)

        print("[-] File Saved as : %s.csv" % (user))
        print('')
    else:
        pass

note = """
 GithubStat (c) [ Ferly Afriliyan (Livian-xyz) ] <https://github.com/Livian-xyz>

 A Simple Github User Statistics Meter based on Github-API.

 Type GithubStat <your github username>

 Example : GithubStat Itsmeafriliyan

 If you Like this Project then don't Forget to leave a Star :)
"""

def main():
    if len(sys.argv) >= 2:
        try:
            stats(sys.argv[1])
        except Exception as exceptions:
            sys.exit(exceptions)
    else:
        sys.exit(note)

if __name__ == '__main__':
    main()
