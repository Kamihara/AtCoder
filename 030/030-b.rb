n,m = gets.chomp.split(" ").map(&:to_i)

hourAngle = (n % 12) * 30 + m * 0.5
minuteAngle = m * 6

if hourAngle > minuteAngle
  angle = hourAngle - minuteAngle
else
  angle = minuteAngle - hourAngle
end

if angle < 180
  puts angle
else
  puts 360 - angle
end
