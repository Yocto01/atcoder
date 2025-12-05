N,A,B = gets.chomp.split(" ").map(&:to_i)
S = gets.chomp
S.insert(0,"b")
pos = []
acnt = 0
bcnt = 0
cnt = 0
(N+1).times do |i|
  pos << S[i]
  if S[i] == "a"
    acnt += 1
  end
  if S[i] == "b"
    bcnt += 1
  end
  if bcnt >= B
    if acnt >= A
      aval = acnt - A + 1 
      cnt += aval * (aval + 1) / 2
    end
    while pos.shift != "b"
      acnt -= 1
    end
    bcnt -= 1
  end
end

if acnt >= A
  aval = acnt - A + 1 
  cnt += aval * (aval + 1) / 2
end

puts cnt
