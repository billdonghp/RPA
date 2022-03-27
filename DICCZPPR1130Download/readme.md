#2022-03-23 v1.08
        解决受内存限制，每批次最大下载量不能超过40个。
        MaterialList 中Material 与 ValidFrom 组合重复，只下载一次
#2022-03-14 v1.0.7
       处理路径输入错误
       处理ProcType = X 未保存至FilterAfter
       处理Comp.Qty Double类型数据
#2022-03-03 v1.0.2
       增加MaterialList 中IsDownload，生成PivotTable
       引用miyag.uipath.desktopnotification.activities 1.1.0 Show ProgressBar、 Show Mesage
       引用microsoft.office.interop.excel  14.0.0.1  对Result中PivotTable 列标题格式调整
       Material对应多个ValidFrom，生成PivotTable处理方案: Material_ValidFrom
#2022-02-28 v1.0.1
        BOM批量下载
        数据清洗 
	1.删除B:Bulk = YES 并另存
	2.删除ProcType = E, 并另存 ProcType = E and M:SPT is null
                3.剩余另存FilterAfter
         部署Assistant

#注意事项：
    1. 切换输入法：英文键盘
    2. 使用电源适配器供电
    3. MaterialList 运行前关闭
    4. SAP GUI选项  -辅助功能与脚本-脚本- 取消勾选：1. 在脚本附加到SAP GUI时发出通知 &2. 在脚本打卡连接时发出通知 