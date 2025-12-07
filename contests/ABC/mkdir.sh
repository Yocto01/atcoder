#!/bin/bash

if [ -z "$1" ]; then
  echo "使い方:"
  echo "bash mkdir.sh ディレクトリ名"
  exit 1
fi

cp -r tmpl "$1"