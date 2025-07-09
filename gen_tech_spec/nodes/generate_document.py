import tempfile
import os
import webbrowser
from datetime import datetime
from gen_tech_spec.classes.State import State
from fpdf import FPDF
import markdown
import re

class PDF(FPDF):
    pass

def markdown_to_pdf(md_text, output_pdf_path):
    html = markdown.markdown(md_text)
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    # Remove HTML tags for simplicity
    text = re.sub('<[^<]+?>', '', html)
    for line in text.splitlines():
        if line.strip():
            pdf.cell(0, 10, line, ln=True)
    pdf.output(output_pdf_path)

def generate_document(state: State):
    """Generate a PDF document from markdown sections in state and open in new tab"""
    # Create a temporary PDF file
    temp_dir = tempfile.mkdtemp()
    pdf_filename = f"tech_spec_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf_path = os.path.join(temp_dir, pdf_filename)

    # Build markdown document from state
    md_sections = []
    title = state.get('topic', 'Untitled')
    md_sections.append(f"# Technical Specification: {title}\n")

    sections = [
        ('Summary', 'summary'),
        ('Tags', 'tags'),
        ('Requirements', 'requirements'),
        ('Components', 'components'),
        ('Flow', 'flow'),
        ('Code', 'code'),
        ('Report', 'report')
    ]

    for section_name, state_key in sections:
        content = state.get(state_key)
        if content and content.strip():
            md_sections.append(f"## {section_name}\n\n{content}\n")

    # Add diagram if available
    if state.get('diagram') and os.path.exists(state['diagram']):
        # Just add a placeholder for the image, as fpdf2 does not support markdown images
        img_path = state['diagram']
        md_sections.append(f"\n## Architecture Diagram\n\n[Diagram image: {img_path}]\n")

    # Generate timestamp
    md_sections.append(f"\n---\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md_text = "\n".join(md_sections)
    markdown_to_pdf(md_text, pdf_path)

    # Open the PDF in a new browser tab
    webbrowser.open(f'file://{pdf_path}')

    return {
        "pdf_path": pdf_path,
        "pdf_generated": True,
        "report": f"PDF generated successfully at: {pdf_path}"
    }