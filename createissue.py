#!/usr/bin/env python3

import json
import sys
import os

import requests

from pelicanconf import GITHUB_REPO

s = requests.Session()

def github_list_issues():
  if 'GH_TOKEN' not in os.environ:
    print("Error: please set GH_TOKEN env var")
    sys.exit(1)
  token = os.environ['GH_TOKEN']
  headers = {'Authorization': "token " + token}
  url = 'https://api.github.com/repos/%s/issues' % GITHUB_REPO
  resp = s.get(url, headers=headers)
  content = json.loads(resp.content.decode('utf-8'))
  slug2ids = {}
  for issue in content:
    slug2ids[issue["title"]] = int(issue["number"])
  return slug2ids

def github_create_issue(subject, message):
  if 'GH_TOKEN' not in os.environ:
    return None
  token = os.environ['GH_TOKEN']
  data = {'title': subject, 'body': message}
  headers = {'Authorization': "token " + token}
  url = 'https://api.github.com/repos/%s/issues' % GITHUB_REPO
  resp = s.post(url, headers=headers, data=json.dumps(data))
  content = json.loads(resp.content.decode('utf-8'))
  return content["number"]

def extract_slug(path):
  slug, issueid = None, None
  with open(path) as fd:
    for line in fd:
      if line.startswith(":slug:"):
        slug = line[len(":slug:"):-1].strip()
      if line.startswith(":issueid:"):
        issueid = int(line[len(":issueid:"):-1].strip())
    return path, slug, issueid

def find_slugs():
  for root, dirs, files in os.walk("content"):
    for filename in files:
      if filename.endswith(".rst"):
        filepath = os.path.join(root, filename)
        yield extract_slug(filepath)

def main():
  slug2ids = github_list_issues()
  for path, slug, issueid in find_slugs():
    if slug == None:
      print("ERROR: file %s don't have slug" % path)
      continue
    if slug in slug2ids:
      if issueid == None:
        print("WARN: file %s should have issueid %s" % (path, slug2ids[slug]))
        continue
      if issueid != slug2ids[slug]:
        print("ERROR: file %s with slug %s have id %s mismatch github id %s " % (path, slug, issueid, slug2ids[slug]))
        continue
    if issueid == None:
      message = "This issue is reserved for https://farseerfc.me/%s.html" % slug
      newissueid = github_create_issue(slug, message)
      print("%s :issueid: %s" % (path, newissueid))
      slug2ids[slug] = newissueid
      continue

if __name__ == '__main__':
  main()