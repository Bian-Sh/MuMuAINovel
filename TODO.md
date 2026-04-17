# TODO — MuMuAINovel 改进计划

> 所有待办任务在此记录，支持 git 版本管理。
> 格式：`[ ] 任务描述` 进行中：`[x]` 完成：`[c]`

---

## 待办

- [ ] **使用 git 为 AI 写作工具（MuMuAINovel/mumu）生成的作品做托管，方便控制版本**

- [ ] **恢复语义搜索/向量记忆功能**：使用 MiniMax embedding API (`embo-01`) 生成向量 + ChromaDB HTTP 模式（独立服务）实现完整向量搜索伏笔推荐，不安装 torch/transformers

---

## 已完成

- [x] 创建并初始化 SQLite 数据库表
- [x] 配置 .env 环境变量（SQLite + MiniMax API）
- [x] 启动后端 FastAPI 服务（uvicorn on port 8000）
- [x] 安装前端依赖并构建静态资源
- [x] 验证前后端运行状态（登录流程测试通过）
- [x] 创建 requirements-lite.txt（移除 torch/transformers/chromadb）
- [x] 重写 memory_service.py 为 stub（保留 API，禁用本地向量功能）
- [x] 修改 config.py 默认 DATABASE_URL 为 SQLite
- [x] 修改 database.py 健康检查支持 SQLite
- [x] 重写 .env.example
- [x] 编写 INSTALL-LITE.md 安装指南
- [x] 创建 alembic-sqlite.ini 迁移配置
- [x] 初始化 27 张数据库表（同步方式绕过 aiosqlite WSL 问题）
