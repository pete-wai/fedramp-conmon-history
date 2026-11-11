import requests, json, concurrent.futures
from pathlib import Path
targets={
 'scanning':'www.fedramp.gov/assets/resources/documents/CSP_Vulnerability_Scanning_Requirements.pdf',
 'strategy':'www.fedramp.gov/assets/resources/documents/CSP_Continuous_Monitoring_Strategy_Guide.pdf',
 'poamguide':'www.fedramp.gov/assets/resources/documents/CSP_POAM_Template_Completion_Guide.pdf',
 'performance':'www.fedramp.gov/assets/resources/documents/CSP_Continuous_Monitoring_Performance_Management_Guide.pdf',
 'containerdraft':'www.fedramp.gov/assets/resources/documents/DRAFT_FedRAMP_Vulnerbility_Scanning_Requirements_for_the_Development_and_Use_of_Containers.pdf',
 'poamtemplate':'www.fedramp.gov/assets/resources/templates/FedRAMP-POAM-Template.xlsm',
 'strategyold':'www.fedramp.gov/files/2015/03/FedRAMP_Continuous_Monitoring_Strategy_Guide.pdf',
 'scandraft':'www.fedramp.gov/*DRAFT*Scan*.pdf',
}
def get(pair):
 key,url=pair
 try:
  r=requests.get('https://web.archive.org/cdx/search/cdx',params={'url':url,'output':'json','filter':'statuscode:200','collapse':'digest','filter':'!mimetype:text/html'},timeout=50);r.raise_for_status();data=r.json()
  Path(f'research/cdx-{key}.json').write_text(json.dumps(data,indent=2));print(key,data)
 except Exception as e: print(key,str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:list(p.map(get,targets.items()))
