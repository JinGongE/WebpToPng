import os
from PIL import Image
from plyer import notification

def convert_webp_to_png():
    # 현재 작업 디렉토리 경로
    current_dir = os.getcwd()
    
    # images 폴더 경로
    images_folder = os.path.join(current_dir, 'images')

    # images 폴더가 없으면 알림을 띄우고 실행 중단
    if not os.path.exists(images_folder):
        notification.notify(
            title="Error",
            message='"images" 폴더가 없습니다.',
            timeout=5  # 알림이 5초 동안 표시됨
        )
        return  # 프로그램 종료
    
    # result 폴더 경로 (없으면 생성)
    result_folder = os.path.join(current_dir, 'result')
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    
    # 성공 및 실패 카운트 초기화
    success_count = 0
    failure_count = 0
    
    # images 폴더에서 .webp 파일들을 찾아서 변환
    for filename in os.listdir(images_folder):
        if filename.endswith(".webp"):
            webp_path = os.path.join(images_folder, filename)
            
            try:
                # .webp 파일을 열어서 .png로 변환
                with Image.open(webp_path) as img:
                    png_filename = f"{os.path.splitext(filename)[0]}.png"
                    png_path = os.path.join(result_folder, png_filename)
                    
                    # PNG로 저장
                    img.save(png_path, "PNG")
                    success_count += 1  # 성공 카운트 증가
                
            except Exception as e:
                failure_count += 1  # 실패 카운트 증가
    
    # 알림 메시지 출력
    message = f"변환이 완료되었습니다. (성공: {success_count}, 실패: {failure_count})"
    notification.notify(
        title="변환 완료",
        message=message,
        timeout=5  # 알림이 5초 동안 표시됨
    )

# 함수 실행
convert_webp_to_png()

