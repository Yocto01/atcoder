N,M = gets.chomp.split(" ").map(&:to_i)
S = []
N.times do |i|
  S << gets.chomp
end

collect = []
for c in 0..N-M
  for d in 0..N-M
    subgrid = ""
    M.times do |i|
      subgrid << S[c+i][d..d+M-1]
    end
    collect << subgrid
  end
end

pattern = collect.uniq

puts pattern.size