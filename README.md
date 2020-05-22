# BiliBiliStreamUploader
一个自动化上传直播录像的小程序

配合Nginx服务器使用的小程序,丢进录像文件夹运行就好啦~
运行之前需要调整config文件

# 依赖
[comwrg/bilibiliupload](https://github.com/comwrg/bilibiliupload)
```
pip3 install bilibiliupload
```
# 配置:

配置文件:

[Common]:

`Path:`录像文件位置,默认`./`相对目录
 
`type:` 录像文件格式 默认`.flv`

[Bilibili]

用户登入信息,使用第三方库，请自行斟酌风险

`Username:` b站用户名/邮箱

`Password:` b站密码

视频信息:

`title:` 视频的标题,例如`[CCS_Covenant] 直播录像` 后缀会自动加上时间
 
`desc:` 视频的简介,可空 

`dynamtic:` 直播动态

`tid:` 视频的分区,例如`17`为单机游戏,详见 [BilibiliAPI](https://github.com/uupers/BiliSpider/wiki/%E8%A7%86%E9%A2%91%E5%88%86%E5%8C%BA%E5%AF%B9%E5%BA%94%E8%A1%A8)

`tag:` 视频的标签,用逗号隔开,例如  `Minecraft,直播录像,CCS_Covenant`

欢迎关注直播间

https://live.bilibili.com/27216

MC玩家~
