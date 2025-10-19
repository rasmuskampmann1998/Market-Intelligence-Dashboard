# Market Intelligence Dashboard

**Stack:** Python · FastAPI · AsyncIO · Apify · OpenAI · AWS · JSON · Automation (Make)

---

## Overview
The **Market Intelligence Dashboard** is a modular data intelligence system built to collect, process, and summarize agricultural market information — including competitor data, regulatory updates, patents, and social media activity.  
It automates web scraping, AI summarization, and structured reporting to support research and business intelligence in ag-tech and seed production.

The system was developed for agricultural analytics use cases like **Veginova Seeds** to centralize market monitoring across multiple data sources.

---

## ⚙️ System Architecture

### 1. **Data Collection**
- `alerts_detail_scraper.py` — Asynchronously crawls agricultural regulatory and alert websites using Crawl4AI.  
- `competitor_data.py` — Scrapes competitor domains and collects text data for pattern analysis.  
- `test_linkedin_scrapper.py` — Uses the Apify API to pull LinkedIn posts related to tomato innovation, patents, and technology.  
- Social-media datasets (`global_agriculture_tweets.json`, `instagram_agriculture_posts.json`) store high-volume trend data for keyword analysis.

### 2. **Processing & Validation**
- `regulation_schema_validation_report.json` — Performs schema validation across government and policy sites to ensure data consistency.  
- Validation results indicate which sources fail schema checks and why (SSL, structure, or missing fields).  

### 3. **AI-Powered Summarization**
- `monthly_data_generator.py` — Uses OpenAI’s API (via `AsyncOpenAI`) to generate monthly news and technical summaries across patents, regulations, and genetics.  
  The output is returned as structured JSON for integration into dashboards or reports.

### 4. **API Layer**
- `main.py` — FastAPI application exposing multiple routes (`auth`, `competitor`, `alerts`, `patents`, etc.) and handling scheduled automation tasks.  
  The system can be deployed on AWS or Docker to serve processed data and insights through an internal dashboard or API client.

---

## 🧩 Output Examples

- **Competitor Insights:** Parsed text content from corporate and research websites.  
- **Regulatory Monitoring:** Status report from multiple government portals.  
- **Social Trends:** Keyword and hashtag metrics across Twitter and Instagram.  
- **Monthly Reports:** Summarized technical and market intelligence JSON files ready for visualization in BI tools.

---

## 📊 Key Features
- Automated web and social scraping using AsyncIO and Crawl4AI.  
- Data validation and normalization for structured BI pipelines.  
- AI-driven summarization (OpenAI GPT-4) of market and regulatory news.  
- FastAPI backend with CORS-enabled endpoints and background schedulers.  
- Easily extendable with new routes, scrapers, or LLM modules.  

---

## 🚀 Usage

1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
