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
    df0 = dflist[0]
    x = df0.values.tolist()
    dict_za = ['ชื่อบริษัท',
                'ที่อยู่',
                'เบอร์โทรศัพท์',
                'เว็บไซต์',
                'กลุ่มอุตสาหกรรม',
                'หมวดธุรกิจ',
                'ทุนจดทะเบียน',
                'ทุนจดทะเบียนชำระแล้ว',
                'นโยบายเงินปันผล',
                ]
    delete_list = ['เบอร์โทรสาร','แบบ','วันที่เริ่มต้นซื้อขาย','หุ้นบุริมสิทธิ','ข้อจำกัดหุ้นต่างด้าว','ตามกฎหมายรายชื่อกรรมการล่าสุด']
    txt = ''
    txt1 = ''
    index = []
    data_Info = []
    final_Info = []


    for i in range(len(x)):
        y = str(x[i][0]).strip()
        txt += y

    for key in dict_za:
        index.append(txt.find(key))
    index.append(len(txt))


    for k in range(len(index)):
        if k < len(index)-1:
            data_Info.append(str(txt[index[k]:index[k+1]]).strip())

    # print(data_Info)
    for l in data_Info:
        # print(l)
        for m in delete_list:
            # print(m)
            if not l.find(m) == -1:
                l = l[:l.find(m)]

        final_Info.append(str(l).strip())

    print(final_Info)


main()