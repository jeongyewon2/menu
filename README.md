# 한밭대학교 학생생활관 식단표 조회 프로그램

---

## 개요 (Abstract)

**한밭대학교 학생생활관 식단표 조회 프로그램**은 생활관 입주생이 매주 갱신되는 학생생활관 식단을 보다 편리하게 확인할 수 있도록 개발된 Python 기반 데스크톱 애플리케이션이다. 기존에는 웹브라우저를 통해 공식 홈페이지에 접속한 뒤 HTML 테이블을 직접 확인해야 했으나, 본 프로그램은 `requests`와 `BeautifulSoup`를 이용한 실시간 웹 스크래핑을 통해 식단 데이터를 자동으로 수집하고, Python 표준 GUI 라이브러리인 `tkinter`를 활용하여 직관적인 사용자 인터페이스로 제공한다. 이를 통해 반복적인 수동 조회의 불편함을 해소하고 신속한 식단 확인이 가능하도록 설계하였다.

---

## 주요 기능 (Key Features)

- **실시간 식단 크롤링** — 프로그램 실행 시 한밭대학교 학생생활관 공식 웹사이트(`dorm.hanbat.ac.kr`)에 접속하여 최신 주간 식단표를 실시간으로 불러온다.

- **오늘 요일 자동 인식** — 시스템 시계를 기반으로 현재 요일을 자동 감지하여, 사용자가 별도로 선택하지 않아도 오늘의 식단을 먼저 출력한다.

- **요일 선택 드롭다운** — 콤보박스(Combobox)를 통해 월요일부터 일요일까지 원하는 요일을 자유롭게 선택하며 식단을 조회할 수 있다.

- **견고한 예외 처리** — 네트워크 장애, 서버 타임아웃, 방학 기간으로 인한 데이터 부재 등 다양한 예외 상황을 `try-except`로 처리하여 프로그램이 비정상 종료되지 않도록 방지하며, `messagebox`를 통해 사용자에게 직관적인 안내 메시지를 제공한다.

- **가독성 높은 출력** — BeautifulSoup 파서로 모든 HTML 태그를 제거하고 불필요한 공백을 정규화하여, 아침/점심/저녁 구분 아래 항목별로 깔끔하게 정리된 텍스트를 출력한다.

---

## 시작하기 (Getting Started)

### 사전 요구사항 (Prerequisites)

- **Python 3.9 이상**이 시스템에 설치되어 있어야 한다.  
  [python.org](https://www.python.org/downloads/)에서 다운로드할 수 있다.
- 인터넷 연결이 필요하다 (식단 데이터 실시간 수집을 위함).
- Linux 사용자의 경우 tkinter 설치가 필요할 수 있다:
  ```bash
  sudo apt install python3-tk   # Ubuntu/Debian
  ```

### 설치 방법 (Installation & Setup)

1. **저장소 복제 또는 다운로드**

   ```bash
   git clone https://github.com/YOUR_USERNAME/hanbat-dorm-meal-viewer.git
   cd hanbat-dorm-meal-viewer
   ```

   > Git을 사용하지 않는 경우 GitHub에서 ZIP 파일을 다운로드하여 압축을 풀고 터미널에서 해당 디렉터리로 이동한다.

2. **가상 환경 생성 (권장)**

   ```bash
   python -m venv venv
   ```

   가상 환경 활성화:

   - **Windows (Command Prompt)**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS / Linux**
     ```bash
     source venv/bin/activate
     ```

3. **의존성 패키지 설치**

   ```bash
   pip install -r requirements.txt
   ```

   위 명령어로 `requests`(HTTP 클라이언트)와 `beautifulsoup4`(HTML 파서)가 최신 안정화 버전으로 설치된다.

### 실행 방법 (Run)

```bash
python main.py
```

**"한밭대학교 학생생활관 식단표"** 제목의 GUI 창이 열린다. 실행 즉시 오늘 요일에 해당하는 식단이 자동으로 표시되며, 드롭다운 메뉴로 다른 요일을 선택하거나 **"새로고침"** 버튼을 눌러 데이터를 다시 불러올 수 있다.
