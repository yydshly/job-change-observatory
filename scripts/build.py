import json,pathlib,collections
from core import compare,SKILLS
ROOT=pathlib.Path(__file__).resolve().parents[1]
snapshots=[json.loads(p.read_text()) for p in sorted((ROOT/'snapshots').glob('*.json'))]
if not snapshots:raise RuntimeError('Real source snapshot required; refusing to build sample placeholders')
latest=snapshots[-1]
history=[{'observedAt':s['observedAt'],'count':len(s['jobs']),'responseSha256':s['responseSha256']} for s in snapshots]
out={**latest,'history':history,'dictionarySize':len(SKILLS),'comparison':compare(snapshots[-2]['jobs'],latest['jobs']) if len(snapshots)>1 else None}
(ROOT/'dist'/'data.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n')
print(json.dumps({'jobs':len(latest['jobs']),'snapshots':len(history),'uniqueSkills':len({e['skill'] for j in latest['jobs'] for e in j['skills']})}))
