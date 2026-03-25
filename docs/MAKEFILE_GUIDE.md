# Makefile 学习笔记（入门）

> 目标：会用、看得懂、能写最基础的 Makefile。

## 1. 你先记住三件事

1. `Makefile` 是“命令快捷键集合”。
2. 执行方式：`make 目标名`。
3. 命令行前必须是 **Tab**，不是空格。

## 2. 最小例子

```make
hello:
	@echo "hello world"
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
	命令1
	命令2
```

解释：
- “依赖”会先执行（如果有规则）
- 再执行目标下的命令

## 4. 变量（最常见的用法）

```make
PY=python3
APP=backend/day1.py

run:
	$(PY) $(APP)
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
	@echo "make setup - create venv and install deps"
	@echo "make run   - run the app"
	@echo "make clean - cleanup"

setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	python3 backend/day1.py

clean:
	rm -rf .venv __pycache__
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
