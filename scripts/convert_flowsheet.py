#!/usr/bin/env python3
"""
将 flowsheet.md 中的 mermaid 流程图转换为 PNG 图片
"""

import re
import subprocess
import hashlib
from pathlib import Path

PROMPT_DIR = Path(__file__).parent.parent / "prompt"
MMDC_PATH = "/home/mozinodey/.nvm/versions/node/v16.20.2/bin/mmdc"
PUPPETEER_CONFIG = "/tmp/puppeteer.json"


def convert_mermaid_to_png(mermaid_code: str, output_path: Path) -> bool:
    """将 mermaid 代码转换为 PNG"""
    try:
        input_file = output_path.with_suffix('.mmd')
        input_file.write_text(mermaid_code, encoding='utf-8')
        
        result = subprocess.run(
            [MMDC_PATH, "-i", str(input_file), "-o", str(output_path), "-p", PUPPETEER_CONFIG, "-w", "1600", "-H", "1200", "-s", "2"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        input_file.unlink(missing_ok=True)
        
        if result.returncode != 0:
            print(f"转换失败: {result.stderr}")
            return False
        
        return output_path.exists()
    except Exception as e:
        print(f"转换失败: {e}")
        return False


def main():
    print("开始转换 flowsheet...")
    
    if not PROMPT_DIR.exists():
        print(f"目录不存在: {PROMPT_DIR}")
        return
    
    converted = 0
    
    for category_dir in PROMPT_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        
        category = category_dir.name
        flowsheet_path = category_dir / "flowsheet.md"
        
        if not flowsheet_path.exists():
            continue
        
        content = flowsheet_path.read_text(encoding='utf-8')
        mermaid_match = re.search(r'```mermaid\n(.*?)```', content, re.DOTALL)
        
        if not mermaid_match:
            print(f"分类 {category}: 未找到 mermaid 代码")
            continue
        
        mermaid_code = mermaid_match.group(1).strip()
        
        png_content_hash = hashlib.md5(mermaid_code.encode()).hexdigest()
        cached_png = category_dir / f"flowsheet_{png_content_hash[:8]}.png"
        
        if cached_png.exists():
            print(f"分类 {category}: 使用现有图片")
            converted += 1
            continue
        
        print(f"分类 {category}: 转换中...")
        
        for old_png in category_dir.glob("flowsheet_*.png"):
            old_png.unlink()
        
        if convert_mermaid_to_png(mermaid_code, cached_png):
            print(f"分类 {category}: 转换成功 -> {cached_png.name}")
            converted += 1
        else:
            print(f"分类 {category}: 转换失败")
    
    print(f"\n完成! 共处理 {converted} 个流程图")


if __name__ == "__main__":
    main()
