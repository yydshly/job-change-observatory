"""Deterministic keyword evidence; no model or credentials required."""
import re, html, hashlib, json
SKILLS = {
 'Python': r'\bpython\b', 'SQL': r'\bsql\b', 'JavaScript':r'\bjavascript\b',
 'TypeScript':r'\btypescript\b', 'React':r'\breact(?:\.js|js)?\b', 'Node.js':r'\bnode\.?(?:js)\b',
 'Java':r'\bjava\b','Go':r'\bgolang\b','C++':r'(?<!\w)c\+\+(?!\w)', 'C#':r'(?<!\w)c#(?!\w)',
 'Rust':r'\brust\b','Swift':r'\bswift\b','Kotlin':r'\bkotlin\b','PHP':r'\bphp\b',
 'AWS':r'\baws\b|amazon web services','Azure':r'\bazure\b','GCP':r'\bgcp\b|google cloud',
 'Docker':r'\bdocker\b','Kubernetes':r'\bkubernetes\b|\bk8s\b','Terraform':r'\bterraform\b',
 'Git':r'\bgit\b','CI/CD':r'\bci/cd\b|continuous integration','Linux':r'\blinux\b',
 '机器学习':r'\bmachine learning\b','LLM':r'\bllms?\b|large language models?',
 'PyTorch':r'\bpytorch\b','TensorFlow':r'\btensorflow\b','数据分析':r'\bdata analy(?:sis|tics)\b',
 'Excel':r'\bexcel\b','Tableau':r'\btableau\b','Power BI':r'\bpower\s*bi\b',
 'Figma':r'\bfigma\b','UX':r'\bux\b|user experience','用户研究':r'\buser research\b',
 'SEO':r'\bseo\b|search engine optimization','Salesforce':r'\bsalesforce\b',
 'HubSpot':r'\bhubspot\b','CRM':r'\bcrm\b','项目管理':r'\bproject management\b',
 '敏捷协作':r'\bagile\b|\bscrum\b','沟通协作':r'\bcommunication skills\b|\bcross-functional\b',
}
def plain(value):
 value = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', str(value or ''), flags=re.S|re.I)
 return re.sub(r'\s+', ' ',html.unescape(re.sub('<[^>]+>', ' ', value))).strip()
def extract(value):
 return [{'skill':name,'matched':sorted(set(m.group().lower() for m in re.finditer(pattern,value,re.I)))} for name,pattern in SKILLS.items() if re.search(pattern,value,re.I)]
def normalize(j):
 if not isinstance(j.get('id'),int) or j['id']<=0: raise ValueError('Invalid source id')
 url = str(j.get('url',''))
 if not re.match(r'^https://jobicy\.com/jobs/[^\s]+$',url): raise ValueError('Unexpected canonical URL')
 title,company=plain(j.get('jobTitle')),plain(j.get('companyName'))
 if not title or not company: raise ValueError('Missing title/company')
 desc=plain(j.get('jobDescription'))
 data={'id':str(j['id']),'title':title,'company':company,'url':url,'location':plain(j.get('jobGeo')) or '未标注','categories':[plain(x) for x in j.get('jobIndustry',[])],'types':[plain(x) for x in j.get('jobType',[])],'level':plain(j.get('jobLevel')) or '未标注','publishedAt':j.get('pubDate'),'skills':extract(title+' '+desc),'source':'Jobicy','availability':'采集时出现在来源列表；未单独核验招聘状态'}
 # Hash is evidence of source changes, not evidence of market trends. Do not store HTML, logos, contacts or complete descriptions.
 data['descriptionHash']=hashlib.sha256(desc.encode()).hexdigest()
 data['recordHash']=hashlib.sha256(json.dumps(data,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
 return data

def compare(previous,current):
 old={j['id']:j for j in previous};new={j['id']:j for j in current}
 return {'firstSeen':sorted(new.keys()-old.keys()),'notInLatestSample':sorted(old.keys()-new.keys()),'changed':sorted(k for k in old.keys()&new.keys() if old[k]['recordHash']!=new[k]['recordHash'])}
