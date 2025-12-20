N,M = gets.chomp.split(" ").map(&:to_i)
a = gets.chomp.split(" ").map(&:to_i)
b = gets.chomp.split(" ").map(&:to_i)
a.sort!.reverse!
b.sort!.reverse!
ans = 0
asum = a.sum
asubsum = 0
asums = []
i = 0
M.times do |j|
  while true
    if i >= N || a[i] < b[j]
      ans += asubsum - b[j]*i + b[j]*(N-i) - (asum - asubsum)
      ans %= 998244353
      break
    end
    if a[i] >= b[j]
      asubsum += a[i]
      i += 1
    end
  end
end
puts ans

