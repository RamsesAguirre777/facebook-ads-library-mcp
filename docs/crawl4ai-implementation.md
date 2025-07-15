# 🚀 Crawl4AI Implementation Guide

## 🧠 Base Architecture

Nuestro MCP está construido sobre **Crawl4AI v0.7.0** - el crawler más avanzado y optimizado para LLMs del mundo, con más de 19.1k stars en GitHub.

### 🔧 Core Components

#### 1. AsyncWebCrawler
```python
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

# Configuración optimizada para Facebook Ads
browser_config = BrowserConfig(
    headless=True,
    browser_type="chromium",
    viewport_width=1920,
    viewport_height=1080,
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
)

# Configuración de crawler específica
crawler_config = CrawlerRunConfig(
    cache_mode=CacheMode.ENABLED,
    screenshot=True,
    pdf=False,
    word_count_threshold=200,
    extraction_strategy=JsonCssExtractionStrategy(schema),
    markdown_generator=DefaultMarkdownGenerator(),
    content_filter=PruningContentFilter(threshold=0.48)
)

async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(url, config=crawler_config)
```

#### 2. Extraction Strategies
```python
# CSS-based extraction (más rápido)
schema = {
    "name": "Facebook Ads",
    "baseSelector": "[data-testid='ad-card']",
    "fields": [
        {
            "name": "advertiser_name",
            "selector": "[data-testid='advertiser-name']",
            "type": "text"
        },
        {
            "name": "ad_text",
            "selector": "[data-testid='ad-text']",
            "type": "text"
        },
        {
            "name": "cta_button",
            "selector": "[role='button']",
            "type": "text"
        }
    ]
}

# LLM-based extraction (más inteligente)
llm_strategy = LLMExtractionStrategy(
    llm_config=LLMConfig(
        provider="openai/gpt-4o-mini",
        api_token=os.getenv("OPENAI_API_KEY")
    ),
    schema=FacebookAdSchema.model_json_schema(),
    instruction="Extract ad data with emotional sentiment analysis"
)
```

#### 3. Advanced Features Implementation

**Stealth Mode para evitar detección:**
```python
browser_config = BrowserConfig(
    headless=True,
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    },
    proxy_config=ProxyConfig(
        server="proxy.example.com:8080",
        username="user",
        password="pass"
    )
)
```

**Session Management para mantener estado:**
```python
# Persistent browser profile
user_data_dir = os.path.join(Path.home(), ".crawl4ai", "facebook_profile")
browser_config = BrowserConfig(
    user_data_dir=user_data_dir,
    use_persistent_context=True,
    session_id="facebook_ads_session"
)
```

### 🎯 Facebook Ads Library Optimization

#### 1. Dynamic Content Handling
```python
# JavaScript para cargar más ads
js_code = """
(async () => {
    // Scroll to trigger lazy loading
    for (let i = 0; i < 5; i++) {
        window.scrollTo(0, document.body.scrollHeight);
        await new Promise(resolve => setTimeout(resolve, 2000));
    }
    
    // Click "Load More" button if exists
    const loadMoreBtn = document.querySelector('[data-testid="load-more-button"]');
    if (loadMoreBtn) {
        loadMoreBtn.click();
        await new Promise(resolve => setTimeout(resolve, 3000));
    }
})();
"""

crawler_config = CrawlerRunConfig(
    js_code=[js_code],
    wait_for_selector="[data-testid='ad-card']",
    delay_before_return_html=5.0
)
```

#### 2. Adaptive Pagination
```python
async def crawl_all_pages(self, brand_name: str, max_pages: int = 10):
    """Crawl all pages of Facebook Ads for a brand"""
    results = []
    
    for page in range(1, max_pages + 1):
        url = f"https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&q={brand_name}&search_type=keyword_unordered&page={page}"
        
        result = await self.crawler.arun(url, config=self.crawler_config)
        
        if not result.success or not result.extracted_content:
            break
            
        ads_data = json.loads(result.extracted_content)
        if not ads_data:
            break
            
        results.extend(ads_data)
        
        # Rate limiting
        await asyncio.sleep(random.uniform(2, 5))
    
    return results
```

#### 3. Error Handling & Retry Logic
```python
from crawl4ai.async_dispatcher import RateLimiter

rate_limiter = RateLimiter(
    base_delay=(2.0, 5.0),
    max_delay=60.0,
    max_retries=3
)

async def robust_crawl(self, url: str, retries: int = 3):
    """Robust crawling with exponential backoff"""
    for attempt in range(retries):
        try:
            result = await self.crawler.arun(url, config=self.crawler_config)
            if result.success:
                return result
        except Exception as e:
            if attempt == retries - 1:
                raise e
            await asyncio.sleep(2 ** attempt)
    
    return None
```

## 🎨 Content Processing Pipeline

### 1. Markdown Generation
```python
# Optimized markdown for LLM processing
markdown_generator = DefaultMarkdownGenerator(
    content_filter=BM25ContentFilter(
        user_query="Facebook advertising campaigns and brand strategies",
        bm25_threshold=1.2
    )
)
```

### 2. Media Extraction
```python
# Extract images, videos, and responsive formats
crawler_config = CrawlerRunConfig(
    screenshot=True,
    extract_media=True,
    lazy_load_images=True,
    capture_network=True  # For tracking resources
)
```

### 3. Structured Data Processing
```python
# Post-processing extracted data
def process_ad_data(self, raw_data):
    """Process and enrich ad data"""
    processed_ads = []
    
    for ad in raw_data:
        processed_ad = {
            "id": ad.get("id"),
            "advertiser": ad.get("advertiser_name"),
            "text": ad.get("ad_text"),
            "cta": ad.get("cta_button"),
            "images": ad.get("images", []),
            "targeting": self.extract_targeting_info(ad),
            "metrics": self.estimate_performance(ad),
            "sentiment": self.analyze_sentiment(ad.get("ad_text", "")),
            "themes": self.extract_themes(ad.get("ad_text", "")),
            "scraped_at": datetime.now().isoformat()
        }
        processed_ads.append(processed_ad)
    
    return processed_ads
```

## 🚀 Performance Optimizations

### 1. Concurrent Processing
```python
async def crawl_multiple_brands(self, brands: List[str]):
    """Crawl multiple brands concurrently"""
    tasks = []
    
    for brand in brands:
        task = asyncio.create_task(self.search_facebook_ads(brand))
        tasks.append(task)
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

### 2. Memory Management
```python
# Memory-adaptive dispatcher
from crawl4ai.async_dispatcher import MemoryAdaptiveDispatcher

dispatcher = MemoryAdaptiveDispatcher(
    rate_limiter=RateLimiter(base_delay=(1.0, 3.0)),
    max_memory_usage=0.8  # Use max 80% of available memory
)
```

### 3. Caching Strategy
```python
# Intelligent caching
crawler_config = CrawlerRunConfig(
    cache_mode=CacheMode.ENABLED,
    cache_ttl=3600,  # 1 hour cache
    bypass_cache=False
)
```

## 🔍 Advanced Features

### 1. Geolocation Support
```python
# World-aware crawling
crawler_config = CrawlerRunConfig(
    locale="en-US",
    timezone_id="America/New_York",
    geolocation=GeolocationConfig(
        latitude=40.7128,
        longitude=-74.0060,
        accuracy=100.0
    )
)
```

### 2. Network Traffic Capture
```python
# Capture network requests for API analysis
crawler_config = CrawlerRunConfig(
    capture_network=True,
    capture_console=True,
    mhtml=True  # Save complete page state
)
```

### 3. Browser Pooling
```python
# Pre-warmed browser instances
browser_config = BrowserConfig(
    pool_size=5,
    pre_warm_pages=True,
    max_concurrent_pages=3
)
```

## 🛡️ Security & Anti-Detection

### 1. Proxy Rotation
```python
# Dynamic proxy switching
proxy_rotation = ProxyRotationStrategy([
    ProxyConfig(server="proxy1.example.com:8080"),
    ProxyConfig(server="proxy2.example.com:8080"),
    ProxyConfig(server="proxy3.example.com:8080")
])

crawler_config = CrawlerRunConfig(
    proxy_rotation_strategy=proxy_rotation
)
```

### 2. User Agent Rotation
```python
# Random user agent selection
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
]

crawler_config = CrawlerRunConfig(
    user_agent=random.choice(user_agents)
)
```

### 3. Robots.txt Compliance
```python
# Respect robots.txt
crawler_config = CrawlerRunConfig(
    check_robots_txt=True,
    respect_robots_txt=True
)
```

## 📊 Monitoring & Analytics

### 1. Performance Metrics
```python
# Built-in performance monitoring
result = await crawler.arun(url, config=crawler_config)

metrics = {
    "fetch_time": result.dispatch_result.end_time - result.dispatch_result.start_time,
    "memory_usage": result.dispatch_result.memory_usage,
    "peak_memory": result.dispatch_result.peak_memory,
    "success_rate": result.success,
    "content_size": len(result.html),
    "extracted_items": len(json.loads(result.extracted_content or "[]"))
}
```

### 2. Error Tracking
```python
# Comprehensive error handling
try:
    result = await crawler.arun(url, config=crawler_config)
except Exception as e:
    error_context = {
        "error_type": type(e).__name__,
        "error_message": str(e),
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "stack_trace": traceback.format_exc()
    }
    await self.log_error(error_context)
```

## 🔮 Future Enhancements

### Planned Features
1. **GraphQL API Integration** - Direct Facebook Graph API access
2. **Real-time Monitoring** - WebSocket connections for live updates
3. **ML-based Targeting Analysis** - AI-powered audience insights
4. **Competitor Benchmarking** - Automated competitive analysis
5. **Sentiment Analysis** - Advanced NLP for ad messaging analysis
6. **Performance Prediction** - ML models for ad performance forecasting
7. **Visual Recognition** - Computer vision for ad creative analysis
8. **Multi-platform Support** - Extend to Instagram, Twitter, LinkedIn
9. **Dashboard Integration** - Real-time analytics dashboard
10. **API Gateway** - RESTful API for external integrations

### Technical Roadmap
- **Q1 2025**: Enhanced extraction strategies
- **Q2 2025**: ML-powered insights
- **Q3 2025**: Multi-platform expansion
- **Q4 2025**: Enterprise features

---

Este MCP representa el futuro del marketing intelligence, combinando la potencia de Crawl4AI con estrategias avanzadas de extracción y procesamiento de datos. 🚀
