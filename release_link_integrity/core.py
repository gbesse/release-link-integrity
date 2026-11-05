import json,math
from .common import number,integer,identifier
import re
from pathlib import Path
from urllib.parse import unquote,urlsplit
def run(d):
 root=Path(d['assets_root']).resolve();files=d['documents']
 if not 1<=len(files)<=100:raise ValueError('documents')
 out=[]
 for filename in files:
  p=(root/filename).resolve()
  if not p.is_relative_to(root)or p.stat().st_size>1000000:raise ValueError('document')
  text=p.read_text();text=re.sub(r'```[\s\S]*?```','',text)
  for match in re.finditer(r'!?\[[^]\n]*\]\(([^)\s]+)\)',text):
   href=match.group(1);u=urlsplit(href)
   if u.scheme or u.netloc:continue
   target=(p.parent/unquote(u.path)).resolve()if u.path else p
   status='outside_root'if not target.is_relative_to(root)else'exists'if target.is_file()else'missing'
   out.append(dict(document=filename,line=text[:match.start()].count('\n')+1,href=href,status=status,fragment_checked=False))
 return dict(links=out,broken=sum(r['status']!='exists'for r in out),scope='inline_relative_markdown_links_no_network')
