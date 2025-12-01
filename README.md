# 线性代数 - 用Python和可视化轻松学习
## Linear Algebra Made Easy - Learn with Python and Visualization

这是一本关于线性代数的教程书籍，配合Python代码和可视化帮助理解。

This is a tutorial book on Linear Algebra with Python code and visualizations.

## 📚 书籍结构 | Book Structure

本书分为上下两册，共15章：

### 上册 (Chapters 1-7)
- 第1章: 向量基础 (向量、坐标系、加减法、标量乘法、单位向量、内积、投影、范数)
- 第2章: 矩阵基础 (矩阵、转置、形状、乘法、几何视角、性质)
- 第3章: 矩阵乘法的四种视角
- 第4章: 行列式
- 第5章: 矩阵的逆
- 第6章: 向量空间和基底
- 第7章: 线性方程组

### 下册 (Chapters 8-15)
- 第8章: 几何变换 (缩放、旋转、剪切、正交投影、镜像、仿射变换)
- 第9章: 正交矩阵和QR分解
- 第10章: 回归分析 (线性回归、多元线性回归、多项式回归)
- 第11章: 特征值分解
- 第12章: 主成分分析 (PCA)
- 第13章: 二次型和Cholesky分解
- 第14章: 奇异值分解 (SVD)
- 第15章: 图论与矩阵

## 📖 生成完整书籍 | Generate Complete Book

本仓库包含散装的PDF章节文件。使用 `merge_book.py` 脚本可以将它们合并成完整的可连续阅读的书籍。

### 前置要求 | Requirements

```bash
pip install PyPDF2
```

### 运行合并脚本 | Run Merge Script

```bash
python merge_book.py
```

### 输出文件 | Output Files

运行脚本后，会在 `merged_books/` 目录下生成以下文件：

| 文件名 | 说明 |
|--------|------|
| `线性代数_上册.pdf` | 上册 (第1-7章，含前言) |
| `线性代数_下册.pdf` | 下册 (第8-15章，含前言) |
| `线性代数_完整版.pdf` | 完整版 (全部15章，含两册前言) |

## 📂 文件说明 | File Description

- `LA_XX_YY_topic.pdf`: 第XX章第YY节的PDF文件
- `LA_XX_YY_ZZ.ipynb`: 对应章节的Jupyter Notebook代码
- `LA_00_上册_正文前_V2.pdf`: 上册前言
- `LA_00_下册_正文前_V2.pdf`: 下册前言

## 🔧 依赖 | Dependencies

- Python 3.6+
- PyPDF2

## 📝 License

Please refer to the original author for licensing information.
