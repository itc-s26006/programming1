data=[
    ['0001','Male','Yamada','Tarou','25','Tokyo'],
    ['0002','Male','satou','Takesh','27','kanagawa'],
    ['0003','female','tanaka','yuko','25','saitama'],
    ['0004','Male','tanaka','suzuki','Ichirou','35','Hokkaidou']]
data

member_infomation={}
for record in data:
     key=record[0]
     info =record[1:]
     member_infomation[key]=info
print('number','information',sep='\t')
for key, info in member_infomation.items():
     print(key,info)





