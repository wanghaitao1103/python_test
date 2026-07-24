以下是 Git 常用命令速查：

### 基础操作

| 命令                   | 说明         |
| -------------------- | ---------- |
| `git init`           | 初始化本地仓库    |
| `git clone <url>`    | 克隆远程仓库     |
| `git status`         | 查看工作区状态    |
| `git add <file>`     | 将文件加入暂存区   |
| `git add .`          | 将所有修改加入暂存区 |
| `git commit -m "消息"` | 提交暂存区内容    |
| `git push`           | 推送到远程仓库    |
| `git pull`           | 拉取远程更新     |

### 分支操作

| 命令                       | 说明        |
| ------------------------ | --------- |
| `git branch`             | 查看本地分支    |
| `git branch <name>`      | 创建新分支     |
| `git checkout <name>`    | 切换到分支     |
| `git checkout -b <name>` | 创建并切换分支   |
| `git merge <name>`       | 合并分支到当前分支 |
| `git branch -d <name>`   | 删除分支      |

### 查看历史

| 命令                     | 说明       |
| ---------------------- | -------- |
| `git log --oneline`    | 简洁版提交历史  |
| `git log --oneline -5` | 最近5条提交   |
| `git diff`             | 查看未暂存的修改 |
| `git diff --staged`    | 查看已暂存的修改 |

### 远程操作

| 命令                            | 说明        |
| ----------------------------- | --------- |
| `git remote -v`               | 查看远程仓库    |
| `git remote add origin <url>` | 添加远程仓库    |
| `git push -u origin main`     | 首次推送并设置上游 |
| `git remote remove origin`    | 移除远程仓库    |

### 撤销操作

| 命令                            | 说明                  |
| ----------------------------- | ------------------- |
| `git restore <file>`          | 撤销工作区修改             |
| `git restore --staged <file>` | 取消暂存                |
| `git reset --soft HEAD~1`     | 撤销最近一次 commit（保留修改） |
| `git stash`                   | 暂存当前修改              |
| `git stash pop`               | 恢复暂存的修改             |

