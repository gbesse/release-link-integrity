import unittest
from release_link_integrity.core import run
class DomainTests(unittest.TestCase):
 def test_broken_and_existing(self):
  import tempfile
  from pathlib import Path
  with tempfile.TemporaryDirectory()as tmp:
   p=Path(tmp);(p/'README.md').write_text('[ok](guide.md) [bad](missing.md) [outside](../x)');(p/'guide.md').write_text('guide')
   x=run({'assets_root':tmp,'documents':['README.md']});self.assertEqual([r['status']for r in x['links']],['exists','missing','outside_root'])
 def test_no_network(self):
  import tempfile
  from pathlib import Path
  with tempfile.TemporaryDirectory()as tmp:
   (Path(tmp)/'r.md').write_text('[external](https://example.invalid)');self.assertEqual(run({'assets_root':tmp,'documents':['r.md']})['links'],[])
