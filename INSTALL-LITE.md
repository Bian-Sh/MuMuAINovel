# MuMuAINovel 精简版 - WSL Ubuntu 本地安装指南

> **精简版特点**：不安装本地 AI 模型（torch / transformers / chromadb），仅保留 AI API 调用功能（支持 OpenAI 兼容接口，包括 Hermes / MiniMax 等）。使用 SQLite 数据库，无需 PostgreSQL。

---

## 环境要求

| 项目 | 最低要求 | 推荐 |
|------|---------|------|
| 内存 | 4 GB | 8 GB+ |
| 磁盘 | 5 GB | 10 GB+ |
| Python | 3.10+ | 3.11 |
| Node.js | 18+ | 20 LTS |
| 包管理器 | npm 或 pnpm | pnpm |

---

## 第一步：克隆项目

```bash
# 克隆原版仓库（你的 GitHub 账号）
git clone https://github.com/Bian-Sh/MuMuAINovel.git
cd MuMuAINovel
```

如果你没有 fork，直接克隆：
```bash
git clone https://github.com/xiamuceer-j/MuMuAINovel.git
cd MuMuAINovel
```

---

## 第二步：安装后端依赖

```bash
cd backend

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装精简版依赖（不包含 torch/transformers/chromadb）
pip install -r requirements-lite.txt
```

> **注意**：必须使用 `requirements-lite.txt`，不要用 `requirements.txt`（完整版包含约 3GB 的 torch 等依赖）。

---

## 第三步：配置环境变量

```bash
cd backend
cp .env.example .env
nano .env   # 编辑配置文件
```

必填项：

```env
# AI API 配置（必须）
OPENAI_API_KEY=你的Hermes_API_Key
OPENAI_BASE_URL=https://api.minimax.chat/v1   # 或你的 Hermes 地址

# 默认 AI
DEFAULT_AI_PROVIDER=openai
DEFAULT_MODEL=gpt-4o-mini

# 本地账户（必须设置）
LOCAL_AUTH_ENABLED=true
LOCAL_AUTH_USERNAME=admin
LOCAL_AUTH_PASSWORD=你的密码
LOCAL_AUTH_DISPLAY_NAME=管理员

# 数据库（SQLite 已默认，无需修改）
DATABASE_URL=sqlite+aiosqlite:///data/ai_story.db
```

---

## 第四步：初始化数据库

```bash
cd backend

# 确保 data 目录存在
mkdir -p data

# 运行数据库迁移（SQLite 版本）
alembic -c alembic-sqlite.ini upgrade head
```

> 如果没有 alembic 命令，激活虚拟环境后重试：`source venv/bin/activate && alembic -c alembic-sqlite.ini upgrade head`

---

## 第五步：构建前端

```bash
# 回到项目根目录
cd ..

# 安装前端依赖（推荐用 pnpm）
pnpm install
# 或者用 npm
npm install

# 构建生产版本
pnpm build
# 构建产物会输出到 backend/static 目录
```

> 前端需要 Node.js 18+，建议使用 [nvm](https://github.com/nvm-sh/nvm) 管理多个 Node 版本。

---

## 第六步：启动后端服务

```bash
cd backend
source venv/bin/activate
python -m app.main
```

服务启动后访问：
- **前端页面**：http://localhost:8000
- **API 文档**：http://localhost:8000/docs

---

## 第七步：可选 - 使用 systemd 管理进程（后台运行）

```bash
# 创建 systemd 服务文件
sudo nano /etc/systemd/system/mumuai.service
```

写入以下内容：

```ini
[Unit]
Description=MuMuAINovel Backend
After=network.target

[Service]
Type=simple
User=biansir
WorkingDirectory=/home/biansir/MuMuAINovel/backend
ExecStart=/home/biansir/MuMuAINovel/backend/venv/bin/python -m app.main
Restart=always
RestartSec=5
Environment=PATH=/home/biansir/MuMuAINovel/backend/venv/bin

[Install]
WantedBy=multi-user.target
```

启用服务：

```bash
sudo systemctl daemon-reload
sudo systemctl enable mumuai
sudo systemctl start mumuai
sudo systemctl status mumuai   # 查看状态
```

---

## 目录结构

```
MuMuAINovel/
├── backend/
│   ├── app/                  # FastAPI 应用
│   │   ├── api/              # API 路由
│   │   ├── models/           # 数据库模型
│   │   ├── services/         # 业务逻辑
│   │   └── main.py           # 入口文件
│   ├── alembic/              # 数据库迁移
│   ├── data/                 # SQLite 数据库文件（自动创建）
│   ├── logs/                 # 日志文件（自动创建）
│   ├── static/              # 前端构建产物
│   ├── requirements.txt      # 完整依赖（含本地 AI）
│   ├── requirements-lite.txt # 精简依赖（无本地 AI）
│   └── .env                  # 配置文件
├── frontend/                 # React 前端源码
│   ├── src/
│   └── dist/                 # 构建产物 → 复制到 backend/static
└── images/                  # 静态资源
```

---

## 精简版 vs 完整版

| 功能 | 精简版 | 完整版 |
|------|--------|--------|
| 小说项目管理 | ✅ | ✅ |
| 章节编辑 | ✅ | ✅ |
| 角色/关系/组织管理 | ✅ | ✅ |
| 伏笔管理 | ✅ | ✅ |
| AI 生成（通过 API） | ✅ | ✅ |
| 语义搜索/向量记忆 | ❌ | ✅ |
| 本地 Embedding 模型 | ❌ | ✅ |
| 数据库 | SQLite | PostgreSQL |
| 磁盘占用 | ~1 GB | ~4-5 GB |
| 内存占用 | ~500 MB | ~4-6 GB |

---

## 常见问题

**Q: 启动时报错 `ModuleNotFoundError: No module named '...' `**
A: 确保激活了虚拟环境：`source venv/bin/activate`，然后重试。

**Q: 邮件发送功能不工作**
A: 需要配置 SMTP。在 `.env` 中填入 QQ 邮箱授权码（不是 QQ 密码）。

**Q: 前端构建失败**
A: 检查 Node.js 版本（需要 18+）。建议用 `nvm` 切换到 Node 20。

**Q: 如何更新代码？**
A: `git pull origin main`，然后重新 `pip install -r requirements-lite.txt`（如有更新）并重启服务。

---

## API 配置说明

本项目支持 OpenAI 兼容接口，可对接以下服务：

### MiniMax（推荐国内用户）
```env
OPENAI_API_KEY=你的MiniMax API Key
OPENAI_BASE_URL=https://api.minimax.chat/v1
DEFAULT_MODEL=gpt-4o-mini
```

### 自定义 OpenAI 兼容服务（如 ollama）
```env
OPENAI_API_KEY=不需要（留空）
OPENAI_BASE_URL=http://localhost:11434/v1
DEFAULT_MODEL=llama3   # 或你的模型名
```

### 其他兼容服务
AnyScale, Groq, Cloudflare Workers AI, 等设置 `OPENAI_BASE_URL` 即可。
