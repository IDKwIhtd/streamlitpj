import datetime
import streamlit as st

class CuteJournal:
    # 클래스 변수
    journal_name = "Daily Dose of Cuteness"

    def __init__(self):
        # 인스턴스 변수
        self.entries = []

    def add_entry(self, title, content):
        """
        새로운 일기 추가
        :param title: 일기 제목
        :param content: 일기 내용
        """
        entry = {
            "id": self.generate_id(),
            "title": str(title),
            "content": str(content),
            "created_at": datetime.datetime.now()
        }
        self.entries.append(entry)
        print(f"Added a new entry: {title}")

    def delete_entry_by_id(self, entry_id):
        """
        ID로 일기 삭제
        :param entry_id: 삭제할 일기의 ID (int)
        """
        self.entries = [entry for entry in self.entries if entry["id"] != entry_id]
        print(f"Deleted entry with ID: {entry_id}")

    def delete_entry_by_title(self, title):
        """
        제목으로 일기 삭제
        :param title: 삭제할 일기의 제목
        """
        initial_count = len(self.entries)
        self.entries = [entry for entry in self.entries if entry["title"] != str(title)]
        if len(self.entries) < initial_count:
            print(f"Deleted entry with title: {title}")
        else:
            print(f"No entry found with title: {title}")

    def find_entry(self, entry_id):
        """
        특정 일기 검색
        :param entry_id: 검색할 일기의 ID (int)
        """
        for entry in self.entries:
            if entry["id"] == entry_id:
                return entry
        return None

    def display_entries(self):
        """
        모든 일기 출력
        """
        print("\nYour Cute Journal Entries:")
        for entry in self.entries:
            print(f"ID: {entry['id']}, Title: {entry['title']}, Created At: {entry['created_at']}")
            print(f"Content: {entry['content']}\n")

    @classmethod
    def set_journal_name(cls, name):
        """
        일기 이름 변경
        :param name: 새로운 일기 이름
        """
        cls.journal_name = name

    @staticmethod
    def generate_id():
        """
        고유 ID 생성
        """
        return int(datetime.datetime.now().timestamp())

# Streamlit 인터페이스
if __name__ == "__main__":
    journal = CuteJournal()

    st.title("📝 Cute Journal")
    st.write("기록하고 싶은 귀여운 순간들을 추가하고 관리하세요!")

    # 새 일기 추가
    st.subheader("새로운 일기 추가")
    new_title = st.text_input("제목")
    new_content = st.text_area("내용")
    if st.button("일기 추가"):
        journal.add_entry(new_title, new_content)
        st.success("새로운 일기가 추가되었습니다!")

    # 일기 목록 표시
    st.subheader("일기 목록")
    if journal.entries:
        for entry in journal.entries:
            st.markdown(f"**제목**: {entry['title']}\n**내용**: {entry['content']}\n**작성일**: {entry['created_at']}\n---")

        # 일기 삭제
        delete_option = st.radio("삭제 방법", ("ID로 삭제", "제목으로 삭제"))
        if delete_option == "ID로 삭제":
            delete_id = st.number_input("삭제할 일기의 ID 입력", min_value=0, step=1)
            if st.button("ID로 삭제"):
                journal.delete_entry_by_id(delete_id)
                st.success("ID로 일기가 삭제되었습니다.")
        elif delete_option == "제목으로 삭제":
            delete_title = st.text_input("삭제할 일기의 제목 입력")
            if st.button("제목으로 삭제"):
                journal.delete_entry_by_title(delete_title)
                st.success("제목으로 일기가 삭제되었습니다.")
    else:
        st.info("아직 작성된 일기가 없습니다.")
