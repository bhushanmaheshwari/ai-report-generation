import os
import webbrowser
from datetime import datetime
from gen_tech_spec.classes.State import State
import markdown
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

def markdown_to_word(md_text, output_path, diagram_path=None):
    """Convert markdown to Word document using python-docx"""
    doc = Document()
    
    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    
    # Process markdown line by line
    lines = md_text.split('\n')
    in_code_block = False
    
    for line in lines:
        original_line = line
        line = line.strip()
        
        # Skip empty lines but add spacing after headings
        if not line:
            continue
            
        # Handle code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
            if not in_code_block:
                doc.add_paragraph()  # Add space after code block
            continue
            
        if in_code_block:
            # Add code content with monospace font
            code_para = doc.add_paragraph(original_line)
            code_run = code_para.runs[0] if code_para.runs else code_para.add_run(original_line)
            code_run.font.name = 'Courier New'
            code_run.font.size = Pt(9)
            continue
            
        # Handle different markdown elements
        if line.startswith('# '):
            # Main title
            title = doc.add_heading(line[2:], 0)
            title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.add_paragraph()  # Add space after title
            
        elif line.startswith('## '):
            # Section heading
            doc.add_paragraph()  # Add space before section
            doc.add_heading(line[3:], 1)
            
        elif line.startswith('### '):
            # Sub-section heading
            doc.add_heading(line[4:], 2)
            
        elif line.startswith('- ') or line.startswith('* '):
            # Bullet points
            doc.add_paragraph(line[2:], style='List Bullet')
            
        elif line.startswith('1. ') or line.startswith('2. ') or line.startswith('3. '):
            # Numbered lists
            doc.add_paragraph(line[3:], style='List Number')
            
        elif '[Diagram image:' in line and diagram_path:
            # Add diagram image
            if os.path.exists(diagram_path):
                try:
                    doc.add_paragraph()  # Add space before image
                    doc.add_picture(diagram_path, width=Inches(6))
                    last_paragraph = doc.paragraphs[-1]
                    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    doc.add_paragraph()  # Add space after image
                except:
                    doc.add_paragraph(f"[Diagram: {diagram_path}]")
                    
        elif line.startswith('<div class=\'timestamp\'>'):
            # Handle timestamp
            timestamp_text = line.replace('<div class=\'timestamp\'>', '').replace('</div>', '')
            doc.add_paragraph()  # Add space before timestamp
            timestamp_para = doc.add_paragraph(timestamp_text)
            timestamp_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            if timestamp_para.runs:
                timestamp_para.runs[0].italic = True
            
        elif line.startswith('**') and line.endswith('**'):
            # Bold text
            para = doc.add_paragraph()
            run = para.add_run(line[2:-2])
            run.bold = True
            
        elif line.startswith('*') and line.endswith('*'):
            # Italic text
            para = doc.add_paragraph()
            run = para.add_run(line[1:-1])
            run.italic = True
            
        elif '|' in line and line.count('|') >= 2:
            # Skip table formatting for now (basic handling)
            doc.add_paragraph(line)
            
        else:
            # Regular paragraph
            if line and not line.startswith('---'):
                # Handle inline formatting
                para = doc.add_paragraph()
                
                # Simple bold/italic handling
                if '**' in line:
                    parts = line.split('**')
                    for i, part in enumerate(parts):
                        if i % 2 == 0:
                            # Normal text
                            if '*' in part:
                                italic_parts = part.split('*')
                                for j, italic_part in enumerate(italic_parts):
                                    run = para.add_run(italic_part)
                                    if j % 2 == 1:
                                        run.italic = True
                            else:
                                para.add_run(part)
                        else:
                            # Bold text
                            run = para.add_run(part)
                            run.bold = True
                else:
                    # No bold formatting, just add the text
                    para.add_run(line)
    
    # Save document
    doc.save(output_path)
    return True

def get_diagram_path(state):
    """Get diagram path, preferring PNG over DOT files"""
    diagram_path = state.get('diagram')
    if not diagram_path:
        return None
    
    if diagram_path.endswith('.dot'):
        png_path = diagram_path + '.png'
        return png_path if os.path.exists(png_path) else None
    
    return diagram_path if os.path.exists(diagram_path) else None

def generate_document(state: State):
    """Generate a Word document from markdown sections in state"""
    # Create Word document in static/reports directory
    reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    
    doc_filename = f"tech_spec_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
    doc_path = os.path.join(reports_dir, doc_filename)

    # Build markdown content
    md_sections = []
    title = state.get('topic', 'Untitled')
    md_sections.append(f"# Technical Specification: {title}\n")

    sections = [
        ('Summary', 'summary'),
        ('Requirements', 'requirements'),
        ('Components', 'components'),
        #('Code', 'code'),
        ('Report', 'report')
    ]

    for section_name, state_key in sections:
        content = state.get(state_key)
        if content and content.strip():
            md_sections.append(f"## {section_name}\n\n{content}\n")

    # Add diagram if available
    diagram_path = get_diagram_path(state)
    if diagram_path:
        md_sections.append(f"\n## Architecture Diagram\n\n[Diagram image: {diagram_path}]\n")

    # Add timestamp
    md_sections.append(f"\n<div class='timestamp'>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>")

    # Generate Word document
    md_text = "\n".join(md_sections)
    success = markdown_to_word(md_text, doc_path, diagram_path)
    
    if success:
        # Open Word document
        webbrowser.open(f'file://{doc_path}')
        return {
            "doc_path": doc_path,
            "doc_generated": True,
            "report": f"Word document generated successfully at: {doc_path}"
        }
    else:
        return {
            "doc_path": None,
            "doc_generated": False,
            "report": "Failed to generate Word document"
        }