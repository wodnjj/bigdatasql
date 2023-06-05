import mylib
import dbdb

print('음원 차트 보기 프로그램')
print('1.데이터 갱신')
print('2.데이터 보기')
print('3.데이터검색(가수이름으로)')

# 사용자에게 입력받기
num = input('선택 번호 입력: ')

# 만약에 1번이면 멜론 정보 가져와서 디비에 저장
if num == '1':
    print('멜론 정보 가져와서 디비에 저장')
# 만약에 2번이면 디비에 저장된 데이터 보기
elif num == '2':
    print('디비에 저장된 데이터 보기')
    m_list = dbdb.get_data() # 디비에서 데이터 가져오기
    for m in m_list:
        print(f"{m[0]}위 {m[1]} - {m[2]}")
# 만약에 3번이면 가수이름 입력받기 만들기
elif num == '3':
    print('가수이름 입력받기 만들기')
    # 가수를 입력 받으면 입력받은 가수이름으로 검색된 데이터 보여주기
    gasu = input('가수이름 입력: ')
    print(f'당신이 검색하고 싶은 가수 이름은 {gasu} 입니다')

# 멜론 가져오기
#m_list = mylib.melon()
# print(m_list)
# 멜론에서 가져온 데이터 리스트를 DB에 넣기 위해
#dbdb.save_data(m_list)

# dbdb.get_data()


# print('가수 이름으로 검색')
# artist = input('가수이름입력: ')
# m_list = dbdb.get_one_data(artist)
# for m in m_list:
#     print(f'{m[0]}위 {m[1]} - {m[2]}')  