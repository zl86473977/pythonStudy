slang_dict = {
    '觉醒年代': 'xxxxxxxxxxxxxxxxxxx',
    'yyds': 'yyyyyyyyyyyyyyyyyyy',
}

slang_dict['双减'] = 'sssssssssssssssssssssssss'
slang_dict['破防'] = 'ppppppppppppppppppppppppp'
slang_dict['元宇宙'] = 'zzzzzzzzzzzzzzzzzzz'
slang_dict['绝绝子'] = 'jjjjjjjjjjjjjjjjjjj'
slang_dict['躺平'] = 'ttttttttttttttttttt'
slang_dict['伤害性不高，侮辱性极强'] = 'gggggggggggggggggg'


query = input("请输入:")

if query in slang_dict:
    print('您查询的' + query + '含义如下')
    print(slang_dict[query])
else:
    print('您查询的暂不存在');
    print('当前本词典收入词条数为:' + str(len(slang_dict)))