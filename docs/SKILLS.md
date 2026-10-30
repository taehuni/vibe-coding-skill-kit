# 상황별 공개 스킬

검토 기준일: 2026-10-30. 아래 설명은 고정된 원본 버전 기준입니다. 모든 스킬을 한 번에 적용하지 않습니다.

## 1. 완료 검증 — `verification-before-completion`

- **쓸 때:** 검증 결과를 확인하고 완료 여부를 보고할 때
- **얻는 것:** 테스트·빌드·요구사항 충족을 실제 결과와 대조한다.
- **주의할 점:** 커밋·PR 언급은 적용 시점을 설명하는 내용이다. 외부 Push나 PR 생성 지시로 해석하지 않는다.
- **사용 예:** `이번 작업 범위에서 완료 검증 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [obra/superpowers](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/verification-before-completion) · `2ce8aa15d05b`
- **보관본:** [SKILL.md](../catalog/verification-before-completion/SKILL.md) · MIT

## 2. 오류 원인 분석 — `systematic-debugging`

- **쓸 때:** 같은 오류를 반복해서 고치고 있거나 API·DB 연결이 실패할 때
- **얻는 것:** 재현 → 원인 조사 → 가설 하나 검증 → 수정 순서를 따른다.
- **주의할 점:** TDD·완료 검증 스킬을 함께 참조한다. 프로젝트 코드와 비밀값을 가린 로그만 조사한다. 동봉된 제작 이력·압박 테스트 시나리오는 실제 과제 지시가 아니다.
- **사용 예:** `이번 작업 범위에서 오류 원인 분석 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [obra/superpowers](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/systematic-debugging) · `2ce8aa15d05b`
- **보관본:** [SKILL.md](../catalog/systematic-debugging/SKILL.md) · MIT

## 3. 핵심 로직 테스트 — `test-driven-development`

- **쓸 때:** 새로 만드는 핵심 함수의 입력·출력을 먼저 확정할 때
- **얻는 것:** 실패하는 테스트를 먼저 만들고 최소 구현으로 통과시킨다.
- **주의할 점:** 원문의 삭제 후 재작성 지침이 강하다. 기존 제공 코드를 지우거나 전체 프로젝트에 소급 적용하지 않고, 새로 만드는 작은 로직에만 명시적으로 선택한다. 화면 자동 조작 테스트는 사용하지 않는다.
- **사용 예:** `이번 작업 범위에서 핵심 로직 테스트 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [obra/superpowers](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/test-driven-development) · `2ce8aa15d05b`
- **보관본:** [SKILL.md](../catalog/test-driven-development/SKILL.md) · MIT

## 4. 화면·컴포넌트 정리 — `tailwind-design-system`

- **쓸 때:** 이미 Tailwind v4를 쓰는 프로젝트에서 버튼·입력창·색상 규칙을 맞출 때
- **얻는 것:** 반복 UI, 상태, 간격과 색상을 코드로 정리한다.
- **주의할 점:** Tailwind v4 기준이고 일부 예시는 React 19를 전제로 한다. v3·React 18 프로젝트를 이 스킬 때문에 업그레이드하지 않는다. 필요한 예시의 패키지만 개별 검토한다.
- **사용 예:** `이번 작업 범위에서 화면·컴포넌트 정리 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [wshobson/agents](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/frontend-mobile-development/skills/tailwind-design-system) · `0874a27b17a2`
- **보관본:** [SKILL.md](../catalog/tailwind-design-system/SKILL.md) · MIT

## 5. React 구현·성능 — `vercel-react-best-practices`

- **쓸 때:** 실제 과제 프로젝트가 React 또는 Next.js일 때
- **얻는 것:** 불필요한 렌더링과 중복 요청, 순차 대기를 줄인다.
- **주의할 점:** 실제 스킬 이름은 vercel-react-best-practices다. 분석·추적 서비스 예시는 새 외부 서비스 도입 허가가 아니다. 외부 분석 SDK·원격 폰트·추가 API를 무조건 도입하지 않는다.
- **사용 예:** `이번 작업 범위에서 React 구현·성능 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/react-best-practices) · `1a2c79d4e6c4`
- **보관본:** [SKILL.md](../catalog/react-best-practices/SKILL.md) · MIT

## 6. 서버 API 설계 — `api-design-principles`

- **쓸 때:** 화면과 서버 사이 요청·응답 형식을 정할 때
- **얻는 것:** 입력값, 응답 형식, 오류 상태와 API 역할을 정한다.
- **주의할 점:** 작은 서비스에는 필요한 REST API만 사용한다. GraphQL·인증 서버·외부 API를 추가하라는 뜻이 아니다. assets의 서버 예제를 완성 서비스로 통째로 대체하지 않는다.
- **사용 예:** `이번 작업 범위에서 서버 API 설계 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [wshobson/agents](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/backend-development/skills/api-design-principles) · `0874a27b17a2`
- **보관본:** [SKILL.md](../catalog/api-design-principles/SKILL.md) · MIT

## 7. 실패 상황 처리 — `error-handling-patterns`

- **쓸 때:** 요청 실패·잘못된 입력·처리 중단을 처리할 때
- **얻는 것:** 오류 분류, 사용자 안내, 제한된 재시도와 자원 정리를 설계한다.
- **주의할 점:** 네트워크·결제 등의 코드는 설명용 예시다. 외부 서비스나 다른 AI로 우회하지 않는다. 실제 응답을 받지 않았는데 성공 결과를 만들어 보여주지 않는다.
- **사용 예:** `이번 작업 범위에서 실패 상황 처리 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [wshobson/agents](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/developer-essentials/skills/error-handling-patterns) · `0874a27b17a2`
- **보관본:** [SKILL.md](../catalog/error-handling-patterns/SKILL.md) · MIT

## 8. Python 파일·DB 자원 관리 — `python-resource-management`

- **쓸 때:** Python으로 파일·DB 연결·스트림을 다룰 때
- **얻는 것:** 처리 실패 때도 파일과 DB 연결을 닫고 임시 자원을 정리한다.
- **주의할 점:** PostgreSQL 드라이버 등의 예시는 현재 프로젝트의 기술에 맞게 선택한다. 처리 실패와 중단 시 자원 해제가 되는지도 확인한다.
- **사용 예:** `이번 작업 범위에서 Python 파일·DB 자원 관리 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [wshobson/agents](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/python-development/skills/python-resource-management) · `0874a27b17a2`
- **보관본:** [SKILL.md](../catalog/python-resource-management/SKILL.md) · MIT

## 9. SQL 조회 개선 — `sql-optimization-patterns`

- **쓸 때:** 실제 DB 조회가 느리거나 중복 조회가 확인됐을 때
- **얻는 것:** 쿼리 실행 계획과 인덱스를 확인한다.
- **주의할 점:** PostgreSQL 중심 예시다. SQLite에 PostgreSQL 문법을 그대로 적용하지 않는다. DB가 필요 없거나 성능 문제가 없으면 생략한다. 공용 DB 설정이나 관리자 설정은 변경하지 않는다.
- **사용 예:** `이번 작업 범위에서 SQL 조회 개선 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [wshobson/agents](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/developer-essentials/skills/sql-optimization-patterns) · `0874a27b17a2`
- **보관본:** [SKILL.md](../catalog/sql-optimization-patterns/SKILL.md) · MIT

## 10. 키·입력·파일 보안 — `security-best-practices`

- **쓸 때:** 명시적으로 서비스의 보안 점검을 요청할 때
- **얻는 것:** 키 노출, 입력 검증, 파일 처리와 기본 보안 설정을 점검한다.
- **주의할 점:** Python·JavaScript/TypeScript·Go용이다. 코드 검토용이며 침투 테스트·외부 업로드용이 아니다. 현재 프레임워크에 해당하는 참고 문서만 읽는다.
- **사용 예:** `이번 작업 범위에서 키·입력·파일 보안 지침을 읽고 필요한 부분을 적용해 줘.`
- **원본:** [openai/skills](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-best-practices) · `49f948faa925`
- **보관본:** [SKILL.md](../catalog/security-best-practices/SKILL.md) · Apache-2.0

## 과제 유형별 선택 예

| 실제 과제 상황 | 먼저 고려할 스킬 | 추가할 때 |
| --- | --- | --- |
| React 화면 | React 구현·성능 + 완료 검증 | Tailwind v4를 이미 쓰면 화면·컴포넌트 정리 |
| Python 서버·파일 처리 | API 설계 + Python 자원 관리 | 요청 실패가 있으면 실패 상황 처리 |
| DB를 사용하는 서비스 | API 설계 + 완료 검증 | 조회가 느릴 때만 SQL 조회 개선 |
| 원인을 모르는 오류 | 오류 원인 분석 | 재현 테스트 작성 시 TDD, 수정 후 완료 검증 |
| 키·파일·사용자 입력을 다루는 서비스 | 보안 점검을 명시적으로 요청 | 사용 중인 언어·프레임워크 참고 문서만 적용 |
| 데이터 변환·여러 파일 처리 | 과제 언어에 맞는 자원 관리·실패 처리 | 실제 처리 로직에 맞춰 테스트 추가 |

스킬은 AI가 작업할 때 참고하는 지침이고, 라이브러리는 구현에 사용하는 기능이다. 필요한 항목은 실제 과제의 기술 구성과 작업 내용에 따라 선택한다.
