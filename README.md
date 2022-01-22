# RPA
20200424
# GitHub
	username: billdonghp
	password: Bill0801@

# 查看config
git config -l

# Token 失效后处理办法
1. github.com  登陆后  Settings \ Developer settings \ Personal access tokens \ Generate new Token  
	要使用token从命令行访问仓库，请选择repo。
	要使用token从命令行删除仓库，请选择delete_repo
2. 2021-12-22 生成Token：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
3. 把token直接添加远程仓库链接中
   git remote set-url origin https://<your_token>@github.com/<USERNAME>/<REPO>.git
   
   your_token = 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
   USERNAME = billdonghp
   REPO = RPA
   
#百度地图开发者账号变更
AK: CZiKqS1c5vE9UWYhVVG3bzqnO9Ptmt8U