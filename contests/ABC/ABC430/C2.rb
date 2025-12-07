# by ChatGPT
N, A, B = gets.split.map(&:to_i)
S = gets.chomp

b_count = 0
l_b = 0
a_pos = []
ans = 0

(0...N).each do |r|
  # bの個数を管理
  if S[r] == 'b'
    b_count += 1
  end

  # bがB個以上にならないように左を詰める
  while b_count >= B
    if S[l_b] == 'b'
      b_count -= 1
    end
    l_b += 1
  end

  # aの出現位置を管理
  if S[r] == 'a'
    a_pos << r
  end

  # aがA個以上あるときのみカウント可能
  if a_pos.size >= A
    l_a = a_pos[a_pos.size - A]
    l = [l_b, l_a].max
    if l <= r
      ans += r - l + 1
    end
  end
end

puts ans
