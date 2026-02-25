# PromptHub

提示词管理工具，用于整理和展示面向 Claude Code / Opencode 的开发流程 Prompt 模板。

## 功能

- 分类管理提示词
- 流程图展示
- Web 界面快速查看和复制

## 快速开始

### 1. 安装依赖

```bash
cd webui
pip install -r requirements.txt
```

### 2. 转换流程图（如有 mermaid 流程图）

```bash
python scripts/convert_flowsheet.py
```

### 3. 启动 WebUI

```bash
./start.sh
```

访问 http://localhost:12000

### 4. 停止服务

```bash
./stop.sh
```

## 项目结构

```
PromptHub/
├── prompt/                 # Prompt 模板目录
│   └── new_feature/       # 新功能开发流程
│       ├── flowsheet.md   # 流程图
│       └── *.md           # 各阶段 Prompt
├── webui/                 # Web 前端
│   └── app.py            # Streamlit 应用
├── scripts/               # 工具脚本
│   └── convert_flowsheet.py
├── env/                   # Docker 环境
│   ├── Dockerfile
│   └── requirements.txt
├── start.sh              # 启动脚本
└── stop.sh               # 停止脚本
```

## 添加新的 Prompt

1. 在 `prompt/` 下创建分类目录
2. 添加 `flowsheet.md`（可选）绘制流程图
3. 添加 Prompt 文件（`.md` 或 `.txt`）
4. 运行 `python scripts/convert_flowsheet.py` 更新流程图
5. 刷新 WebUI
