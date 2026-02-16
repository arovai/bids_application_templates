"""
HTML Report Template - Usage Examples

This file demonstrates how the html_report_template can be used across
different analysis pipelines while maintaining consistent visual design.
"""

from pathlib import Path
from html_report_template import generate_html_report


# =============================================================================
# EXAMPLE 1: Generic Data Processing Pipeline
# =============================================================================

def example_generic_pipeline():
    """Basic usage for any analysis pipeline."""
    html = generate_html_report(
        title="Data Analysis Report",
        description="Summary of analysis results",
        sections=["summary", "metrics", "visualizations"],
        theme="light",
        author="Data Science Team",
        tags=["analysis", "report"],
        metadata={
            "Date": "2024-01-15",
            "Status": "Complete",
            "Records": "1,250",
        }
    )
    
    output_path = Path("example_generic_report.html")
    output_path.write_text(html)
    print(f"✓ Generic pipeline report: {output_path}")


# =============================================================================
# EXAMPLE 2: Neuroimaging fMRI Analysis
# =============================================================================

def example_fmri_analysis():
    """Report for fMRI preprocessing/analysis pipeline."""
    html = generate_html_report(
        title="fMRI Analysis Report",
        description="Functional MRI preprocessing and analysis results",
        sections=["summary", "metrics", "visualizations", "quality"],
        theme="dark",
        author="Neuroimaging Lab",
        tags=["fmri", "neuroimaging", "preprocessing", "qc"],
        metadata={
            "Pipeline": "fMRIPrep + Custom Analysis",
            "Subjects": "48",
            "Sessions": "1 (baseline)",
            "Timepoint": "2024-01-15",
            "Processing Time": "18.5 hours",
            "Output Space": "MNI152NLin2009cAsym",
        }
    )
    
    output_path = Path("example_fmri_report.html")
    output_path.write_text(html)
    print(f"✓ fMRI analysis report: {output_path}")


# =============================================================================
# EXAMPLE 3: Image Processing Quality Control
# =============================================================================

def example_image_qc():
    """Report for image quality control pipeline."""
    html = generate_html_report(
        title="Image Quality Assessment Report",
        description="Quality metrics and validation for image dataset",
        sections=["summary", "quality", "metadata"],
        theme="minimal",
        author="QC Pipeline",
        tags=["quality-control", "imaging", "validation"],
        metadata={
            "Dataset": "ImageSet_2024_Q1",
            "Total Images": "5,240",
            "Passed QC": "5,182 (98.9%)",
            "Failed": "58 (1.1%)",
            "Validation Date": "2024-01-15",
        }
    )
    
    output_path = Path("example_qc_report.html")
    output_path.write_text(html)
    print(f"✓ Quality control report: {output_path}")


# =============================================================================
# EXAMPLE 4: Statistical Analysis Report
# =============================================================================

def example_statistical_analysis():
    """Report for statistical analysis pipeline."""
    html = generate_html_report(
        title="Statistical Analysis Results",
        description="Results from group-level statistical analysis",
        sections=["summary", "metrics", "visualizations", "metadata"],
        theme="light",
        author="Statistics Team",
        tags=["statistics", "group-analysis", "fmri"],
        metadata={
            "Analysis Type": "Mixed-effects GLM",
            "N Subjects": "48",
            "N Runs": "120",
            "Contrasts": "8",
            "Threshold": "p < 0.001 (FWE corrected)",
            "Date": "2024-01-15",
        }
    )
    
    output_path = Path("example_stats_report.html")
    output_path.write_text(html)
    print(f"✓ Statistical analysis report: {output_path}")


# =============================================================================
# EXAMPLE 5: Machine Learning Model Evaluation
# =============================================================================

def example_ml_evaluation():
    """Report for machine learning model evaluation."""
    html = generate_html_report(
        title="Machine Learning Model Evaluation",
        description="Performance metrics and evaluation of predictive model",
        sections=["summary", "metrics", "visualizations", "quality"],
        theme="dark",
        author="ML Team",
        tags=["machine-learning", "model-evaluation", "classification"],
        metadata={
            "Model": "Random Forest Classifier",
            "Training Set": "3,000 samples",
            "Test Set": "1,000 samples",
            "Features": "45",
            "Accuracy": "0.945",
            "F1 Score": "0.923",
            "Date": "2024-01-15",
        }
    )
    
    output_path = Path("example_ml_report.html")
    output_path.write_text(html)
    print(f"✓ ML evaluation report: {output_path}")


# =============================================================================
# EXAMPLE 6: Genomic Analysis Report
# =============================================================================

def example_genomic_analysis():
    """Report for genomic/bioinformatics pipeline."""
    html = generate_html_report(
        title="Genomic Analysis Report",
        description="Results from next-generation sequencing analysis",
        sections=["summary", "metrics", "quality", "metadata"],
        theme="light",
        author="Bioinformatics Core",
        tags=["genomics", "sequencing", "ngs", "analysis"],
        metadata={
            "Study": "GEN_STUDY_2024",
            "Samples": "156",
            "Sequencing Type": "Whole Genome",
            "Coverage": "30x mean depth",
            "Total Reads": "2.1B",
            "Quality Pass": "98.5%",
            "Analysis Date": "2024-01-15",
        }
    )
    
    output_path = Path("example_genomic_report.html")
    output_path.write_text(html)
    print(f"✓ Genomic analysis report: {output_path}")


# =============================================================================
# EXAMPLE 7: Custom Theme with Branding
# =============================================================================

def example_custom_branding():
    """Example showing custom color scheme for organization branding."""
    # Custom colors matching organization branding
    custom_colors = {
        "header_bg_start": "#003366",  # Dark blue
        "header_bg_end": "#004499",    # Blue
        "accent_color": "#0066cc",     # Bright blue
        "tag_bg": "#e6f2ff",           # Light blue
        "tag_color": "#003366",        # Dark blue
    }
    
    html = generate_html_report(
        title="Branded Analysis Report",
        description="Report generated using organization branding",
        sections=["summary", "metrics", "visualizations"],
        theme="light",
        author="Organization Name",
        tags=["branded", "organization"],
        metadata={
            "Organization": "Acme Research Institute",
            "Department": "Data Science",
            "Project": "2024 Research Initiative",
        },
        custom_colors=custom_colors,
    )
    
    output_path = Path("example_branded_report.html")
    output_path.write_text(html)
    print(f"✓ Branded report (custom colors): {output_path}")


# =============================================================================
# EXAMPLE 8: Minimal Report with Few Sections
# =============================================================================

def example_minimal_report():
    """Minimal report with just summary and metrics."""
    html = generate_html_report(
        title="Quick Analysis Summary",
        description="Fast overview of key results",
        sections=["summary", "metrics"],
        theme="minimal",
        author="Quick Report",
        tags=["summary"],
        metadata={
            "Run Time": "2 hours",
            "Status": "Success",
        }
    )
    
    output_path = Path("example_minimal_report.html")
    output_path.write_text(html)
    print(f"✓ Minimal report: {output_path}")


# =============================================================================
# EXAMPLE 9: Comprehensive Report with All Sections
# =============================================================================

def example_comprehensive_report():
    """Report with all available sections for complete documentation."""
    html = generate_html_report(
        title="Comprehensive Analysis Report",
        description="Complete analysis with all sections and detailed documentation",
        sections=["summary", "metrics", "visualizations", "quality", "metadata"],
        theme="light",
        author="Analysis Team",
        tags=["comprehensive", "complete", "documentation"],
        metadata={
            "Project": "Large-scale Analysis",
            "Subjects": "500",
            "Total Data Points": "125,000",
            "Analysis Phases": "5",
            "Duration": "72 hours",
            "Completion": "2024-01-15 16:45 UTC",
        }
    )
    
    output_path = Path("example_comprehensive_report.html")
    output_path.write_text(html)
    print(f"✓ Comprehensive report: {output_path}")


# =============================================================================
# EXAMPLE 10: Dark Theme for Presentation
# =============================================================================

def example_presentation_theme():
    """Report optimized for presentation with dark theme."""
    html = generate_html_report(
        title="Research Findings Overview",
        description="Key results from recent study - optimized for presentation",
        sections=["summary", "metrics", "visualizations"],
        theme="dark",
        author="Research Team",
        tags=["presentation", "findings", "research"],
        metadata={
            "Study": "2024 Clinical Trial",
            "Duration": "6 months",
            "Participants": "250",
            "Primary Outcome": "Significant improvement",
        }
    )
    
    output_path = Path("example_presentation_report.html")
    output_path.write_text(html)
    print(f"✓ Presentation report (dark theme): {output_path}")


# =============================================================================
# MAIN: Run all examples
# =============================================================================

def main():
    """Generate all example reports."""
    print("=" * 70)
    print("HTML Report Template - Generating Examples")
    print("=" * 70)
    print()
    
    examples = [
        ("Generic Pipeline", example_generic_pipeline),
        ("fMRI Analysis", example_fmri_analysis),
        ("Image Quality Control", example_image_qc),
        ("Statistical Analysis", example_statistical_analysis),
        ("ML Evaluation", example_ml_evaluation),
        ("Genomic Analysis", example_genomic_analysis),
        ("Custom Branding", example_custom_branding),
        ("Minimal Report", example_minimal_report),
        ("Comprehensive Report", example_comprehensive_report),
        ("Presentation Theme", example_presentation_theme),
    ]
    
    for name, example_func in examples:
        print(f"Generating: {name}")
        try:
            example_func()
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print()
    print("=" * 70)
    print("All example reports generated successfully!")
    print("Open the .html files in a web browser to view.")
    print("=" * 70)


if __name__ == "__main__":
    main()
