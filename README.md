# Demo : Claude Code for Amazon Bedrock

 이 깃 리포는 Aamzon Bedrock 을 연결해서 Claude Code 를 사용해서 만든 코드 입니다. 
실제 생성 내용은 여기 [영상:
Demo : Claude Code for Amazon Bedrock](https://youtu.be/Ra9YLsJO-Jg) 을 보시면 됩니다.

## Stock Agent

Strands Agents SDK와 Amazon Bedrock Claude를 활용한 주식 정보 AI Agent입니다.

## 기능

- 종목 심볼로 현재 주가 조회 (예: AAPL, TSLA, GOOGL)
- Claude 기반 자연어 대화

## 기술 스택

- [Strands Agents SDK](https://github.com/strands-agents/sdk-python) - Agent 프레임워크
- Amazon Bedrock Claude Sonnet - LLM
- yfinance - 주식 데이터 API

## 설치

### 사전 요구사항

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) 패키지 매니저
- AWS 자격 증명 설정 (`aws configure`)
- Amazon Bedrock 모델 액세스 활성화

### 설치 방법

```bash
cd setup
bash create_env.sh
```

## 사용법

```bash
uv run --project setup python agent.py
```

### 실행 예시

```
Stock Agent Ready! (type 'quit' to exit)
----------------------------------------

You: 애플 주가 알려줘

Agent: Apple Inc. (AAPL)의 현재 주가는 258.28 USD입니다.

You: quit
Goodbye!
```

## 프로젝트 구조

```
├── setup/
│   ├── create_env.sh      # 환경 설정 스크립트
│   └── pyproject.toml     # 의존성 설정
├── tools/
│   └── stock_tool.py      # 주가 조회 Tool
├── agent.py               # 메인 Agent
└── test_stock_tool.py     # Tool 테스트 스크립트
```

## 라이선스

MIT License
