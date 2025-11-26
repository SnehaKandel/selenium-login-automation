from selenium import webdriver
import time
from selenium.webdriver.common.by import By  
import requests  

POPULAR_NEPALI_SITES = [
    "https://www.daraz.com.np/",
    "https://www.sastodeal.com/", 
    "https://www.thulo.com/",
    "https://www.gyapu.com/",
    "https://www.muncha.com/",
    "https://www.onlinekhabar.com/",
    "https://www.setopati.com/",
    "https://thehimalayantimes.com/",
    "https://www.nrb.org.np/",
    "https://tribhuvan-university.edu.np/"
]

print("NEPALI WEBSITE BROKEN LINK ANALYSIS")
print("===================================")

results = []

for site_url in POPULAR_NEPALI_SITES:
    print(f"\n>>> Testing: {site_url}")
    
    # Create a NEW browser instance for each site (more reliable)
    try:
        browser = webdriver.Chrome()
        browser.set_page_load_timeout(30)
        
        browser.get(site_url)  
        time.sleep(3)

        all_links = browser.find_elements(By.TAG_NAME, "a")
        print(f"Total links found: {len(all_links)}")
        
        tested = 0
        broken = 0
        
        # Check first 20 links only
        for link in all_links[:20]:
            href = link.get_attribute('href')
            
            if href and href.startswith('http'):
                tested += 1
                try:
                    response = requests.get(href, timeout=3)
                    if response.status_code >= 400:  
                        broken += 1
                        print(f"  BROKEN [{response.status_code}]: {href[:50]}...")
                except:
                    broken += 1
        
        broken_percentage = (broken/tested)*100 if tested > 0 else 0
        
        results.append({
            'site': site_url,
            'total_links': len(all_links),
            'tested': tested,
            'broken': broken,
            'percentage': broken_percentage
        })
        
        print(f"RESULTS: Tested={tested}, Broken={broken}, Rate={broken_percentage:.1f}%")
        
        browser.quit()  # Close browser after each site
        
    except Exception as e:
        print(f"  [FAILED] {str(e)[:50]}...")
        results.append({
            'site': site_url,
            'total_links': 0,
            'tested': 0,
            'broken': 0,
            'percentage': 0
        })
        try:
            browser.quit()
        except:
            pass

# Final results
print("\n" + "="*70)
print("FINAL RESULTS")
print("="*70)

for result in results:
    if result['tested'] > 0:
        print(f"{result['site']}")
        print(f"  Tested: {result['tested']} | Broken: {result['broken']} | Rate: {result['percentage']:.1f}%")
        print()

print("Testing completed!")


