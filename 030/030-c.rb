###WIP###

n,m = gets.chomp.split(" ").map(&:to_i)
x,y = gets.chomp.split(" ").map(&:to_i)
a_i = gets.chomp.split(" ").map(&:to_i)
b_j = gets.chomp.split(" ").map(&:to_i)

#n:空港Aから空港Bへの飛行機の本数
#m:空港Bから空港Aへの飛行器の本数
#x:空港Aから空港Bへの所要時間
#y:空港Bから空港Aへの所要時間
#a_i:空港Aを出発する時刻を格納した配列
#b_j:空港Bを出発する時刻を格納した配列

current_time = 0
current_place = A
ouhukukaisuu = 0

if current_place = A
  if current_time = a_i[i]
    current_time += x
    current_place = B
    ouhukukaisuu += 0.5
  end
else
  if current_time = b_j[j]
    current_time += y
    current_place = A
    ouhukukaisuu += 0.5
  end
end
