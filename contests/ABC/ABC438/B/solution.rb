N,M = gets.split.map(&:to_i)
S = gets.chomp
T = gets.chomp
min = 10**100
(N-M+1).times do |i|
  substr = S[i...i+M]
  t = T.dup
  cnt = 0
  M.times do |j|
    while t[j] != substr[j]
      if t[j] != '9'
        t[j] = (t[j].ord + 1).chr
      else
        t[j] = '0'
      end
      #puts "i = #{i},t = #{t}"

      cnt += 1
    end
  end
  #puts cnt
  min = [min,cnt].min
end
puts min