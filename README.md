# Vibe Coding Skill Kit

공개 스킬 10개를 상황별로 모아 둔 준비용 저장소입니다. 기존 스킬 원문을 보관하고, README 분석부터 제출까지의 작업 순서를 따로 정리했습니다.

이 저장소는 특정 시험의 공식 승인 목록이 아닙니다. 당일 규정과 과제 README가 먼저이며, 공개 스킬도 실제 수행 행동이 허용되는 범위에서만 사용합니다. 비공개 안내 PDF·실제 문제·답안·녹음·개인 키는 포함하지 않았습니다.

## 먼저 볼 문서

1. [사용 범위와 선별 기준](docs/USE_WITH_CONSTRAINTS.md)
2. [상황별 스킬 목록과 주의점](docs/SKILLS.md)
3. [전체 작업 순서](docs/WORKFLOW.md)
4. [구현 전 준비와 첫 프롬프트](docs/FIRST_PROMPT.md)
5. [제외한 후보와 이유](docs/EXCLUDED.md)

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
| 8 | Python 파일·DB 자원 관리 | [`python-resource-management`](catalog/python-resource-management/SKILL.md) | Python으로 파일·오디오·DB 연결·스트림을 다룰 때 |
| 9 | SQL 조회 개선 | [`sql-optimization-patterns`](catalog/sql-optimization-patterns/SKILL.md) | 실제 DB 조회가 느리거나 중복 조회가 확인됐을 때 |
| 10 | 키·입력·파일 보안 | [`security-best-practices`](catalog/security-best-practices/SKILL.md) | 명시적으로 서비스의 보안 점검을 요청할 때 |

## 어떻게 사용하는가

규정상 공개 저장소 다운로드가 허용된 환경에서, 제공된 AI에 아래 공개 주소를 알려 가져오게 합니다. 실제 문제나 결과물을 이 저장소로 보내지 않습니다.

```text
https://github.com/taehuni/vibe-coding-skill-kit
```

**Git Clone은 필수가 아닙니다.** 허용된 다운로드 경로에서 ZIP이나 필요한 스킬 폴더만 받아도 됩니다. 파일 보관이 필요 없으면 제공 AI가 공개 원문을 읽어 참고할 수도 있습니다. 외부 브라우저 직접 접근이 제한된 환경에서는 플랫폼 안의 AI와 허용된 경로를 이용합니다. 개인 PC의 파일을 올리는 것과 공개 저장소에서 내려받는 것은 구분합니다.

저장소에는 자동 설치·자동 실행 과정이 없습니다. `catalog/`는 보관용이며 `.agents/skills/` 같은 자동 발견 폴더에 스킬 10개를 전부 넣어 두지 않았습니다. 처음에는 필요한 스킬의 `SKILL.md`를 제공된 AI에게 직접 읽게 해도 됩니다.

```text
먼저 이 저장소의 docs/USE_WITH_CONSTRAINTS.md와 docs/SKILLS.md를 읽어 줘.
현재 과제의 요구사항과 기술 구성을 기준으로 필요한 스킬만 골라 이유를 설명해 줘.
선택한 스킬의 SKILL.md와 해당 참고 파일만 읽고, 이번 작업에서 허용된 범위에 적용해 줘.
스킬의 다른 도구·예시·연관 스킬을 자동 설치하거나 실행하지 마.
```

정식 스킬 등록이 필요하면 제공 환경의 안내에 따라 선택한 폴더 전체와 라이선스를 복사합니다. `SKILL.md` 한 파일만 복사하면 참고 문서가 빠질 수 있습니다. 글로벌 설정·플러그인·MCP를 변경할 필요는 없습니다.

React 프로젝트가 아니면 React 스킬은 건너뜁니다. Tailwind v4가 아니면 Tailwind 스킬도 건너뜁니다. DB 성능 문제가 없다면 SQL 최적화도 생략합니다. 처음에는 완료 검증과 과제에 맞는 분야 스킬 한두 개로 충분합니다.

## 작업 순서 한눈에 보기

README 직접 읽기 → AI와 요구사항 대조 → 실행 환경 확인 → 현업자 질문 → 구현 범위·완료 기준 결정 → 스킬·라이브러리 선택 → 핵심 제약 먼저 검증 → 최소 흐름 완성 → 기능·화면 보완 → 테스트·직접 확인 → 설명·제출 준비 → 제출·접수 확인.

별도의 후속 문답이 있는 경우에는 그 단계의 규정을 따르며 본인이 직접 답변합니다.

## 원본 확인

각 스킬의 원본 커밋과 파일 해시는 [manifest.json](catalog/manifest.json)에 있습니다. 원본 내용은 수정하지 않았고, 필요한 저작권·라이선스 고지만 추가했습니다. 라이브러리나 별도 AI가 이 저장소를 받는 것만으로 설치되지는 않습니다.

Python 3.9 이상이 이미 제공된 환경에서는 다음 명령으로 원본 보존 상태를 확인할 수 있습니다. 네트워크 접속이나 추가 패키지 설치는 하지 않습니다.

```text
python tools/check_catalog.py
```

검사 성공은 파일 무결성 확인이며 시험 운영자의 사용 승인을 뜻하지 않습니다. 출처와 라이선스는 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)를 참고하세요.
