n = gets.chomp.to_i
a = Array.new(2025){Array.new(2025,0)}
b = Array.new(2025){Array.new(2025,0)}

# 二次元imos法
for k in 1..n
  u,d,l,r = gets.chomp.split(" ").map(&:to_i)
  d += 1
  r += 1
  a[u][l] += 1
  a[u][r] -= 1
  a[d][l] -= 1
  a[d][r] += 1
  b[u][l] += k
  b[u][r] -= k
  b[d][l] -= k
  b[d][r] += k
end

2025.times do |i|
  2025.times do |j|
    if j != 0
      a[i][j] += a[i][j-1]
      b[i][j] += b[i][j-1]
    end
  end
end

2025.times do |i|
  2025.times do |j|
    if i != 0
      a[i][j] += a[i-1][j]
      b[i][j] += b[i-1][j]
    end
  end
end

bk = Array.new(n+1,0)
for i in 1..2000
  for j in 1..2000
    bk[0] += 1 if a[i][j] == 0
    bk[b[i][j]] += 1 if a[i][j] == 1
  end
end 

for i in 1..n
  puts bk[0] + bk[i]
end