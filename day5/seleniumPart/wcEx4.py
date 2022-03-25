import pandas as pd

danawa_data = pd.read_csv('./files/danawa_final.csv')
danawa_data = danawa_data.dropna(axis=0)
tot_suction = danawa_data.sort_values(['흡입력'], ascending=False)
#print(tot_suction)

tot_utime = danawa_data.sort_values(['사용시간'], ascending=False)
#print(tot_utime)

tot_utime_suction = danawa_data.sort_values(['사용시간', '흡입력'], ascending=False)
#print(tot_utime_suction)

print('가격 평균 값:', danawa_data['가격'].mean())
print('흡입력 평균 값:', danawa_data['흡입력'].mean())
print('사용시간 평균 값:', danawa_data['사용시간'].mean())