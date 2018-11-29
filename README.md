# CookiePoll
这是一个Cookie池，是使用flask框架和redis数据库实现的。
现在暂时只实现了新浪账号的模拟登陆，可以把生成cookie信息存入redis数据库，但程序有很强的扩展性。
程序主要分为三个模块：API、Cookie生成器和Cookie检测器
通过定时检查cookie，来确保cookie信息的有效性

## API
本模块主要提供了几个api，用户可用通过访问对应的网络地址，从而使用程序的相应功能

## Cookie生成器
本模块主要是用来实现模拟登陆的，模拟登陆是使用selenium模块，现在可以使用phantomjs或者使用chromedriver作为驱动，
本模块是利用多线程来实现效率的提升，用户可以在setting中设置线程的数量

## Cookies测试器
对redis数据库中的cookie信息进行测试，如果有效则保持，如果无效就删除
