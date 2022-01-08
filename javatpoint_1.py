import random
import math
train_length = int(input("Enter the length of the train:"))
crossing_time = int(input("Enter the time for the train to cross the man:"))
t_l = ( train_length / 1000)
c_t = ( crossing_time / 3600)
m_s = int(input("Enter the speed of the man:"))
relative_speed = (t_l / c_t)
t_s = (relative_speed + m_s) 
print(t_s)
exit (0)
