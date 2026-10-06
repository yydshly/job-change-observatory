import unittest,sys,pathlib,json
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from core import extract,normalize,compare,plain
class EvidenceTests(unittest.TestCase):
 def test_boundaries(self):
  self.assertEqual([s['skill'] for s in extract('JavaScript and TypeScript, we go forward')],['JavaScript','TypeScript'])
 def test_once_per_skill(self):
  x=extract('Python PYTHON python');self.assertEqual(len(x),1);self.assertEqual(x[0]['matched'],['python'])
 def test_special_languages(self):
  self.assertEqual({s['skill'] for s in extract('C++ C# Golang')},{'C++','C#','Go'})
 def test_html_stripped(self):
  self.assertEqual(plain('<script>Python</script><p>React &amp; SQL</p>'),'React & SQL')
 def test_missing_is_not_closed(self):
  self.assertEqual(compare([{'id':'1','recordHash':'a'}],[]),{'firstSeen':[],'notInLatestSample':['1'],'changed':[]})
 def test_changed(self):
  self.assertEqual(compare([{'id':'1','recordHash':'a'}],[{'id':'1','recordHash':'b'},{'id':'2','recordHash':'c'}])['changed'],['1'])
 def test_unsafe_source(self):
  with self.assertRaises(ValueError):normalize({'id':1,'url':'javascript:alert(1)'})
 def test_real_snapshot(self):
  root=pathlib.Path(__file__).resolve().parents[1];data=json.loads((root/'dist/data.json').read_text())
  self.assertGreater(len(data['jobs']),0);self.assertLessEqual(len(data['jobs']),100);self.assertEqual(len({j['id'] for j in data['jobs']}),len(data['jobs']));self.assertGreaterEqual(len(data['history']),1)
  if len(data['history'])==1:self.assertIsNone(data['comparison'])
  for j in data['jobs']:
   self.assertTrue(j['url'].startswith('https://jobicy.com/jobs/'));self.assertNotIn('jobDescription',j);self.assertEqual(len(j['descriptionHash']),64)
if __name__=='__main__':unittest.main()
