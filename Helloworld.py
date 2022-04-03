# ref0
# https://docs.python.org/3/library/asyncio.html

# import asyncio
# import pandas as pd

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')

# # Python 3.7+
# asyncio.run(main())

# ref1
# https://phyblas.hinaboshi.com/20200315

# ref2
# https://nopnithi.medium.com/python-asynchronous-i-o-%E0%B8%84%E0%B8%B7%E0%B8%AD%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3-%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%95%E0%B8%B1%E0%B8%A7%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89-asyncio-%E0%B9%80%E0%B8%9A%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%95%E0%B9%89%E0%B8%99-93d523211427

import pandas as pd

def main():
    dflist = pd.read_html('https://www.set.or.th/set/companyprofile.do?symbol=ACE&country=TH'
                        , match="ชื่อบริษัท" ,encoding='utf8')
    df = dflist[0]
    # print(df)
    # print((df.loc[[0]]))
    # df.loc[[0]].to_csv('test')

    # x = str(df.loc[[0]])
    # y = x.replace('0','')
    # print(y.strip())
    # y.replace('ที่อยู่','#ที่อยู่')

    df.loc[[0]].astype(str)
    df.to_csv('test')

main()