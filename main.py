import os
import glob
import time
from rich.console import Console
from rich.panel import Panel # 패널 추가 (더 멋지게)

console = Console()

def run_party():
    # students 폴더 안의 모든 .py 파일 찾기
    student_files = glob.glob("students/*.py")
    
    # [수정된 부분] style="bold big" -> style="bold"
    console.print(Panel(f"[bold green]🚀 총 {len(student_files)}개의 작품을 실행합니다![/bold green]", title="Class 2024 Finale", expand=False))
    time.sleep(2)

    for file_path in student_files:
        # 파일명에서 이름만 추출 (예: students/minsu.py -> minsu)
        student_name = os.path.basename(file_path).replace(".py", "")
        
        console.rule(f"[bold magenta]🎨 Creator: {student_name}[/bold magenta]")
        
        # uv run으로 각 파일 실행
        # (윈도우/맥 호환성을 위해 sys.executable 사용 권장하지만, uv run도 좋습니다)
        exit_code = os.system(f"uv run {file_path}")
        
        if exit_code != 0:
            console.print(f"[red]⚠️ {student_name}님의 코드 실행 중 오류가 발생했습니다.[/red]")
        
        time.sleep(1) # 감상을 위한 1초 대기

    console.print("\n[bold yellow]🎉 Class 2025 Python Course Complete! 🎉[/bold yellow]", justify="center")

if __name__ == "__main__":
    run_party()