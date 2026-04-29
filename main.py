import argparse
import logging
from agent.compliance_agent import ComplianceAgent
from utils.document_parser import DocumentParser

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="Financial Compliance Agent")
    parser.add_argument('--contract', type=str, required=True, help="Path to the contract file (PDF/Word)")
    args = parser.parse_args()

    logging.info(f"Starting compliance check for: {args.contract}")

    # 1. 解析合同
    parser = DocumentParser()
    contract_text = parser.parse(args.contract)
    logging.info("Contract parsing completed.")

    # 2. 初始化 Agent
    agent = ComplianceAgent()

    # 3. 执行合规巡检
    logging.info("Agent is analyzing the contract...")
    report = agent.analyze(contract_text)

    # 4. 输出报告
    logging.info("Analysis completed. Generating report...")
    print("\n--- Compliance Report ---")
    print(report)
    print("-------------------------\n")

if __name__ == "__main__":
    main()
