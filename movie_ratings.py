# new.py
import csv

mega_list = []

with open('./ratings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    num_appended = 0
    for row in csv_reader:
        mega_list.append(row)
        num_appended += 1
        if num_appended > 300:
            break

'''
for mini_list in mega_list[:100]:
    print(mini_list)
'''
   
total_1_scores = 0
num_1_score = 0
user_id = 1

for mini_list in mega_list[1:]:
    if int(mini_list[0]) == user_id:
        num_1_score = num_1_score + float(mini_list[2])
        total_1_scores += 1
        user_id += 1

user_rankings_dict = {}
for mini_list in mega_list[1:]:
    userId = int(mini_list[0])
    if not (userId in user_rankings_dict):
        user_rankings_dict[userId] = [float(mini_list[2])]
    else:
        user_rankings_dict[userId].append(float(mini_list[2]))

user_id = 1

for key in user_rankings_dict:
    average = (sum(user_rankings_dict[key])/len(user_rankings_dict[key]))
    print("user " + str(user_id) + "'s average movie score = " + str((round(average,1))))
    user_id += 1

# loop through the dictionary
# calculate average movie ranking for each user

