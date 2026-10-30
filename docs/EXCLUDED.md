# 제외한 후보와 이유

아래 후보를 공식적으로 금지된 스킬이라고 판정한 것은 아니다. 제한된 환경에서 원문 예시를 그대로 따라 하다가 범위를 벗어날 가능성을 줄이기 위해 이번 보관 목록에서 제외했다. 일부는 규정과 무관하게 의존성·버전 고정·운영상의 이유로 제외했다.

| 후보 | 확인한 내용 | 이번 목록의 판단 |
| --- | --- | --- |
| `frontend-design` · anthropics/skills | 화면 스크린샷으로 자체 검토하는 권고 | 캡처를 쓰지 않는 구성으로 한정하기 위해 제외 |
| `accessibility-compliance` · wshobson/agents | 자동 접근성 검사 도구·별도 보조 도구를 통한 검증 권고 | 코드 검토·내부 미리보기 직접 확인으로 범위를 좁히기 위해 제외 |
| `python-testing-patterns` · wshobson/agents | 참고 문서에 Codecov로 커버리지를 업로드하는 원격 CI 예제 | 테스트 결과 외부 전송 예제의 재사용 가능성을 줄이기 위해 제외 |
| `python-error-handling` · wshobson/agents | 참고 문서에 예시 외부 URL로 파일을 올리는 코드 | 일반 오류 처리 스킬로 대체 |
| `design-system-patterns` · wshobson/agents | Figma 동기화·CI 파이프라인·Storybook 연계 권고 | 외부 서비스 설정 없이 쓸 코드 중심 스킬로 대체 |
| `responsive-design` · wshobson/agents | 실제 기기에서 테스트하라는 권고 | 별도 기기를 쓰지 않는 검증 흐름으로 한정하기 위해 제외 |
| `web-design-guidelines` · vercel-labs/agent-skills | 실행 시 외부 지침의 최신본을 다시 가져오는 구조 | 같은 내용을 고정 검토하기 어렵고 선택 폴더의 라이선스 고지도 불충분해 제외 |
| `writing-plans` · obra/superpowers | 별도 worktree·하위 에이전트 실행 스킬과 이어지는 절차 | 추가 실행 체계를 도입하지 않고 일반 작업 순서 문서로 정리 |

검토한 원본:

- [anthropics/skills — frontend-design](https://github.com/anthropics/skills/tree/ca45fc496a3436251f191354091d557da31c15b5/skills/frontend-design)
- [wshobson/agents — UI skills](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/ui-design/skills)
- [wshobson/agents — Python skills](https://github.com/wshobson/agents/tree/0874a27b17a22e2b7c2e2bcd725768e0803cad06/plugins/python-development/skills)
- [vercel-labs/agent-skills — web-design-guidelines](https://github.com/vercel-labs/agent-skills/tree/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/web-design-guidelines)
- [obra/superpowers — writing-plans](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/writing-plans)

수록된 TDD 스킬의 엄격한 재작성 지침, SQL 스킬의 PostgreSQL 전제, Tailwind·React의 버전 전제는 [SKILLS.md](SKILLS.md)에 별도로 표시했다. 선택적 예시가 남아 있다는 이유로 추가 도구를 자동 설치하거나 외부 연결을 허용하지 않는다.
