
import pandas as pd
from common import log

def code(value):
    import re
    code = re.sub(r'[^0-9]', '', value)
    return code

from datetime import datetime
def date(value):
    value=str(value)
    value=value.replace(" ","")
    if value=="":
        return value
    if value == "nan":
        return ""
    if value == "NaN":
        return ""
    if value=="--":
        return ""

    date_obj = datetime.strptime(value, "%Y%m%d")
        # 2. 使用 strftime 将 datetime 对象格式化为目标字符串
    value = date_obj.strftime("%Y-%m-%d")
    return value

def list_difference_set(list_a, list_b):
    """
    计算列表 A 和列表 B 的差集 (A - B)。
    结果包含所有在 A 中，但不在 B 中的元素。

    注意：此方法会自动去除重复元素。
    """
    # 1. 将列表转换为集合
    set_a = set(list_a)
    set_b = set(list_b)

    # 2. 计算集合差集 (set_a - set_b)
    difference_set = set_a - set_b

    # 3. 将结果转换回列表
    return list(difference_set)


def str2floatstr(value):
    import re
    value=str(value)

    dot_count=value.count(".")
    if dot_count>1:
        print("小数点个数",dot_count)
        print( "失败的行",value)
    if value=="":
        return ""
    if value == "nan":
        return ""
    if value == "NaN":
        return ""

    is_percent=False
    if "%" in value:
        is_percent=True

    # 先去掉两个负号避免被干扰
    value=value.replace(" ","")
    value=value.replace("--","")

    value = re.sub(r'[^0-9.\-]', '', value)

    if value == "":
        return ""

    if value == "-":
        return ""

    if value == ".":
        return ""


    # try:
    #     result=float(value)
    # except Exception as e:
    #     print(e)
    #     print(value)

    result=float(value)

    if is_percent:
        result=result/100
    return str(result)


def clean_str(value):
    value=str(value)


    value=value.replace(" ","")

    if value in ["","NaN","nan","--","无"]:
        return ""
    return value



def clean(raw_file_path: str) -> str:
    df = pd.read_csv(raw_file_path, encoding="gbk", sep="\t", dtype="str")
    df.columns = df.columns.str.replace(" ", "")
    df.columns = df.columns.str.replace("%", "")
    columns_to_drop = [".", "..1", "Unnamed:68"]
    df = df.drop(columns=columns_to_drop)
    df["代码"] = df["代码"].apply(code)
    df["上市日期"] = df["上市日期"].apply(date)
    str_list = [
        "代码",
        "名称",
        "备注",
        "利空",
        "利好",
        "细分行业",
        "所属行业",
        "异动类型",
        "自选时间",
        "上市日期"
    ]
    column_list = df.columns.tolist()
    number_list = list_difference_set(column_list, str_list)
    df[number_list] = df[number_list].applymap(str2floatstr)
    df = df[df["名称"] != "无"]
    df = df[df["代码"] != ""]
    df[str_list] = df[str_list].applymap(clean_str)
    df.to_csv("./cleaned_个股数据.csv", encoding="utf-8", index=False, sep=",")
    rename_map = {
        "代码": "code",
        "名称": "name",
        "涨幅": "change_rate",
        "现价": "current_price",
        "涨跌": "change_value",
        "买价": "buy_price",
        "卖价": "sell_price",
        "总手": "total_volume",
        "总金额": "total_amount",
        "现手": "current_volume",
        "1分钟涨速": "speed_1min",
        "实体涨幅": "real_change_rate",
        "现均差": "avg_diff",
        "换手": "turnover_rate",
        "委比": "order_ratio",
        "总市值": "total_market_cap",
        "流通市值": "circulating_market_cap",
        "流通比例": "circulation_ratio",
        "4分钟涨速": "speed_4min",
        "当日偏离值": "deviation_today",
        "异动偏离值": "deviation_unusual",
        "10日内偏离值": "deviation_10d",
        "30日内偏离值": "deviation_30d",
        "10日异动次数": "unusual_count_10d",
        "内盘": "inner_volume",
        "外盘": "outer_volume",
        "内外比": "inner_outer_ratio",
        "备注": "remark",
        "利空": "negative_factor",
        "利好": "positive_factor",
        "主力净量": "main_net_volume",
        "量比": "volume_ratio",
        "TTM市盈率": "pe_ttm",
        "净利润": "net_profit",
        "市净率": "pb_ratio",
        "每股盈利": "eps",
        "细分行业": "sub_industry",
        "所属行业": "industry",
        "昨收": "prev_close",
        "开盘": "open_price",
        "开盘涨幅": "open_change_rate",
        "竞价换手": "auction_turnover",
        "最高": "high_price",
        "最低": "low_price",
        "5日涨幅": "change_5d",
        "10日涨幅": "change_10d",
        "20日涨幅": "change_20d",
        "年初至今": "ytd_change",
        "振幅": "amplitude",
        "买量": "buy_volume",
        "卖量": "sell_volume",
        "笔数": "trade_count",
        "贡献度": "contribution",
        "机构动向": "institution_trend",
        "异动类型": "unusual_type",
        "总股本": "total_shares",
        "流通股本": "circulating_shares",
        "利润总额": "total_profit",
        "净利润增长率": "net_profit_growth",
        "每股净资产": "bvps",
        "金叉个数": "golden_cross_count",
        "散户数量": "retail_count",
        "自选时间": "self_select_time",
        "自选价格": "self_select_price",
        "自选收益": "self_select_profit",
        "上市日期": "listing_date"
    }

    df.rename(columns=rename_map, inplace=True)

    df.to_csv("./pg_import_stock.csv", encoding="utf-8", index=False, sep=",")
    log.info("清洗完成，生成文件 pg_import_stock.csv")
    print(df.info())

    kline_columns = [
        "code",
        "name",
        "open_price",
        "high_price",
        "low_price",
        "current_price",
        "change_rate",
        "amplitude",
        "total_volume",
        "total_amount",
        "turnover_rate",
        "trade_count"
        ]
    kline_df=df[kline_columns]
    kline_df.rename(columns={
        "code":"code",
        "name":"name",
        "open_price":"open",
        "high_price":"high",
        "low_price":"low",
        "current_price":"close",
        "change_rate":"change_rate",
        "amplitude":"amplitude",
        "total_volume":"volume",
        "total_amount":"amount",
        "turnover_rate":"turnover_rate",
        "trade_count":"trade_count",
    },inplace=True)
    kline_df.insert(2,column="trade_date",value=datetime.now().strftime("%Y-%m-%d"))
    kline_df.to_csv("./pg_import_kline.csv", encoding="utf-8", index=False, sep=",")
    log.info("K线数据清洗完成，生成文件 pg_import_kline.csv")
    print(kline_df.info())
