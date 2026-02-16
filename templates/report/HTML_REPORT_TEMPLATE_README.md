HTML Report Template - Documentation
===================================

## Overview

This template (`html_report_template.py`) provides a **pipeline-agnostic, portable framework** for generating standardized HTML reports. It's designed to be used as a foundation for harmonizing report design across multiple analysis tools.

## Purpose

The template demonstrates:
- **Consistent visual styling** for reports regardless of the underlying analysis pipeline
- **Flexible CLI interface** for configuring report appearance and content
- **Reusable CSS color schemes** (light, dark, minimal) that can be applied across tools
- **Modular section structure** for adding custom analysis-specific content
- **Professional HTML5 structure** with responsive design and embedded assets

## Key Features

### 1. Color Schemes (Pipeline-Agnostic)
Three built-in themes that work for any pipeline:
- **Light Theme**: Professional, clean appearance (default)
- **Dark Theme**: Reduced eye strain for extended viewing
- **Minimal Theme**: Focus on content with serif typography

Each theme is defined as a color dictionary and can be easily extended for custom branding.

### 2. Flexible CLI Options
**Styling options:**
```bash
--theme {light|dark|minimal|custom}     # Select color theme
--color-scheme SCHEME                   # Override specific colors
--font-family FONT                      # Change typography
--logo PATH                             # Add header logo
--embed-assets                          # Embed all assets for portability
```

**Content options:**
```bash
--title TEXT                            # Report title
--description TEXT                      # Report description
--author NAME                           # Author name
--tags TAG [TAG ...]                    # Report tags
--sections SECTION [SECTION ...]        # Select sections
```

**Output options:**
```bash
--theme {light|dark|minimal|custom}     # Report color theme
--plot-format {svg|png|interactive}     # Visualization format
--export {html|pdf|markdown}            # Export formats
--overwrite                             # Replace existing files
```

### 3. Report Sections (Customizable)
Pre-built placeholder sections:
- **Summary**: Status, timing, data statistics
- **Metrics**: Key performance indicators and measurements
- **Visualizations**: Charts, graphs, plots
- **Quality**: Data quality assessment and validation
- **Metadata**: Execution information and configuration

Sections can be mixed and matched via CLI, or custom sections can be added by extending `generate_section_placeholder()`.

### 4. Responsive Design
- Works on desktop, tablet, and mobile
- Flexible grid layouts that adapt to screen size
- Sticky navigation for easy section access
- Accessible HTML structure

## Usage Guide

### Basic Example
```bash
python html_report_template.py /data/input /reports/output.html
```

### With Custom Styling
```bash
python html_report_template.py /data/input /reports/output.html \
    --theme dark \
    --title "My Analysis Report" \
    --author "Jane Smith" \
    --embed-assets
```

### Specific Sections and Metadata
```bash
python html_report_template.py /data/input /reports/output.html \
    --sections summary metrics quality \
    --author "Team X" \
    --tags analysis neuroimaging quality-control \
    --description "Batch analysis of 50 subjects"
```

### Programmatic Usage (Python)
```python
from html_report_template import generate_html_report

html_content = generate_html_report(
    title="Analysis Results",
    description="Results from experiment XYZ",
    sections=["summary", "metrics", "visualizations", "quality"],
    theme="light",
    author="Dr. Smith",
    tags=["neuroimaging", "clinical"],
    metadata={
        "Study": "STUDY_001",
        "Date": "2024-01-15",
    }
)

# Write to file
with open("report.html", "w") as f:
    f.write(html_content)
```

## Customization Guide

### 1. Adding Custom Sections
Extend `generate_section_placeholder()`:
```python
def generate_section_placeholder(section_name: str) -> str:
    # ... existing code ...
    elif section_id == "custom":
        return """
    <section id="custom" class="section">
        <h2>Custom Analysis</h2>
        <p>Your custom content here</p>
    </section>
    """
```

### 2. Adding Custom Color Schemes
Add to `build_color_scheme()`:
```python
schemes = {
    # ... existing schemes ...
    "brand-blue": {
        "bg_color": "#f0f4f8",
        "accent_color": "#003366",
        # ... other color definitions ...
    },
}
```

### 3. Custom Metadata Fields
Pass metadata to `generate_html_report()`:
```python
html = generate_html_report(
    title="Report",
    metadata={
        "Custom Field 1": "Value 1",
        "Custom Field 2": "Value 2",
        "Custom Field 3": "Value 3",
    }
)
```

### 4. Modifying CSS Styles
Edit `DEFAULT_CSS` for global styling changes, or override specific classes:
```python
custom_css = DEFAULT_CSS.replace(
    "max-width: 1200px;",
    "max-width: 1400px;"
)
```

## Integration with Pipelines

### For fMRI Denoising Tools
```python
from html_report_template import generate_html_report

# In your pipeline
html = generate_html_report(
    title="fMRI Denoising Report",
    description="Results of denoising analysis",
    sections=["summary", "metrics", "visualizations", "quality"],
    metadata={
        "Denoising Method": "ICA-AROMA",
        "Input Files": "25 subjects",
        "Duration": "1hr 23min",
    },
    tags=["fmri", "denoising", "ica-aroma"],
)
```

### For Other Neuroimaging Pipelines
```python
# Adapt for your tool
html = generate_html_report(
    title="[Tool Name] Analysis Report",
    description="[Tool-specific description]",
    sections=["summary", "metrics", "quality"],  # Select relevant sections
    metadata={
        "Tool": "[Tool Name]",
        "Version": "[Version]",
        # Add tool-specific metadata
    },
    theme="dark",  # or any theme
)
```

## Color Scheme Reference

### Light Theme (Default)
- Primary Color: `#667eea` (Indigo)
- Background: `#ffffff` (White)
- Text: `#333333` (Dark Gray)
- Best for: Professional reports, printing

### Dark Theme
- Primary Color: `#63b3ed` (Light Blue)
- Background: `#1a202c` (Dark Gray)
- Text: `#e2e8f0` (Light Gray)
- Best for: Long viewing sessions, presentations

### Minimal Theme
- Primary Color: `#000000` (Black)
- Background: `#fafafa` (Off-white)
- Text: `#444444` (Gray)
- Typography: Georgia serif
- Best for: Academic reports, publications

## File Size and Portability

- **With `--embed-assets`**: Single self-contained HTML file (~50-100KB)
- **Without `--embed-assets`**: HTML + separate CSS/JS/images (~10-20KB html)
- **Mobile-friendly**: Optimized for all screen sizes
- **No external dependencies**: Pure HTML5, works offline

## Browser Compatibility

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support
- Internet Explorer: Not supported (use modern browsers)

## Performance Notes

- CSS Grid and Flexbox for modern layout
- SVG charts recommended over raster for quality
- Images should be optimized (< 100KB each)
- Report typically loads in < 500ms on standard connection

## Future Enhancement Ideas

1. **Interactive Charts**: Add Plotly, D3.js, or Chart.js integration
2. **Export Formats**: PDF generation, Markdown export
3. **Dynamic Content**: JavaScript for filtering, sorting, toggling sections
4. **Search**: Full-text search within report
5. **Themes**: Add more pre-built color schemes
6. **Accessibility**: Enhanced WCAG 2.1 AA compliance
7. **Printing**: CSS print media queries for paper output
8. **Multi-language**: i18n support for section headers

## License & Attribution

This template can be freely adapted for any analysis tool. When using, consider:
- Maintaining the footer attribution
- Documenting any significant modifications
- Contributing improvements back to the community

## Support

For issues or questions:
1. Check this documentation
2. Review code comments in `html_report_template.py`
3. Examine the `generate_*()` functions for customization points
4. Test with `python html_report_template.py --help` for CLI options
