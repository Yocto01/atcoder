N = gets.to_i
A = gets.split.map(&:to_i)

stack = []
now = 0
series = 0
z = [1,2,3]
A.each do |n|
  stack << n
  #p stack
  if stack[-1] == stack[-2] && stack[-2] == stack[-3] && stack[-3] == stack[-4]
    4.times do
      stack.pop()
    end
  end
end
puts stack.size