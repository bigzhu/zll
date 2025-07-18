# ZLL - SSH Connection Manager

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

一个简单高效的 SSH 连接管理工具，帮助你快速管理和连接到远程服务器。

## 特性

- 🔒 **安全优先**: 仅支持 SSH 密钥认证，不存储密码
- 📋 **连接管理**: 保存和管理 SSH 连接信息
- 🔍 **智能搜索**: 支持通过主机名、IP 或描述快速查找连接
- ⚡ **快速连接**: 通过序号或关键字快速连接到服务器
- 📝 **简单配置**: 使用 CSV 格式存储连接信息，易于编辑和备份

## 安装

### 使用 pip 安装

```bash
pip install zll
```

### 从源码安装

```bash
git clone https://github.com/bigzhu/zll.git
cd zll
poetry install
```

## 使用方法

启动 zll：

```bash
zll
```

### 主要功能

- **添加连接**: 输入 `a` 添加新的 SSH 连接信息
- **退出程序**: 输入 `q` 退出
- **数字连接**: 输入对应序号直接连接到服务器
- **搜索连接**: 输入主机名、IP 或描述关键字进行搜索
- **删除连接**: 输入 `d` 然后输入要删除的连接序号

### 使用示例

```bash
# 启动 zll
$ zll

# 显示所有连接列表
Number  User    Host            Port    Description
0       root    192.168.1.100   22      Web Server
1       admin   db.example.com  22      Database Server
2       user    staging.app.com 2222    Staging Environment

# 直接连接
Input number, IP, or hostname (q to quit, a to add, d to delete): 0
# 连接到 192.168.1.100

# 搜索连接
Input number, IP, or hostname (q to quit, a to add, d to delete): web
# 显示包含 "web" 关键字的连接

# 添加新连接
Input number, IP, or hostname (q to quit, a to add, d to delete): a
Input username: myuser
Input ip or hostname: newserver.com
Input port (default 22): 2222
Input comment: My New Server
Added successfully!
```

## 配置文件

连接信息存储在 CSV 格式的配置文件中，位置：

- **macOS**: `~/Library/Application Support/zll/hosts.csv`
- **Linux**: `~/.local/share/zll/hosts.csv`
- **Windows**: `%APPDATA%\zll\hosts.csv`

文件格式：
```csv
User,Host,Port,Description
root,192.168.1.100,22,Web Server
admin,db.example.com,22,Database Server
```

## 开发

### 环境设置

```bash
# 克隆项目
git clone https://github.com/bigzhu/zll.git
cd zll

# 安装 Poetry（如果未安装）
curl -sSL https://install.python-poetry.org | python3 -

# 安装依赖
poetry install

# 激活虚拟环境
poetry shell
```

### 运行测试

```bash
# 运行所有测试
poetry run pytest

# 运行测试并生成覆盖率报告
poetry run pytest --cov=zll --cov-report=html

# 运行类型检查
poetry run mypy zll

# 代码格式化
poetry run black zll tests
poetry run isort zll tests

# 代码检查
poetry run ruff zll tests
```

### 安装 pre-commit hooks

```bash
poetry run pre-commit install
```

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 贡献

欢迎提交 Issue 和 Pull Request！

## 变更日志

### v0.2.0
- 重大代码质量改进
- 修复测试导入问题，将测试文件移至正确目录
- 添加完整的类型注解和文档字符串
- 改进异常处理和输入验证
- 添加开发工具配置（Black, isort, mypy, ruff, pytest）
- 配置 pre-commit hooks
- 更新所有依赖包到最新版本
- 完全重写 README 文档
- 添加贡献指南（CONTRIBUTING.md）
- 提升代码格式化和质量标准

### v0.1.11
- 基础功能实现