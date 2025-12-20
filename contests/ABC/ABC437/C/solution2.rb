T = gets.to_i
T.times do
  n = gets.to_i
  power = 0
  stack = [[0,0]]
  n.times do
    w,p = gets.split.map(&:to_i)
    new_stack = []
    stack.each do |power,cnt|
      new_stack << [power + p, cnt]
      new_stack << [power - w, cnt + 1]
    end
    stack = new_stack
  end
  while true
    power,cnt = stack.pop
    if power >= 0
      puts cnt
      break
    end
  end
end