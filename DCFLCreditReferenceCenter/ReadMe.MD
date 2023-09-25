#20230915 V1.0.52
新增变更登记流程
   承租人变更流程(CrsRegisterChange)  前置调用百度地图获取省市区LocationInfo
        共同:CrsLesseeInfo
   租赁物变更流程(CrsRegisterChangeGoods)  前置调用GetMatterDesc获取MatterDesc 和IdentificationCode
        共同:CrsGoods、CrsIdentificationCode

#20230905 V1.0.51
处理注销登记流程升级
	主要改善内容：注销登记功能跳转、修改码录入、获取注销登记编号，登记期限已届满等异常内容的处理。
	费弃原有功能2EA，菜单跳转（CrsNavigate）、注销登记（CrsUnRegister）
	新增功能3EA:，菜单跳转（CrsNavigate）、注销登记（CrsRegisterCancel）、其他类型登记完成处理（CrsCompleteOther）
	Dependencies：Microsoft.Activities1.0.1

#20230509 V1.0.48
处理注销登记异常情况时返写错误登记编号

#20230327 V1.0.47
将租赁财产类型字段根据中登网报表的实际内容进行登记

#20220927 V1.0.45
合同状态：取消、协商有损失结清，触发注销流程

#20220614 V1.0.40
融资租赁系统升级Edge浏览器

#20220616 V1.0.42
自然人登记身份证号码 GetTransactionData

