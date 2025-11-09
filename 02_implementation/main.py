from agents.search_agent import SearchAgent
from agents.analysis_agent import AnalysisAgent
import logging
import platform
import psutil
import pkg_resources

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  
        logging.FileHandler("execution_log.txt", mode="a", encoding="utf-8")  # logs to file
    ]
)

def system_capabilities():
    """Log system capabilities and environment info."""
    logging.info("=== SYSTEM CAPABILITIES CHECK ===")
    try:
        logging.info(f"Python version: {platform.python_version()}")
        logging.info(f"Platform: {platform.system()} {platform.release()}")
        logging.info(f"CPU cores: {psutil.cpu_count(logical=True)}")
        mem = psutil.virtual_memory()
        logging.info(f"Memory: {round(mem.total / 1e9, 2)} GB total, {round(mem.available / 1e9, 2)} GB available")

        installed_packages = [f"{d.project_name}=={d.version}" for d in pkg_resources.working_set]
        logging.info(f"Installed packages ({len(installed_packages)}):")
        for pkg in sorted(installed_packages):
            logging.info(f" - {pkg}")
    except Exception as e:
        logging.exception(f"Failed to assess system capabilities: {e}")

def main():
    search_agent = SearchAgent()
    analysis_agent = AnalysisAgent()


    try:
        summary = search_agent.search_trends(input("Enter your search query: "))
        print("\n=== SUMMARY FROM WEB AGENT ===\n")
        logging.info(summary)

        analysis = analysis_agent.analyze_trends(summary)
        print("\n=== ANALYSIS FROM ANALYSIS AGENT ===\n")
        logging.info(analysis)

        logging.info("Analysis completed successfully.")
    except:
        logging.exception(f"Error while processing query")

if __name__ == "__main__":
    main()