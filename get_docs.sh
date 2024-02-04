#!/usr/bin/env bash
git clone https://github.com/pallets/flask
pushd ./flask/docs
make html
popd
ln -s ./flask/docs/_build/html ./docs
