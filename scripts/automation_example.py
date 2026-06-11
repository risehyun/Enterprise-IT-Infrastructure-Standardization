import csv
from datetime import datetime

# 기준일 설정
CURRENT_DATE = datetime.strptime("2026-05-25", "%Y-%m-%d")
IDLE_THRESHOLD_DAYS = 30 # 30일 이상 미사용 시 유휴로 간주

def detect_and_revoke_licenses(csv_path, output_path):
    """
    SaaS 사용 로그를 분석하여 30일 이상 미사용자 및 퇴사자의 라이선스 회수 목록을 생성합니다.
    """
    print("🔍 [SaaS 라이선스 최적화] 유휴 라이선스 탐지를 시작합니다...\n")
    print("-" * 60)
    
    revocation_list = []
    
    try:
        with open(csv_path, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                name = row['User_Name']
                email = row['Email']
                license_type = row['License_Type']
                status = row['Status']
                last_login_str = row['Last_Login_Date']
                
                # 1. 퇴사자 즉시 회수 판별
                if status == "퇴사":
                    revocation_list.append(f"[퇴사자] {name} ({email}) - {license_type} 회수 요망")
                    continue
                
                # 2. 장기 미사용자(30일 초과) 판별
                last_login_date = datetime.strptime(last_login_str, "%Y-%m-%d")
                days_idle = (CURRENT_DATE - last_login_date).days
                
                if days_idle > IDLE_THRESHOLD_DAYS:
                    revocation_list.append(f"[장기 미사용: {days_idle}일] {name} ({email}) - {license_type} 회수 요망")

        # 결과 출력 및 파일 저장
        if revocation_list:
            print(f"⚠️ 총 {len(revocation_list)}건의 회수 대상 라이선스가 발견되었습니다.")
            with open(output_path, mode='w', encoding='utf-8') as out_file:
                out_file.write("=== Enterprise SaaS 라이선스 회수 대상자 목록 ===\n")
                for item in revocation_list:
                    print(f"   -> {item}")
                    out_file.write(f"{item}\n")
            print("-" * 60)
            print(f"✅ 회수 대상 목록이 '{output_path}' 파일로 저장되었습니다. 부서장 통보 프로세스를 시작합니다.")
        else:
            print("✨ 유휴 또는 회수 대상 라이선스가 존재하지 않습니다. 인프라 비용이 최적화된 상태입니다.")
            
    except Exception as e:
        print(f"[오류] 데이터 분석 중 문제가 발생했습니다: {e}")

if __name__ == "__main__":
    log_csv = "saas_usage_log.csv"
    output_txt = "revoke_list.txt"
    detect_and_revoke_licenses(log_csv, output_txt)