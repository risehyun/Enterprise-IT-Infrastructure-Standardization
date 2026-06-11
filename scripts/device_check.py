import platform

# 사내 표준 보안 정책 설정 (Baseline)
REQUIRED_OS_WINDOWS = "10.0.19045" # Windows 10 22H2 이상
REQUIRED_OS_MAC = "13.0.0"         # macOS Ventura 이상

def check_compliance(device_info):
    """
    단말기의 보안 상태를 검사하여 사내망 접근 허용 여부를 반환합니다.
    """
    print(f"🔍 [{device_info['asset_tag']}] 단말기 보안 검증을 시작합니다...")
    
    is_compliant = True
    reasons = []

    # 1. 디스크 암호화 검사
    if not device_info.get("is_encrypted"):
        is_compliant = False
        reasons.append("디스크 암호화(BitLocker/FileVault)가 비활성화되어 있습니다.")

    # 2. EDR(백신) 구동 상태 검사
    if not device_info.get("edr_active"):
        is_compliant = False
        reasons.append("EDR(보안 백신) 프로세스가 실행 중이지 않습니다.")

    # 3. OS 버전 검사
    os_type = device_info.get("os_type")
    os_version = device_info.get("os_version")
    
    if os_type == "Windows" and os_version < REQUIRED_OS_WINDOWS:
        is_compliant = False
        reasons.append(f"OS 버전이 낮습니다. (현재: {os_version}, 권장: {REQUIRED_OS_WINDOWS} 이상)")
    elif os_type == "macOS" and os_version < REQUIRED_OS_MAC:
        is_compliant = False
        reasons.append(f"OS 버전이 낮습니다. (현재: {os_version}, 권장: {REQUIRED_OS_MAC} 이상)")

    # 최종 결과 출력
    if is_compliant:
        print("   ✅ [Pass] 모든 보안 정책을 준수합니다. 사내 표준망(Company-Corp) 접근을 허용합니다.")
    else:
        print("   ❌ [Fail] 보안 정책 미준수(Non-Compliant) 단말입니다. 사내망 접근을 차단합니다.")
        for reason in reasons:
            print(f"      - {reason}")
    print("-" * 60)

if __name__ == "__main__":
    # 테스트를 위한 가상의 단말기 데이터들
    mock_devices = [
        {
            "asset_tag": "AST-PC-26001",
            "os_type": "macOS",
            "os_version": "14.4.1",
            "is_encrypted": True,
            "edr_active": True
        },
        {
            "asset_tag": "AST-PC-26002",
            "os_type": "Windows",
            "os_version": "10.0.15063", # 하위 버전 가정
            "is_encrypted": True,
            "edr_active": False # EDR 비활성화 가정
        }
    ]
    
    print("📋 [엔드포인트 Compliance 점검 시뮬레이션]\n")
    for device in mock_devices:
        check_compliance(device)