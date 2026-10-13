"""Rebuild conceptual figures, not empirical estimates. AI-assisted code; author responsibility."""
import csv
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT = Path(__file__).resolve().parents[1]
FIGURES = json.loads((OUT / 'data/figure_spec.json').read_text(encoding='utf-8'))
GEOMETRY = []


def save_figure(fig, name):
    fig.canvas.draw(); renderer = fig.canvas.get_renderer()
    texts = [text for ax in fig.axes for text in ax.texts]
    collisions = [[a.get_text(), b.get_text()] for i,a in enumerate(texts) for b in texts[i+1:] if a.get_window_extent(renderer).overlaps(b.get_window_extent(renderer))]
    outside = [text.get_text() for text in texts if not all(fig.bbox.contains(*p) for p in text.get_window_extent(renderer).get_points())]
    GEOMETRY.append(dict(figure=name, text_collisions=collisions, text_outside_canvas=outside, text_artists=len(texts)))
    for extension in ('png','pdf','svg'):
        fig.savefig(OUT / 'figures' / (name + '.' + extension), dpi=300, facecolor='white')
    plt.close(fig)

def figures():
    with (OUT / 'data/figure_label_matrix.csv').open(encoding='utf-8-sig', newline='') as handle:
        labels = list(csv.DictReader(handle))
    plt.rcParams.update({'font.family':'Arial', 'font.size':11, 'svg.fonttype':'none', 'pdf.fonttype':42})
    colors = ['#246e68','#a9443c','#666b29']
    fig, ax = plt.subplots(figsize=(8.8,7.1)); fig.subplots_adjust(left=.02,right=.985,bottom=.02,top=.985)
    ax.set(xlim=(0,8.8),ylim=(0,7.1)); ax.axis('off'); xs = [.1,2.49,5.83]
    for letter, title, y, group, top, spacing in [('a','Public model triggers',6.86,'triggers',6.27,.66),('b','Baseline and variations',3.72,'variations',3.16,.64)]:
        ax.text(.1,y,letter,fontweight='bold',fontsize=14); ax.text(.43,y,title,fontweight='bold',fontsize=13)
        headers = ['Model term','Trigger to examine','Inference limit'] if group=='triggers' else ['Hypothetical','Changed premise','Question that changes']
        for x,value in zip(xs,headers): ax.text(x,y-.38,value,fontweight='bold',fontsize=11.4)
        records = [row for row in labels if row['panel']==group]
        for i,row in enumerate(records):
            yy = top-i*spacing; ax.plot([.1,8.64],[yy,yy],color=colors[i%3],lw=.65)
            for x,key in zip(xs,['left','middle','right']): ax.text(x,yy-.13,row[key],va='top',linespacing=1.4,fontsize=10.8)
    ax.text(.1,4.23,'Model terms are not guidance. The $500 threshold concerns copies, not pass-through.',fontsize=10.5,color='#444444')
    ax.text(.1,.56,'Permission may settle approval; it does not prove safeguard performance.',fontsize=10.5,color='#444444')
    ax.text(.1,.22,'A0 is an assumed baseline. A1 / A2 vs A0; A3 vs A2. Worked A1 adds premises.',fontsize=10.5,color='#444444')
    save_figure(fig, FIGURES[0]['name'])
    fig, ax = plt.subplots(figsize=(8.8,5.75)); fig.subplots_adjust(left=.02,right=.985,bottom=.025,top=.985)
    ax.set(xlim=(0,8.8),ylim=(0,5.75)); ax.axis('off'); xs=[.1,2.86,6.16]
    ax.text(.1,5.49,'a',fontweight='bold',fontsize=14); ax.text(.43,5.49,'Contract paths',fontweight='bold',fontsize=13)
    for x,value in zip(xs,['Claimant and defendant','Undertaking invoked','Entitlement to examine']): ax.text(x,5.09,value,fontweight='bold',fontsize=11.2)
    for i,row in enumerate([r for r in labels if r['panel']=='contracts']):
        y=4.87-i*.72; ax.plot([.1,8.63],[y,y],color=colors[i%3],lw=.65)
        for x,key in zip(xs,['left','middle','right']): ax.text(x,y-.14,row[key],va='top',linespacing=1.4,fontsize=11.1)
    ax.text(.1,1.80,'N2 is optional. Reporting or confidentiality labels do not guarantee survival.',fontsize=10.7,color='#444444')
    ax.text(.1,1.30,'b',fontweight='bold',fontsize=14); ax.text(.43,1.30,'Copyright path',fontweight='bold',fontsize=13)
    ax.plot([.1,8.63],[1.09,1.09],color=colors[0],lw=.65)
    row = next(r for r in labels if r['panel']=='copyright')
    for x,key in zip(xs,['left','middle','right']): ax.text(x,.93,row[key],va='top',linespacing=1.4,fontsize=11.1)
    ax.text(.1,.16,'Permission, statutory prerequisites, defences and other merits requirements remain open.',fontsize=10.6,color='#444444')
    save_figure(fig, FIGURES[1]['name'])
    (OUT / 'data/figure_spec.json').write_text(json.dumps(FIGURES, indent=2), encoding='utf-8')
    (OUT / 'qa/figure_geometry_audit.json').write_text(json.dumps(GEOMETRY, indent=2), encoding='utf-8')

if __name__ == '__main__':
    (OUT/'qa').mkdir(exist_ok=True)
    (OUT/'figures').mkdir(exist_ok=True)
    figures()
    if any(row['text_collisions'] or row['text_outside_canvas'] for row in GEOMETRY):
        raise SystemExit('Figure geometry requires review')
    print('Two conceptual figures rebuilt. No transaction observations or liability results estimated.')
