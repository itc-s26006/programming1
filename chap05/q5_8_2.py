data =[ 
['01','0001','Male','Yamada','Tarou','25','Tokyo'],
['01','0002','Male','satou','Takesh','27','kanagawa'],
['01','0003','Female','tanaka','yuko','25','saitama'],
['02','0001','Male','smith','mike','22','newjersey'],
['02','0002','Male','Turner','Tom','27','kansas'],
['03','0003','Male','Jackson','David','22','florida']
]

data
member_information={}

#表データをレコードごとに格納する
for record in data:
    key = (record[0],record[1])
    info = record[2:]
    member_information[key]=info

print('number','information',sep='\t')
for key, info in member_information.items():
    print(key,info)

