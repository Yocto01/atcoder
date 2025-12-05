H,B = gets.chomp.split(" ").map(&:to_i)
if H > B
  puts H - B
else
  puts 0
end
  
