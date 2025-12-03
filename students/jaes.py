from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich import box # 박스 테두리 모양을 바꾸기 위해 필요

# 1. 메인 콘텐츠 (이름과 소감) 꾸미기
# Text 객체를 사용하면 부분적으로 스타일을 적용하기 좋습니다.
main_text = Text()
main_text.append("\n🚀 Python Master 🚀\n", style="bold yellow underline") # 굵게, 노란색, 밑줄
main_text.append("\n") # 줄바꿈
main_text.append("💻 AI와 함께라면 코딩이 쉽다! 💻", style="italic white") # 기울임, 흰색

# 2. 추가 정보 (하단 링크 등) - 선택 사항
# 실제 터미널에서 클릭 가능한 링크를 만들 수도 있습니다.
sub_text = Text.from_markup(
    "\n\n[dim]------------------------------[/dim]\n"
    "📧 Email: [cyan]master@python.com[/cyan]\n"
    "🌐 Github: [link=https://github.com]github.com/master[/link]"
)

# 3. 전체 내용을 합치기
# 중앙 정렬을 위해 Align.center 사용
final_content = Align.center(main_text + sub_text)

# 4. 패널(박스) 디자인 업그레이드
# box.ROUNDED: 둥근 모서리
# title/subtitle: 박스 위아래에 제목 달기
# padding: 텍스트와 테두리 사이 여백 (상, 하)
card = Panel(
    final_content,
    title="[bold cyan]✨ Business Card ✨[/]",
    subtitle="[dim]Verified by Rich[/]",
    style="cyan",
    border_style="bold cyan",
    box=box.ROUNDED, 
    padding=(1, 4), # (상하 여백, 좌우 여백)
    width=50 # 명함의 고정 너비 설정
)

# 출력
print(card) 