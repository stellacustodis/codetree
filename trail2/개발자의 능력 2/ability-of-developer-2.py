ability = list(map(int, input().split()))

# Please write your code here.
sort_ability = sorted(ability)
# print(sort_ability)

team_a = sort_ability[0]+sort_ability[-1]
team_b = sort_ability[1]+sort_ability[-2]
team_c = sort_ability[2]+sort_ability[-3]

# print(team_a, team_b, team_c)
MIN = min(min(team_a,team_b),team_c)
MAX = max(max(team_a,team_b),team_c)

print(MAX-MIN)