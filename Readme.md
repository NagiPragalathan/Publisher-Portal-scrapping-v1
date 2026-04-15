# Publisher-Portal-Scrapping-v1 🚀

A high-fidelity college data extraction system designed to crawl, deep-search, and scrape comprehensive institutional data from Shiksha.com.

## 📊 Current Scraping Status
*   **Total College URLs Indexed:** 2,308
*   **Deep-Scraped Colleges:** 1 (Full Profile)
*   **Tabular Data Scraped:** 5 Colleges (Fees, Rankings, etc.)
*   **Data Density:** ~14,600 data points per deep-scraped institution.

👉 **View Full Status Report**: [docs/ScrapingStatusReport.md](file:///c:/Users/Admin/Documents/Work/XtraCut_Works/Publisher-Portal-scrapping-v1/docs/ScrapingStatusReport.md)

## 📂 Project Structure

```bash
C:.
├───Data
│   ├───Extracted Data
│   └───Required Data
├───Garbage
│   ├───ClgLinkScrap
│   ├───Extract
│   ├───HTML Extractor
│   ├───LLM
│   │   └───Content
│   │       └───__pycache__
│   └───Scrap
└───Sample
    ├───Content Modification
    │   ├───AI_Content_Tools
    │   └───Content
    ├───HTML Extractor
    └───Link Scrapper
```

### Directory Roles
*   **Data/**: Master college lists (`DicData.json`) and final scraped results (`extracted_data.json`).
*   **RetrieveInfo/**: The "Deep Search" engine for full profile extraction.
*   **TabExractions/**: Automated batch processor for specific tables (Fees, Rankings, etc.).

## ⚙️ How to Run

### 1. Identify Target Colleges
Ensure `ClgNames.json` or `college_urls.json` contains the target URLs in the `Data/` folder.

### 2. Run Bulk Tabular Extraction
To get specific data (like Fees) for a list of colleges:
```bash
python TabExractions/main.py
```

### 3. Run Deep Search Extraction
To get a full detailed dump for a single institution:
```bash
python RetrieveInfo/main.py
```

## 📝 Configuration
*   **XPaths**: Adjust `XPaths.json` to update targeting logic for website changes.
*   **Looping**: Update `RetrieveInfo/main.py` with a loop to extend "Deep Search" to all 2,308 indexed colleges.

---
*Last Updated: April 2026*
