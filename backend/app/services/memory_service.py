"""
向量记忆服务（精简版 - 已禁用本地 AI）
本模块依赖 chromadb + sentence-transformers，已在精简版中移除。
所有记忆/向量相关功能返回空结果，不影响其他功能运行。
如需启用向量记忆，请安装完整版 requirements.txt。
"""
from typing import List, Dict, Any, Optional
from app.logger import get_logger

logger = get_logger(__name__)

# 打印警告，仅一次
logger.warning("=" * 60)
logger.warning("⚠️  MemoryService [精简版] - 向量记忆已禁用")
logger.warning("   本版本不安装 chromadb / sentence-transformers / torch")
logger.warning("   所有语义搜索、记忆分析功能暂时不可用")
logger.warning("   其他功能（项目管理、章节编辑、AI生成等）正常")
logger.warning("   如需启用向量记忆，请使用完整版 requirements.txt")
logger.warning("=" * 60)


class MemoryService:
    """向量记忆管理服务（精简版 - 功能已禁用）"""

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        logger.info("✅ MemoryService [精简版] 初始化完成（空实现）")

    # ------------------------------------------------------------------
    # 空操作实现 - 所有需要向量数据库的方法返回安全默认值
    # ------------------------------------------------------------------

    def get_collection(self, user_id: str, project_id: str):
        """获取 collection（精简版不执行任何操作）"""
        return None

    async def add_memory(
        self,
        user_id: str,
        project_id: str,
        memory_id: str,
        content: str,
        memory_type: str,
        metadata: Dict[str, Any]
    ) -> bool:
        """添加记忆（精简版：静默忽略）"""
        logger.debug(f"[MemoryStub] add_memory ignored: {memory_id[:8]}")
        return True

    async def batch_add_memories(
        self,
        user_id: str,
        project_id: str,
        memories: List[Dict[str, Any]]
    ) -> int:
        """批量添加记忆（精简版：静默忽略）"""
        return len(memories) if memories else 0

    async def search_memories(
        self,
        user_id: str,
        project_id: str,
        query: str,
        memory_types: Optional[List[str]] = None,
        limit: int = 10,
        min_importance: float = 0.0,
        chapter_range: Optional[tuple] = None
    ) -> List[Dict[str, Any]]:
        """语义搜索（精简版：返回空列表）"""
        logger.debug(f"[MemoryStub] search_memories ignored query: {query[:20]}")
        return []

    async def get_recent_memories(
        self,
        user_id: str,
        project_id: str,
        current_chapter: int,
        recent_count: int = 3,
        min_importance: float = 0.5
    ) -> List[Dict[str, Any]]:
        """获取最近记忆（精简版：返回空列表）"""
        return []

    async def delete_chapter_memories(
        self,
        user_id: str,
        project_id: str,
        chapter_id: str
    ) -> bool:
        """删除章节记忆（精简版：静默成功）"""
        return True

    async def delete_project_memories(
        self,
        user_id: str,
        project_id: str
    ) -> bool:
        """删除项目所有记忆（精简版：静默成功）"""
        return True

    async def update_memory(
        self,
        user_id: str,
        project_id: str,
        memory_id: str,
        content: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """更新记忆（精简版：静默忽略）"""
        return True

    async def get_memory_stats(
        self,
        user_id: str,
        project_id: str
    ) -> Dict[str, Any]:
        """获取记忆统计（精简版：返回全零统计）"""
        return {
            "total_count": 0,
            "by_type": {},
            "by_chapter": {},
            "foreshadow_count": 0,
            "foreshadow_resolved": 0
        }

    # ------------------------------------------------------------------
    # 以下方法在原版中使用 chromadb，直接返回默认值
    # ------------------------------------------------------------------

    async def find_unresolved_foreshadows(
        self,
        user_id: str,
        project_id: str,
        before_chapter: Optional[int] = None,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """查找未回收伏笔（精简版：返回空列表）"""
        return []

    async def get_memory_context_for_chapter(
        self,
        user_id: str,
        project_id: str,
        chapter_number: int,
        memory_types: Optional[List[str]] = None,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """获取章节相关记忆上下文（精简版：返回空列表）"""
        return []

    async def delete_foreshadow_memories(
        self,
        user_id: str,
        project_id: str,
        chapter_id: str
    ) -> int:
        """删除伏笔记忆（精简版：返回0）"""
        return 0


# 创建全局实例（启动时实例化，不会因导入失败而崩溃）
memory_service = MemoryService()
