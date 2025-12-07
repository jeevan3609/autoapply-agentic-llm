import argparse
from pathlib import Path

from src.agents.jd_parser import parse_job_description
from src.agents.resume_analyzer import analyze_resume
from src.agents.gap_recommender import recommend_gaps
from src.agents.application_generator import generate_application_materials


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="AutoApply agentic pipeline: JD + resume -> tailored materials"
    )
    parser.add_argument(
        "--resume",
        type=str,
        required=True,
        help="Path to resume text file",
    )
    parser.add_argument(
        "--job",
        type=str,
        required=True,
        help="Path to job description text file",
    )

    args = parser.parse_args()

    resume_path = Path(args.resume)
    job_path = Path(args.job)

    resume_text = read_text(resume_path)
    job_text = read_text(job_path)

    print("\n=== STEP 1: JD Parser ===")
    jd_summary = parse_job_description(job_text)
    print(jd_summary)

    print("\n=== STEP 2: Resume Analyzer ===")
    analysis = analyze_resume(jd_summary, resume_text)
    print(analysis)

    print("\n=== STEP 3: Recommendations ===")
    recommendations = recommend_gaps(analysis)
    print(recommendations)

    print("\n=== STEP 4: Application Materials ===")
    materials = generate_application_materials(jd_summary, resume_text, analysis)
    print(materials)

    print("\nPipeline complete.\n")


if __name__ == "__main__":
    main()
