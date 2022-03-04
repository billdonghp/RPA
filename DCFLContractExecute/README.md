#v1.0.20   2022-03-04
	【合同文本打印】增加查询后Wait Element Vanish 
		生成合同文本、生成合同、打包下载根据进行状态选择性执行
	【合同文本打印】、【合同执行】事前确认未通过和当月合同数据
			Wait Element Vanish 调整TimeOut=10000;
			增加点击"重置"解决合同编号输入错误;
			取消当月合同数据录入合同编号
	增加网络状态的确认操作，优秀：700；良：850；正常：1000；差：1200；差+：1500
	合同上传参照1M/s 进行计算 优秀优化30% 差+延时50%
	合同打印中生成合同 4倍网络状态  打包下载6倍网络状态
	修改根据文本编号判断RZHT & MMHT逻辑
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