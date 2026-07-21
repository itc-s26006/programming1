import random

def generate_students_data(num_students=10):
    '''生徒名,身長,体重からなるデータをランダムに生成する

    引数:num_students:生徒の人数を取る
    戻り:num_students:個のタプル(生徒名,身長,体重)からなるリスト

    データの内容
        生徒名 'nXx,XX は10から50の番号
        身長150-190cm からランダムに選んだ値
        体重 50-80kg からランダムに選んだ値
    '''
    students_data = []
    for i in range(num_students):
        name = 'n' + str(random.randint(10, 50))  # radint -> randint
        height = random.randint(150, 190)
        weight = random.randint(50, 80)
        students_data.append((name, height, weight))
        
        if i == 0:
            print('i,name,height,weight')
        if i < 2 or i == num_students - 1:
            print(i, name, height, weight)
        elif i == 2:
            print('...')
            
    return students_data  # forループの外に出す

students_data = generate_students_data(10)  # 関数名を統一
print('\nsort by height')
for student in students_by_height:
    print(student)

print('\nsort by weight')
for student in student_by_weight:
    print(student)
