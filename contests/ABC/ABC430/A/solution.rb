A,B,C,D = gets.chomp.split(" ").map(&:to_i)

if A <= C && B > D
  puts "Yes"
else
  puts "No"
end