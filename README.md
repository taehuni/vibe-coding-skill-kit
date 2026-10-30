# Vibe Coding Skill Kit

공개 스킬 10개를 상황별로 모아 둔 준비용 저장소입니다. 기존 스킬 원문과 과제 파악부터 제출까지의 공통 작업 순서를 정리했습니다. 언어 선택과 프로젝트 생성부터 시작하며, 결과물의 형태와 기술 구성은 실제 요구사항에 따라 정합니다.

## 먼저 볼 문서

1. [상황별 스킬 목록](docs/SKILLS.md)
2. [전체 작업 순서](docs/WORKFLOW.md)
3. [첫 프롬프트·기술 선택·프로젝트 생성](docs/FIRST_PROMPT.md)

## 상황별 공개 스킬

| 번호 | 상황 | 스킬 | 적용 시점 |
| --- | --- | --- | --- |
| 1 | 완료 검증 | [`verification-before-completion`](catalog/verification-before-completion/SKILL.md) | 검증 결과를 확인하고 완료 여부를 보고할 때 |
| 2 | 오류 원인 분석 | [`systematic-debugging`](catalog/systematic-debugging/SKILL.md) | 같은 오류를 반복해서 고치고 있거나 API·DB 연결이 실패할 때 |
| 3 | 핵심 로직 테스트 | [`test-driven-development`](catalog/test-driven-development/SKILL.md) | 새로 만드는 핵심 함수의 입력·출력을 먼저 확정할 때 |
| 4 | 화면·컴포넌트 정리 | [`tailwind-design-system`](catalog/tailwind-design-system/SKILL.md) | 이미 Tailwind v4를 쓰는 프로젝트에서 버튼·입력창·색상 규칙을 맞출 때 |
| 5 | React 구현·성능 | [`vercel-react-best-practices`](catalog/react-best-practices/SKILL.md) | 실제 과제 프로젝트가 React 또는 Next.js일 때 |
| 6 | 서버 API 설계 | [`api-design-principles`](catalog/api-design-principles/SKILL.md) | 화면과 서버 사이 요청·응답 형식을 정할 때 |
| 7 | 실패 상황 처리 | [`error-handling-patterns`](catalog/error-handling-patterns/SKILL.md) | 요청 실패·잘못된 입력·처리 중단을 처리할 때 |
| 8 | Python 파일·DB 자원 관리 | [`python-resource-management`](catalog/python-resource-management/SKILL.md) | Python으로 파일·DB 연결·스트림을 다룰 때 |
| 9 | SQL 조회 개선 | [`sql-optimization-patterns`](catalog/sql-optimization-patterns/SKILL.md) | 실제 DB 조회가 느리거나 중복 조회가 확인됐을 때 |
| 10 | 키·입력·파일 보안 | [`security-best-practices`](catalog/security-best-practices/SKILL.md) | 명시적으로 서비스의 보안 점검을 요청할 때 |

## 어떻게 사용하는가

제공된 AI에 아래 공개 주소를 알려 가져오게 합니다.

```text
https://github.com/taehuni/vibe-coding-skill-kit
```

**Git Clone은 필수가 아닙니다.** 제공 환경의 다운로드 기능으로 ZIP이나 필요한 스킬 폴더만 받아도 되고, AI가 공개 원문을 읽어 참고할 수도 있습니다.

저장소에는 자동 설치·자동 실행 과정이 없습니다. `catalog/`는 보관용이며 `.agents/skills/` 같은 자동 발견 폴더에 스킬 10개를 전부 넣어 두지 않았습니다. 처음에는 필요한 스킬의 `SKILL.md`를 제공된 AI에게 직접 읽게 해도 됩니다.

```text
먼저 이 저장소의 docs/SKILLS.md를 읽어 줘.
현재 과제의 요구사항과 기술 구성을 기준으로 필요한 스킬만 골라 이유를 설명해 줘.
선택한 스킬의 SKILL.md와 해당 참고 파일을 읽고 현재 작업에 적용해 줘.
```

정식 스킬 등록이 필요하면 제공 환경의 안내에 따라 선택한 폴더 전체와 라이선스를 복사합니다. `SKILL.md` 한 파일만 복사하면 참고 문서가 빠질 수 있습니다. 글로벌 설정·플러그인·MCP를 변경할 필요는 없습니다.

스킬 목록에서 현재 기술과 작업에 맞는 항목을 선택합니다. 처음에는 완료 검증과 과제에 맞는 분야 스킬 한두 개로 충분합니다.

## 작업 순서 한눈에 보기

과제 안내·README 직접 읽기 → AI와 요구사항·자료 분석 → 현재 상태·환경 확인 → 중요한 불확실성 질문 → 범위·성공 기준 결정 → 구현 구조·언어·도구 선택 → 프로젝트 생성·환경 준비·최소 실행 확인 → 핵심 가정 먼저 확인 → 작은 단위로 구현 → 전체 결과 검증 → 중요한 부족분 수정 → 재현 방법·설명 정리 → 제출·완료 확인.

과제에 맞는 단계만 필요한 깊이로 수행하고, 새 사실이나 검증 결과로 판단이 바뀌면 앞 단계로 돌아갑니다. 스킬은 필요한 경우에만 선택합니다.

별도의 후속 문답이 있는 경우에는 그 단계의 규정을 따르며 본인이 직접 답변합니다.

## 원본 확인

각 스킬의 원본 커밋과 파일 해시는 [manifest.json](catalog/manifest.json)에 있습니다. 원본 내용은 수정하지 않았고, 필요한 저작권·라이선스 고지만 추가했습니다. 라이브러리나 별도 AI가 이 저장소를 받는 것만으로 설치되지는 않습니다.

Python 3.9 이상이 이미 제공된 환경에서는 다음 명령으로 원본 보존 상태를 확인할 수 있습니다. 네트워크 접속이나 추가 패키지 설치는 하지 않습니다.

```text
python tools/check_catalog.py
```

출처와 라이선스는 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)를 참고하세요.
