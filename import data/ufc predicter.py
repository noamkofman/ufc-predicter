import pandas as pd


pf = pd.read_csv(r'import data\ufcdata.csv.zip')
#           prints specific category (only)

print(pf.columns)





#     prints specific line
#print(pf.head(1))


#    gives all the values for the category
#print(pf['Attack'], pf['Name'])


#print(pf.loc[pf['R_fighter'] == "Merab Dvalishvili"])
#print(pf.sort_values(['R_win_by_KO/TKO'], ascending=  [1]))
user_input1 = input("Enter your first fighter" )

user_input2 = input("Enter your second fighter" )

#print(user_inp

# below we define what user_input is as R_fighter
filterd_pf = (pf.loc[pf['R_fighter'] == user_input1])
#opponent = user_input1['B_fighter']

# deifine userinput2 as second fighter
opponent_of_input1 = filterd_pf['B_fighter'].iloc[0]

# Filter the DataFrame to get data for the second fighter (using opponent_of_input1)
filterd_pf2 = pf[pf['R_fighter'] == opponent_of_input1]


# here we sort the results based on the most recent by 'date' so that it dosent spit out random fighters not in order
filterd_pf_sort = (filterd_pf.sort_values(['date'], ascending =False))

# fighter 2
filterd_pf_sort2 = (filterd_pf2.sort_values(['date'], ascending =False))

# below we define all the fighter stats based on kd rate age exedra
filterd_pf_sort['Age']= filterd_pf_sort['R_age']
filterd_pf_sort['avg_kd']= filterd_pf_sort['R_avg_KD']
filterd_pf_sort['win_sub']= filterd_pf_sort['R_win_by_Submission']

# fighter 2

filterd_pf_sort2['Age']= filterd_pf_sort2['R_age']
filterd_pf_sort2['avg_kd']= filterd_pf_sort2['R_avg_KD']
filterd_pf_sort2['win_sub']= filterd_pf_sort2['R_win_by_Submission']

kd_rate1 = float(filterd_pf_sort['avg_kd'].iloc[0])
kd_rate2 = float(filterd_pf_sort2['avg_kd'].iloc[0])

sub_rate1= float(filterd_pf_sort['win_sub'].iloc[0])
sub_rate2= float(filterd_pf_sort2['win_sub'].iloc[0])

doc_stop_rate= float(filterd_pf_sort['R_win_by_TKO_Doctor_Stoppage'].iloc[0])
doc_stop_rate2= float(filterd_pf_sort2['R_win_by_TKO_Doctor_Stoppage'].iloc[0])


Rreach1 = float(filterd_pf_sort['R_Reach_cms'].iloc[0])
Rreach2 = float(filterd_pf_sort2['R_Reach_cms'].iloc[0])


ko_rate1 = float(filterd_pf_sort2['R_win_by_KO/TKO'].iloc[0])
ko_rate2 = float(filterd_pf_sort2['R_win_by_KO/TKO'].iloc[0])

age1 = float(filterd_pf_sort2['R_age'].iloc[0])
age2 = float(filterd_pf_sort2['R_age'].iloc[0])

weight1 = float(filterd_pf_sort2['R_Weight_lbs'].iloc[0])
weight2 = float(filterd_pf_sort2['B_Weight_lbs'].iloc[0])

decsion1 = float(filterd_pf_sort2['R_win_by_Decision_Unanimous'].iloc[0])
decsion2 = float(filterd_pf_sort2['R_win_by_Decision_Unanimous'].iloc[0])

height1 = float(filterd_pf_sort2['R_Height_cms'].iloc[0])
height2 = float(filterd_pf_sort2['R_Height_cms'].iloc[0])


# here we print out the fighetr stats and sort it based on the latests result in .iloc[0]
# print(user_input1 + " age is: " + filterd_pf_sort['Age'].astype(str).iloc[0])
# print(user_input1 + " knockdown rate is:" + filterd_pf_sort['avg_kd'].astype(str).iloc[0])
# print(user_input1 + " wins by submisson is: " + filterd_pf_sort['win_sub'].astype(str).iloc[0] + "\n")

# # fighter 2
# print(user_input2 + " age is: " + filterd_pf_sort2['Age'].astype(str).iloc[0])
# print(user_input2 + " knockdown rate is"  + filterd_pf_sort2['avg_kd'].astype(str).iloc[0])
# print(user_input2 + " wins by submisson is: " + filterd_pf_sort2['win_sub'].astype(str).iloc[0])
# if one thing is better than other fighetr gets +1 point at the end fogjter with most pooints wins
user_points1 = 0
user_points2 = 0

# defining standard of predciting fights
if (kd_rate1 > kd_rate2):
    user_points1 += 1
else:
    user_points2 += 1
if (ko_rate1 > ko_rate2):
    user_points1 += 1
else:
    user_points2 += 1

if (sub_rate1 > sub_rate2):
    user_points1 += 1
else:
    user_points2 += 1
if (doc_stop_rate > doc_stop_rate2):
    user_points1 += 1
else:
    user_points2 += 1
if (Rreach1 > Rreach2):
    user_points1 += 1
else:
    user_points2 += 1
if (age1 > age2):
    user_points2 += 1
else:
    user_points1 += 1
if (weight1 > weight2):
    user_points1 += 1
else:
    user_points2 += 1
if (decsion1 > decsion2):
    user_points1 += 1
else:
    user_points2 += 1
if (height1 > height2):
    user_points1 += 0.5
else:
    user_points2 += 0.5







print(user_points1, user_points2)

if user_points1 > user_points2:
     print(user_input1 + " would beat " + user_input2)
else:
     print(user_input2 + " would beat " + user_input1)



# pit a fighter aginst another fighter
    

blue_fighter_matches = pf[pf['R_fighter'] == user_input1]

# Print the opponents and winners of the matches
# for index, row in blue_fighter_matches.iterrows():
#     opponent = row['R_fighter']

#below we define results of real fights
opponents = blue_fighter_matches['B_fighter'].unique()
won = blue_fighter_matches['Winner']

for opponent in opponents:
    matches_against_opponent = blue_fighter_matches[blue_fighter_matches['B_fighter'] == opponent]
    if (matches_against_opponent['Winner'] == 'Red').any():
        result = "won"
    else:
        result = "lost"
    print(user_input1 + " has fought: " + opponent + " and " + result)

    print("-------------------")
    if user_points1 > user_points2:
        print(user_input1 + " would beat " + opponent)
    else:
        print(opponent + " would beat " + user_input1 + " according to your algorithom")

    print(user_points2) 