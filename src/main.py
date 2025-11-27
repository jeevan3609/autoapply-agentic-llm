import argparse
from pathlib import Path

from src.agents.jd_parser import parse_job_description
from src.agents.resume_analyzer import analyze_resume
from src.agents.gap_recommender import recommend_improvements
from src.agents.application_generator import generate_application_materials

def read_text_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="AutoApply Agentic Workflow")
    parser.add_argument("--resume", type=str, required=True)
    parser.add_argument("--job", type=str, required=True)
    args = parser.parse_args()

    resume_text = read_text_file(Path(args.resume))
    job_text = read_text_file(Path(args.job))

    print("\n=== STEP 1: JD Parser ===")
    jd_summary = parse_job_description(job_text)
    print(jd_summary)

    print("\n=== STEP 2: Resume Analyzer ===")
    analysis = analyze_resume(resume_text, jd_summary)
    print(analysis)

    print("\n=== STEP 3: Recommendations ===")
    recs = recommend_improvements(analysis)
    print(recs)

    print("\n=== STEP 4: Application Materials ===")
    materials = generate_application_materials(resume_text, jd_summary, recs)
    print(materials)

    print("\nPipeline complete.\n")

if __name__ == "__main__":
    main()
