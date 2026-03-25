# Makefile 学习笔记（入门）

> 目标：会用、看得懂、能写最基础的 Makefile。

## 1. 你先记住三件事

1. `Makefile` 是“命令快捷键集合”。
2. 执行方式：`make 目标名`。
3. 命令行前必须是 **Tab**，不是空格。

## 2. 最小例子

文档中的 `make` 代码块里使用 `\t` 表示 Tab。

```make
hello:
\t@echo "hello world"
```

执行：

```bash
make hello
```

说明：

- `hello` 是目标名
- `@` 表示不打印命令本身（只打印结果）

## 3. 常用结构

```make
目标名: 依赖1 依赖2
\t命令1
\t命令2
```

解释：

- “依赖”会先执行（如果有规则）
- 再执行目标下的命令

## 4. 变量（最常见的用法）

```make
PY=python3
APP=backend/day1.py

run:
\t$(PY) $(APP)
```

执行：

```bash
make run
```

## 5. PHONY 的意义

```make
.PHONY: run clean
```

作用：

- 告诉 `make`：这些目标不对应真实文件
- 防止同名文件干扰执行

## 6. 多个目标的习惯写法

```make
.PHONY: help setup run clean

help:
\t@echo "make setup - create venv and install deps"
\t@echo "make run   - run the app"
\t@echo "make clean - cleanup"

setup:
\tpython3 -m venv .venv
\t. .venv/bin/activate && pip install -r requirements.txt

run:
\tpython3 backend/day1.py

clean:
\trm -rf .venv __pycache__
```

## 7. 常见坑

- **Tab** 必须要有，空格不行。
- `make` 默认只在当前目录找 `Makefile`。
- 同名文件会影响执行，记得用 `.PHONY`。

## 8. 练习（你可以试试）

1. 写一个 `make greet`，输出你的名字。
2. 写一个 `make list`，执行 `ls -la`。
3. 写一个 `make pyversion`，输出 `python3 --version`。

## 9. 下一步

当你熟悉后，可以学习：

- 变量覆盖（命令行传参）
- 条件判断
- 多文件编译（大型项目）

## 10. 命令行覆盖变量（很常用）

```make
PY=python3

ver:
\t$(PY) --version
```

执行：

```bash
make ver
make ver PY=python
```

## 11. 默认目标（进来先跑谁）

```make
.DEFAULT_GOAL := help

help:
\t@echo "make run / make setup / make clean"
```

说明：

- 直接 `make` 会跑 `help`

## 12. 自动变量（看懂规则就行）

```make
target: dep1 dep2
\t@echo $@   # 目标名
\t@echo $^   # 所有依赖
\t@echo $<   # 第一个依赖
```

## 13. 简单模式规则（批量处理）

```make
%.txt: %.md
\t@echo "convert $< to $@"
```

说明：

- `%` 是通配符
- 适合批量处理文件

## 14. 组织多个文件（拆分）

```make
include Makefile.local
```

说明：

- `Makefile.local` 可以放你自己的私有配置
- 不建议提交到 Git（可加入 `.gitignore`）

## 15. 常见实用片段

```make
clean:
\trm -rf .venv __pycache__

lint:
\tpython3 -m py_compile backend/day1.py
```

## 16. 小练习（进阶一点）

1. 写一个 `make open`，打开当前目录（macOS 用 `open .`）。
2. 写一个 `make tree`，如果安装了 `tree` 就打印目录结构。
3. 写一个 `make run`，支持 `FILE=xxx.py` 参数运行指定脚本。

## 17. 常见问题排查

- 报错 “missing separator” 通常是 **Tab** 写成了空格
- `make` 找不到命令：检查该命令是否装在系统里
- 变量没有生效：检查变量名是否拼写一致

## 18. 条件判断（只需会看懂）

```make
OS := $(shell uname -s)

open:
ifeq ($(OS),Darwin)
\topen .
else
\t@echo "Use xdg-open . on Linux"
endif
```

说明：

- `ifeq` / `endif` 是条件块
- `$(shell ...)` 可以执行 shell 命令并拿到结果

## 19. 默认值与覆盖

```make
FILE ?= backend/day1.py

run:
\tpython3 $(FILE)
```

执行：

```bash
make run
make run FILE=backend/other.py
```

说明：

- `?=` 表示“如果没传入就用默认值”

## 20. 多行命令与 .ONESHELL

```make
.ONESHELL:

setup:
\tpython3 -m venv .venv
\tsource .venv/bin/activate
\tpip install -r requirements.txt
```

说明：

- 默认每一行命令都会开启新 shell
- `.ONESHELL` 让同一目标里使用同一个 shell

## 21. 安静模式与打印

```make
.SILENT:

version:
\tpython3 --version
```

说明：

- `.SILENT` 会隐藏命令本身，只显示输出
- 或者单行用 `@` 隐藏

## 22. 和 Python 常见任务绑定

```make
fmt:
\tpython3 -m pip install black
\tpython3 -m black backend/

lint:
\tpython3 -m py_compile backend/day1.py

test:
\tpython3 -m unittest discover -s tests -p "test_*.py"
```

说明：

- 这些目标只是示例，你可以按项目需求改

## 23. 小结（你先掌握这些就够）

- 会用 `make 目标名`，知道 Tab 要求
- 会写目标 + 命令，理解变量
- 能看懂常见 Makefile，不会也知道查哪里

## 24. 实战模板（适合 Python 小项目）

```make
.PHONY: help setup run clean fmt lint test

.DEFAULT_GOAL := help

PY=python3
APP=backend/day1.py

help:
\t@echo "make setup - create venv and install deps"
\t@echo "make run   - run the app"
\t@echo "make fmt   - format code (black)"
\t@echo "make lint  - quick syntax check"
\t@echo "make test  - run tests"
\t@echo "make clean - cleanup"

setup:
\t$(PY) -m venv .venv
\t. .venv/bin/activate && pip install -r requirements.txt

run:
\t$(PY) $(APP)

fmt:
\t$(PY) -m pip install black
\t$(PY) -m black backend/

lint:
\t$(PY) -m py_compile $(APP)

test:
\t$(PY) -m unittest discover -s tests -p "test_*.py"

clean:
\trm -rf .venv __pycache__
```

说明：

- 你可以把 `APP` 改成别的脚本
- 暂时没测试也没关系，`test` 只是模板

## 25. 常用写法速记

- `VAR=xxx` 定义变量
- `VAR ?= xxx` 默认值
- `$(VAR)` 引用变量
- `@` 隐藏命令本身
- `.PHONY` 保护目标
- `.DEFAULT_GOAL` 设置默认目标

## 26. 常见错误示例

### 错误 1：Tab 写成空格

```make
run:
    python3 backend/day1.py
```

会报：

```text
missing separator
```

### 正确写法

```make
run:
\tpython3 backend/day1.py
```

## 27. 建议的学习顺序

1. 学会用：`make run`
2. 学会看：变量 + 目标结构
3. 学会改：把 `APP` 换成你自己的脚本
4. 学会扩展：加 `fmt/lint/test`
