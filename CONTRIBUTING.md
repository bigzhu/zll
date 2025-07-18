# 贡献指南

感谢你对 ZLL 项目的兴趣！我们欢迎各种形式的贡献。

## 开发环境设置

### 1. 克隆项目

```bash
git clone https://github.com/bigzhu/zll.git
cd zll
```

### 2. 安装 Poetry

如果你还没有安装 Poetry，请使用以下命令：

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. 安装依赖

```bash
poetry install
```

### 4. 激活虚拟环境

```bash
poetry shell
```

## 开发工作流

### 1. 创建分支

```bash
git checkout -b feature/your-feature-name
```

### 2. 进行开发

确保你的代码符合项目标准：

#### 代码格式化

```bash
# 使用 black 格式化代码
poetry run black zll tests

# 使用 isort 排序导入
poetry run isort zll tests
```

#### 代码检查

```bash
# 使用 ruff 进行代码检查
poetry run ruff check zll tests

# 使用 mypy 进行类型检查
poetry run mypy zll --ignore-missing-imports
```

#### 运行测试

```bash
# 运行所有测试
poetry run pytest

# 运行测试并生成覆盖率报告
poetry run pytest --cov=zll --cov-report=html

# 运行特定测试
poetry run pytest tests/test_zll.py::TestZLL::test_add_new
```

### 3. 提交更改

我们使用 pre-commit hooks 来确保代码质量：

```bash
# 安装 pre-commit hooks
poetry run pre-commit install

# 手动运行 pre-commit
poetry run pre-commit run --all-files
```

### 4. 提交消息规范

请使用清晰、描述性的提交消息：

```bash
# 好的提交消息示例
git commit -m "feat: add port validation in add_new function"
git commit -m "fix: handle empty input in ssh connection"
git commit -m "docs: update README with new features"
git commit -m "test: add tests for error handling"
```

提交消息前缀：
- `feat:` - 新功能
- `fix:` - 修复 bug
- `docs:` - 文档更新
- `test:` - 测试相关
- `refactor:` - 代码重构
- `style:` - 代码格式更改
- `chore:` - 构建过程或辅助工具的变动

## 代码标准

### Python 代码风格

- 使用 [Black](https://black.readthedocs.io/) 进行代码格式化
- 使用 [isort](https://pycqa.github.io/isort/) 排序导入语句
- 使用 [Ruff](https://docs.astral.sh/ruff/) 进行 linting
- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 标准

### 类型注解

- 所有函数都应该有完整的类型注解
- 使用 [mypy](http://mypy-lang.org/) 进行类型检查

### 文档字符串

为所有公共函数添加文档字符串：

```python
def ssh(ssh_info: List[str]) -> None:
    """Connect to SSH server with given connection info.
    
    Args:
        ssh_info: List containing [user, host, port, description]
    
    Raises:
        ValueError: If user or host is empty
    """
```

### 测试

- 为新功能编写测试
- 确保测试覆盖率不低于现有水平
- 使用 pytest 进行测试

## 提交 Pull Request

1. 确保所有测试通过
2. 确保代码通过所有质量检查
3. 更新相关文档
4. 创建 Pull Request 并填写详细描述

### Pull Request 模板

```markdown
## 描述
简要描述这个 PR 的目的和更改内容。

## 更改类型
- [ ] Bug 修复
- [ ] 新功能
- [ ] 文档更新
- [ ] 代码重构
- [ ] 其他：_____________

## 测试
描述你如何测试这些更改：
- [ ] 运行了所有现有测试
- [ ] 添加了新测试
- [ ] 手动测试了相关功能

## 检查清单
- [ ] 代码通过了所有 linting 检查
- [ ] 代码通过了类型检查
- [ ] 添加/更新了相关文档
- [ ] 添加/更新了测试
```

## 报告问题

如果你发现了 bug 或有功能建议，请在 GitHub Issues 中报告：

1. 搜索现有 issues 以避免重复
2. 使用清晰的标题和描述
3. 提供重现步骤（对于 bug）
4. 包含环境信息（Python 版本、操作系统等）

## 获取帮助

如果你在贡献过程中遇到问题，可以：

1. 查看项目 README
2. 在 GitHub Issues 中提问
3. 联系维护者

再次感谢你的贡献！