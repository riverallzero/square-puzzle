from PIL import Image
import os


def split_and_save_image(input_path):
    # 이미지 불러오기
    original_image = Image.open(input_path)

    # 이미지의 크기 가져오기
    width, height = original_image.size

    # 16개의 부분 이미지 크기 계산
    part_width = width // 4
    part_height = height // 4

    # 출력 폴더가 없으면 생성
    all_output_folder = 'data'
    if not os.path.exists(all_output_folder):
        os.makedirs(all_output_folder)

    # 이미지를 16개로 나누어 각각 저장
    for row in range(4):
        for col in range(4):
            left = col * part_width
            top = row * part_height
            right = (col + 1) * part_width
            bottom = (row + 1) * part_height

            # 부분 이미지 추출
            part_image = original_image.crop((left, top, right, bottom))

            # 폴더에 저장
            all_output_path = os.path.join(all_output_folder, f'{item}_part_{row * 4 + col + 1}.jpg')
            part_image.save(all_output_path)


if __name__ == '__main__':
    for item in ['origin', 'split']:
        split_and_save_image(f'{item}.jpg')
