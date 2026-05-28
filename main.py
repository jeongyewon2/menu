import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime


class MealScraper:
    URL = "https://dorm.hanbat.ac.kr/sub-0205"

    @staticmethod
    def fetch_meal_data():
        response = requests.get(MealScraper.URL, timeout=10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.select_one(".diet table")
        if not table:
            raise ValueError("식단표 테이블을 찾을 수 없습니다.")
        rows = table.select("tbody tr")
        if not rows:
            raise ValueError("식단 데이터가 없습니다.")
        day_map = {
            "월": "월요일", "화": "화요일", "수": "수요일",
            "목": "목요일", "금": "금요일", "토": "토요일", "일": "일요일",
        }
        meal_data = {}
        for row in rows:
            day_cell = row.find("th")
            if not day_cell:
                continue
            day_text = day_cell.get_text(strip=True)
            match = re.search(r"\(([월화수목금토일])\)", day_text)
            if not match:
                continue
            day_key = day_map.get(match.group(1))
            if not day_key:
                continue
            cells = row.find_all("td")
            if len(cells) < 3:
                continue
            meal_data[day_key] = {
                "아침": cells[0].get_text("\n", strip=True),
                "점심": cells[1].get_text("\n", strip=True),
                "저녁": cells[2].get_text("\n", strip=True),
            }
        return meal_data

    @staticmethod
    def get_today_korean():
        weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        return weekdays[datetime.today().weekday()]


class MealApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("한밭대학교 학생생활관 식단표")
        self.window.geometry("650x700")
        self.window.resizable(True, True)
        self.meal_data = {}
        self._setup_ui()
        self._load_data()

    def _setup_ui(self):
        title = tk.Label(
            self.window,
            text="한밭대학교 학생생활관 식단표",
            font=("맑은 고딕", 16, "bold"),
        )
        title.pack(pady=(15, 5))
        frame = tk.Frame(self.window)
        frame.pack(pady=5)
        tk.Label(frame, text="요일 선택:", font=("맑은 고딕", 11)).pack(
            side=tk.LEFT, padx=(0, 5)
        )
        self.day_var = tk.StringVar()
        self.combo = ttk.Combobox(
            frame,
            textvariable=self.day_var,
            state="readonly",
            width=12,
            font=("맑은 고딕", 11),
        )
        days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        self.combo["values"] = days
        self.combo.pack(side=tk.LEFT)
        self.combo.bind("<<ComboboxSelected>>", self._on_day_change)
        self.refresh_btn = tk.Button(
            frame,
            text="새로고침",
            font=("맑은 고딕", 10),
            command=self._load_data,
        )
        self.refresh_btn.pack(side=tk.LEFT, padx=(10, 0))
        text_frame = tk.Frame(self.window)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(5, 15))
        self.text = tk.Text(
            text_frame,
            font=("맑은 고딕", 11),
            wrap=tk.WORD,
            state=tk.DISABLED,
            bg="#f9f9f9",
            relief=tk.SUNKEN,
            bd=2,
        )
        scrollbar = tk.Scrollbar(text_frame, command=self.text.yview)
        self.text.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(fill=tk.BOTH, expand=True)

    def _load_data(self):
        try:
            data = MealScraper.fetch_meal_data()
            if not data:
                raise ValueError("식단 데이터를 불러올 수 없습니다.")
            self.meal_data = data
            days = self.combo["values"]
            available = [d for d in days if d in data]
            if not available:
                raise ValueError("식단 데이터에 유효한 요일 정보가 없습니다.")
            self.combo["values"] = available
            today = MealScraper.get_today_korean()
            if today in available:
                self.day_var.set(today)
            else:
                self.day_var.set(available[0])
            self._display_menu()
        except requests.RequestException as e:
            messagebox.showerror(
                "네트워크 오류",
                f"인터넷 연결을 확인해주세요.\n오류: {e}",
            )
        except ValueError as e:
            messagebox.showwarning("데이터 없음", str(e))
        except Exception as e:
            messagebox.showerror(
                "오류",
                f"예상치 못한 오류가 발생했습니다.\n{e}",
            )

    def _on_day_change(self, event=None):
        self._display_menu()

    def _display_menu(self):
        day = self.day_var.get()
        if not day or day not in self.meal_data:
            self.text.config(state=tk.NORMAL)
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, "선택한 요일의 식단 정보가 없습니다.")
            self.text.config(state=tk.DISABLED)
            return
        meals = self.meal_data[day]
        content = f"  {day} 식단표\n"
        content += "\u2500" * 40 + "\n\n"
        for meal_time in ["아침", "점심", "저녁"]:
            content += f"  [{meal_time}]\n"
            menu_text = meals.get(meal_time, "").strip()
            if menu_text:
                for item in menu_text.split("\n"):
                    if item.strip():
                        content += f"    \u2022 {item.strip()}\n"
            else:
                content += "    (제공되는 메뉴가 없습니다)\n"
            content += "\n"
        self.text.config(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, content)
        self.text.config(state=tk.DISABLED)


if __name__ == "__main__":
    app = MealApp()
    app.window.mainloop()
