# coding UTF-8

"""
目標：生徒と生徒の得点を入力していくだけで自動的に偏差値を表示するプログラムの作成
"""
from datetime import datetime
import sys, csv, os, pprint
import matplotlib.pyplot as plt
import numpy as np


roop = int(input('生徒の総数を入力>> '))

n = 1
if n > roop:
    print('最初からやり直してください')
    sys.exit()
#生徒数0としてしまった場合の抜け道


##生徒リストの作成
class StudentList:

    def name_list(self, roop):
        global student_name
        student_name = []

        n = 1
        while n <= roop:
            n += 1
            name = input('生徒の名前を入力>> ')
            student_name.append(name)
        student_name.sort(reverse = False)
        #五十音順に並び替え
        print('グローバルリスト"student_name"が作成されました')
        print('student_name={}'.format(student_name))

        print('---------------------------------------------------')

        while True:
            conti = input('入力ミスはありますか？（y or n）>> ')
            if conti == 'y':
                print('最初からやり直してください')
                sys.exit()
            elif conti == 'n':
                return False

    def id(self, name_list):
        global student_id
        student_id = []
        for i in range(1, len(name_list)+1):
            student_id.append(i)
        print('生徒の出席番号は%x番まで存在します' %(student_id[-1]))
        print('---------------------------------------------------')

    def score_dic(self, roop, student_name):
        global student_score
        student_score = []
        global Scores

        n = 1
        while n <= roop:
            n += 1
            score = int(input('生徒の得点を入力（ただし名簿順）>> '))
            student_score.append(score)
            #.append()に,end=''は使えない

        print('グローバルリスト"stuent_score"が作成されました')
        print('student_score={}'.format(student_score))

        Scores = list(zip(student_name, student_score))
        print('グローバルディクショナリ"Scores"が作成されました')
        print('Scores={}'.format(Scores))
        print('---------------------------------------------------')

        while True:
            conti = input('入力ミスはありますか？（y or n）>> ')
            if conti == 'y':
                print('最初からやり直してください')
                sys.exit()
            elif conti == 'n':
                return False


student_L = StudentList()
student_L.name_list(roop)
#student_nameの作成

student_id = StudentList()
student_id.id(student_name)
#student_idの作成

student_L.score_dic(roop, student_name)
#student_score, Scoresの作成

##平均値の計算
score_ave = sum(student_score) / len(student_score)


##標準偏差の計算
StDv_list = []
n = 0
while n < len(student_score):
    StDv_element = (student_score[n] - score_ave) ** 2
    StDv_list.append(StDv_element)
    n += 1
standard_dev = sum(StDv_list) / len(student_score)

print(f'平均点：{score_ave: .3f}点\n標準偏差：{standard_dev: .3f}')


##偏差値の計算
deviation_value_list = []
n = 0
while n < len(student_score):
    one_DevVal = (student_score[n] - score_ave) * 10 / standard_dev + 50
    deviation_value_list.append(one_DevVal)
    n += 1
new_deviation_value_list = [round(deviation_value_list[i], 2) for i in range(len(deviation_value_list))]
#偏差値の少数第三位以下を切り捨て
Student_Grades = list(zip(student_id, student_name, student_score, new_deviation_value_list))


time = datetime.now()
f_altered_time = '{0:%y/%m/%d %H:%M:%S}'.format(time)

print('---------------------------------------------------')
print('\n＜成績表＞\n\n※[(出席番号, 名前, 得点, 標準偏差)]で表示されます')
pprint(Student_Grades)
print(f'\nGenerated：{f_altered_time}\n')


##csvに出力
def GenerateCSV():
    tag_list = ('id', 'name', 'score', 'deviation')
    Student_Grades.insert(0, tag_list)

    alt_alt_time = '{0:%y%m%d %H.%M.%S}'.format(time)
    #ファイル名に'/'はNG
    csv_name = 'StuDev' + '' + alt_alt_time + '.csv'
    f = open(csv_name, 'w', encoding='utf-8', newline='')
    #引数の'w'はモードの指定、'newline'は改行コード
    writer = csv.writer(f)
    for x in Student_Grades:
        element = list(x)
        writer.writerow(x)
    f.close()

GenerateCSV()



##頻度のグラフ化
def MakeGragh():
    open_file = input("グラフ化したいcsvファイルを入力>> ")
    if not os.path.isfile(open_file):
        return f"ファイル:{open_file}は存在しません"

    data_set = np.loadtxt(fname=open_file, dtype='float', delimiter=',')
    #csvファイルの読み込み
    for data in data_set:
        print(data[0])
        print(data[1])
        print(data[2])

MakeGragh()
