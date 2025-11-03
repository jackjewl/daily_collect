from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. 创建数据库连接（这里用 SQLite）
engine = create_engine("postgresql+psycopg2://user1:12345@localhost:5432/stock", echo=True)

# 2. 创建 Base 类
Base = declarative_base()

# 3. 定义模型（表）
from sqlalchemy import Column, Integer, Float, String, BigInteger, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Stock(Base):
    __tablename__ = "stock"
    # 主键
    id = Column(Integer, primary_key=True, autoincrement=True)

    # 字符串类列
    code = Column(String(20), comment="代码")
    name = Column(String(50), comment="名称")
    remark = Column(String(200), comment="备注")
    negative_factor = Column(String(100), comment="利空")
    positive_factor = Column(String(100), comment="利好")
    sub_industry = Column(String(100), comment="细分行业")
    industry = Column(String(100), comment="所属行业")
    institution_trend = Column(String(100),
                               comment="机构动向")  # 尽管不在 str_list 中，但原代码是 String，且中文名"机构动向"不在 float 集合，故保留 String
    unusual_type = Column(String(100), comment="异动类型")
    self_select_time = Column(String(50), comment="自选时间")
    listing_date = Column(String(50), comment="上市日期")
    # 数值类列 (Float)
    current_price = Column(Float, comment="现价")
    change_rate = Column(Float, comment="涨幅")
    change_value = Column(Float, comment="涨跌")
    buy_price = Column(Float, comment="买价")
    sell_price = Column(Float, comment="卖价")
    total_volume = Column(Float, comment="总手")
    total_amount = Column(Float, comment="总金额")
    current_volume = Column(Float, comment="现手")
    speed_1min = Column(Float, comment="1分钟涨速")
    real_change_rate = Column(Float, comment="实体涨幅")
    avg_diff = Column(Float, comment="现均差")
    turnover_rate = Column(Float, comment="换手")
    order_ratio = Column(Float, comment="委比")
    total_market_cap = Column(Float, comment="总市值")
    circulating_market_cap = Column(Float, comment="流通市值")
    circulation_ratio = Column(Float, comment="流通比例")
    speed_4min = Column(Float, comment="4分钟涨速")
    deviation_today = Column(Float, comment="当日偏离值")
    deviation_unusual = Column(Float, comment="异动偏离值")
    deviation_10d = Column(Float, comment="10日内偏离值")
    deviation_30d = Column(Float, comment="30日内偏离值")
    unusual_count_10d = Column(Float, comment="10日异动次数")
    inner_volume = Column(Float, comment="内盘")
    outer_volume = Column(Float, comment="外盘")
    inner_outer_ratio = Column(Float, comment="内外比")
    main_net_volume = Column(Float, comment="主力净量")
    volume_ratio = Column(Float, comment="量比")
    pe_ttm = Column(Float, comment="TTM市盈率")
    net_profit = Column(Float, comment="净利润")
    pb_ratio = Column(Float, comment="市净率")
    eps = Column(Float, comment="每股盈利")
    prev_close = Column(Float, comment="昨收")
    open_price = Column(Float, comment="开盘")
    open_change_rate = Column(Float, comment="开盘涨幅")
    auction_turnover = Column(Float, comment="竞价换手")
    high_price = Column(Float, comment="最高")
    low_price = Column(Float, comment="最低")
    change_5d = Column(Float, comment="5日涨幅")
    change_10d = Column(Float, comment="10日涨幅")
    change_20d = Column(Float, comment="20日涨幅")
    ytd_change = Column(Float, comment="年初至今")
    amplitude = Column(Float, comment="振幅") ##这里是百分比
    buy_volume = Column(Float, comment="买量")
    sell_volume = Column(Float, comment="卖量")
    trade_count = Column(Float, comment="笔数")
    contribution = Column(Float, comment="贡献度")
    total_shares = Column(Float, comment="总股本")
    circulating_shares = Column(Float, comment="流通股本")
    total_profit = Column(Float, comment="利润总额")
    net_profit_growth = Column(Float, comment="净利润增长率")
    bvps = Column(Float, comment="每股净资产")
    golden_cross_count = Column(Float, comment="金叉个数")
    retail_count = Column(Float, comment="散户数量")
    self_select_price = Column(Float, comment="自选价格")
    self_select_profit = Column(Float, comment="自选收益")

    def __repr__(self):
        return f"<Stock(code='{self.code}', name='{self.name}', current_price={self.current_price})>"


class KLine(Base):
    __tablename__ = "kline"
    id = Column(Integer, primary_key=True,autoincrement=True)
    code = Column(String(20), comment="股票代码")
    name=Column(String(50), comment="股票名称")
    trade_date = Column(Date, comment="日期")
    open = Column(Float, comment="开盘价")
    high = Column(Float, comment="最高价")
    low = Column(Float, comment="最低价")
    close = Column(Float, comment="收盘价")
    change_rate= Column(Float, comment="涨幅")
    amplitude=Column(Float,comment="振幅") ##这里是百分比
    volume = Column(Float, comment="总手")
    amount = Column(Float, comment="总金额")
    turnover_rate = Column(Float, comment="换手率")
    trade_count = Column(Float, comment="成交次数")

def create_tables():
    Base.metadata.create_all(engine)

