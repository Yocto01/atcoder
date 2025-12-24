# level 2
H,W = gets.split.map(&:to_i)
a = []
H.times do
  a << gets.split.map(&:to_i)
end

res = Array.new(H){Array.new(W,0)}
H.times do |i|
  s = a[i].sum
  W.times do |j|
    res[i][j] += s
  end
end

s2 = Array.new(W,0)
H.times do |i|
  W.times do |j|
    s2[j] += a[i][j]
  end
end

H.times do |i|
  W.times do |j|
    res[i][j] += s2[j] - a[i][j]
  end
end

H.times do |i|
  puts res[i].join(" ")
end
