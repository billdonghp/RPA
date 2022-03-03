#v1.0.20   2022-02-23
	【合同文本打印】增加查询后Wait Element Vanish 
		生成合同文本、生成合同、打包下载根据进行状态选择性执行
	【合同文本打印】、【合同执行】事前确认未通过和当月合同数据
			Wait Element Vanish 调整TimeOut=10000;
			增加点击"重置"解决合同编号输入错误;
			取消当月合同数据录入合同编号
#v1.0.19   2022-02-21 
	处理DcflContractUpload报Exception:"If: Index and length must refer to a location within the string.\r\nParameter name: length"
	IF判断时调用Substring方法(Index和length必须引用字符串中的位置)
#v1.0.18   2022-02-17 
	【合同执行】当月合同数据判断逻辑，未签约的合同无法查询时先判断DataTable.Rows.Count > 0 AndAlso  
	上传附件等待时间由1S/M  扩大1.2倍
	调用邮件服务器发送邮件(执行结果)收件人：修睿 抄送王宏、魏飞、董海朋、袁二梅
	修睿申请邮件发送白名单
	环境配置 JAVA_HOME  PATH  JDK6U31  
	cc:{"haipeng.dong@hyundai-di.com","hong.wang@hyundai-di.com","fei.wei@hyundai-di.com","ermei.yuan@hyundai-di.com"}
	from:"DCFL.credit@Hyundai-di.com"