N = gets.chomp.to_i
a = gets.chomp.split(" ").map(&:to_i)

s = [0]
N.times do |i|
  s[i+1] = s[i] + a[i]
end

cnt = 0
for l in 1..N
  for r in l..N
    sum = s[r] - s[l-1]
    is = true
    for i in l..r
      if sum % a[i-1] == 0
        is = false
      end
    end
    cnt += 1 if is
  end
end

puts cnt

    
