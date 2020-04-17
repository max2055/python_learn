#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import subprocess
import json
import sys


class RequestClient(object):

    def __init__(self, login_url, username, password):
        self.username = username
        self.password = password
        self.login_url = login_url
        self.session = requests.Session()
        self.login()

    def login(self):
        self.session.post(self.login_url, params={"principal": self.username, "password": self.password})


class HarborRepos(object):

    def __init__(self, harbor_domain, harbor_new_domain, password, new_password, schema="https", new_schema="https",
                 username="wucl", new_username="wucl"):
        self.schema = schema
        self.harbor_domain = harbor_domain
        self.harbor_new_domain = harbor_new_domain
        self.harbor_url = self.schema + "://" + self.harbor_domain
        self.login_url = self.harbor_url + "/login"
        self.api_url = self.harbor_url + "/api"
        self.pro_url = self.api_url + "/projects"
        self.repos_url = self.api_url + "/repositories"
        self.username = username
        self.password = password
        self.client = RequestClient(self.login_url, self.username, self.password)

        self.new_schema = new_schema
        self.harbor_new_url = self.new_schema + "://" + self.harbor_new_domain
        self.login_new_url = self.harbor_new_url + "/c/login"
        self.api_new_url = self.harbor_new_url + "/api"
        self.pro_new_url = self.api_new_url + "/projects"
        self.new_username = new_username
        self.new_password = new_password
        self.new_client = RequestClient(self.login_new_url, self.new_username, self.new_password)

    def __fetch_pros_obj(self):
        # TODO
        self.pros_obj = self.client.session.get(self.pro_url).json()

        return self.pros_obj

    def fetch_pros_id(self):
        self.pros_id = []
        # TODO
        pro_res = self.__fetch_pros_obj()

        for i in pro_res:
            self.pros_id.append(i['project_id'])

        return self.pros_id

    def fetch_pro_name(self, pro_id):
        # TODO
        pro_res = self.__fetch_pros_obj()

        for i in pro_res:
            if i["project_id"] == pro_id:
                self.pro_name = i["name"]

        return self.pro_name

    # def judge_pros(self,pro_name):
    #    res = self.new_client.session.head(self.pro_new_url,params={"project_name": pro_name})
    #    print(res.status_code)
    #    if res.status_code == 404:
    #        return False
    #    else:
    #        return True

    def fetch_repos_name(self, pro_id):
        self.repos_name = []

        repos_res = self.client.session.get(self.repos_url, params={"project_id": pro_id})
        # TODO
        for repo in repos_res.json():
            self.repos_name.append(repo['name'])
        return self.repos_name

    def fetch_repos(self, repo_name):
        self.repos = {}

        tag_url = self.repos_url + "/" + repo_name + "/tags"
        # TODO
        for tag in self.client.session.get(tag_url).json():
            full_repo_name = self.harbor_domain + "/" + repo_name + ":" + tag["name"]
            full_new_repo_name = self.harbor_new_domain + "/" + repo_name + ":" + tag["name"]
            self.repos[full_repo_name] = full_new_repo_name

        return self.repos


if __name__ == "__main__":
    harbor_domain = "10.17.73.38"
    harbor_new_domain = "10.17.75.30"
    re_pass = "Tpam1234"
    re_new_pass = "Tpam1234!"


    res = HarborRepos(harbor_domain, harbor_new_domain, re_pass, re_new_pass)
    # pros_id = res.fetch_pro_id()

    for pro_id in res.fetch_pros_id():
        #pro_id = 13
        pro_name = res.fetch_pro_name(pro_id)
        print(pro_name)
        ret = res.judge_pros(pro_name)
        print(ret)
        # res.create_pros(pro_name)
    #sys.exit() 
    for pro_id in res.fetch_pros_id():
        repos_name = res.fetch_repos_name(pro_id=pro_id)
        for repo_name in repos_name:
            repos = res.fetch_repos(repo_name=repo_name)
            for full_repo_name, full_new_repo_name in repos.items():
                res.migrate_repos(full_repo_name, full_new_repo_name, redis_conn)