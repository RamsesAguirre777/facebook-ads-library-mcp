# facebook_ads_mcp_complete.py
from fastmcp import FastMCP
import requests
import json
import sys
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union
import re
from urllib.parse import urlencode
import time
import base64
from crawl4ai import AsyncWebCrawler   # <<< CHANGED: replaced WebCrawler with AsyncWebCrawler >>>
import asyncio                         # <<< CHANGED: required for async run() handling >>>


class FacebookAdsLibraryAPI:
    """Complete Facebook Ads Library API wrapper with advanced features"""
    
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/v19.0/ads_archive"
        self.crawler = None             # <<< CHANGED: removed WebCrawler() instance; Async crawler will be created per call >>>
        
    def _make_request(self, params: dict) -> dict:
        """Make API request with error handling"""
        params['access_token'] = self.access_token
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "success": False}
    
    def _extract_ad_id_from_url(self, snapshot_url: str) -> str:
        """Extract ad ID from snapshot URL"""
        match = re.search(r'id=(\d+)', snapshot_url)
        return match.group(1) if match else None
    
    def _analyze_ad_creative(self, snapshot_url: str) -> dict:
        """Analyze ad creative using AsyncWebCrawler"""   # <<< CHANGED: updated description >>>
        async def crawl_page():                           # <<< CHANGED: async inner function for AsyncWebCrawler >>>
            async with AsyncWebCrawler(verbose=True) as crawler:
                result = await crawler.arun(url=snapshot_url, only_text=True)
                return {
                    "text_content": result.cleaned_html,
                    "extracted_text": result.extracted_content,
                    "success": True
                }

        try:
            # Run the async crawler synchronously via asyncio.run()
            return asyncio.run(crawl_page())              # <<< CHANGED: replaced old sync .run() with asyncio.run(async func) >>>
        except Exception as e:
            return {"error": str(e), "success": False}    # <<< CHANGED: identical error handling retained >>>


# Initialize MCP Server
mcp = FastMCP(
    name="Facebook Ads Library Complete",
    instructions="""
    Complete Facebook Ads Library MCP with 15+ advanced tools for comprehensive ad intelligence.
    Provides deep insights into competitor advertising strategies, creative analysis, and market intelligence.
    """
)

# Initialize API client
def get_facebook_token():
    """Get Facebook access token from command line arguments"""
    if "--facebook-token" in sys.argv:
        token_index = sys.argv.index("--facebook-token") + 1
        if token_index < len(sys.argv):
            return sys.argv[token_index]
    return os.getenv("FACEBOOK_ACCESS_TOKEN")

fb_api = FacebookAdsLibraryAPI(get_facebook_token())

# ===== BÚSQUEDA Y DESCUBRIMIENTO =====

@mcp.tool(description="Search Facebook Ads Library with advanced filters")
def search_facebook_ads(
    brand_name: str,
    country: str = "US",
    ad_type: str = "ALL",
    date_range: int = 30,
    limit: int = 50
) -> dict:
    """
    Search Facebook Ads Library with comprehensive filters
    
    Args:
        brand_name: Brand or company name to search
        country: Target country code (US, GB, CA, etc.)
        ad_type: Type of ads (ALL, POLITICAL_AND_ISSUE_ADS, etc.)
        date_range: Days to look back (default: 30)
        limit: Maximum number of ads to return
    """
    params = {
        'search_terms': brand_name,
        'ad_reached_countries': [country],
        'fields': 'id,ad_creation_time,ad_creative_bodies,ad_creative_link_captions,ad_creative_link_descriptions,ad_creative_link_titles,ad_snapshot_url,currency,demographic_distribution,delivery_by_region,impressions,page_id,page_name,publisher_platforms,spend',
        'limit': limit,
        'ad_active_status': 'ALL'
    }
    
    if ad_type != "ALL":
        params['ad_type'] = ad_type
    
    result = fb_api._make_request(params)
    
    if result.get("success") is False:
        return result
    
    return {
        "brand": brand_name,
        "total_ads": len(result.get("data", [])),
        "ads": result.get("data", []),
        "search_params": params,
        "success": True
    }

@mcp.tool(description="Discover competitor brands in an industry")
def discover_competitor_brands(
    industry_keywords: str,
    region: str = "US",
    min_ads: int = 5,
    limit: int = 100
) -> dict:
    """
    Discover competitor brands by industry keywords
    """
    params = {
        'search_terms': industry_keywords,
        'ad_reached_countries': [region],
        'fields': 'page_name,page_id,ad_creation_time',
        'limit': limit * 3,
        'ad_active_status': 'ACTIVE'
    }
    
    result = fb_api._make_request(params)
    
    if result.get("success") is False:
        return result
    
    brand_counts = {}
    for ad in result.get("data", []):
        page_name = ad.get("page_name", "")
        if page_name:
            brand_counts[page_name] = brand_counts.get(page_name, 0) + 1
    
    qualified_brands = {
        brand: count for brand, count in brand_counts.items() 
        if count >= min_ads
    }
    
    sorted_brands = sorted(qualified_brands.items(), key=lambda x: x[1], reverse=True)
    
    return {
        "industry": industry_keywords,
        "region": region,
        "discovered_brands": sorted_brands[:limit],
        "total_qualified_brands": len(qualified_brands),
        "success": True
    }

@mcp.tool(description="Analyze ad creative elements in detail")
def analyze_ad_creative_elements(
    ad_snapshot_url: str,
    extract_text: bool = True,
    analyze_images: bool = True,
    detect_cta: bool = True
) -> dict:
    """
    Deep analysis of ad creative elements
    """
    creative_analysis = fb_api._analyze_ad_creative(ad_snapshot_url)
    
    if not creative_analysis.get("success"):
        return creative_analysis
    
    analysis_result = {
        "ad_url": ad_snapshot_url,
        "ad_id": fb_api._extract_ad_id_from_url(ad_snapshot_url),
        "analysis": {}
    }
    
    if extract_text:
        text_content = creative_analysis.get("extracted_text", "")
        analysis_result["analysis"]["text_analysis"] = {
            "word_count": len(text_content.split()),
            "character_count": len(text_content),
            "sentiment_keywords": re.findall(r'\b(?:amazing|best|free|save|new|limited|exclusive|now)\b', text_content.lower()),
            "full_text": text_content
        }
    
    if detect_cta:
        text_content = creative_analysis.get("extracted_text", "")
        cta_patterns = [
            r'\b(?:shop now|buy now|learn more|sign up|download|get started|try free|claim offer)\b',
            r'\b(?:click here|tap here|swipe up|see more|order now|book now)\b'
        ]
        
        detected_ctas = []
        for pattern in cta_patterns:
            matches = re.findall(pattern, text_content.lower())
            detected_ctas.extend(matches)
        
        analysis_result["analysis"]["cta_analysis"] = {
            "detected_ctas": detected_ctas,
            "cta_count": len(detected_ctas),
            "urgency_words": re.findall(r'\b(?:now|today|limited|hurry|urgent|expires|deadline)\b', text_content.lower())
        }
    
    analysis_result["success"] = True
    return analysis_result

# (Rest of the file remains unchanged)
# All other classes, MCP tools, and methods are exactly as before.

if __name__ == "__main__":
    token = get_facebook_token()
    if not token:
        print("❌ Facebook access token required!")
        print("Usage: python facebook_ads_mcp_complete.py --facebook-token YOUR_TOKEN")
        sys.exit(1)
    
    print("✅ Facebook Ads Library MCP Server starting...")
    print("🔧 Available tools: 8 advanced Facebook advertising intelligence tools")
    mcp.run(transport="stdio")
