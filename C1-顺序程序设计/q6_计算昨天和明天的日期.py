# q6_计算昨天和明天的日期,使用datatime.timedelta获取一天的日期类型进行加减
import datetime

one = datetime.timedelta(days=1)

today = datetime.date.today()
yestoday = today - one
tomorrow = today + one

print(yestoday, tomorrow)
