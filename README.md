# News MCP Server with Gradio 🌍

A Model Context Protocol (MCP) server built with Gradio that serves BBC Science and Environment news from RSS feeds.

## Features

- 📰 Fetches news from BBC Science and Environment RSS feed
- 🎨 Interactive Gradio interface
- 📊 JSON output format for MCP protocol
- 🚀 Deployed on Hugging Face Spaces

## RSS Feed Source

- **URL**: https://feeds.bbci.co.uk/news/science_and_environment/rss.xml
- **Category**: Science and Environment
- **Provider**: BBC News

## Deployment to Hugging Face Spaces

This application is designed to be deployed directly to Hugging Face Spaces.

### Setup Instructions

1. **Create a new Space** on Hugging Face:
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Gradio" as the SDK
   - Set visibility as needed

2. **Configure Secrets**:
   - In your Space settings, add a secret variable:
   - Name: `HF_TOKEN`
   - Value: Your Hugging Face token

3. **Deploy**:
   - Push this repository to your Space
   - The Space will automatically install dependencies from `requirements.txt`
   - The app will start automatically using `app.py`

## Local Development

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
pip install -r requirements.txt
```

### Running Locally

```bash
python app.py
```

The server will start on `http://localhost:7860`

## Usage

### Web Interface

1. **Formatted News Tab**: View news in a readable format with titles, descriptions, and links
2. **JSON Output Tab**: Get news in JSON format for integration with other services
3. **About Tab**: Information about the MCP server

### API Access

The Gradio interface automatically provides an API endpoint for programmatic access.

## Environment Variables

- `HF_TOKEN`: Hugging Face token (optional, used for authentication if needed)

## MCP Protocol

This server implements a simple MCP interface for serving news data. The JSON output can be consumed by AI models and other applications that need access to current science and environment news.

## License

MIT License