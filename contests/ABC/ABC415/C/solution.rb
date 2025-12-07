T = gets.chomp.to_i

T.times do |c|
  n = gets.chomp.to_i
  s = gets.chomp 
  s = "0"+s # 状態0を追加

  ok = Array.new(1<<n,false)
  ok[0]=true
  # bit全探索
  for i in 0...(1<<n)
    next if !ok[i]  # すでに探索済みなら
    n.times do |j|
      next if i&(1<<j) > 0  # すでに混ぜた後なら
      nxt = (i|(1<<j))  # 混ぜる
      ok[nxt] = true if s[nxt] == '0' # 移動さきの状態が大丈夫なら
    end
  end

  puts (ok[(1<<n)-1] ? "Yes" : "No")
end



