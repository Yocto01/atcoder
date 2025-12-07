S = gets.chomp

a = []
S.size.times do |i|
  if S[i] == "#"
    a << i+1
  end
end

(a.size/2).times do |i|
  puts "#{a[i*2+0]},#{a[i*2+1]}"
end