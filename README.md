# 🔥 Facebook Ads Library MCP - Advanced Intelligence Platform

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.6+-green.svg)](https://github.com/modelcontextprotocol/python-sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/RamsesAguirre777/facebook-ads-library-mcp)

> **The most powerful Facebook Ads Library MCP server with 15+ advanced tools for competitive intelligence, market analysis, and advertising insights. Built with FastMCP and completely FREE.**

## 🌟 **Why This MCP?**

**Beats paid services like ScrapeCreators ($497/month) with:**
- ✅ **15+ Advanced Tools** vs their 5-6 basic ones
- ✅ **AI-Powered Creative Analysis** (they don't have this)
- ✅ **ML Performance Prediction** (they don't have this)
- ✅ **Direct API Access** (no proxy limitations)
- ✅ **100% Free & Open Source** (vs $497/month)
- ✅ **Complete Customization** (add your own features)

## 🚀 **Quick Start**

### **1. Installation**
```bash
git clone https://github.com/RamsesAguirre777/facebook-ads-library-mcp.git
cd facebook-ads-library-mcp
pip install -r requirements.txt
```

### **2. Get Facebook Access Token**
1. Go to [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. Generate access token with `ads_read` permission
3. (Optional) [Extend token](https://developers.facebook.com/tools/debug/accesstoken/) to 60 days

### **3. Configure Claude Desktop**
Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "facebook_ads": {
      "command": "python",
      "args": [
        "/path/to/facebook-ads-library-mcp/facebook_ads_mcp_complete.py",
        "--facebook-token",
        "YOUR_FACEBOOK_ACCESS_TOKEN"
      ]
    }
  }
}
```

### **4. Restart Claude Desktop**

## 🛠️ **15+ Advanced Tools**

### **🔍 Search & Discovery**
- **`search_facebook_ads()`** - Advanced search with multiple filters
- **`discover_competitor_brands()`** - Find industry competitors automatically
- **`find_similar_advertisers()`** - Discover brands with similar strategies

### **📊 Deep Analysis**
- **`analyze_ad_creative_elements()`** - AI-powered creative analysis
- **`analyze_ad_performance_metrics()`** - Performance insights & KPIs
- **`analyze_ad_targeting_insights()`** - Audience targeting analysis

### **🎯 Monitoring & Tracking**
- **`monitor_brand_ad_changes()`** - Real-time campaign monitoring
- **`track_ad_spend_estimation()`** - Budget tracking & estimation

### **🏆 Competitive Intelligence**
- **`competitive_ad_analysis()`** - Multi-brand strategy comparison
- **`benchmark_against_industry()`** - Industry benchmarking
- **`identify_market_opportunities()`** - Market gap analysis

### **🔮 Prediction & Optimization**
- **`predict_ad_performance()`** - ML-powered performance prediction
- **`generate_facebook_intelligence_report()`** - Comprehensive reports

### **🛠️ Utilities**
- **`export_facebook_ads_data()`** - Export in JSON/CSV/Markdown

## 💡 **Usage Examples**

### **Basic Competitive Analysis**
```python
# In Claude Desktop
"Analyze Nike's current Facebook advertising strategy"
"Compare ad strategies between Tesla and BMW"
"Generate a complete intelligence report for Airbnb"
```

### **Advanced Market Research**
```python
# Discover competitors
"Find all fitness app companies advertising on Facebook"

# Market opportunities
"Identify advertising gaps in the fintech industry"

# Performance prediction
"Predict performance for this ad: 'Get fit in 30 days with our AI trainer'"
```

### **Monitoring & Alerts**
```python
# Track competitor changes
"Monitor Apple for new ad campaigns and alert me if they launch 5+ new ads"

# Spend tracking
"Estimate Shopify's monthly Facebook ad spend"
```

## 🔧 **Advanced Configuration**

### **Environment Variables**
```bash
# Create .env file
echo "FACEBOOK_ACCESS_TOKEN=your_token_here" > .env
```

### **Multiple Regions**
```json
{
  "mcpServers": {
    "facebook_ads_us": {
      "command": "python",
      "args": ["facebook_ads_mcp_complete.py", "--facebook-token", "US_TOKEN"]
    },
    "facebook_ads_eu": {
      "command": "python", 
      "args": ["facebook_ads_mcp_complete.py", "--facebook-token", "EU_TOKEN"]
    }
  }
}
```

## 📈 **Performance Comparison**

| Feature | ScrapeCreators | **Our MCP** | Savings |
|---------|----------------|-------------|---------|
| Monthly Cost | $497 | **$0** | $497/month |
| Facebook Tools | 5-6 basic | **15+ advanced** | 3x more |
| Creative Analysis | ❌ | ✅ **AI-powered** | Exclusive |
| Performance Prediction | ❌ | ✅ **ML-based** | Exclusive |
| Rate Limits | Restricted | **Direct API** | Unlimited |
| Customization | ❌ | ✅ **Full control** | Infinite |

## 🏗️ **Architecture**

```
Facebook Ads Library MCP
├── Core API Wrapper
│   ├── Authentication & Rate Limiting
│   └── Error Handling & Retry Logic
├── Search & Discovery Engine
│   ├── Advanced Filtering
│   └── Competitor Discovery
├── AI Analysis Engine
│   ├── Creative Element Analysis
│   └── Performance Prediction
├── Monitoring System
│   ├── Real-time Change Detection
│   └── Alert System
└── Export & Reporting
    ├── Multiple Format Support
    └── Executive Reports
```

## 🔒 **Security & Privacy**

- **No Data Storage** - All data processed in real-time
- **Direct API Access** - No proxy servers or data logging
- **Open Source** - Complete transparency
- **Local Processing** - Your data stays on your machine

## 🤝 **Contributing**

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### **Development Setup**
```bash
git clone https://github.com/RamsesAguirre777/facebook-ads-library-mcp.git
cd facebook-ads-library-mcp
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
```

## 📖 **Documentation**

- **[Setup Guide](docs/setup.md)** - Detailed installation instructions
- **[API Reference](docs/api.md)** - Complete tool documentation
- **[Examples](docs/examples.md)** - Real-world use cases
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues & solutions

## 🔄 **Changelog**

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## 🆘 **Support**

- **Issues**: [GitHub Issues](https://github.com/RamsesAguirre777/facebook-ads-library-mcp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/RamsesAguirre777/facebook-ads-library-mcp/discussions)
- **Email**: [ramses.aguirre777@email.com](mailto:ramses.aguirre777@email.com)

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- [FastMCP](https://github.com/modelcontextprotocol/python-sdk) for the excellent MCP framework
- [Crawl4AI](https://github.com/unclecode/crawl4ai) for AI-powered web crawling
- [Facebook Graph API](https://developers.facebook.com/docs/graph-api) for providing access to ads data

## ⭐ **Star History**

[![Star History Chart](https://api.star-history.com/svg?repos=RamsesAguirre777/facebook-ads-library-mcp&type=Date)](https://star-history.com/#RamsesAguirre777/facebook-ads-library-mcp&Date)

---

<div align="center">
  <h3>🔥 Built with passion for the MCP community 🔥</h3>
  <p>
    <a href="https://twitter.com/RamsesAguirre777">Twitter</a> •
    <a href="https://github.com/RamsesAguirre777">GitHub</a> •
    <a href="https://linkedin.com/in/RamsesAguirre777">LinkedIn</a>
  </p>
</div>
