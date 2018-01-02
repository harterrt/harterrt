#!/bin/bash

branch="post-{{cookiecutter.slug}}" &&
git checkout master &&
git checkout -b $branch &&
git push -u origin $branch
