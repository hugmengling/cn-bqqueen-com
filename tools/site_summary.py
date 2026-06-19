import json
import sys
from datetime import datetime

SITE_DATA = {
    "url": "https://cn-bqqueen.com",
    "keywords": ["赏金女王", "娱乐", "游戏", "在线", "休闲"],
    "tags": ["赏金", "女王", "休闲娱乐", "在线平台"],
    "description": "赏金女王是一个专注于高品质在线娱乐与休闲游戏体验的平台，提供多样化的互动内容与用户友好的界面。",
    "last_updated": "2025-04-07"
}

def load_site_summary(data: dict) -> dict:
    """从内置数据字典中提取并组织站点摘要信息。"""
    return {
        "url": data.get("url", ""),
        "keywords": data.get("keywords", []),
        "tags": data.get("tags", []),
        "description": data.get("description", ""),
        "last_updated": data.get("last_updated", "")
    }

def format_keywords(keywords: list) -> str:
    """将关键词列表格式化为逗号分隔的字符串。"""
    if not keywords:
        return "无关键词"
    return ", ".join(keywords)

def format_tags(tags: list) -> str:
    """将标签列表格式化为以 # 开头的字符串。"""
    if not tags:
        return "无标签"
    return " ".join([f"#{tag}" for tag in tags])

def build_report(summary: dict) -> str:
    """构建格式化结构化摘要报告。"""
    lines = []
    lines.append("=" * 50)
    lines.append("技术站点摘要报告")
    lines.append("=" * 50)
    lines.append(f"站点地址: {summary['url']}")
    lines.append(f"核心关键词: {format_keywords(summary['keywords'])}")
    lines.append(f"标签: {format_tags(summary['tags'])}")
    lines.append(f"简短说明: {summary['description']}")
    lines.append(f"数据更新时间: {summary['last_updated']}")
    lines.append("-" * 50)
    lines.append(f"报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)
    return "\n".join(lines)

def build_json_output(summary: dict) -> str:
    """将摘要数据序列化为格式化的 JSON 字符串。"""
    output = {
        "url": summary["url"],
        "keywords": summary["keywords"],
        "tags": summary["tags"],
        "description": summary["description"],
        "last_updated": summary["last_updated"],
        "generated_at": datetime.now().isoformat()
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def display_usage() -> None:
    """打印工具使用说明。"""
    print("使用方法: python tools/site_summary.py [--json]")
    print("  --json  以 JSON 格式输出摘要")
    print("  (无参数) 以可读文本格式输出摘要")

def main() -> None:
    """主入口：读取站点数据并输出结构化摘要。"""
    args = sys.argv[1:]
    use_json = "--json" in args
    show_help = "-h" in args or "--help" in args

    if show_help:
        display_usage()
        return

    summary = load_site_summary(SITE_DATA)

    if use_json:
        print(build_json_output(summary))
    else:
        print(build_report(summary))

if __name__ == "__main__":
    main()