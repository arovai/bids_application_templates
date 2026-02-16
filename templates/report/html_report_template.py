"""
HTML Report Template: Pipeline-Agnostic Report Generation Framework

This template provides a standardized HTML report design and CLI interface for
generating analysis reports. It demonstrates best practices for:
  - Consistent visual styling across different analysis tools
  - Colored console output during report generation
  - Command-line configuration for report parameters
  - HTML report structure and CSS styling
  - Integration of analysis results and metrics

This is a design template, not a functional tool. Customize the HTML template
and analysis sections for your specific pipeline needs.
"""

import argparse
import sys
import textwrap
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any


class Colors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class ColoredHelpFormatter(argparse.RawDescriptionHelpFormatter):
    """Custom formatter with colored section headers."""

    def __init__(self, prog, indent_increment=2, max_help_position=40, width=100):
        super().__init__(prog, indent_increment, max_help_position, width)

    def _format_usage(self, usage, actions, groups, prefix):
        if prefix is None:
            prefix = f'{Colors.BOLD}Usage:{Colors.END} '
        return super()._format_usage(usage, actions, groups, prefix)

    def start_section(self, heading):
        if heading:
            heading = f'{Colors.BOLD}{Colors.CYAN}{heading}{Colors.END}'
        super().start_section(heading)


def create_parser() -> argparse.ArgumentParser:
    """Create command-line argument parser for report generation."""

    description = textwrap.dedent(f"""
    {Colors.BOLD}{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════╗
    ║                     ANALYSIS REPORT GENERATOR v1.0.0                          ║
    ║                   Portable HTML Report Generation Tool                        ║
    ╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}

    {Colors.BOLD}Description:{Colors.END}
      This tool generates standardized HTML reports from analysis outputs. It
      combines analysis metrics, visualizations, and quality assessment into a
      professional, portable HTML document with consistent styling and layout.

    {Colors.BOLD}Workflow:{Colors.END}
      1. Collect analysis input data and metrics
      2. Configure report appearance and content
      3. Generate HTML report with embedded assets
      4. Apply consistent styling and formatting
      5. Produce standalone, portable report file
      6. Validate report integrity and completeness
    """)

    epilog = textwrap.dedent(f"""
    {Colors.BOLD}{Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}
    {Colors.BOLD}EXAMPLES{Colors.END}
    {Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}

    {Colors.BOLD}Basic Usage:{Colors.END}

      {Colors.YELLOW}# Generate report with default settings{Colors.END}
      generate-report /data/inputs /reports/output.html

      {Colors.YELLOW}# Generate report for specific analysis{Colors.END}
      generate-report /data/inputs /reports/output.html --analysis-id analysis_001

    {Colors.BOLD}Styling and Appearance:{Colors.END}

      {Colors.YELLOW}# Generate report with custom theme{Colors.END}
      generate-report /data/inputs /reports/output.html --theme dark

      {Colors.YELLOW}# Generate report with custom color scheme{Colors.END}
      generate-report /data/inputs /reports/output.html --color-scheme custom --config style.yaml

      {Colors.YELLOW}# Generate report with embedded assets{Colors.END}
      generate-report /data/inputs /reports/output.html --embed-assets

    {Colors.BOLD}Content Configuration:{Colors.END}

      {Colors.YELLOW}# Include specific sections in report{Colors.END}
      generate-report /data/inputs /reports/output.html \\
          --sections summary metrics visualizations

      {Colors.YELLOW}# Generate report with custom title and description{Colors.END}
      generate-report /data/inputs /reports/output.html \\
          --title "My Analysis Report" --description "Analysis of dataset XYZ"

      {Colors.YELLOW}# Generate report with metadata{Colors.END}
      generate-report /data/inputs /reports/output.html \\
          --author "Jane Smith" --tags analysis quality-metrics

    {Colors.BOLD}Output Options:{Colors.END}

      {Colors.YELLOW}# Override existing report{Colors.END}
      generate-report /data/inputs /reports/output.html --overwrite

      {Colors.YELLOW}# Generate multiple format exports{Colors.END}
      generate-report /data/inputs /reports/output --export html pdf

      {Colors.YELLOW}# Generate verbose report with detailed logging{Colors.END}
      generate-report /data/inputs /reports/output.html -v

    {Colors.BOLD}{Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}
    {Colors.BOLD}REPORT THEMES{Colors.END}
    {Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}

      {Colors.CYAN}light{Colors.END}         Light theme - clean, professional appearance
      {Colors.CYAN}dark{Colors.END}          Dark theme - reduced eye strain in low light
      {Colors.CYAN}minimal{Colors.END}       Minimal theme - focus on content
      {Colors.CYAN}custom{Colors.END}        Custom theme - requires --config file

    {Colors.BOLD}Note:{Colors.END} Theme selection affects color scheme, typography, and
    overall visual presentation of the report.

    {Colors.BOLD}{Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}
    {Colors.BOLD}MORE INFORMATION{Colors.END}
    {Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}

      Documentation:  https://github.com/example/report-template
      Report Issues:  https://github.com/example/report-template/issues
      Version:        1.0.0
    """)

    parser = argparse.ArgumentParser(
        prog="generate-report",
        description=description,
        epilog=epilog,
        formatter_class=ColoredHelpFormatter,
        add_help=False,
    )

    # =========================================================================
    # REQUIRED ARGUMENTS
    # =========================================================================
    required = parser.add_argument_group(
        f'{Colors.BOLD}Required Arguments{Colors.END}'
    )

    required.add_argument(
        "input_dir",
        type=Path,
        metavar="INPUT_DIR",
        help="Path to directory containing analysis outputs and metrics.",
    )

    required.add_argument(
        "output_file",
        type=Path,
        metavar="OUTPUT_FILE",
        help="Path to output HTML report file.",
    )

    # =========================================================================
    # GENERAL OPTIONS
    # =========================================================================
    general = parser.add_argument_group(
        f'{Colors.BOLD}General Options{Colors.END}'
    )

    general.add_argument(
        "-h", "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show this help message and exit.",
    )

    general.add_argument(
        "--version",
        action="version",
        version="generate-report 1.0.0",
        help="Show program version and exit.",
    )

    general.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output (DEBUG level logging).",
    )

    general.add_argument(
        "-c", "--config",
        type=Path,
        metavar="FILE",
        help="Path to configuration file (.json, .yaml, or .yml). "
             "CLI arguments override config file settings.",
    )

    # =========================================================================
    # REPORT CONTENT OPTIONS
    # =========================================================================
    content = parser.add_argument_group(
        f'{Colors.BOLD}Report Content Options{Colors.END}'
    )

    content.add_argument(
        "--title",
        metavar="TEXT",
        default="Analysis Report",
        help="Report title displayed in header (default: 'Analysis Report').",
    )

    content.add_argument(
        "--description",
        metavar="TEXT",
        help="Report description or summary text.",
    )

    content.add_argument(
        "--analysis-id",
        metavar="ID",
        dest="analysis_id",
        help="Unique identifier for this analysis.",
    )

    content.add_argument(
        "--author",
        metavar="NAME",
        help="Report author name.",
    )

    content.add_argument(
        "--tags",
        metavar="TAG",
        nargs='+',
        help="Tag report with keywords (can be specified multiple times).",
    )

    content.add_argument(
        "--sections",
        metavar="SECTION",
        nargs='+',
        choices=["summary", "metrics", "visualizations", "quality", "metadata"],
        help="Which sections to include in report. "
             "Choose from: summary, metrics, visualizations, quality, metadata.",
    )

    # =========================================================================
    # STYLING OPTIONS
    # =========================================================================
    styling = parser.add_argument_group(
        f'{Colors.BOLD}Styling Options{Colors.END}',
        "Customize report appearance and visual presentation."
    )

    styling.add_argument(
        "--theme",
        metavar="THEME",
        choices=["light", "dark", "minimal", "custom"],
        default="light",
        help="Report color theme (default: light).",
    )

    styling.add_argument(
        "--color-scheme",
        metavar="SCHEME",
        dest="color_scheme",
        help="Custom color scheme name or path to color configuration.",
    )

    styling.add_argument(
        "--font-family",
        metavar="FONT",
        dest="font_family",
        help="CSS font family for report text.",
    )

    styling.add_argument(
        "--logo",
        metavar="PATH",
        type=Path,
        help="Path to logo image to embed in report header.",
    )

    styling.add_argument(
        "--embed-assets",
        action="store_true",
        dest="embed_assets",
        help="Embed all assets (images, CSS) directly in HTML file "
             "for portability.",
    )

    # =========================================================================
    # VISUALIZATION OPTIONS
    # =========================================================================
    visuals = parser.add_argument_group(
        f'{Colors.BOLD}Visualization Options{Colors.END}',
        "Configure charts, graphs, and visual elements."
    )

    visuals.add_argument(
        "--plot-format",
        metavar="FORMAT",
        dest="plot_format",
        choices=["svg", "png", "interactive"],
        default="interactive",
        help="Format for plot generation (default: interactive).",
    )

    visuals.add_argument(
        "--dpi",
        metavar="DPI",
        type=int,
        default=100,
        help="DPI resolution for raster images (default: 100).",
    )

    visuals.add_argument(
        "--include-thumbnails",
        action="store_true",
        dest="include_thumbnails",
        help="Include thumbnail previews of images in report.",
    )

    # =========================================================================
    # OUTPUT OPTIONS
    # =========================================================================
    output = parser.add_argument_group(
        f'{Colors.BOLD}Output Options{Colors.END}'
    )

    output.add_argument(
        "--export",
        metavar="FORMAT",
        nargs='+',
        choices=["html", "pdf", "markdown"],
        default=["html"],
        help="Export formats for report (default: html).",
    )

    output.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing output files.",
    )

    output.add_argument(
        "--validate",
        action="store_true",
        help="Validate report integrity and completeness after generation.",
    )

    return parser


# ============================================================================
# HTML REPORT TEMPLATE
# ============================================================================

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="{author}">
    <meta name="description" content="{description}">
    <title>{title}</title>
    <style>
        {css_content}
    </style>
</head>
<body>
    <div class="report-container">
        {header_html}
        {navigation_html}
        {main_content_html}
        {footer_html}
    </div>
    <script>
        {javascript_content}
    </script>
</body>
</html>
"""

DEFAULT_CSS = """
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    body {{
        font-family: {font_family};
        line-height: 1.6;
        color: {text_color};
        background-color: {bg_color};
    }}

    .report-container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }}

    header {{
        background: linear-gradient(135deg, {header_bg_start}, {header_bg_end});
        color: white;
        padding: 40px 20px;
        border-radius: 8px;
        margin-bottom: 30px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }}

    header h1 {{
        font-size: 2.5em;
        margin-bottom: 10px;
    }}

    header .subtitle {{
        font-size: 1.1em;
        opacity: 0.95;
    }}

    .metadata {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
        margin-top: 20px;
        font-size: 0.9em;
    }}

    .metadata-item {{
        background: rgba(0, 0, 0, 0.1);
        padding: 10px;
        border-radius: 4px;
    }}

    .metadata-label {{
        font-weight: bold;
        opacity: 0.9;
    }}

    nav {{
        background: {nav_bg};
        padding: 0;
        margin-bottom: 30px;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        position: sticky;
        top: 0;
        z-index: 100;
    }}

    nav ul {{
        list-style: none;
        display: flex;
        flex-wrap: wrap;
    }}

    nav li {{
        flex: 1;
        min-width: 120px;
    }}

    nav a {{
        display: block;
        padding: 15px 20px;
        color: {nav_link_color};
        text-decoration: none;
        border-bottom: 3px solid transparent;
        transition: all 0.3s ease;
    }}

    nav a:hover {{
        border-bottom-color: {accent_color};
        background: rgba(0, 0, 0, 0.05);
    }}

    .section {{
        margin-bottom: 40px;
        padding: 20px;
        background: {section_bg};
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }}

    .section h2 {{
        color: {heading_color};
        font-size: 1.8em;
        margin-bottom: 20px;
        border-bottom: 2px solid {accent_color};
        padding-bottom: 10px;
    }}

    .section h3 {{
        color: {heading_color};
        font-size: 1.3em;
        margin-top: 20px;
        margin-bottom: 10px;
    }}

    .metrics-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }}

    .metric-card {{
        background: {card_bg};
        border: 1px solid {border_color};
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        transition: transform 0.2s ease;
    }}

    .metric-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
    }}

    .metric-value {{
        font-size: 2.2em;
        font-weight: bold;
        color: {accent_color};
        margin: 10px 0;
    }}

    .metric-label {{
        font-size: 0.95em;
        color: {muted_color};
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    .metric-unit {{
        font-size: 0.8em;
        color: {muted_color};
    }}

    .visualization {{
        background: {chart_bg};
        border: 1px solid {border_color};
        border-radius: 6px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
    }}

    .visualization img {{
        max-width: 100%;
        height: auto;
        border-radius: 4px;
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }}

    thead {{
        background: {table_header_bg};
        color: white;
    }}

    th {{
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }}

    td {{
        padding: 12px;
        border-bottom: 1px solid {border_color};
    }}

    tbody tr:hover {{
        background: {table_hover_bg};
    }}

    .status-badge {{
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: bold;
    }}

    .status-success {{
        background: #d4edda;
        color: #155724;
    }}

    .status-warning {{
        background: #fff3cd;
        color: #856404;
    }}

    .status-error {{
        background: #f8d7da;
        color: #721c24;
    }}

    .status-info {{
        background: #d1ecf1;
        color: #0c5460;
    }}

    .tag {{
        display: inline-block;
        background: {tag_bg};
        color: {tag_color};
        padding: 5px 10px;
        border-radius: 4px;
        margin: 5px 5px 5px 0;
        font-size: 0.85em;
    }}

    footer {{
        background: {footer_bg};
        color: {footer_text};
        padding: 30px 20px;
        text-align: center;
        border-top: 1px solid {border_color};
        margin-top: 40px;
        border-radius: 0 0 8px 8px;
    }}

    footer p {{
        margin: 5px 0;
        font-size: 0.9em;
    }}

    .footer-links {{
        margin-top: 15px;
    }}

    .footer-links a {{
        color: {accent_color};
        text-decoration: none;
        margin: 0 10px;
    }}

    .footer-links a:hover {{
        text-decoration: underline;
    }}

    @media (max-width: 768px) {{
        header h1 {{
            font-size: 1.8em;
        }}

        .metrics-grid {{
            grid-template-columns: 1fr;
        }}

        nav ul {{
            flex-direction: column;
        }}

        nav li {{
            min-width: 100%;
        }}

        .metadata {{
            grid-template-columns: 1fr;
        }}
    }}
"""


# ============================================================================
# REPORT GENERATOR FUNCTIONS
# ============================================================================

def build_color_scheme(theme: str) -> Dict[str, str]:
    """Build color scheme based on selected theme."""
    schemes = {
        "light": {
            "bg_color": "#ffffff",
            "text_color": "#333333",
            "header_bg_start": "#667eea",
            "header_bg_end": "#764ba2",
            "nav_bg": "#f8f9fa",
            "nav_link_color": "#333333",
            "accent_color": "#667eea",
            "section_bg": "#f9f9f9",
            "card_bg": "#ffffff",
            "heading_color": "#2d3748",
            "muted_color": "#718096",
            "border_color": "#e2e8f0",
            "chart_bg": "#ffffff",
            "table_header_bg": "#667eea",
            "table_hover_bg": "#f7fafc",
            "tag_bg": "#edf2f7",
            "tag_color": "#2d3748",
            "footer_bg": "#2d3748",
            "footer_text": "#ffffff",
            "font_family": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        },
        "dark": {
            "bg_color": "#1a202c",
            "text_color": "#e2e8f0",
            "header_bg_start": "#5a67d8",
            "header_bg_end": "#6b46c1",
            "nav_bg": "#2d3748",
            "nav_link_color": "#e2e8f0",
            "accent_color": "#63b3ed",
            "section_bg": "#2d3748",
            "card_bg": "#374151",
            "heading_color": "#e2e8f0",
            "muted_color": "#a0aec0",
            "border_color": "#4a5568",
            "chart_bg": "#2d3748",
            "table_header_bg": "#5a67d8",
            "table_hover_bg": "#374151",
            "tag_bg": "#4a5568",
            "tag_color": "#e2e8f0",
            "footer_bg": "#1a202c",
            "footer_text": "#a0aec0",
            "font_family": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        },
        "minimal": {
            "bg_color": "#fafafa",
            "text_color": "#444444",
            "header_bg_start": "#000000",
            "header_bg_end": "#333333",
            "nav_bg": "#ffffff",
            "nav_link_color": "#444444",
            "accent_color": "#000000",
            "section_bg": "#ffffff",
            "card_bg": "#ffffff",
            "heading_color": "#000000",
            "muted_color": "#999999",
            "border_color": "#dddddd",
            "chart_bg": "#ffffff",
            "table_header_bg": "#333333",
            "table_hover_bg": "#f5f5f5",
            "tag_bg": "#f0f0f0",
            "tag_color": "#333333",
            "footer_bg": "#333333",
            "footer_text": "#ffffff",
            "font_family": "'Georgia', serif",
        },
    }
    return schemes.get(theme, schemes["light"])


def generate_header(title: str, description: Optional[str], metadata: Dict[str, Any]) -> str:
    """Generate HTML header section."""
    metadata_html = ""
    if metadata:
        items = []
        for key, value in metadata.items():
            if value:
                items.append(
                    f'<div class="metadata-item"><span class="metadata-label">{key}:</span> {value}</div>'
                )
        if items:
            metadata_html = '<div class="metadata">' + "".join(items) + '</div>'

    desc_html = f'<p class="subtitle">{description}</p>' if description else ""

    return f"""
    <header>
        <h1>{title}</h1>
        {desc_html}
        {metadata_html}
    </header>
    """


def generate_navigation(sections: List[str]) -> str:
    """Generate navigation section."""
    nav_items = "".join([f'<li><a href="#{section}">{section.title()}</a></li>' for section in sections])
    return f"""
    <nav>
        <ul>
            {nav_items}
        </ul>
    </nav>
    """


def generate_section_placeholder(section_name: str) -> str:
    """Generate placeholder content for a report section."""
    section_id = section_name.lower()

    if section_id == "summary":
        return f"""
    <section id="{section_id}" class="section">
        <h2>Summary</h2>
        <p>This section provides an overview of the analysis results and key findings.</p>
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-label">Status</div>
                <div class="metric-value"><span class="status-badge status-success">Complete</span></div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Processing Time</div>
                <div class="metric-value">2<span class="metric-unit">h 15m</span></div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Data Points</div>
                <div class="metric-value">10,240</div>
            </div>
        </div>
    </section>
    """

    elif section_id == "metrics":
        return f"""
    <section id="{section_id}" class="section">
        <h2>Analysis Metrics</h2>
        <p>Quantitative measurements and key performance indicators.</p>
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-label">Metric One</div>
                <div class="metric-value">0.92</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Metric Two</div>
                <div class="metric-value">87.5<span class="metric-unit">%</span></div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Metric Three</div>
                <div class="metric-value">156<span class="metric-unit">ms</span></div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Metric Four</div>
                <div class="metric-value">p &lt; 0.001</div>
            </div>
        </div>
    </section>
    """

    elif section_id == "visualizations":
        return f"""
    <section id="{section_id}" class="section">
        <h2>Visualizations</h2>
        <p>Graphical representations of analysis results and trends.</p>
        <div class="visualization">
            <p style="color: #999; font-size: 1.2em; padding: 40px;">
                [Chart/Graph/Plot Placeholder]
            </p>
        </div>
        <div class="visualization">
            <p style="color: #999; font-size: 1.2em; padding: 40px;">
                [Visualization Placeholder]
            </p>
        </div>
    </section>
    """

    elif section_id == "quality":
        return f"""
    <section id="{section_id}" class="section">
        <h2>Quality Assessment</h2>
        <p>Data quality evaluation and validation results.</p>
        <table>
            <thead>
                <tr>
                    <th>Check</th>
                    <th>Result</th>
                    <th>Details</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Data Completeness</td>
                    <td><span class="status-badge status-success">Pass</span></td>
                    <td>100% of expected data present</td>
                </tr>
                <tr>
                    <td>Value Range Validation</td>
                    <td><span class="status-badge status-success">Pass</span></td>
                    <td>All values within expected ranges</td>
                </tr>
                <tr>
                    <td>Format Compliance</td>
                    <td><span class="status-badge status-warning">Warning</span></td>
                    <td>Minor formatting inconsistencies detected</td>
                </tr>
            </tbody>
        </table>
    </section>
    """

    elif section_id == "metadata":
        return f"""
    <section id="{section_id}" class="section">
        <h2>Metadata</h2>
        <p>Information about the analysis execution and configuration.</p>
        <table>
            <thead>
                <tr>
                    <th>Parameter</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Generated Date</td>
                    <td>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</td>
                </tr>
                <tr>
                    <td>Generator Version</td>
                    <td>1.0.0</td>
                </tr>
                <tr>
                    <td>Input Source</td>
                    <td>Analysis output directory</td>
                </tr>
                <tr>
                    <td>Configuration</td>
                    <td>Default template</td>
                </tr>
            </tbody>
        </table>
    </section>
    """

    return f""


def generate_footer(tags: Optional[List[str]] = None) -> str:
    """Generate HTML footer section."""
    tags_html = ""
    if tags:
        tag_elements = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
        tags_html = f"""
        <p>
            <strong>Tags:</strong><br>
            {tag_elements}
        </p>
        """

    return f"""
    <footer>
        {tags_html}
        <p>&copy; {datetime.now().year} Analysis Report. All rights reserved.</p>
        <div class="footer-links">
            <a href="#">Documentation</a>
            <a href="#">Report Issue</a>
            <a href="#">Contact Support</a>
        </div>
    </footer>
    """


def generate_html_report(
    title: str,
    description: Optional[str] = None,
    sections: Optional[List[str]] = None,
    theme: str = "light",
    author: Optional[str] = None,
    tags: Optional[List[str]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    custom_colors: Optional[Dict[str, str]] = None,
) -> str:
    """
    Generate complete HTML report.

    Args:
        title: Report title
        description: Report description
        sections: List of sections to include
        theme: Color theme (light, dark, minimal)
        author: Report author
        tags: List of report tags
        metadata: Dictionary of metadata key-value pairs
        custom_colors: Custom color overrides

    Returns:
        Complete HTML document as string
    """
    if sections is None:
        sections = ["summary", "metrics", "visualizations"]

    if metadata is None:
        metadata = {}

    if author:
        metadata["Author"] = author

    # Build color scheme
    colors = build_color_scheme(theme)
    if custom_colors:
        colors.update(custom_colors)

    # Generate CSS
    css_content = DEFAULT_CSS.format(**colors)

    # Generate sections
    header_html = generate_header(title, description, metadata)
    navigation_html = generate_navigation(sections)
    main_content_html = "".join([generate_section_placeholder(section) for section in sections])
    footer_html = generate_footer(tags)

    # Build Javascript placeholder
    javascript_content = """
    document.addEventListener('DOMContentLoaded', function() {
        console.log('Report loaded successfully');
        // Add interactive features here
    });
    """

    # Render complete HTML
    html = HTML_TEMPLATE.format(
        title=title,
        author=author or "Analysis Pipeline",
        description=description or "Generated analysis report",
        css_content=css_content,
        header_html=header_html,
        navigation_html=navigation_html,
        main_content_html=main_content_html,
        footer_html=footer_html,
        javascript_content=javascript_content,
    )

    return html


def main():
    """Main entry point for report generator CLI."""
    parser = create_parser()
    args = parser.parse_args()

    # TODO: Implement main logic here

    try:
        print(f"{Colors.BOLD}{Colors.GREEN}Generating HTML Report...{Colors.END}")
        print(f"  Input: {args.input_dir}")
        print(f"  Output: {args.output_file}")
        print(f"  Theme: {args.theme}")

        # Generate report
        report_html = generate_html_report(
            title=args.title,
            description=args.description,
            sections=args.sections or ["summary", "metrics", "visualizations"],
            theme=args.theme,
            author=args.author,
            tags=args.tags,
        )

        # Write report
        args.output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(report_html)

        print(f"{Colors.GREEN}✓ Report generated successfully{Colors.END}")
        print(f"  Location: {args.output_file}")

    except KeyboardInterrupt:
        print(f"{Colors.YELLOW}Interrupted by user{Colors.END}", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"{Colors.RED}Error: {e}{Colors.END}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
