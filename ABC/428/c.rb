Q = gets.chomp.to_i

left = 0
right = 0
error = false
over = 0
str = []

Q.times do |i|
  query = gets.chomp

  if query == '2'
    if error
      over -= 1
      if over == 0
        error = false
        str.pop
        right -= 1
      end
    else
      c = str.pop
      if c == '('
        left -= 1
      else
        right -= 1
      end
    end
  else
    if error
      over += 1
    else
      str << query[2]
      if query[2] == '('
        left += 1
      else
        right += 1
      end
    end
    
    if !error && left < right
      error = true
      over = 1
    end
  end

  if !error && left == right
    puts "Yes"
  else
    puts "No"
  end
end
      
