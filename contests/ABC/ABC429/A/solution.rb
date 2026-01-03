N,M = gets.split.map(&:to_i)
for i in 1..N
  if i <= M
    puts "OK"
  else
    puts "Too Many Requests"
  end
end