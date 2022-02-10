# scrapy and ajax
```

    简单使用scrapy实现抓取异步豆瓣经典各标签电影信息，
    爬取信息包括：编号、名称、评分、地址、图书地址、显示x轴、显示y轴、是否热映等信息.
    
```

1.pymysql

2.scrapy


# 信用卡绑定功能

## 更新或新增广告账号所绑定的信用卡信息
* 按照有则更新，无则插入的原则，更新bm_id、credit_id、remark、add_time、update_time字段
### 接口地址
测试  
POST http://dev-nb-adsaccount-fapi-bigdata.internal.codefriend.top/adsaccount/update_credit_info

### 请求参数
| 参数名称|  | 描述 | 类型 | 必填 |
| ------ | ------ | ------ | ------ | ------ |
| data | |信用卡列表 | 数组 |是|
|  | account_id | 广告账号ID | string |是|
|  | bm_id | 查询bm | string |是|
|  | credit_id | 信用卡号 | string |是|
|  | remark | 信用卡备注信息 | string | 是|
### 示例
### 请求
```
{ 
    "data":[
        {
            "account_id": "1000017467133187",
            "bm_id": "100101211428877",
            "credit_id": "21777428877",
            "remark": "信用卡备注信息-test"
        },
        {
            "account_id": "1000020143852271",
            "bm_id": "100101211428877",
            "credit_id": "21451242887",
            "remark": "信用卡备注信息-test"
        },
        {
            "account_id": "1000057917079054",
            "bm_id": "100101211428877",
            "credit_id": "21115114288",
            "remark": "信用卡备注信息-test"
        }
    ]
}
```
### 返回成功
`{`  
`    "status": 0,`  
`    "message": "更新成功"`    
`}`  

### 返回失败
`{`  
`    "status": -1,`  
`    "message": "传入参数错误"`  
`}`  


## 获取广告账号所绑定的信用卡信息

### 接口地址
测试  
POST http://dev-nb-adsaccount-fapi-bigdata.internal.codefriend.top/adsaccount/credit_infos

## 请求参数
| 参数名称|  |  | 描述 | 类型 | 必填 |
| ------ | ------ | ------ | ------ | ------ | ------ |
| limit_id| | | 起始记录，默认从0开始| int | 是|
| limit_count| | | 每页数量 | int | 是|
| order_by| | | 排序| 对象| 否|
| | by| | 排序目标| provider, card, spend<br>默认以provider排序 | 是|
| | sort| | 排序方式| ASC<br>DESC<br>默认为ASC| 是|
| filter| | | 过滤| 对象| 否|
| | relation| | 过滤条件集合“set”之间的关系| and| 是|
| | set| | 条件集合| 对象数组| 是|
| | | field| 过滤字段| pc<br>card<br>person| 是|
| | | op| 过滤操作| in, eq, like | 是|
| | | value| 过滤值| 数组列表<br>| 是|

**注：搜索持卡人时，op应为like**

## 返回参数
| 参数名称| | 描述 | 类型 | 必填 |
| ------  | ------ | ------ | ------ | ------ |
| status| | 处理结果| 数值| 是|
| message| | 结果描述| String| 否|
| total| |总条目数 | Integer| 是|
| amount| |总消耗 | Float| 是|
| data| | 数据| 数组| 是|
| | account_id| 广告账号ID| String| 是|
| | bm_id| 卡号| String| 是|
| | credit_id| 编码| String| 是|
| | person| 持卡人| String| 是|
| | add_time| 添加时间| String| 是|
| | update_time| 更新时间| String| 是|

* 请求实例<br>
```
{
    "limit_id": "0",
    "limit_count": "10",
    "order_by": {
        "by": "add_time",
        "sort": "asc"
    },
    "filter": {
        "relation": "and",
        "set": [
            {
                "field": "account_id",
                "op": "NIN",
                "operator": "zeng",
                "value": ["1000017467133164", "1000017467133187"]
            },
            {
                "field": "add_time",
                "op": "gte",
                "value": "2022-02-10"
            }
        ]
    }
}
```


* 返回示例实例<br>
```
{
    "status": 0,
    "message": "查询成功",
    "total": 3,
    "data": [
        {
            "account_id": "1000017467133178",
            "bm_id": "100101211428877",
            "credit_id": "21271142887",
            "person": "信用卡备注信息-test",
            "add_time": "2022-02-10 13:37:34",
            "update_time": "2022-02-10 17:20:38"
        },
        {
            "account_id": "1000057917079008",
            "bm_id": "100101211428877",
            "credit_id": "21211428877",
            "person": "信用卡备注信息-test",
            "add_time": "2022-02-10 13:37:34",
            "update_time": "2022-02-10 17:20:38"
        },
        ...
    ]
}
```



### 数据表
* 信用卡信息表：adsaccount.account_credit<br>
> 主键：account_id<br>

| 字段        | 类型      | 描述      |
|-------------|-----------|-----------|
| account_id    | varchar   | 账号ID    |
| bm_id        | varchar   | 查询BM      |
| credit_id      | varchar   | 信用编号      |
| remark       | float     | 信用卡备注信息      |
| add_time    | timestamp | 添加时间  |
| update_time | timestamp | 更新时间  |
