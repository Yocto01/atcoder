N,M = gets.split.map(&:to_i)
cnt = 0
acc = Hash.new()
M.times do |i|
  can = true
  r,c = gets.split.map(&:to_i)

  for i in r-1..r+1
    for j in c-1..c+1
      can = false if acc.has_key?(i) && acc[i].include?(j)
    end
  end

  if can
    if !(acc.has_key?(r))
      acc[r] = []
    end
    acc[r] << c
    cnt += 1
  end
end
puts cnt