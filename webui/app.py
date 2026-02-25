import streamlit as st
import re
from pathlib import Path

PROMPT_DIR = Path(__file__).parent.parent / "prompt"


def scan_prompts():
    prompts = []
    flowsheets = {}
    
    if not PROMPT_DIR.exists():
        return prompts, flowsheets
    
    for category_dir in PROMPT_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        
        category = category_dir.name
        flowsheet_path = category_dir / "flowsheet.md"
        
        if flowsheet_path.exists():
            content = flowsheet_path.read_text(encoding='utf-8')
            
            mermaid_match = re.search(r'```mermaid\n(.*?)```', content, re.DOTALL)
            png_path = None
            
            if mermaid_match:
                mermaid_code = mermaid_match.group(1).strip()
                import hashlib
                png_hash = hashlib.md5(mermaid_code.encode()).hexdigest()[:8]
                png_candidate = category_dir / f"flowsheet_{png_hash}.png"
                if png_candidate.exists():
                    png_path = str(png_candidate)
            
            flowsheets[category] = {
                "content": content,
                "png": png_path
            }
        
        for file_path in category_dir.iterdir():
            if file_path.name == "flowsheet.md":
                continue
            if file_path.suffix.lower() not in ['.md', '.txt']:
                continue
            
            content = file_path.read_text(encoding='utf-8')
            
            prompts.append({
                "id": f"{category}/{file_path.name}",
                "title": file_path.stem,
                "category": category,
                "content": content,
                "path": str(file_path)
            })
    
    return sorted(prompts, key=lambda x: (x["category"], x["title"])), flowsheets


def init_session_state():
    if "prompts" not in st.session_state or "flowsheets" not in st.session_state:
        prompts, flowsheets = scan_prompts()
        st.session_state.prompts = prompts
        st.session_state.flowsheets = flowsheets


def main():
    st.set_page_config(page_title="PromptHub", page_icon="💡", layout="wide")
    st.title("💡 PromptHub - 提示词库")

    init_session_state()

    with st.sidebar:
        st.header("📁 提示词分类")
        
        categories = sorted(set(p["category"] for p in st.session_state.prompts))
        selected_category = st.selectbox("选择分类", categories, key="category_select")

        st.divider()
        if st.button("🔄 刷新列表", use_container_width=True):
            prompts, flowsheets = scan_prompts()
            st.session_state.prompts = prompts
            st.session_state.flowsheets = flowsheets
            st.rerun()

    filtered_prompts = [p for p in st.session_state.prompts if p["category"] == selected_category]

    if not filtered_prompts:
        st.info("暂无提示词")
        return

    if selected_category in st.session_state.flowsheets:
        flowsheet = st.session_state.flowsheets[selected_category]
        
        st.subheader("📊 流程图")
        
        if flowsheet.get("png"):
            st.image(flowsheet["png"], use_container_width=True)
        else:
            text_content = re.sub(r'```mermaid\n.*?```', '', flowsheet["content"], flags=re.DOTALL).strip()
            if text_content:
                st.markdown(text_content)
        
        st.divider()

    st.subheader("📄 提示词")

    for prompt in filtered_prompts:
        stage = get_stage(prompt["title"])
        expander_label = f"**Step {stage}** {get_title_without_stage(prompt['title'])}" if stage else f"📄 {prompt['title']}"
        
        with st.expander(expander_label, expanded=False):
            st.text_area(
                "内容（选中后 Ctrl+C 复制）",
                value=prompt["content"],
                height=200,
                key=f"content_{prompt['id']}",
                disabled=True
            )


def get_stage(title):
    match = re.match(r'^(\d+)', title)
    if match:
        return match.group(1)
    return None


def get_title_without_stage(title):
    return re.sub(r'^\d+_', '', title)


if __name__ == "__main__":
    main()
