N = gets.to_i

dp = [0]
prev = []

N.times do
  w, h, b = gets.split.map(&:to_i)

  # prev に dp を移して dp を空にする
  prev, dp = dp, prev
  m = prev.length
  dp.fill(0, dp.length...(m + w))  # dp を m + w に拡張（不足分は 0）

  # DP 遷移
  m.times do |i|
    # 頭に取り付ける（重さは i）
    dp[i] = [dp[i], prev[i] + h].max

    # 体に取り付ける（重さは i + w）
    dp[i + w] = [dp[i + w], prev[i] + b].max
  end
end

# dp の後半から最大値を取る
half = dp.length / 2
puts dp[half..].max