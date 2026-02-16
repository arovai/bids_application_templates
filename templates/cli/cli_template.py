"""
CLI Template: Pipeline-Agnostic Design Template for BIDS-based Analysis Tools

This template provides a standardized command-line interface design for BIDS-based
analysis pipelines. It demonstrates best practices for CLI organization, help text,
colored output, and argument parsing.

This is a design template, not a functional tool.
"""

import argparse
import sys
import textwrap
from pathlib import Path


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
    """Create command-line argument parser."""

    description = textwrap.dedent(f"""
    {Colors.BOLD}{Colors.GREEN}╔══════════════════════════════════════════════════════════════════════════════╗
    ║                     ANALYSIS PIPELINE v0.1.0                                   ║
    ║                  BIDS-based Analysis Tool Template                             ║
    ╚══════════════════════════════════════════════════════════════════════════════╝{Colors.END}

    {Colors.BOLD}Description:{Colors.END}
      This tool performs BIDS-compliant analysis on neuroimaging data. It processes
      preprocessed data and applies standardized workflows to produce analysis-ready
      outputs that conform to BIDS derivative standards.

    {Colors.BOLD}Workflow:{Colors.END}
      1. Discover input data from BIDS dataset structure
      2. Validate data integrity and consistency
      3. Configure analysis parameters
      4. Execute main processing pipeline
      5. Generate BIDS-compliant outputs with metadata
      6. Produce analysis reports and quality metrics
    """)

    epilog = textwrap.dedent(f"""
    {Colors.BOLD}{Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}
    {Colors.BOLD}EXAMPLES{Colors.END}
    {Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}

    {Colors.BOLD}Basic Usage:{Colors.END}

      {Colors.YELLOW}# Process all subjects with default settings{Colors.END}
      pipeline /data/bids /data/derivatives/output participant

      {Colors.YELLOW}# Process a specific subject{Colors.END}
      pipeline /data/bids /data/derivatives/output participant \\
          --participant-label 01

    {Colors.BOLD}Using Processing Strategies:{Colors.END}

      {Colors.YELLOW}# Use minimal analysis pipeline{Colors.END}
      pipeline /data/bids /data/output participant --strategy minimal

      {Colors.YELLOW}# Use advanced analysis pipeline{Colors.END}
      pipeline /data/bids /data/output participant --strategy advanced

      {Colors.YELLOW}# Use custom configuration{Colors.END}
      pipeline /data/bids /data/output participant --strategy custom --config config.yaml

    {Colors.BOLD}Specifying Input Derivatives:{Colors.END}

      {Colors.YELLOW}# When input derivatives are not in default location{Colors.END}
      pipeline /data/bids /data/output participant \\
          --derivatives preprocessed=/data/derivatives/preproc

    {Colors.BOLD}Temporal Processing:{Colors.END}

      {Colors.YELLOW}# Apply temporal filtering{Colors.END}
      pipeline /data/bids /data/output participant \\
          --strategy standard --low-freq 0.01 --high-freq 0.1

      {Colors.YELLOW}# Process a specific subset of data{Colors.END}
      pipeline /data/bids /data/output participant \\
          --task mytask --session 01 --space MNI

      {Colors.YELLOW}# Drop initial volumes and set minimum segment length{Colors.END}
      pipeline /data/bids /data/output participant \\
          --drop-initial 4 --min-segment-length 5

    {Colors.BOLD}{Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}
    {Colors.BOLD}ANALYSIS STRATEGIES{Colors.END}
    {Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}

      {Colors.CYAN}minimal{Colors.END}        Minimal analysis - basic preprocessing
      {Colors.CYAN}standard{Colors.END}       Standard analysis - recommended for most studies
      {Colors.CYAN}advanced{Colors.END}       Advanced analysis - includes all processing options
      {Colors.CYAN}custom{Colors.END}         Custom analysis - requires --config file

    {Colors.BOLD}Note:{Colors.END} Strategy selection affects which processing modules are
    executed and their parameter defaults.

    {Colors.BOLD}{Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}
    {Colors.BOLD}MORE INFORMATION{Colors.END}
    {Colors.GREEN}═══════════════════════════════════════════════════════════════════════════════{Colors.END}

      Documentation:  https://github.com/example/pipeline
      Report Issues:  https://github.com/example/pipeline/issues
      Version:        0.1.0
    """)

    parser = argparse.ArgumentParser(
        prog="pipeline",
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
        help="Path to the BIDS dataset root directory.",
    )

    required.add_argument(
        "output_dir",
        type=Path,
        metavar="OUTPUT_DIR",
        help="Path to output directory for analysis derivatives.",
    )

    required.add_argument(
        "analysis_level",
        choices=["participant"],
        metavar="{participant}",
        help="Analysis level. Currently only 'participant' is supported.",
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
        version="pipeline 0.1.0",
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
    # DERIVATIVES OPTIONS
    # =========================================================================
    derivatives = parser.add_argument_group(
        f'{Colors.BOLD}Input Derivatives Options{Colors.END}'
    )

    derivatives.add_argument(
        "-d", "--derivatives",
        action="append",
        metavar="NAME=PATH",
        dest="derivatives",
        help="Specify location of BIDS derivatives. Format: name=path "
             "(e.g., preprocessed=/data/derivatives/preproc). Can be specified "
             "multiple times.",
    )

    # =========================================================================
    # BIDS ENTITY FILTERS
    # =========================================================================
    filters = parser.add_argument_group(
        f'{Colors.BOLD}BIDS Entity Filters{Colors.END}',
        "Filter which data to process based on BIDS entities."
    )

    filters.add_argument(
        "-p", "--participant-label",
        metavar="LABEL",
        dest="participant_label",
        nargs='+',
        help="Process one or more participants (without 'sub-' prefix).",
    )

    filters.add_argument(
        "-t", "--task",
        metavar="TASK",
        help="Process only this task (without 'task-' prefix).",
    )

    filters.add_argument(
        "-s", "--session",
        metavar="SESSION",
        help="Process only this session (without 'ses-' prefix).",
    )

    filters.add_argument(
        "-r", "--run",
        metavar="RUN",
        type=int,
        help="Process only this run number.",
    )

    filters.add_argument(
        "--space",
        metavar="SPACE",
        help="Process only data in this template space "
             "(e.g., 'MNI152NLin2009cAsym').",
    )

    filters.add_argument(
        "--label",
        metavar="STRING",
        help="Custom label added to all output filenames (BIDS entity).",
    )

    # =========================================================================
    # PROCESSING OPTIONS
    # =========================================================================
    processing = parser.add_argument_group(
        f'{Colors.BOLD}Processing Options{Colors.END}'
    )

    processing.add_argument(
        "--strategy",
        metavar="STRATEGY",
        choices=["minimal", "standard", "advanced", "custom"],
        help="Use a predefined analysis strategy. See ANALYSIS STRATEGIES "
             "section for details.",
    )

    processing.add_argument(
        "--low-freq",
        metavar="HZ",
        type=float,
        dest="low_freq",
        help="Low-frequency cutoff for temporal filtering in Hz.",
    )

    processing.add_argument(
        "--high-freq",
        metavar="HZ",
        type=float,
        dest="high_freq",
        help="High-frequency cutoff for temporal filtering in Hz.",
    )

    processing.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing output files.",
    )

    # =========================================================================
    # TEMPORAL PROCESSING OPTIONS
    # =========================================================================
    temporal = parser.add_argument_group(
        f'{Colors.BOLD}Temporal Processing Options{Colors.END}',
        "Options for temporal volume selection and segmentation."
    )

    temporal.add_argument(
        "--threshold",
        metavar="VALUE",
        type=float,
        dest="threshold",
        help="Quality threshold for volume selection. Volumes with values "
             "below this threshold will be excluded from analysis.",
    )

    temporal.add_argument(
        "--extend",
        metavar="N",
        type=int,
        dest="extend",
        default=0,
        help="Extend exclusion to N volumes before AND after flagged volumes "
             "(default: 0).",
    )

    temporal.add_argument(
        "--min-segment-length",
        metavar="N",
        type=int,
        dest="min_segment_length",
        default=0,
        help="Minimum contiguous segment length to retain after volume "
             "exclusion. Segments shorter than this will be removed. "
             "Requires --threshold.",
    )

    temporal.add_argument(
        "--drop-initial",
        metavar="N",
        type=int,
        dest="drop_initial",
        default=0,
        help="Number of initial volumes to drop (default: 0).",
    )

    return parser


def parse_derivatives_arg(derivatives_list: list) -> dict:
    """
    Parse derivatives arguments into dictionary.
    
    Expected format: name=path
    Example: fmriprep=/data/derivatives/fmriprep
    """
    if not derivatives_list:
        return {}

    derivatives_dict = {}
    for derivative_arg in derivatives_list:
        if "=" not in derivative_arg:
            raise ValueError(
                f"Invalid derivatives argument: {derivative_arg}. "
                f"Expected format: name=path (e.g., preprocessed=/path/to/data)"
            )
        name, path = derivative_arg.split("=", 1)
        derivatives_dict[name] = Path(path)

    return derivatives_dict


def main():
    """Main entry point for CLI."""
    parser = create_parser()
    args = parser.parse_args()

    # TODO: Implement main logic here

    # Placeholder for logging setup
    # log_level = logging.DEBUG if args.verbose else logging.INFO
    # logger = setup_logging(log_level)

    try:
        # TODO: Build configuration from args and config file
        # config = _build_config(args, logger)

        # Parse derivatives
        derivatives = parse_derivatives_arg(args.derivatives) if args.derivatives else None

        if args.analysis_level == "participant":
            # TODO: Import and run main analysis pipeline
            # run_analysis_pipeline(
            #     input_dir=args.input_dir,
            #     output_dir=args.output_dir,
            #     config=config,
            #     derivatives=derivatives,
            #     logger=logger,
            # )
            print(f"Analysis pipeline would run here")
            print(f"  Input: {args.input_dir}")
            print(f"  Output: {args.output_dir}")
            print(f"  Level: {args.analysis_level}")
        else:
            print(f"Unknown analysis level: {args.analysis_level}", file=sys.stderr)
            sys.exit(1)

    except KeyboardInterrupt:
        print("Interrupted by user", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
