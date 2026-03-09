# Backend Vibe Coding - v6.0 架构重构版本

> **智能路由 + 分层开发流程**
> 自动判断任务类型和项目规模，引导进入合适的开发流程

---

## 快速开始

### 第一步：读取入口决策

```
prompts/v6_refactored/A_Decision.txt
```

AI 会引导你：
1. 判断任务类型（新功能 / Bug修复 / 配置 / 优化 / 文档）
2. 判断项目规模（小项目 / 大项目）
3. 自动选择合适的流程

---

## 目录结构

```
v6_refactored/
├── A_Decision.txt              # 入口决策（第一步必读）
├── D_quick/                     # 快速通道（4种场景）
│   ├── D1_bugfix.txt           # Bug修复
│   ├── D2_config.txt           # 配置变更
│   ├── D3_optimize.txt         # 小优化
│   └── D4_doc.txt              # 文档更新
├── S_simple/                    # 小项目流程（单一数据对象）
│   ├── 初始化/
│   │   └── S0_init.txt         # 项目初始化
│   ├── 文档阶段/
│   │   ├── S1_prd.txt          # 需求文档
│   │   ├── S2_features.txt     # 功能梳理
│   │   ├── S3_api.txt          # API设计
│   │   ├── S4_schema.txt       # 数据模型
│   │   ├── S5_service.txt      # 服务设计
│   │   └── S6_test.txt         # 测试设计
│   └── 实施阶段/
│       ├── S7_infra.txt        # 基础设施
│       ├── S8_models.txt       # 数据模型代码
│       ├── S9_repo.txt         # Repository代码
│       ├── S10_service.txt     # Service代码
│       ├── S11_api.txt         # API代码
│       ├── S12_verify.txt      # 验证测试
│       └── S13_report.txt      # 测试报告
└── L_large/                     # 大项目流程（多模块）
    ├── 初始化/
    │   ├── L0_init.txt         # 项目初始化
    │   └── L1_lane.txt         # 泳道图+时序图
    ├── 文档阶段/
    │   ├── L2_prd.txt          # 整体需求
    │   ├── L3_features.txt     # 整体功能
    │   ├── L4_business.txt     # 业务文档
    │   ├── L5_schema.txt       # 整体数据模型
    │   ├── L6_api.txt          # 整体API
    │   ├── L7_split.txt        # 模块拆分（关键节点）
    │   ├── L8_module_features.txt   # 模块功能
    │   ├── L9_module_business.txt   # 模块业务
    │   ├── L10_module_schema.txt    # 模块数据模型
    │   ├── L11_module_api.txt       # 模块API
    │   ├── L12_module_prd.txt       # 模块PRD
    │   └── L13_test.txt            # 测试设计
    └── 实施阶段/
        ├── L14_infra.txt       # 基础设施
        ├── L15_models.txt      # 数据模型
        ├── L16_repo.txt        # Repository
        ├── L17_service.txt     # Service
        ├── L18_api.txt         # API
        ├── L19_integrate.txt   # 模块集成
        ├── L20_gateway.txt     # API Gateway
        └── L21_verify.txt      # 整体验证
```

---

## 流程对比

| 流程 | 适用场景 | 步骤数 | 文档 | 测试 |
|------|---------|--------|------|------|
| **D_quick** | Bug、配置、优化、文档 | 5-8 | 否 | 视情况 |
| **S_simple** | 单一数据对象 | 14 | 完整 | 每层+报告 |
| **L_large** | 多模块系统 | 22+ | 整体+模块 | 单元+集成+E2E |

---

## 使用示例

### 示例1：用户管理系统（S_simple）

```
A_Decision.txt
    ↓
判断为：小项目
    ↓
S0 → S1 → S2 → S3 → S4 → S5 → S6
    ↓
[上下文重置]
    ↓
S7 → S8 → S9 → S10 → S11 → S12 → S13
```

### 示例2：电商系统（L_large）

```
A_Decision.txt
    ↓
判断为：大项目
    ↓
L0 → L1 → L2 → L3 → L4 → L5 → L6 → L7（模块拆分）
    ↓
模块A: S_simple流程
模块B: S_simple流程
模块C: S_simple流程
    ↓
L14 → L15 → L16 → L17 → L18 → L19 → L20 → L21
```

### 示例3：修复登录Bug（D_quick）

```
A_Decision.txt
    ↓
判断为：Bug修复
    ↓
D1_bugfix.txt（5-8步完成）
```

---

## 核心设计原则

### 1. 智能路由

通过 A_Decision.txt 自动判断，避免用户手动选择困扰。

### 2. 分层开发

- 文档阶段：设计先行，不写代码
- 实施阶段：按层实现，每层有测试

### 3. 上下文重置

在关键节点重置会话，保持AI输出质量：
- S6 → S7（文档→实施）
- L7 → L14（规划→实施）
- 模块A → 模块B

### 4. 测试驱动

每层代码都有对应测试，每步都有测试报告。

---

## 与 v5 的区别

| 特性 | v5 | v6 |
|------|----|----|
| 入口 | A_init（固定流程） | A_Decision（智能路由） |
| 流程 | 单一流程 | D/S/L 三种流程 |
| 项目规模 | 不区分 | 明确区分小项目/大项目 |
| 模块化 | 不支持 | L_large 支持多模块 |
| 文档结构 | 扁平 | 分层目录 |

---

## 相关文档

- [使用指南](../../docs/02-快速开始.md)
- [流程选择](../../docs/04-流程选择指南.md)
- [流程图](../../docs/flowsheet.md)

---

*版本：v6.0*
*更新日期：2026-03-09*
