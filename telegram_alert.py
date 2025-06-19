import requests
from datetime import datetime

TELEGRAM_TOKEN = "7288688740:AAG_M_isdHNIvZJhNAUXk8oJcGqQ1zCfV4I"
CHAT_ID = "6949859996"

def send_telegram_alert(ip_address, score):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    message = (
        "[비정상 트래픽 탐지] \n"
        f"• IP 주소 : {ip_address}\n"
        f"• 탐지 스코어 : {score:.4f}\n"
        f"• 시각 : {timestamp}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("텔레그램 알림 전송 완료")
        else:
            print("전송 실패:", response.text)
    except Exception as e:
        print("텔레그램 오류:", e)
