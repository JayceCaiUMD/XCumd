import requests
import time
import datetime
import openpyxl


def parse_html(sheet, url):
    # 伪造请求头
    headers = {
        'Host': 'www.p2peye.com',
        'Referer': 'https://www.p2peye.com/shuju/ptsj/',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    # 发起get请求
    rsp = requests.get(url=url, headers=headers)

    # 遍历每一行
    # 这里全是做处理，结果为空或者-1或者0, 网页上显示的就是--
    for item in rsp.json():
        if item['jdbalance'] is None or float(item['jdbalance']) == 0.0 or float(item['jdbalance']) == -1.0:
            item['jdbalance'] = '--'
        else:
            item['jdbalance'] = item['jdbalance'] + '万'
        if item['cjmoney'] is None or float(item['cjmoney']) == 0.0 or float(item['cjmoney']) == -1.0:
            item['cjmoney'] = '--'
        else:
            item['cjmoney'] = item['cjmoney'] + '万'
        if item['dqcjpumber'] is None or float(item['dqcjpumber']) == 0.0 or float(item['dqcjpumber']) == -1.0:
            item['dqcjpumber'] = '--'
        else:
            item['dqcjpumber'] = item['dqcjpumber'] + '人'
        if item['dqjkpumber'] is None or float(item['dqjkpumber']) == 0.0 or float(item['dqjkpumber']) == -1.0:
            item['dqjkpumber'] = '--'
        else:
            item['dqjkpumber'] = item['dqjkpumber'] + '人'
        if item['pjcjsyrate'] is None or float(item['pjcjsyrate']) == 0.0 or float(item['pjcjsyrate']) == -1.0:
            item['pjcjsyrate'] = '--'
        else:
            item['pjcjsyrate'] = item['pjcjsyrate'] + '%'
        if item['yqmoney'] is None or float(item['yqmoney']) == 0.0 or float(item['yqmoney']) == -1.0:
            item['yqmoney'] = '--'
        else:
            item['yqmoney'] = item['yqmoney'] + '万'
        if item['zjjlrmoney'] is None or float(item['zjjlrmoney']) == 0.0 or float(item['zjjlrmoney']) == -1.0:
            item['zjjlrmoney'] = '--'
        else:
            item['zjjlrmoney'] = item['zjjlrmoney'] + '万'
        print([item['platname'], item['jdbalance'], item['cjmoney'], item['dqcjpumber'], item['dqjkpumber'],
               item['pjcjsyrate'], item['yqmoney'], item['zjjlrmoney']])

        # 添加每一行
        sheet.append([item['platname'], item['jdbalance'], item['cjmoney'], item['dqcjpumber'], item['dqjkpumber'],
               item['pjcjsyrate'], item['yqmoney'], item['zjjlrmoney']])


if __name__ == "__main__":

    # 创建excel
    xls = openpyxl.Workbook()

    # 生成开始时间和结束时间，2017到2019年
    start_day = datetime.date(2017, 7, 1)
    end_day = datetime.date(2019, 7, 1)
    # 遍历时间, 遍历两个时间的所有月份
    # 例如，2017-7, 2017-8, 2017-9...
    months = (end_day.year - start_day.year) * 12 + end_day.month - start_day.month
    month_range = ['%s-%s' % (start_day.year + mon // 12, mon % 12 + 1)
                   for mon in range(start_day.month - 1, start_day.month + months)]
    # 遍历每一月
    for month in month_range:
        print(month)
        # 创建sheet，每一月一个
        sheet = xls.create_sheet(month)
        title = ['platform', 'balance', 'transaction amount', 'population of lending', 'population of borrowing', 'average yield', 'balance overdue', 'net cash flow income']
        # 添加列头
        sheet.append(title)

        # 示例 2017年8月  ->  1501545600  -> 2017-8-1 8:0:0
        timeArray = time.strptime(month + '-1 8:0:0', "%Y-%m-%d %H:%M:%S")  # 手动拼接时间戳
        # 转换为时间戳:
        timeStamp = int(time.mktime(timeArray))

        # 请求地址通过浏览器f12调试查找
        # 提交方式为get方式, 请求参数为month： 时间戳类型
        # 手动拼接地址
        url = 'https://www.p2peye.com/platformData.php?mod=list&ajax=2&type=1&month={}'.format(timeStamp)
        # 解析每一月的网页数据
        # 并保存到excel中
        parse_html(sheet, url)

        # break

    # 保存
    xls.save('data of loan platform monthly.xlsx')
    print('over')

