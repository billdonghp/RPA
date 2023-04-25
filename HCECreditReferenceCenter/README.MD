中登网账号
用户名：hce202301
密码：Bill8899
绑定手机号：13953548069

VPN账号
用户名：hdi-01
密码：a0.1234

IP:10.102.105.110
网关：10.102.105.1
DNS:10.102.105.36

开始流程【合同号:CF202009-0224变更登记】,登记编号:09396109001119410585;   -已登记、待变更、结束
？ 文件状况
确定事项：
1.直租与售后回租的与否  Y ： 回租
2.初始登记与变更登记， 企业与个人客户的判断逻辑： 营业执照号为空：个人客户
3.所属行业：行业代码（报告用）、企业规模
4.起租状态（文件状态）：结束、退库 需要注销
5.复核登记取消后进行【变更保存】、初始登记时使用【批量录入】

待确认事项
1.展期登记： 初始登记时：租赁期限：72个月， 



<html url='http://10.102.105.34:8080/fi/FI3400_POP.jsp?taskCode=update&amp;P_PBOFLDYON=Y&amp;P_PBOFLDDAT=20230202&amp;P_PBOFLDUSR=test001&amp;P_PBOFLDUSR_NM=%25E6%25B5%258B%25E8%25AF%2595%25E8%25B4%25A6%25E5%258F%25B7&amp;P_PBOINICOD=qq&amp;P_PBOMODCOD=&amp;P_PBOCHGCOD=&amp;P_PBOCFTERM=&amp;SSmenuIdData=2070050000&amp;SSprgIdData=FI3400_POP' />
<webctrl name='PBOINICOD' tag='INPUT' type='text' />
<html url='http://10.102.105.34:8080/fi/FI3400_POP.jsp?taskCode=insert&amp;P_PBOFLDYON=&amp;P_PBOFLDDAT=&amp;P_PBOFLDUSR=&amp;P_PBOFLDUSR_NM=&amp;P_PBOINICOD=&amp;P_PBOMODCOD=&amp;P_PBOCHGCOD=&amp;P_PBOCFTERM=&amp;SSmenuIdData=2070050000&amp;SSprgIdData=FI3400_POP' />
<webctrl name='PBOINICOD' tag='INPUT' type='text' />


"N".Equals(in_row("展期登记与否").ToString) AndAlso

#V1.0.2
承租人变更登记与展期登记同时进行
#V1.0.3 2023-03-16
企业所属行业与中登网不符，处理方案，不一致时默认“建筑业”进行登记
#V1.0.4 2023-03-16
处理地址问题 菏泽
#V1.0.9  2023-04-25需要
1.固定登陆账号HFLRPA，默认不输入
2.处理合同号重复引起的异常
3.补充逻辑：输入8位时可选择查询单日合同或区间查询