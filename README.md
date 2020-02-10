# ssh_oper

ssh 命令行辅助登录工具

记录ssh登录信息，显示列表并协助登录

# 配置文件
用如下的格式，放到ssh.ini文件中，多条记录就换行, 空格分割
`user_name 8.8.8.8 password description`

例子

```
用户名 主机ip或者hostname 密码(已经废弃,随便输入点什么就好) 描述说明 端口号(可选) 
bigzhu 192.168.0.1 ? 测试机 2345
admin 192.168.0.2 p 哈哈鸡
```


# install
运行

请先安装 [bash_tools](https://github.com/bigzhu/bash_tools)

```bash
install.sh ssh.py
```

只是建了一个 link 到 `/usr/local/bin/`, 方便在任意目录启动

# 使用

输入以下三种类型均可, 优先级别按顺序匹配

- q 退出
- 输入序列直接登录
- 输入主机hostname 或者 ip 关键字匹配搜索
