#!/usr/bin/env python3
"""Export the site's CV data and bibliography to assets/pdf/jonathan-lys-cv.pdf.

Run with a Python environment containing reportlab; Ruby dependencies come from
this site's bundle. No separately maintained CV content is required.
"""
import json
import re
import subprocess
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, PageBreak

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets/pdf/jonathan-lys-cv.pdf'
RUBY = '''require 'yaml'; require 'date'; require 'json'; require 'bibtex'
cv = YAML.safe_load_file('_data/cv.yml', permitted_classes: [Date])['cv']
papers = BibTeX.open('_bibliography/papers.bib').entries.values.map do |p|
  %w[title year author arxiv doi url].to_h { |k| [k, p[k].to_s] }
end
puts JSON.generate({cv: cv, papers: papers})'''
data = json.loads(subprocess.check_output(['bundle', 'exec', 'ruby', '-e', RUBY], cwd=ROOT))
cv = data['cv']
ink, muted, teal = '#243438', '#52686d', '#22616b'
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=26, leading=30, textColor=colors.HexColor(ink), spaceAfter=8),
    'heading': ParagraphStyle('heading', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=colors.HexColor(teal), spaceBefore=14, spaceAfter=8, keepWithNext=True),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=12, textColor=colors.HexColor(ink), spaceAfter=4),
    'meta': ParagraphStyle('meta', fontName='Helvetica', fontSize=8, leading=11, textColor=colors.HexColor(muted), spaceAfter=4),
}
story = []

def clean(value):
    text = str(value).replace('--', '-').replace('–', '-').replace('—', '-').replace('’', "'")
    text = re.sub(r'[{}]', '', text)
    text = escape(text)
    text = re.sub(r'&lt;br\s*/?&gt;', '<br/>', text)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)

def para(text, style='body'):
    return Paragraph(text, styles[style])

def date_range(entry):
    start, end = str(entry.get('start_date', '')), str(entry.get('end_date', 'Present'))
    return start if start == end else f'{start} - {end}'

story += [para(clean(cv['name']), 'name'), para('Research / representations / generation', 'meta'),
          para(f'<link href="mailto:{cv["email"]}" color="{teal}">{cv["email"]}</link> &nbsp; | &nbsp; <link href="{cv["website"]}" color="{teal}">jonathanlys01.github.io</link>', 'meta'),
          Spacer(1, 8), para('Third-year PhD candidate at IMT Atlantique. Research on discrete diffusion, diversity-aware decoding, and EEG foundation models.')]

for section, entries in cv['sections'].items():
    if section in ('Education', 'Skills'): story.append(PageBreak())
    story.append(para(clean(section), 'heading'))
    for entry in sorted(entries, key=lambda e: str(e.get('end_date', '')), reverse=True) if section in ('Experience', 'Education') else entries:
        group = []
        if section in ('Experience', 'Education'):
            title = entry.get('position', entry.get('degree', ''))
            org = entry.get('company', entry.get('institution', ''))
            group += [para(f'<b>{clean(title)}</b> &nbsp; / &nbsp; {clean(date_range(entry))}'), para(clean(org), 'meta')]
            if entry.get('summary'): group.append(para(clean(entry['summary'])))
            group += [para('- ' + clean(item)) for item in entry.get('highlights', [])]
        elif 'label' in entry:
            group.append(para(f'<b>{clean(entry["label"])}</b> - {clean(entry["details"])}'))
        else:
            detail = entry.get('summary', ', '.join(entry.get('keywords', [])))
            group.append(para(f'<b>{clean(entry.get("name", ""))}</b>: {clean(detail)}'))
        story.append(KeepTogether(group + [Spacer(1, 5)]))
    if section == 'Education':
        story.append(para('Publications', 'heading'))
        for paper in sorted(data['papers'], key=lambda p: p['year'], reverse=True):
            url = 'https://arxiv.org/abs/' + paper['arxiv'] if paper['arxiv'] else 'https://doi.org/' + paper['doi'] if paper['doi'] else paper['url']
            title = clean(paper['title'])
            if url: title = f'<link href="{escape(url)}" color="{teal}">{title}</link>'
            story.append(KeepTogether([para(f'<b>{title}</b> ({clean(paper["year"])})'), para(clean(paper['author']).replace(' and ', ', '), 'meta'), Spacer(1, 4)]))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
def footer(canvas, doc):
    canvas.setStrokeColor(colors.HexColor('#dce4e3'))
    canvas.line(44, 35, A4[0] - 44, 35)
    canvas.setFont('Helvetica', 7)
    canvas.setFillColor(colors.HexColor(muted))
    canvas.drawString(44, 23, 'Jonathan Lys / Curriculum vitae')
    canvas.drawRightString(A4[0] - 44, 23, str(doc.page))

SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=44, rightMargin=44, topMargin=40, bottomMargin=48,
                  title='Jonathan Lys - Curriculum vitae', author='Jonathan Lys').build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
