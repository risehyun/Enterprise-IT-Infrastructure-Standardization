# [ITAM/ITSM] Zero Trust 기반 사내 IT인프라 표준화 및 운영 자동화 프로젝트

## 📌 프로젝트 기획 배경 및 개요
수백 대 규모의 엔드포인트 디바이스 현장 지원 업무를 수행하며, 수작업 중심의 자산 관리와 파편화된 IT 환경이 가져오는 운영의 비효율성을 경험했습니다. 
본 프로젝트는 이러한 현장의 페인 포인트(Pain Point)를 해결하기 위해, 기업의 IT 인프라를 '표준화된 정책(Policy)'으로 정의하고, 
이를 '파이썬(Python) 기반 스크립트'로 자동화하는 Zero Trust 운영 체계를 직접 설계한 결과물입니다.

단순한 기술 지원을 넘어, 신규 입사자 온보딩 자동화, 단말기 보안 컴플라이언스 통제, SaaS 유휴 라이선스 관리를 통한 비용 최적화(Cost Optimization)를 달성하는 것을 목표로 합니다.

---

## 📂 디렉토리 구조 및 산출물 안내

ITSM(IT 서비스 관리) 표준 프레임워크에 맞추어 정책 설계, 스크립트, 양식을 분리하여 구성했습니다.

### 1. docs/ (운영 설계 및 정책 문서)
- `onboarding_process.pdf`: 신규 입사자 온보딩 및 오프보딩 프로세스 설계 (RBAC 권한 모델 적용)
- `asset_management.pdf`: 엔드포인트 디바이스 및 IT 자산(SaaS 포함) 생애주기 관리 정책서
- `incident_response.pdf`: 장애 우선순위(SLA) 정의 및 보안 사고 대응(Troubleshooting) 가이드
- `it_policy_summary.pdf`: WPA2-Enterprise 기반 무선망 및 VPN Split Tunneling 접근 통제 방침

### 2. scripts/ (운영 자동화 파이썬 스크립트)
- `account_setup.py`: HR 신규 입사자 명단(CSV)을 파싱하여 사내 이메일 및 직무별 권한 그룹을 자동 할당하는 스크립트
- `device_check.py`: 단말기 OS 버전, EDR 활성화, 디스크 암호화 상태를 판별하여 사내망 접근을 인가하는 Zero Trust 검증 스크립트
- `automation_example.py`: SaaS 접속 로그를 분석하여 30일 이상 미접속한 유휴 라이선스를 탐지하고 회수 대상자 목록(txt)을 자동 추출하는 비용 최적화 스크립트

### 3. templates/ (양식 및 템플릿)
- `onboarding_checklist.md`: 신규 입사자 IT 환경 세팅 및 검수 체크리스트
- `it_request_form.md`: 사내 임직원 표준 IT 지원 요청 양식 (장애/일반 요청 분류)
- `asset_inventory.csv`: 사내 IT 자산 관리 대장 (샘플 데이터 포함)

---

## 🚀 기술 스택 및 실행 방법 (How to run)

본 프로젝트의 자동화 스크립트는 인프라 운영 환경의 종속성을 줄이기 위해, 
외부 라이브러리 설치 없이 기본 **Python 3.x** 내장 모듈만으로 완벽하게 동작하도록 설계되었습니다.

1. 저장소를 클론한 후 `scripts/` 폴더로 이동합니다.
    ```bash
    git clone [Repository URL]
    cd scripts
    ```
    
2. **계정 생성 자동화 실행** (가상의 HR CSV 파일 로드)
    ```bash
    python account_setup.py
    ```
    
3. **단말기 보안 상태 검증 실행** (가상의 디바이스 Mock Data 검사)
    ```bash
    python device_check.py
    ```
    
4. **유휴 SaaS 라이선스 탐지 및 회수 스크립트 실행**
    ```bash
    python automation_example.py
    ```
    *(실행 시 동일 디렉토리에 `revoke_list.txt` 파일이 자동 생성됩니다.)*
