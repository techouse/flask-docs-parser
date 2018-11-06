#!/usr/bin/env bash
git clone https://github.com/pallets/flask
cd ./flask/docs
make html
cd -
ln -s ./flask/docs/_build/html ./docs
