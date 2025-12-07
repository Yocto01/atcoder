# by ChatGPT
# 自分と同じ考え方の場合
# input
n, a_req, b_req = gets.split.map!(&:to_i)
s = gets.chomp
chars = s.chars
ans = 0

r_a = 0   # r_a は [l, r_a) が最小で a_count >= A となる r（半開区間）
r_b = 0   # r_b は [l, r_b) が最小で b_count >= B となる r（見つからなければ n+1 扱い）
ca = 0
cb = 0

(0...n).each do |l|
  # r_a を右へ動かして最小の r_a を作る（a の個数が A 以上になる最小の r_a）
  while r_a < n && ca < a_req
    ca += 1 if chars[r_a] == 'a'
    r_a += 1
  end

  # r_b を右へ動かして最小の r_b を作る（b の個数が B 以上になる最小の r_b）
  while r_b < n && cb < b_req
    cb += 1 if chars[r_b] == 'b'
    r_b += 1
  end

  # r_a が条件を満たしてない（=この l 以降どこまで伸ばしても a が A に達しない）なら終わり
  break if ca < a_req && r_a == n

  # 実際の r_b の位置（もし b_count < B で末尾まで来てしまったなら r_b を n+1 と扱う）
  effective_r_b = (cb < b_req ? n + 1 : r_b)

  # r の取りうる範囲は [r_a, effective_r_b)
  if ca >= a_req
    add = [0, effective_r_b - r_a].max
    ans += add
  end

  # 左端を 1 進めるのでカウントを減らす
  ca -= 1 if chars[l] == 'a'
  cb -= 1 if chars[l] == 'b'
end

puts ans