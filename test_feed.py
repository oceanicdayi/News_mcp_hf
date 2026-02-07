#!/usr/bin/env python3
"""
Test script for the BBC News MCP Server

This script tests the core functionality of fetching and parsing RSS feeds.
Run this in an environment with network access.
"""
import sys
import feedparser
import json

def test_rss_feed():
    """Test fetching the BBC Science & Environment RSS feed"""
    feed_url = 'https://feeds.bbci.co.uk/news/science_and_environment/rss.xml'
    
    print("Testing BBC Science & Environment RSS Feed")
    print("=" * 60)
    print(f"Feed URL: {feed_url}")
    print()
    
    try:
        # Parse the feed
        feed = feedparser.parse(feed_url)
        
        # Check for parsing errors
        if feed.bozo:
            print(f"⚠️  Feed parsing warning: {feed.bozo_exception}")
            if not feed.entries:
                print("❌ No entries found. This might be a network issue.")
                return False
        
        # Get feed metadata
        feed_title = feed.feed.get('title', 'N/A')
        feed_description = feed.feed.get('description', 'N/A')
        
        print(f"Feed Title: {feed_title}")
        print(f"Feed Description: {feed_description}")
        print(f"Total Entries: {len(feed.entries)}")
        print()
        
        if not feed.entries:
            print("❌ No entries found in the feed")
            return False
        
        # Display first 3 entries
        print("First 3 News Items:")
        print("-" * 60)
        
        for i, entry in enumerate(feed.entries[:3], 1):
            print(f"\n{i}. {entry.get('title', 'No title')}")
            print(f"   Published: {entry.get('published', 'N/A')}")
            print(f"   Link: {entry.get('link', 'N/A')}")
            description = entry.get('summary', 'No description')
            print(f"   Description: {description[:150]}...")
        
        print("\n" + "=" * 60)
        print("✅ RSS feed test PASSED!")
        print(f"✅ Successfully fetched {len(feed.entries)} news items")
        
        # Test JSON export
        news_items = []
        for entry in feed.entries[:5]:
            news_items.append({
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'description': entry.get('summary', ''),
                'published': entry.get('published', '')
            })
        
        print("\nJSON Export (first 5 items):")
        print(json.dumps(news_items, indent=2))
        
        return True
        
    except Exception as e:
        print(f"❌ Error during test: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_rss_feed()
    sys.exit(0 if success else 1)
