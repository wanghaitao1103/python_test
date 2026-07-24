# CLI 常用命令速查

### 目录操作（增删查改）

| 命令 | 说明 |
| --- | --- |
| `cd <path>` | 切换目录 |
| `cd ..` | 返回上级目录 |
| `cd \` | 返回根目录 |
| `pwd` | 显示当前路径 |
| `dir` | 列出当前目录内容 |
| `dir *.py` | 列出当前目录下所有 .py 文件 |
| `dir /s *.txt` | 递归搜索当前目录及子目录下的 .txt 文件 |
| `dir /ad` | 只列出目录，不列出文件 |
| `dir /ah` | 只列出隐藏文件/目录 |
| `mkdir <name>` | 创建单个目录 |
| `mkdir dir1\dir2\dir3` | 递归创建多级目录 |
| `rmdir <name>` | 删除空目录 |
| `rmdir /s <name>` | 递归删除目录（含子目录和文件） |
| `ren <旧名> <新名>` | 重命名目录 |
| `tree` | 目录树结构展示 |
| `tree /f` | 目录树展示（含文件名） |

### 文件操作（增删查改）

| 命令 | 说明 |
| --- | --- |
| **创建** | |
| `echo "text" > file` | 写入内容到文件（覆盖） |
| `echo "text" >> file` | 追加内容到文件 |
| `type nul > file.txt` | 创建空文件 |
| `fsutil file createnew file.txt 1024` | 创建指定大小的文件（字节） |
| **查看** | |
| `type <file>` | 查看文件全部内容 |
| `more <file>` | 分页查看文件内容 |
| `Get-Content <file> -Head 10` | 查看文件前10行（PowerShell） |
| `Get-Content <file> -Tail 10` | 查看文件后10行（PowerShell） |
| **复制/移动** | |
| `copy <src> <dst>` | 复制文件 |
| `copy *.py backup\` | 批量复制 .py 文件到目录 |
| `xcopy <src> <dst> /s /e` | 复制目录及子目录（含空目录） |
| `robocopy <src> <dst> /e` | 高效复制目录（支持断点续传） |
| `move <src> <dst>` | 移动文件 / 重命名文件 |
| **删除** | |
| `del <file>` | 删除单个文件 |
| `del *.log` | 删除所有 .log 文件 |
| `del /s *.pyc` | 递归删除所有 .pyc 文件 |
| `del /f <file>` | 强制删除只读文件 |
| **搜索** | |
| `dir /s <filename>` | 按文件名搜索 |
| `find "keyword" <file>` | 在文件中搜索字符串 |
| `findstr "pattern" *.py` | 在多个文件中搜索正则模式 |
| `findstr /s /i "error" *.log` | 递归忽略大小写搜索 error |

### 文本处理

| 命令 | 说明 |
| --- | --- |
| `sort <file>` | 对文件内容排序 |
| `sort <file> /o out.txt` | 排序后输出到文件 |
| `find /c "str" <file>` | 统计字符串出现次数 |
| `findstr /n "pattern" <file>` | 搜索并显示行号 |
| `fc file1 file2` | 对比两个文件差异 |
| `comp file1 file2` | 比较两个文件是否相同 |

### 系统信息

| 命令 | 说明 |
| --- | --- |
| `hostname` | 查看主机名 |
| `whoami` | 查看当前用户 |
| `ipconfig` | 查看网络配置 |
| `ipconfig /all` | 查看详细网络配置 |
| `systeminfo` | 查看系统信息 |
| `tasklist` | 查看运行中的进程 |
| `taskkill /pid <id> /f` | 强制结束指定进程 |
| `ver` | 查看系统版本 |
| `driverquery` | 查看已安装驱动 |

### 环境与变量

| 命令 | 说明 |
| --- | --- |
| `set` | 查看所有环境变量 |
| `echo %PATH%` | 查看 PATH 变量（CMD） |
| `$env:PATH` | 查看 PATH 变量（PowerShell） |
| `setx VAR "value"` | 永久设置用户环境变量 |

### Python 相关

| 命令 | 说明 |
| --- | --- |
| `python --version` | 查看 Python 版本 |
| `python <file.py>` | 运行 Python 脚本 |
| `pip install <pkg>` | 安装包 |
| `pip uninstall <pkg>` | 卸载包 |
| `pip list` | 查看已安装的包 |
| `pip show <pkg>` | 查看包详细信息 |
| `pip freeze > requirements.txt` | 导出依赖列表 |
| `pip install -r requirements.txt` | 安装依赖列表 |
| `python -m venv venv` | 创建虚拟环境 |
| `venv\Scripts\activate` | 激活虚拟环境 |
| `deactivate` | 退出虚拟环境 |

### 网络操作

| 命令 | 说明 |
| --- | --- |
| `ping <host>` | 测试网络连通性 |
| `ping -t <host>` | 持续 ping |
| `tracert <host>` | 跟踪路由路径 |
| `nslookup <domain>` | DNS 查询 |
| `netstat -an` | 查看所有网络连接和端口 |
| `curl <url>` | 发送 HTTP 请求 |
| `curl -o file <url>` | 下载文件 |

### 磁盘与存储

| 命令 | 说明 |
| --- | --- |
| `dir <drive>:` | 查看磁盘内容（如 `dir d:`） |
| `chkdsk` | 检查磁盘错误 |
| `diskpart` | 磁盘管理工具 |

### 其他常用

| 命令 | 说明 |
| --- | --- |
| `cls` | 清屏 |
| `exit` | 退出终端 |
| `help <cmd>` | 查看命令帮助 |
| `<cmd> /?` | 查看命令帮助（CMD） |
| `where <cmd>` | 查找命令/程序路径 |
| `start .` | 在文件资源管理器中打开当前目录 |
| `start notepad file.txt` | 用记事本打开文件 |
| `shutdown /s /t 0` | 立即关机 |
| `shutdown /r /t 0` | 立即重启 |
| `powercfg /batteryreport` | 生成电池报告 |
