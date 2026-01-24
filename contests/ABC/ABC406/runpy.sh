#!/bin/bash

# 第1引数チェック
if [ -z "$1" ]; then
  echo "使い方:"
  echo "  bash runpy.sh A"
  echo "  bash runpy.sh A -log"
  echo "  bash runpy.sh A -logp"
  exit 1
fi

# --- a -logp：標準出力＋Log.txt ---
if [ "$2" = "-logp" ]; then
  python3 "$1/solution.py" < $1/input.txt | tee $1/input.txt
  exit 0
fi

# --- a -log：Log.txt のみに出力 ---
if [ "$2" = "-log" ]; then
  python3 "$1/solution.py" < $1/input.txt > $1/input.txt
  exit 0
fi

# --- a：通常実行 ---
python3 "$1/solution.py" < $1/input.txt