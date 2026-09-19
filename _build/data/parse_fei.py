#!/usr/bin/env python3
"""Transforme un résultat brut du navigateur (JSON {key,n,blocks}) en liste de centres normalisés."""
import json,re,sys
def parse_result_file(path):
    arr=json.loads(open(path,encoding='utf-8').read())
    out=[]
    for a in arr:
        t=a['text']
        if t.startswith('[javascript_tool:javascript_exec] '):
            s=t[len('[javascript_tool:javascript_exec] '):].strip()
            dec=json.JSONDecoder(); inner,_=dec.raw_decode(s)
            out.append(json.loads(inner))
    return out
CP_FR=re.compile(r'^(\d{5})\s+(.+)$')
CP_MAGHREB=re.compile(r'^(\d{4,5})\s+(.+)$')
CP_CA=re.compile(r'^([A-Z]\d[A-Z][ -]?\d[A-Z]\d|QC-[A-Z0-9-]+|NS-[A-Z0-9-]+|NU-[A-Z0-9-]+|BC-[A-Z0-9-]+|SK-[A-Z0-9-]+|[A-Z0-9]{5,7})\s+(.+)$')
def norm_centre(lines, country):
    if lines and lines[0].strip()==country: lines=lines[1:]
    name=lines[0]
    rest=lines[1:]
    so=any('ordinateur' in l for l in rest)
    rest=[l for l in rest if 'ordinateur' not in l]
    url=next((l for l in rest if re.match(r'https?://',l)),'')
    email=next((l for l in rest if '@' in l and ' ' not in l.strip()),'')
    emails=[l for l in rest if '@' in l]
    phone=next((l for l in rest if re.match(r'^[\d+()\s./-]{6,}$',l)),'')
    others=[l for l in rest if l not in (url,phone) and '@' not in l]
    # ligne code postal + ville
    cp='';city=''
    addr=[]
    for l in others:
        m=CP_FR.match(l) if country in ('France',) else (CP_MAGHREB.match(l) or CP_CA.match(l))
        if m and not cp:
            cp,city=m.group(1),m.group(2)
        else:
            addr.append(l)
    # ville depuis le nom « Ville - Centre »
    if ' - ' in name:
        city_name, centre = name.split(' - ',1)
    else:
        city_name, centre = city or '', name
    # emails : on retire ceux qui ressemblent à prénom.nom
    pub_emails=[e.strip() for e in ','.join(emails).replace(';',',').split(',') if e.strip()]
    pub_emails=[e for e in pub_emails if not re.match(r'^[a-z]+\.[a-z]+@',e.lower())]
    return {'name':centre.strip(),'city':city_name.strip(),'cp':cp,'city_cp':city,'address':' '.join(addr).strip(),
            'phone':phone,'emails':pub_emails,'url':url,'so':so}
if __name__=='__main__':
    src,country,out=sys.argv[1],sys.argv[2],sys.argv[3]
    res=parse_result_file(src)
    data=res[0]
    centres=[norm_centre(b,country) for b in data['blocks']]
    json.dump({'country':country,'key':data['key'],'n':len(centres),'date':'2026-09-19','centres':centres},open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(country, data['key'], len(centres), 'centres ;', sum(1 for c in centres if c['phone']),'tél ;', sum(1 for c in centres if c['emails']),'email ;', sum(1 for c in centres if c['url']),'site')
    for c in centres[:3]: print(' ',c)
