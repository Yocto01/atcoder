T = gets.chomp.to_i

T.times do |i|
  N,H = gets.chomp.split(" ").map(&:to_i)
  a = [[0,H,H]]
  N.times do
	  a << gets.chomp.split(" ").map(&:to_i)
  end
  can = true

  nextrange = [H,H]
  N.times do |i|
    nowrange = nextrange
    dt = a[i+1][0] - a[i][0]
    range = a[i+1][1..2]
    canrange = [nowrange[0]-dt,nowrange[1]+dt]

    if canrange[0] > range[1] || canrange[1] < range[0]
      can = false
      break
    end

    nextrange = []
    nextrange[0] = [canrange[0],range[0]].max
    nextrange[1] = [canrange[1],range[1]].min
  end

  if can
    puts "Yes"
  else
    puts "No"
  end
end