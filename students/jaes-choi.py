# rich 라이브러리를 사용하여 터미널에 명함을 출력하는 코드입니다.
# rich가 설치되어 있지 않다면 'pip install rich' 명령어로 설치해주세요.

# rich 라이브러리에서 필요한 모듈들을 가져옵니다.
from rich import print
from rich.panel import Panel
from rich.box import DOUBLE

# 1. 명함에 들어갈 내용을 설정합니다.
# 이모지와 rich의 마크업을 사용하여 텍스트를 꾸밉니다.
name = "jaes-choi"
motto = "AI와 함께라면 코딩이 쉽다!"
content = f"🚀 [bold magenta]{name}[/bold magenta] 💻\n\n{motto}"

# 2. Panel을 사용하여 명함을 디자인합니다.
# expand=False는 패널이 터미널 너비에 맞춰 확장되지 않도록 합니다.
business_card = Panel(
    content,
    title="✨ My Business Card ✨",
    border_style="cyan",  # 테두리 색상을 네온 블루(cyan)로 설정
    box=DOUBLE,           # 테두리를 이중선으로 변경
    style="on yellow",    # 배경색을 노란색으로 설정
    expand=False,
    padding=(1, 5)        # 내용과 테두리 사이의 여백 (상하, 좌우)
)

# 3. 완성된 명함을 터미널에 출력합니다.
print(business_card)