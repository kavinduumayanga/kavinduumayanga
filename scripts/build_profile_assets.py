"""Generate self-contained README SVGs. Python standard library only."""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
BG, PANEL, BORDER = '#101619', '#161f23', '#2b383d'
WHITE, MUTED, GREEN, CYAN = '#eef4ee', '#a3b4b7', '#b0e5aa', '#77ccd0'
FONT = 'system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif'
MONO = 'ui-monospace, SFMono-Regular, Consolas, monospace'


def text(x, y, value, size=18, color=WHITE, weight=400, mono=False, extra=''):
    return f'<text x="{x}" y="{y}" font-family="{MONO if mono else FONT}" font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>'


def rect(x,y,w,h,fill=PANEL,stroke=BORDER,rx=14,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" {extra}/>'


def path(d,color=MUTED,width=1.5,extra=''):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def line_icon(kind,x,y,s=24,color=GREEN):
    shapes={
      'code':'M8 6 L2 12 L8 18 M16 6 L22 12 L16 18 M14 3 L10 21',
      'build':'M3 7 L12 2 L21 7 L21 17 L12 22 L3 17 Z M3 7 L12 12 L21 7 M12 12 V22 M8 4 L17 9',
      'test':'M12 2 L21 6 V12 Q21 18 12 22 Q3 18 3 12 V6 Z M7 12 L10 15 L17 8',
      'deploy':'M4 18 H20 M12 17 V3 M6 9 L12 3 L18 9',
      'monitor':'M2 3 H22 V19 H2 Z M7 23 H17 M12 19 V23 M5 12 H8 L10 7 L14 15 L16 11 H19',
      'server':'M3 2 H21 V10 H3 Z M3 14 H21 V22 H3 Z M7 6 H7.1 M7 18 H7.1 M12 6 H17 M12 18 H17',
      'cloud':'M6 19 H19 Q24 18 22 13 Q21 10 18 10 Q18 3 12 3 Q7 3 6 9 Q0 9 1 15 Q1 19 6 19',
      'branch':'M6 3 V17 Q6 21 10 21 H18 M6 7 H13 Q18 7 18 12 V15',
      'arrow':'M5 19 L19 5 M6 5 H19 V18',
      'terminal':'M3 4 H21 V20 H3 Z M7 8 L11 12 L7 16 M13 16 H17',
      'container':'M2 5 H22 V20 H2 Z M6 8 V17 M10 8 V17 M14 8 V17 M18 8 V17',
    }
    return f'<g transform="translate({x} {y}) scale({s/24})">{path(shapes[kind],color,1.6)}</g>'


def icon(name,x,y,size=34,tile=True):
    # Embed the source paths: image-mode SVGs cannot fetch sibling SVG files.
    s=(ASSETS/'icons'/f'{name}.svg').read_text()
    # Strip the outer tile created by the first design; retain the original SVG.
    inner=s[s.index('<svg',s.index('>')+1):s.rfind('</svg>')]
    inner=re.sub(r'\s(?:x|y|width|height)="[^"]*"','',inner,count=4)
    inner=inner.replace('<svg','<svg x="0" y="0" width="128" height="128"',1)
    prefix=f'{name}-{x}-{y}-'
    ids=re.findall(r'\bid="([^"]+)"',inner)
    for i in sorted(ids,key=len,reverse=True):
        inner=inner.replace(f'id="{i}"',f'id="{prefix}{i}"').replace(f'url(#{i})',f'url(#{prefix}{i})').replace(f'href="#{i}"',f'href="#{prefix}{i}"')
    if not tile and name=='linux': inner=inner.replace('fill="#000"',f'fill="{GREEN}"').replace('fill="black"',f'fill="{GREEN}"')
    pad=5 if tile else 0
    return (rect(x,y,size,size,'#e7eee6','none',9) if tile else '')+f'<svg x="{x+pad}" y="{y+pad}" width="{size-pad*2}" height="{size-pad*2}" viewBox="0 0 128 128">{inner}</svg>'


def start(w,h,title,desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs>
 <radialGradient id="glow"><stop stop-color="#345e49" stop-opacity=".35"/><stop offset="1" stop-color="#101619" stop-opacity="0"/></radialGradient>
 <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#7da9a1" stroke-opacity=".07"/></pattern>
 <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0L6 3L0 6" fill="none" stroke="#6c9090"/></marker>
</defs>
<style>.ink{{fill:{WHITE}}}@media(prefers-reduced-motion:reduce){{.motion{{display:none}}.typing{{clip-path:none}}}}</style>
{rect(1,1,w-2,h-2,BG,BORDER,20)}'''


def write(name,s):
    (ASSETS/name).write_text(s+'\n</svg>\n')


def eyebrow(x,y,label): return text(x,y,label,13,GREEN,500,True,extra='letter-spacing="1.5"')


def hero(m=False):
    w,h=(400,454) if m else (840,454)
    s=start(w,h,'Kavindu Umayanga — Aspiring DevOps Engineer','Linux workstation portfolio. Linux, cloud, CI/CD, automation. Learn the system. Automate the repeatable.')
    s+=f'<ellipse cx="{330 if m else 685}" cy="185" rx="{240 if m else 290}" ry="205" fill="url(#glow)"/>'
    s+=rect(1,1,w-2,300,'url(#grid)','none',20)
    s+=path(f'M1 48 H{w-1}',BORDER,1)
    for i,c in enumerate(['#b0e5aa','#77ccd0','#586e70']):s+=f'<circle cx="{24+i*16}" cy="25" r="3.5" fill="{c}"/>'
    s+=text(82,30,'kavindu / workstation',12,MUTED,mono=True)
    if not m:s+=text(808,30,'LINUX · DEVOPS',12,MUTED,mono=True,extra='text-anchor="end"')
    x=26 if m else 40
    s+=eyebrow(x,88,'LEARNING BY BUILDING')
    s+=text(x,153,'Kavindu',58 if m else 64,WHITE,650,extra='letter-spacing="-2"')
    s+=text(x,219 if m else 229,'Umayanga.',58 if m else 64,WHITE,650,extra='letter-spacing="-2"')
    s+=text(x,263 if m else 275,'Aspiring DevOps Engineer',25 if m else 27,GREEN,500)
    s+=text(x,296 if m else 305,'Linux · Cloud · CI/CD · Automation',16 if m else 18,MUTED)
    if not m:
        # Abstract workstation topology; no uptime or performance claims.
        s+=f'<g opacity=".9">{path("M652 122V152M652 238V268M572 194H545V268H620M732 194H760V268H684", "#47695c",1.5)}</g>'
        s+=rect(592,78,120,44,'#14221d','#3f5c4c',12)+line_icon('cloud',607,88,24)+text(640,106,'cloud',16,MUTED,mono=True)
        s+=rect(572,152,160,86,'#172720','#5c8b6b',16)+line_icon('server',590,172,44)+text(645,190,'linux',19,GREEN,600,True)+text(645,214,'lab',15,MUTED,mono=True)
        for bx,label in [(518,'build'),(622,'ship'),(726,'learn')]:
            s+=rect(bx,268,84,34,'#17211f','#334b40',8)+text(bx+42,290,label,13,MUTED,mono=True,extra='text-anchor="middle"')
        s+='<circle class="motion" r="3" fill="#b0e5aa" opacity="0"><animate attributeName="opacity" values="0;1;1;0" dur="4s" repeatCount="2"/><animateMotion path="M652 122V152M652 238V268" dur="4s" repeatCount="2"/></circle>'
    s+=rect(x,326,w-2*x,102,'#0c1214','#2d4039',12)
    s+=text(x+18,351,'kavindu@workstation ~',12,MUTED,mono=True)
    s+=f'<defs><clipPath id="type"><rect x="{x+18}" y="361" width="320" height="26"><animate attributeName="width" from="0" to="320" dur="1.8s" fill="freeze"/></rect></clipPath></defs>'
    s+=text(x+18,381,'$ ./build-journey.sh',18,GREEN,mono=True,extra='class="typing" clip-path="url(#type)"')
    s+=f'<rect class="motion" x="{x+246}" y="365" width="8" height="19" fill="{GREEN}"><animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="4"/></rect>'
    s+=text(x+18,409,'learn → build → improve',15,MUTED,mono=True)
    if not m:s+=text(w-x-18,409,'small steps. reliable systems.',13,MUTED,mono=True,extra='text-anchor="end"')
    write('terminal-mobile.svg' if m else 'terminal.svg',s)


def about(m=False):
    w,h=(400,430) if m else (840,306)
    s=start(w,h,'The engineer behind the terminal','Kavindu Umayanga. Software Engineering undergraduate at SLIIT. Java and backend foundation. Linux and cloud interests. Microsoft Learn Student Ambassador and Postman Student Expert.')
    s+=eyebrow(26 if m else 32,35,'THE ENGINEER BEHIND THE TERMINAL')
    if m:
        s+=rect(26,59,90,96,'#c0dfb9','none',18)+icon('linux',37,67,68,False)
        s+=text(136,89,'kavindu@linux',19,GREEN,600,True)+text(136,119,'Curious by default.',17,WHITE)+text(136,144,'Learning by doing.',17,MUTED)
        rows=[('STUDY','Software Engineering'),('CAMPUS','Undergraduate @ SLIIT'),('BASE','Java & backend engineering'),('FOCUS','Linux, cloud & automation')]
        for i,(key,value) in enumerate(rows):
            y=194+i*36;s+=text(26,y,key,12,CYAN,mono=True)+text(110,y,value,18,WHITE)
        s+=path('M26 326H374',BORDER,1)+text(26,357,'Microsoft Learn Student Ambassador',16,MUTED)+text(26,384,'Postman Student Expert',16,MUTED)
        s+=text(26,411,'Learn the system. Automate the repeatable.',12,GREEN,mono=True)
    else:
        s+=rect(32,59,188,210,'#192720','#35503e',16)
        s+='<circle cx="126" cy="154" r="64" fill="#c0dfb9"/>'+icon('linux',79,104,94,False)
        s+=text(126,247,'GNU / LINUX',13,GREEN,mono=True,extra='text-anchor="middle" letter-spacing="2"')
        s+=text(256,88,'kavindu@linux',24,GREEN,600,True)+text(790,85,'$ fastfetch',14,MUTED,mono=True,extra='text-anchor="end"')
        rows=[('STUDY','Software Engineering undergraduate @ SLIIT'),('BASE','Java & backend engineering'),('FOCUS','Linux systems · Cloud · Automation')]
        for i,(key,value) in enumerate(rows):
            y=128+i*34;s+=text(256,y,key,12,CYAN,mono=True)+text(340,y,value,17)
        s+=path('M256 218H802',BORDER,1)+text(256,246,'Microsoft Learn Student Ambassador',16,MUTED)+text(256,272,'Postman Student Expert',16,MUTED)
    write('about-mobile.svg' if m else 'about.svg',s)


def stack(m=False):
    w,h=(400,912) if m else (840,570)
    s=start(w,h,'Engineering toolkit','Hands-on project tools grouped by Linux and Systems, Cloud and Infrastructure, CI/CD and Automation, and Backend Engineering. Currently learning Linux administration, Bash provisioning, cloud delivery; Docker, Kubernetes, Terraform, Ansible, Prometheus and Grafana are next-lab goals.')
    x=26 if m else 32
    s+=eyebrow(x,35,'ENGINEERING TOOLKIT')+text(x,72,'Tools with a purpose.',28,WHITE,600)
    s+=text(x,101,'Hands-on work across labs, demos & coursework.',14 if m else 17,MUTED)
    if m:
        groups=[('Linux & Systems','Ubuntu · CentOS Stream · Nginx',[('linux','Linux'),('ubuntu','Ubuntu'),('centos','CentOS'),('nginx','Nginx')]),('Cloud & Infrastructure','Azure Static Web Apps · local virtual machines',[('azure','Azure'),('vagrant','Vagrant')]),('CI/CD & Automation','GitHub Actions · experimental Bash provisioning',[('git','Git'),('githubactions','Actions'),('bash','Bash')]),('Backend Engineering','Java · Spring Boot · Maven · Python',[('java','Java'),('spring','Spring'),('maven','Maven'),('python','Python')])]
        for i,(title,sub,items) in enumerate(groups):
            yy=124+i*146
            s+=rect(x,yy,348,132,PANEL,BORDER,14)+text(x+18,yy+29,title,21,WHITE,600)+text(x+18,yy+53,sub,12,MUTED)
            for j,(name,label) in enumerate(items):
                xx=x+18+j*(312/len(items))+(312/len(items))/2;s+=icon(name,xx-15,yy+65,30)+text(xx,yy+118,label,16 if len(items)==4 else 17,WHITE,extra='text-anchor="middle"')
        y=722
        s+=rect(x,y,348,164,'#17251d','#3e5945',14)+eyebrow(x+18,y+29,'CURRENTLY LEARNING')
        s+=text(x+18,y+57,'Linux admin · Bash · cloud delivery',17,WHITE)
        s+=text(x+18,y+87,'NEXT LABS / learning goals',12,GREEN,mono=True)+text(x+18,y+115,'Docker · Kubernetes · Terraform',17,MUTED)
        s+=text(x+18,y+140,'Ansible · Prometheus · Grafana',17,MUTED)
    else:
        # Each tile uses two compact icon-and-name rows for generous spacing.
        groups=[(32,126,'Linux & Systems','Linux server administration',[('linux','Linux'),('ubuntu','Ubuntu'),('centos','CentOS Stream'),('nginx','Nginx')]),(430,126,'Cloud & Infrastructure','Cloud demos & local VM labs',[('azure','Azure'),('vagrant','Vagrant')]),(32,300,'CI/CD & Automation','Bash provisioning remains experimental',[('git','Git'),('githubactions','GitHub Actions'),('bash','Bash')]),(430,300,'Backend Engineering','Applications, APIs & practical automation',[('java','Java'),('spring','Spring Boot'),('maven','Maven'),('python','Python')])]
        for xx,yy,title,sub,items in groups:
            s+=rect(xx,yy,378,160,PANEL,BORDER,14)+text(xx+20,yy+30,title,22,WHITE,600)+text(xx+20,yy+54,sub,13,MUTED)
            for i,(name,label) in enumerate(items):
                ix=xx+20+(i%2)*170;iy=yy+73+(i//2)*43
                s+=icon(name,ix,iy,28)+text(ix+38,iy+20,label,15)
        s+=rect(32,476,776,70,'#17251d','#3e5945',12)+eyebrow(50,502,'CURRENTLY LEARNING')+text(50,526,'Linux admin · Bash · cloud delivery',14,WHITE)
        s+=text(385,501,'NEXT LABS / learning goals',12,GREEN,mono=True)+text(385,524,'Docker · Kubernetes · Terraform · Ansible',13,MUTED)+text(385,541,'Prometheus · Grafana',12,MUTED)
    write('toolkit-mobile.svg' if m else 'toolkit.svg',s)


def project(name,m=False):
    primary=name=='linux-lab'
    w=400 if m else 840
    h=(470 if m else 350) if primary else (246 if m else 186)
    data={
      'linux-lab':('FEATURED / INFRASTRUCTURE','Multi-tier Linux','deployment lab','Seven VMs. One connected system.','Linux · Vagrant · Nginx · Tomcat · Java'),
      'ridelink':('BACKEND / TEAM PROJECT','RideLink backend','','Ride lifecycle, driver assignment & service integration.','Java · Spring Boot · MongoDB · CI'),
      'certloop':('AUTOMATION / PYTHON','CertLoop','','CSV → personalized PDFs → tracked email delivery.','Python · FastAPI · SQLite'),
      'azure':('CLOUD / COMMUNITY DEMO','Azure Static Web Apps','','A portfolio deployment demo for an MLSA session.','Azure · GitHub Actions · HTML / CSS / JS'),
    }
    label,title,title2,desc,tech=data[name]
    s=start(w,h,title+' '+title2,desc+' '+tech)
    x=26 if m else 32
    if primary:s+=f'<ellipse cx="{w-80}" cy="160" rx="250" ry="180" fill="url(#glow)"/>'
    s+=eyebrow(x,34,label)+line_icon('arrow',w-47,20,20,CYAN)
    if primary:
        s+=text(x,76,title,31 if m else 36,WHITE,650)+text(x,120,title2,31 if m else 36,WHITE,650)
        s+=text(x,151,desc,18,MUTED)
        if m:
            s+=text(x,180,'Nginx load balancing · shared services',15,MUTED)
            s+=text(x,204,'Manual setup + infrastructure dashboard',14,MUTED)
            s+=architecture(26,229,348,True)
            s+=text(x,411,'Linux · Vagrant · Nginx · Tomcat · Java',14,GREEN)
            s+=text(x,445,'Explore the repository',16,WHITE,500)+line_icon('arrow',212,430,18)
        else:
            s+=text(x,183,'Nginx load balancing. Shared services.',17,MUTED)
            s+=text(x,210,'Manual setup, monitoring & failover testing.',16,MUTED)
            s+=architecture(476,80,330,False)
            s+=path('M32 268H808',BORDER,1)+text(x,301,tech,16,GREEN)
            s+=text(x,328,'Explore the repository',15,WHITE,500)+line_icon('arrow',211,314,17)
    else:
        s+=text(x,76,title,28 if m else 30,WHITE,600)
        if m:
            descriptions={
              'ridelink':['My contribution: Ride Management.','Ride lifecycle & cross-service integration.'],
              'certloop':['CSV to personalized PDF certificates.','Confirmed email sends & delivery tracking.'],
              'azure':['A portfolio demo for an MLSA session.','Deployment through GitHub Actions.']}
            for i,l in enumerate(descriptions[name]):s+=text(x,111+i*25,l,18,MUTED)
            s+=text(x,174,tech,15 if name=='azure' else 16,GREEN)
            s+=path('M26 191H374',BORDER,1)+text(x,222,'View repository',15,WHITE,500)+line_icon('arrow',151,207,18)
        else:
            s+=text(x,110,desc if name!='ridelink' else 'My contribution: Ride Management, lifecycle & cross-service integration.',17,MUTED)
            s+=text(x,151,tech,15,GREEN)+text(802,151,'View repository ↗',14,WHITE,500,extra='text-anchor="end"')
    write(f'projects/{name}{"-mobile" if m else ""}.svg',s)


def architecture(x,y,w,m):
    # Explicitly a simplified architecture, not a topology of all seven VMs.
    s=rect(x,y,w,155,'#0d1715','#334d40',12)
    s+=text(x+15,y+24,'SIMPLIFIED LAB TOPOLOGY',10,GREEN,mono=True,extra='letter-spacing="1"')
    s+=path(f'M{x+70} {y+77}H{x+103}M{x+103} {y+58}V{y+97}M{x+103} {y+58}H{x+126}M{x+103} {y+97}H{x+126}M{x+217} {y+58}H{x+238}V{y+97}H{x+217}M{x+238} {y+77}H{x+258}', '#658f75')
    s+=rect(x+14,y+56,65,42,'#21362a','#567d5e',8)+text(x+46.5,y+82,'Nginx',13,GREEN,500,extra='text-anchor="middle"')
    for yy,label in [(y+41,'Tomcat 1'),(y+80,'Tomcat 2')]:
        s+=rect(x+126,yy,91,33,'#1b2b25','#3d594a',7)+text(x+171.5,yy+22,label,12,WHITE,extra='text-anchor="middle"')
    s+=line_icon('server',x+270,y+61,27,GREEN)+text(x+284,y+108,'data',11,MUTED,mono=True,extra='text-anchor="middle"')
    s+=text(x+15,y+139,'MySQL · Memcached · NFS · RabbitMQ',11,MUTED)
    return s


def workflow(m=False):
    w,h=(400,484) if m else (840,280)
    s=start(w,h,'From commit to confidence','Learning the DevOps lifecycle: Code, Build, Test, Deploy, Monitor. Monitoring informs the next change.')
    x=26 if m else 32
    s+=eyebrow(x,35,'THE DELIVERY LOOP')+text(x,74,'From commit to confidence.',25 if m else 30,WHITE,600)
    labels=[('code','Code','Version the change'),('build','Build','Package the app'),('test','Test','Verify behavior'),('deploy','Deploy','Run the release'),('monitor','Monitor','Observe & improve')]
    if m:
        for i,(kind,label,detail) in enumerate(labels):
            yy=105+i*65
            if i<4:s+=path(f'M51 {yy+43}V{yy+66}','#476553',2)
            s+=rect(28,yy,46,44,'#1d3026','#49654e',11)+line_icon(kind,39,yy+10,24)
            s+=text(94,yy+19,label,21,WHITE,600)+text(94,yy+42,detail,15,MUTED)
        s+=text(26,460,'feedback → the next change',15,CYAN,mono=True)
        motionpath='M51 149V170M51 214V235M51 279V300M51 344V365'
    else:
        for i,(kind,label,detail) in enumerate(labels):
            xx=32+i*159
            if i<4:s+=path(f'M{xx+56} 135H{xx+147}','#476553',1.5,'marker-end="url(#arrow)"')
            s+=rect(xx,109,54,54,'#1d3026','#49654e',13)+line_icon(kind,xx+13,122,28)
            s+=text(xx,193,label,22,WHITE,600)+text(xx,218,detail,13,MUTED)
        s+=path('M32 244H808',BORDER,1)+text(32,264,'feedback → the next change',12,CYAN,mono=True)+text(808,264,'A lifecycle I’m learning to connect.',12,MUTED,extra='text-anchor="end"')
        motionpath='M88 135H179M247 135H338M406 135H497M565 135H656'
    s+=f'<circle class="motion" r="3" fill="{GREEN}" opacity="0"><animate attributeName="opacity" values="0;1;1;0" dur="5s" repeatCount="2"/><animateMotion path="{motionpath}" dur="5s" repeatCount="2"/></circle>'
    write('devops-workflow-mobile.svg' if m else 'devops-workflow.svg',s)


if __name__=='__main__':
    for mobile in (False,True):
        hero(mobile);about(mobile);stack(mobile);workflow(mobile)
        for name in ('linux-lab','ridelink','certloop','azure'):project(name,mobile)
    print('Generated 16 standalone SVG assets.')
