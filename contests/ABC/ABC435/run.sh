#!/bin/bash

# 第1引数チェック
if [ -z "$1" ]; then
  echo "使い方:"
  echo "  bash run.sh A"
  echo "  bash run.sh A -log"
  echo "  bash run.sh A -logp"
  exit 1
fi

# --- a -logp：標準出力＋Log.txt ---
if [ "$2" = "-logp" ]; then
  ruby "$1/solution.rb" < $1/input.txt | tee $1/output.txt
  exit 0
fi

# --- a -log：Log.txt のみに出力 ---
if [ "$2" = "-log" ]; then
  ruby "$1/solution.rb" < $1/input.txt > $1/output.txt
  exit 0
fi

# --- a：通常実行 ---
ruby "$1/solution.rb" < $1/input.txt