# 🚀 Facebook Ads Library MCP - Complete Setup Guide

## 📋 **Prerequisites**

- Python 3.8 or higher
- Claude Desktop app installed
- Facebook Developer account
- Basic command line knowledge

## 🔧 **Step 1: Installation**

### **Clone the Repository**
```bash
git clone https://github.com/RamsesAguirre777/facebook-ads-library-mcp.git
cd facebook-ads-library-mcp
```

### **Create Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

## 🔑 **Step 2: Get Facebook Access Token**

### **Method 1: Facebook Graph API Explorer (Recommended)**
1. Go to [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. Select your app (or create a new one)
3. Click "Generate Access Token"
4. Add these permissions:
   - `ads_read`
   - `pages_read_engagement`
   - `business_management` (optional)
5. Copy the generated token

### **Method 2: Create Facebook App from Scratch**
1. Go to [Facebook for Developers](https://developers.facebook.com/apps/)
2. Click "Create App" → Select "Business"
3. Fill in app details:
   - App Name: "My Facebook Ads MCP"
   - App Contact Email: your-email@example.com
4. Go to Graph API Explorer
5. Select your new app
6. Generate token with required permissions

### **Method 3: Extend Token (For Long-term Use)**
1. Go to [Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken/)
2. Paste your short-lived token
3. Click "Extend Access Token"
4. Get a token that lasts ~60 days

## 🔧 **Step 3: Configure Claude Desktop**

### **Locate Claude Desktop Config**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### **Add MCP Server Configuration**
```json
{
  "mcpServers": {
    "facebook_ads": {
      "command": "python",
      "args": [
        "/full/path/to/facebook-ads-library-mcp/facebook_ads_mcp_complete.py",
        "--facebook-token",
        "YOUR_FACEBOOK_ACCESS_TOKEN_HERE"
      ]
    }
  }
}
```

### **Example Full Configuration**
```json
{
  "mcpServers": {
    "facebook_ads": {
      "command": "python",
      "args": [
        "/Users/ramses/projects/facebook-ads-library-mcp/facebook_ads_mcp_complete.py",
        "--facebook-token",
        "EAABwzLixnjYBO1234567890abcdefghijklmnop"
      ]
    },
    "other_mcps": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}
```

## 🚀 **Step 4: Test Installation**

### **Restart Claude Desktop**
1. Quit Claude Desktop completely
2. Restart the application
3. Look for the hammer icon (🔨) in the interface

### **Test Basic Functionality**
Try these commands in Claude Desktop:
```
"Search for Nike's current Facebook ads"
"Analyze Tesla's Facebook advertising strategy"
"Generate a competitive analysis report for Apple vs Samsung"
```

## 🛠️ **Step 5: Advanced Configuration**

### **Environment Variables (Optional)**
Create a `.env` file in the project directory:
```bash
# .env
FACEBOOK_ACCESS_TOKEN=your_token_here
```

Then modify the config to use environment variables:
```json
{
  "mcpServers": {
    "facebook_ads": {
      "command": "python",
      "args": [
        "/path/to/facebook_ads_mcp_complete.py"
      ],
      "env": {
        "FACEBOOK_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

### **Multiple Regions Configuration**
```json
{
  "mcpServers": {
    "facebook_ads_us": {
      "command": "python",
      "args": [
        "/path/to/facebook_ads_mcp_complete.py",
        "--facebook-token",
        "US_TOKEN"
      ]
    },
    "facebook_ads_eu": {
      "command": "python",
      "args": [
        "/path/to/facebook_ads_mcp_complete.py",
        "--facebook-token",
        "EU_TOKEN"
      ]
    }
  }
}
```

## 🎯 **Available Tools**

Once configured, you'll have access to these tools:

### **🔍 Search & Discovery**
- **`search_facebook_ads()`** - Advanced search with filters
- **`discover_competitor_brands()`** - Find industry competitors
- **`find_similar_advertisers()`** - Discover similar brands

### **📊 Analysis**
- **`analyze_ad_creative_elements()`** - Creative analysis
- **`analyze_ad_performance_metrics()`** - Performance insights
- **`competitive_ad_analysis()`** - Multi-brand comparison

### **📈 Intelligence**
- **`generate_facebook_intelligence_report()`** - Comprehensive reports
- **`export_facebook_ads_data()`** - Data export

## 💡 **Usage Examples**

### **Basic Queries**
```
"Show me all current Facebook ads for Shopify"
"What's Nike's Facebook advertising strategy?"
"Compare Facebook ads between Coca-Cola and Pepsi"
```

### **Advanced Analysis**
```
"Generate a complete intelligence report for Airbnb including competitors"
"Analyze the creative elements of this Facebook ad: [URL]"
"Export Tesla's Facebook ads data in CSV format"
```

### **Market Research**
```
"Discover all fitness app companies advertising on Facebook"
"Find companies similar to Stripe in their Facebook advertising"
"Analyze Facebook ad performance metrics for the SaaS industry"
```

## 🚨 **Troubleshooting**

### **Common Issues**

#### **"Invalid access token" Error**
```bash
# Test your token
curl -G "https://graph.facebook.com/me" -d "access_token=YOUR_TOKEN"
```

**Solutions:**
- Regenerate token with correct permissions
- Check if token has expired
- Verify app has access to Ads Library

#### **"Permission denied" Error**
**Solutions:**
- Add `ads_read` permission to your token
- Ensure your Facebook app is approved for business use
- Check if your account has access to Facebook Ads Library

#### **"Rate limit exceeded" Error**
**Solutions:**
- Wait 5-10 minutes between large requests
- Reduce the `limit` parameter in functions
- Use pagination for large data sets

#### **"MCP server not found" Error**
**Solutions:**
- Check file path in claude_desktop_config.json
- Ensure Python is in your PATH
- Verify virtual environment is activated

#### **"Module not found" Error**
**Solutions:**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Check if virtual environment is activated
source venv/bin/activate
```

### **Debug Mode**
Add debug logging to troubleshoot:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### **Verify Installation**
```bash
# Test Python script directly
python facebook_ads_mcp_complete.py --facebook-token YOUR_TOKEN

# Check MCP server status
echo '{"jsonrpc": "2.0", "method": "initialize", "params": {}, "id": 1}' | python facebook_ads_mcp_complete.py --facebook-token YOUR_TOKEN
```

## 🔒 **Security Best Practices**

### **Token Security**
- Never commit tokens to version control
- Use environment variables for tokens
- Regularly rotate your access tokens
- Use read-only permissions only

### **Rate Limiting**
- Implement delays between requests
- Use pagination for large datasets
- Monitor API usage in Facebook Developer console

### **Data Privacy**
- Don't store user data locally
- Process data in real-time only
- Comply with Facebook's data usage policies

## 📊 **Performance Optimization**

### **Caching (Optional)**
```python
# Add simple caching for repeated requests
import functools
import time

@functools.lru_cache(maxsize=100)
def cached_request(url, params_str):
    # Implementation
    pass
```

### **Async Processing**
```python
import asyncio
import aiohttp

# For handling multiple concurrent requests
async def fetch_multiple_brands(brands):
    # Implementation
    pass
```

## 🔄 **Updates and Maintenance**

### **Update Dependencies**
```bash
pip install --upgrade -r requirements.txt
```

### **Update Facebook API Version**
Change the version in `facebook_ads_mcp_complete.py`:
```python
self.base_url = "https://graph.facebook.com/v19.0/ads_archive"  # Update version
```

### **Monitor API Changes**
- Follow [Facebook Developer Blog](https://developers.facebook.com/blog/)
- Check [Graph API Changelog](https://developers.facebook.com/docs/graph-api/changelog/)
- Test functionality after Facebook updates

## 📈 **Advanced Features**

### **Custom Metrics**
Add your own analysis functions:
```python
@mcp.tool(description="Custom analysis function")
def my_custom_analysis(brand_name: str) -> dict:
    # Your custom logic here
    pass
```

### **Webhook Integration**
Set up webhooks for real-time updates:
```python
# Monitor for new ads automatically
def setup_webhook_monitoring():
    # Implementation
    pass
```

### **Data Export Automation**
```python
# Scheduled exports
def schedule_daily_export():
    # Implementation
    pass
```

## 🆘 **Support**

### **Getting Help**
- **GitHub Issues**: [Report bugs](https://github.com/RamsesAguirre777/facebook-ads-library-mcp/issues)
- **Discussions**: [Ask questions](https://github.com/RamsesAguirre777/facebook-ads-library-mcp/discussions)
- **Documentation**: [API Reference](api.md)

### **Community**
- Share your use cases and improvements
- Contribute to the project
- Help other users in discussions

## 🎉 **Next Steps**

1. **Test all tools** with different brands
2. **Explore advanced features** like competitive analysis
3. **Integrate with your workflow** (reports, dashboards)
4. **Contribute improvements** back to the project
5. **Build additional tools** on top of this foundation

---

**You're now ready to use the most powerful Facebook Ads intelligence MCP available! 🚀**

For more examples and advanced usage, see the [Examples Documentation](examples.md).
