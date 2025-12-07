# 各クエリ後に Yes/No を出力する
Q = gets.to_i

sums = []   # 各長さでの累積和（最後が現在の合計）
mins = []   # 各長さでの prefix min（最後が現在までの最小値）

# 初期状態（長さ0）の累積和 0 と min 0 を空スタックとして扱うので、
# sums.empty? のときは sum=0, min=0 と解釈する。

Q.times do
  line = gets.chomp
  if line == '2'
    # pop（S は空でないことが保証されている）
    sums.pop
    mins.pop
  else
    # "1 c"
    c = line[2]  # '(' か ')'
    prev_sum = sums.empty? ? 0 : sums[-1]
    new_sum = prev_sum + (c == '(' ? 1 : -1)
    prev_min = mins.empty? ? 0 : mins[-1]
    new_min = [prev_min, new_sum].min
    sums.push(new_sum)
    mins.push(new_min)
  end

  # 判定
  if sums.empty?
    puts "Yes"   # 空文字列は良い括弧列
  else
    cur_sum = sums[-1]
    cur_min = mins[-1]
    if cur_sum == 0 && cur_min >= 0
      puts "Yes"
    else
      puts "No"
    end
  end
end