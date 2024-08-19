#v1.0.35	2024-08-19
	菜单打开方式变更，输入功能代码
	合同执行【事前确认未通过】，明细页面调整引起的机号未输入。
#v1.0.24    2022-05-26
	解决未确认“网络状态”情况的赋值networkState="正常"
	解决不规则还款方式的合同中“日程交付日”为空的异常，合同明细画面、期未留购价计算完毕后,赋值当天日期
	通知邮箱 DCFL.credit@Hyundai-di.com 切换至notice_cn@hyundai-di.com
#v1.0.22	2022-04-18
	解决UiPath在edge扩展异常
#v1.0.21   2022-03-18
	【合同文本打印】增加查询后Wait Element Vanish 
		生成合同文本、生成合同、打包下载根据进行状态选择性执行
	增加网络状态的确认操作，优秀：700ms；良：850ms；正常：1000ms；差：1200ms；差+：1500ms
	合同上传参照1M/1000ms 进行计算 优秀优化30% 差+延时50%
	合同打印中生成合同 4倍网络状态  打包下载7倍网络状态(增加是否延迟自动化逻辑)
#v1.0.20   2022-03-04	
	【合同文本打印】、【合同执行】事前确认未通过和当月合同数据
			Wait Element Vanish 调整TimeOut=10000ms;
			增加点击"重置"解决合同编号输入错误;
			取消当月合同数据录入合同编号
	修改根据文本编号判断RZHT & MMHT逻辑(适用2022年新版合同)
#v1.0.19   2022-02-21 
	处理DcflContractUpload报Exception:"If: Index and length must refer to a location within the string.\r\nParameter name: length"
	IF判断时调用Substring方法(Index和length必须引用字符串中的位置)
#v1.0.18   2022-02-17 
	【合同执行】当月合同数据判断逻辑，未签约的合同无法查询时先判断DataTable.Rows.Count > 0 AndAlso  
	上传附件等待时间由1S/M  扩大1.2倍
	调用邮件服务器发送邮件(执行结果)收件人：修睿 抄送王宏、魏飞、董海朋、袁二梅
	修睿申请邮件发送白名单
	环境配置 JAVA_HOME  PATH  
	安装JDK6U31  
	cc:{"haipeng.dong@hyundai-di.com","hong.wang@hyundai-di.com","fei.wei@hyundai-di.com","ermei.yuan@hyundai-di.com"}
	from:"DCFL.credit@Hyundai-di.com"