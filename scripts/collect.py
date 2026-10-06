"""One bounded Jobicy public API pass. Never runs more than once an hour."""
import argparse,json,urllib.request,datetime,pathlib,sys,hashlib
from core import normalize
ROOT=pathlib.Path(__file__).resolve().parents[1]
URL='https://jobicy.com/api/v2/remote-jobs?count=100'
def collect():
 p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,help='Import a previously fetched genuine response; never synthetic data');p.add_argument('--observed-at',help='Required UTC retrieval timestamp for imported response');a=p.parse_args()
 now=datetime.datetime.now(datetime.timezone.utc)
 prior=sorted((ROOT/'snapshots').glob('*.json'))
 if a.input:
  if not a.observed_at: p.error('--input requires --observed-at')
  observed=datetime.datetime.fromisoformat(a.observed_at.replace('Z','+00:00'))
  if observed.tzinfo is None or observed>now: p.error('observed-at must be a real past UTC retrieval timestamp')
  raw=a.input.read_bytes()
 else:
  if prior:
   last=json.loads(prior[-1].read_text())['observedAt']
   if (now-datetime.datetime.fromisoformat(last)).total_seconds()<3600: sys.exit('Collection skipped: one-hour minimum interval')
  req=urllib.request.Request(URL,headers={'Accept':'application/json','User-Agent':'JobChangeObservatory/0.1 (private research dashboard; Jobicy attributed)'})
  with urllib.request.urlopen(req,timeout=40) as r: raw=r.read(5_000_001)
  if len(raw)>5_000_000: raise ValueError('Response too large')
  observed=datetime.datetime.now(datetime.timezone.utc)
 body=json.loads(raw)
 if body.get('success') is False or not isinstance(body.get('jobs'),list): raise ValueError('Unexpected API response')
 jobs=[];seen=set()
 for j in body['jobs']:
  normalized=normalize(j)
  if normalized['id'] not in seen: jobs.append(normalized);seen.add(normalized['id'])
 if not jobs: raise ValueError('Empty response: keep previous snapshot unchanged')
 snapshot={'schemaVersion':1,'observedAt':observed.isoformat(),'source':'Jobicy','sourceUrl':URL,'documentation':'https://jobicy.com/jobs-rss-feed','responseSha256':hashlib.sha256(raw).hexdigest(),'responseJobCount':len(body['jobs']),'pageCount':1,'hasMore':body.get('hasMore'), 'nextCursorPresent':bool(body.get('nextCursor')),'scope':'One first page, up to 100 Jobicy remote jobs; not a complete market census. Source feed covers last 7 days with 3-hour delay.','extractorVersion':'keywords-v1','jobs':jobs}
 path=ROOT/'snapshots'/ (observed.strftime('%Y%m%dT%H%M%SZ')+'.json')
 if path.exists(): raise ValueError('Snapshot exists; never overwrite history')
 path.write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'snapshot':str(path),'jobs':len(jobs),'observedAt':snapshot['observedAt'],'hasMore':snapshot['hasMore']}))
if __name__=='__main__':collect()
