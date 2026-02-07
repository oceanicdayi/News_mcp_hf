#!/usr/bin/env python3
"""
MCP Server for BBC Science and Environment News using Gradio
"""
import os
import feedparser
import gradio as gr
from typing import List, Dict, Any
import json

# RSS Feed URL
BBC_NEWS_RSS_URL = "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml"

def fetch_news(max_items: int = 10) -> List[Dict[str, Any]]:
    """
    Fetch news from BBC Science and Environment RSS feed
    
    Args:
        max_items: Maximum number of news items to return
        
    Returns:
        List of news items with title, link, description, and published date
    """
    try:
        feed = feedparser.parse(BBC_NEWS_RSS_URL)
        
        # Check for parsing errors
        if feed.bozo and not feed.entries:
            return [{"error": f"Failed to parse feed: {feed.bozo_exception}"}]
        
        if not feed.entries:
            return [{"error": "No news items found in the feed"}]
        
        news_items = []
        for entry in feed.entries[:max_items]:
            news_item = {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "description": entry.get("summary", ""),
                "published": entry.get("published", "")
            }
            news_items.append(news_item)
        
        return news_items
    except Exception as e:
        return [{"error": f"Failed to fetch news: {str(e)}"}]

def get_news_formatted(num_items: int = 10) -> str:
    """
    Get formatted news for display in Gradio interface
    
    Args:
        num_items: Number of news items to fetch
        
    Returns:
        Formatted string with news items
    """
    news_items = fetch_news(max_items=num_items)
    
    if not news_items:
        return "No news items available."
    
    if "error" in news_items[0]:
        return news_items[0]["error"]
    
    output = []
    for i, item in enumerate(news_items, 1):
        output.append(f"**{i}. {item['title']}**")
        output.append(f"📅 {item['published']}")
        output.append(f"📝 {item['description']}")
        output.append(f"🔗 [Read more]({item['link']})")
        output.append("\n" + "-" * 80 + "\n")
    
    return "\n".join(output)

def get_news_json(num_items: int = 10) -> str:
    """
    Get news in JSON format for MCP protocol
    
    Args:
        num_items: Number of news items to fetch
        
    Returns:
        JSON string with news items
    """
    news_items = fetch_news(max_items=num_items)
    return json.dumps(news_items, indent=2)

# Create Gradio interface
with gr.Blocks(title="BBC Science & Environment News MCP Server") as demo:
    gr.Markdown("# 🌍 BBC Science & Environment News MCP Server")
    gr.Markdown(f"Fetching news from: {BBC_NEWS_RSS_URL}")
    
    with gr.Tab("Formatted News"):
        with gr.Row():
            num_items_slider = gr.Slider(
                minimum=1, 
                maximum=20, 
                value=10, 
                step=1, 
                label="Number of News Items"
            )
        
        fetch_button = gr.Button("Fetch News", variant="primary")
        news_output = gr.Markdown()
        
        fetch_button.click(
            fn=get_news_formatted,
            inputs=[num_items_slider],
            outputs=[news_output]
        )
    
    with gr.Tab("JSON Output"):
        with gr.Row():
            num_items_json = gr.Slider(
                minimum=1, 
                maximum=20, 
                value=10, 
                step=1, 
                label="Number of News Items"
            )
        
        fetch_json_button = gr.Button("Fetch News (JSON)", variant="primary")
        json_output = gr.Code(language="json", label="News Data (JSON)")
        
        fetch_json_button.click(
            fn=get_news_json,
            inputs=[num_items_json],
            outputs=[json_output]
        )
    
    with gr.Tab("About"):
        gr.Markdown("""
        ## About this MCP Server
        
        This is a Model Context Protocol (MCP) server built with Gradio that serves news from:
        - **Source**: BBC Science and Environment RSS Feed
        - **URL**: https://feeds.bbci.co.uk/news/science_and_environment/rss.xml
        
        ### Features:
        - Fetch latest science and environment news
        - View news in formatted or JSON format
        - Configurable number of news items
        - Deployed on Hugging Face Spaces
        
        ### MCP Protocol:
        This server can be used as a data source for AI models and other applications
        that need access to current science and environment news.
        """)

if __name__ == "__main__":
    # Get HF_TOKEN from environment (for authentication if needed)
    # This token is automatically available in Hugging Face Spaces
    # and can be used for authenticated API calls if required in the future
    hf_token = os.getenv("HF_TOKEN")
    
    # Launch the Gradio app
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )
