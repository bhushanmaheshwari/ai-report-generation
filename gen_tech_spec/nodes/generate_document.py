from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from gen_tech_spec.classes.State import State
import tempfile
import os
import webbrowser
from datetime import datetime

def generate_document(state: State):
    """Generate a PDF document with all sections from state and open in new tab"""
    
    # Create a temporary PDF file
    temp_dir = tempfile.mkdtemp()
    pdf_filename = f"tech_spec_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf_path = os.path.join(temp_dir, pdf_filename)
    
    # Create the PDF document
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=HexColor('#2E4A6B'),
        alignment=1  # Center alignment
    )
    
    section_header_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=20,
        textColor=HexColor('#2E4A6B')
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        leading=14
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Courier',
        backgroundColor=HexColor('#F5F5F5'),
        borderColor=HexColor('#CCCCCC'),
        borderWidth=1,
        leftIndent=20,
        rightIndent=20,
        spaceAfter=12,
        spaceBefore=6
    )
    
    # Build the document content
    story = []
    
    # Title
    title = Paragraph(f"Technical Specification: {state.get('topic', 'Untitled')}", title_style)
    story.append(title)
    story.append(Spacer(1, 20))
    
    # Add sections based on available data in state
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
        if content and content.strip():  # Only add sections with content
            # Section header
            header = Paragraph(section_name, section_header_style)
            story.append(header)
            
            # Section content
            if state_key == 'code':
                # Clean markdown code blocks and format for PDF
                clean_code = content
                if clean_code.startswith("```python"):
                    clean_code = clean_code[9:]  # Remove ```python
                elif clean_code.startswith("```"):
                    clean_code = clean_code[3:]  # Remove ```
                
                if clean_code.endswith("```"):
                    clean_code = clean_code[:-3]  # Remove trailing ```
                
                # Strip whitespace and escape HTML entities
                clean_code = clean_code.strip()
                clean_code = clean_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                
                # Format code with proper line breaks
                formatted_code = clean_code.replace('\n', '<br/>')
                code_paragraph = Paragraph(formatted_code, code_style)
                story.append(code_paragraph)
            else:
                # Regular content - handle markdown-like formatting
                formatted_content = content.replace('\n', '<br/>')
                content_paragraph = Paragraph(formatted_content, body_style)
                story.append(content_paragraph)
            
            story.append(Spacer(1, 12))
    
    # Add diagram if available
    if state.get('diagram') and os.path.exists(state['diagram']):
        story.append(PageBreak())
        diagram_header = Paragraph("Architecture Diagram", section_header_style)
        story.append(diagram_header)
        
        try:
            # Add the diagram image
            img = Image(state['diagram'], width=6*inch, height=4*inch)
            story.append(img)
        except Exception as e:
            error_text = Paragraph(f"Could not load diagram: {str(e)}", body_style)
            story.append(error_text)
    
    # Generate timestamp
    timestamp = Paragraph(
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
        styles['Normal']
    )
    story.append(Spacer(1, 30))
    story.append(timestamp)
    
    # Build the PDF
    doc.build(story)
    
    # Open the PDF in a new browser tab
    webbrowser.open(f'file://{pdf_path}')
    
    return {
        "pdf_path": pdf_path,
        "pdf_generated": True,
        "report": f"PDF generated successfully at: {pdf_path}"
    }