import csv
import os

# 사내 표준 인프라 설정
DOMAIN = "@company.com"
DEFAULT_PASSWORD = "InitPassword123!" # 초기 임시 비밀번호

def assign_okta_group(role):
    """
    직무(Role)에 따라 사내 중앙 계정(SSO) 그룹 및 권한을 자동 할당합니다.
    """
    groups = ["공통_Google_Workspace", "공통_Slack", "공통_AI_Chatbot"]
    
    if "개발" in role or "엔지니어" in role:
        groups.extend(["개발_GitHub_Access", "개발_AWS_Dev", "라이선스_JetBrains"])
    elif "디자이너" in role:
        groups.extend(["디자인_Adobe_CC"])
        
    return groups

def process_new_hires(csv_file_path):
    """
    HR CSV 파일을 읽어 계정을 셋업하는 메인 함수입니다.
    """
    print(f"[{csv_file_path}] 데이터를 읽어 계정 셋업을 시작합니다...\n")
    print("-" * 50)
    
    if not os.path.exists(csv_file_path):
        print(f"[오류] 파일을 찾을 수 없습니다: {csv_file_path}")
        return

    try:
        with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                name = row.get('Name', 'Unknown')
                name_eng = row.get('Name_Eng', 'Unknown')
                department = row.get('Department', 'Unknown')
                role = row.get('Role', 'Unknown')
                
                # 1. 사내 이메일 계정 생성
                email = f"{name_eng}{DOMAIN}"
                
                # 2. 권한 그룹 할당
                assigned_groups = assign_okta_group(role)
                
                # 결과 출력 (실제 운영 환경에서는 하단 영역에서 IAM API 호출을 진행하도록 연계)
                print(f"✅ [계정 생성 완료] {name} ({department} / {role})")
                print(f"   - 사내 이메일 : {email}")
                print(f"   - 임시 패스워드 : {DEFAULT_PASSWORD}")
                print(f"   - 할당된 권한 그룹 : {assigned_groups}")
                print("-" * 50)
                
        print("\n✨ 모든 신규 입사자에 대한 IT 온보딩 계정 셋업이 완료되었습니다.")
        
    except Exception as e:
        print(f"[오류] 파일 처리 중 문제가 발생했습니다: {e}")

if __name__ == "__main__":
    # 테스트용 HR 신규 입사자 파일 지정
    test_csv = "hr_new_hires.csv"
    process_new_hires(test_csv)